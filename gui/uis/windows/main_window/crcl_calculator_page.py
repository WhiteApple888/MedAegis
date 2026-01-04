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

# BACKEND LOGIC 
# ///////////////////////////////////////////////////////////////
from logic.crcl import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////

class CrClCalculatorPage:
    def __init__(self, parent_ui, themes):
        # SETTINGS
        self.themes = themes
        self.ui = parent_ui # This is self.ui from SetupMainWindow
        
        # Initialize UI
        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        
        # 1) CREATININE CLEARANCE CALCULATOR
        self.crcl_calculator_title = PyTitleWidget(title="Cockcroft-Gault CrCl Calculator")

        self.age_label_1 = self.create_label("Age (Years)", minh=45, minw=225)
        self.weight_label_1 = self.create_label("Weight (kg)", minh=45, minw=225)
        self.scr_label_1 = self.create_label("Serum Creatinine", minh=45, minw=150)
        
        self.age_1 = self.create_line_edit(place_holder_text="input")
        self.weight_1 = self.create_line_edit(place_holder_text="input")
        self.scr_value_1 = self.create_line_edit(place_holder_text="input")


        # 4) UNIT TOGGLE (ComboBox)
        self.unit_toggle_1 = PyComboBox(items=["µmol/L", "mg/dL", "mg/mL"])
        self.result_male_label_1 = self.create_label("Male Result", color=self.themes["app_color"]["text_foreground"])
        self.result_female_label_1 = self.create_label("Female Result", color=self.themes["app_color"]["text_foreground"])
        
        self.val_male_1 = self.create_label(text="--- mL/min", color="#2CA02C")
        self.val_female_1 = self.create_label(text="--- mL/min", color="#2CA02C")

        
        # REPLACE DESIGNER PLACEHOLDERS
        # Targeting the object names you set in Qt Designer

        # 1) CALCULATE END DATE
        self.replace_widget(self.ui.load_pages.crcl_calculator_title, self.crcl_calculator_title)
        self.replace_widget(self.ui.load_pages.age_label_1, self.age_label_1)
        self.replace_widget(self.ui.load_pages.weight_label_1, self.weight_label_1)
        self.replace_widget(self.ui.load_pages.scr_label_1, self.scr_label_1)
        self.replace_widget(self.ui.load_pages.age_1, self.age_1)
        self.replace_widget(self.ui.load_pages.weight_1, self.weight_1)
        self.replace_widget(self.ui.load_pages.unit_toggle_1, self.unit_toggle_1)
        self.replace_widget(self.ui.load_pages.scr_value_1, self.scr_value_1)
        self.replace_widget(self.ui.load_pages.result_male_label_1, self.result_male_label_1)
        self.replace_widget(self.ui.load_pages.result_female_label_1, self.result_female_label_1)
        self.replace_widget(self.ui.load_pages.val_male_1, self.val_male_1)
        self.replace_widget(self.ui.load_pages.val_female_1, self.val_female_1)
        

    
    def create_label(self, text, color=None, minh=45, minw=125):
        """Factory function to create styled PyLabel widgets"""
        # If no color is provided, use the theme default
        if color is None:
            color = self.themes["app_color"]["text_labels"]
        
        label = PyLabel(
            text = text,
            radius = 8,
            color = color
        )
        label.setMinimumHeight(minh)
        label.setMinimumWidth(minw)
        return label
    
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
    
    def create_line_edit(self, place_holder_text):
        """Factory function to create styled PyLineEdit widgets"""
        line_edit = PyLineEdit(
            radius = 8,
            border_size = 2,
            place_holder_text = place_holder_text
        )
        line_edit.setMinimumHeight(45)
        # Optional: Set default to current date/time
        return line_edit
    
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

    
    def connect_signals(self):
        # Trigger crcl calculation whenever any input changes
        self.age_1.textChanged.connect(self.run_calculation)
        self.weight_1.textChanged.connect(self.run_calculation)
        self.scr_value_1.textChanged.connect(self.run_calculation)
        self.unit_toggle_1.currentIndexChanged.connect(self.run_calculation)

    # =========================
    # CALCULATOR EVENT HANDLING LOGIC
    # =========================
    def run_calculation(self):
        print("calculation triggered")
        # 1. Gather data from widgets
        age = self.age_1.text().strip()
        weight = self.weight_1.text().strip()
        scr = self.scr_value_1.text().strip()
        unit = self.unit_toggle_1.currentText()

        # Check if any field is empty before calling logic
        if not age or not weight or not scr:
            self.val_male_1.setText("---")
            self.val_female_1.setText("---")
            return
        
        # 2. Call external backend function
        m_result, f_result = cal_clcr_results(age, weight, scr, unit)

        # 3. Update UI based on result
        if m_result is not None:
            self.val_male_1.setText(f"{m_result} mL/min")
            self.val_female_1.setText(f"{f_result} mL/min")
            # Using your existing status helper for color feedback
            self.set_label_status(self.val_male_1, f"{m_result} mL/min", is_valid=True)
            self.set_label_status(self.val_female_1, f"{f_result} mL/min", is_valid=True)
        else:
            self.val_male_1.setText("---")
            self.val_female_1.setText("---")

    def set_label_status(self, label, text, is_valid=True):
        label.setText(text)

        if is_valid == True:
            # Change to green (or your theme's success color)
            color = self.themes["app_color"]["valid_green"] 
        else:
            # Change to red
            color = self.themes["app_color"]["red"]
        # Apply the color via inline stylesheet
        label._color = color
        label.apply_styles()

    def clear_all(self):
        self.input_text.clear()

    