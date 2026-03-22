# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *


# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////

class MFDInfoPage:
    def __init__(self, parent_ui, themes):
        # SETTINGS
        self.themes = themes
        self.ui = parent_ui # This is self.ui from SetupMainWindow
        
        # Initialize UI
        self.setup_ui()

    def setup_ui(self):
        
        # 1) CREATININE CLEARANCE CALCULATOR
        self.mfd_title = PyTitleWidget(title="MEDIFUND INFORMATION")

        # 2) CREATE STATIC REFERENCE LISTS
        self.mfd_coverage = self.create_image("mfd/mfd_coverage.png")
        self.mfd_exclusions = self.create_image("mfd/mfd_exclusions.png")
        self.mfd_auto_switch = self.create_image("mfd/mfd_auto_switch.png", width=700)
        self.mfd_retail = self.create_image("mfd/mfd_retail.png", width=420)

        
        # REPLACE DESIGNER PLACEHOLDERS
        # Targeting the object names you set in Qt Designer

        # 1) CALCULATE END DATE
        self.replace_widget(self.ui.load_pages.mfd_title, self.mfd_title)
        self.replace_widget(self.ui.load_pages.mfd_coverage, self.mfd_coverage)
        self.replace_widget(self.ui.load_pages.mfd_auto_switch, self.mfd_auto_switch)
        self.replace_widget(self.ui.load_pages.mfd_exclusions, self.mfd_exclusions)
        self.replace_widget(self.ui.load_pages.mfd_retail, self.mfd_retail)
    
    def create_header(self, title):
        """
        Helper function to quickly create and add a PyTitleWidget to a layout.
        :param layout: The parent layout (QVBoxLayout or QHBoxLayout)
        :param title: The string for the title
        :param color: The accent color (default is your signature blue)
        :return: The created widget instance (in case you need to update it later)
        """
        header = PyTitleWidget(title=title)
        return header
    
    
    def create_image(self, image_path, width=200, height=150):
        """Factory function to create a label containing a static image"""
        zoom_widget = ZoomableImage(image_path)
        # Set a fixed/minimum size for the container in the layout
        zoom_widget.setMinimumSize(width, height)
        return zoom_widget
    
    def replace_widget(self, old_widget, new_widget):
        """ Replaces a Designer widget with a custom one while keeping layout index """
        if old_widget and old_widget.parentWidget():
            layout = old_widget.parentWidget().layout()
            if layout:
                # 1. HANDLE FORM LAYOUT
                if isinstance(layout, QFormLayout):
                    row, role = layout.getWidgetPosition(old_widget)
                    layout.removeWidget(old_widget)
                    old_widget.deleteLater()
                    layout.setWidget(row, role, new_widget)
                    # new_widget.setMinimumSize(QSize(0, 0))
                    new_widget.setMaximumSize(QSize(16777215, 16777215)) # This is the "Ignored" maximum
                
                # 2. HANDLE GRID LAYOUT
                elif isinstance(layout, QGridLayout):
                    # Find the index of the widget in the grid
                    idx = layout.indexOf(old_widget)
                    # Get the location: (row, column, rowSpan, columnSpan)
                    location = layout.getItemPosition(idx)
                
                    layout.removeWidget(old_widget)
                    old_widget.deleteLater()
                
                    # Re-insert with the exact same coordinates and spanning
                    layout.addWidget(new_widget, *location)
                    new_widget.setMinimumSize(QSize(0, 0))
                    new_widget.setMaximumSize(QSize(16777215, 16777215)) # This is the "Ignored" maximum

                # 3. HANDLE BOX LAYOUT (Vertical / Horizontal)
                else:
                    index = layout.indexOf(old_widget) # This checks if it's in the field column
                    stretch = 0
                    if hasattr(layout, "stretch"):
                        stretch = layout.stretch(index)
                
                    new_widget.setSizePolicy(old_widget.sizePolicy()) # Map size policy
                    layout.removeWidget(old_widget)
                    old_widget.deleteLater()
                    layout.insertWidget(index, new_widget, stretch) # Map size policy

class ZoomableImage(QScrollArea):
    def __init__(self, image_path):
        super().__init__()
        self.setWidgetResizable(True)
        self.setAlignment(Qt.AlignCenter)
        
        # The display label
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        
        # Load and store original pixmap
        self.original_pixmap = QPixmap(image_path)
        self.scale_factor = 1.0
        self.first_show = True # Flag to trigger initial "fit"

        self.setWidget(self.label)
        self.update_view()

    def resizeEvent(self, event):
        """Automatically fits the image to width on first load"""
        if self.first_show and not self.original_pixmap.isNull():
            # Calculate scale to fit width (leaving a small 20px margin)
            available_width = self.viewport().width()
            self.scale_factor = available_width / self.original_pixmap.width()
            
            # Ensure we don't scale it UP if the image is tiny
            self.scale_factor = min(self.scale_factor, 1.0)
            
            self.update_view()
            self.first_show = False
        super().resizeEvent(event)

    def update_view(self):
        if not self.original_pixmap.isNull():
            size = self.original_pixmap.size() * self.scale_factor
            scaled_pixmap = self.original_pixmap.scaled(
                size, 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            self.label.setPixmap(scaled_pixmap)
            self.label.setFixedSize(size)

    def wheelEvent(self, event):
        # Only zoom if Ctrl is held down
        if event.modifiers() == Qt.ControlModifier:
            angle = event.angleDelta().y()
            if angle > 0:
                self.scale_factor *= 1.1  # Zoom In
            else:
                self.scale_factor *= 0.9  # Zoom Out
            
            # Limit zoom range
            self.scale_factor = max(0.2, min(self.scale_factor, 5.0))
            self.update_view()
        else:
            # Otherwise, perform normal scrolling
            super().wheelEvent(event)