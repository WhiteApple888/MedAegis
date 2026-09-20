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
from logic.adjusted_body_weight import *

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
        
        # 1) CREATININE CLEARANCE and EGFR CALCULATOR
        self.crcl_calculator_title = PyTitleWidget(title="Cockcroft-Gault CrCl and eGFR Calculator")

        self.age_label_1 = self.create_label("Age (Years)", minh=45, minw=225)
        self.weight_label_1 = self.create_label("Weight (kg)", minh=45, minw=225)
        self.scr_label_1 = self.create_label("Serum Creatinine", minh=45, minw=150)
        
        self.age_1 = self.create_line_edit(place_holder_text="input")
        self.weight_1 = self.create_line_edit(place_holder_text="input")
        self.scr_value_1 = self.create_line_edit(place_holder_text="input")


        # 2) UNIT TOGGLE (ComboBox)
        self.unit_toggle_1 = PyComboBox(items=["µmol/L", "mg/dL", "mg/mL"])
        self.crcl_male_label = self.create_label("Male CrCl", color=self.themes["app_color"]["text_foreground"])
        self.crcl_female_label = self.create_label("Female CrCl", color=self.themes["app_color"]["text_foreground"])
        
        self.crcl_male = self.create_label(text="--- mL/min", color="#2CA02C")
        self.crcl_female = self.create_label(text="--- mL/min", color="#2CA02C")

        # 3) BMI, IBW and AdjBW
        self.ibw_abw_bmi_title = PyTitleWidget(title="Adjusted Body Weight Calculator")
        self.height_label = self.create_label("Height (cm)", minh=45, minw=225)
        self.weight_label_2 = self.create_label("Weight (kg)", minh=45, minw=225)
        self.height = self.create_line_edit(place_holder_text="input")
        self.weight_2 = self.create_line_edit(place_holder_text="input")
        self.bmi_label = self.create_label("BMI (kg/m^2)", minh=45, minw=150)

        self.ibw_male_label = self.create_label("Male Ideal Body Weight", minh=45, minw=150)
        self.ibw_female_label = self.create_label("Female Ideal Body Weight", minh=45, minw=150)
        self.abw_male_label = self.create_label("Male Adjusted Body Weight", minh=45, minw=150)
        self.abw_female_label = self.create_label("Female Adjusted Body Weight", minh=45, minw=150)

        self.bmi = self.create_label(text="---", color="#2CA02C", minh=45, minw=150)
        self.ibw_male = self.create_label(text="--- kg")
        self.ibw_female = self.create_label(text="--- kg")
        self.abw_male = self.create_label(text="--- kg")
        self.abw_female = self.create_label(text="--- kg")

        # 4) CREATE STATIC REFERENCE LISTS
        self.renal_drugs_list = self.create_image("crcl_cal_ref/renal_drugs_list.png", width=500, height=500)
        self.ddi_drugs_list = self.create_image("crcl_cal_ref/ddi_drugs_list.png", width=700, height=500)

        
        # REPLACE DESIGNER PLACEHOLDERS
        # Targeting the object names you set in Qt Designer

        # 1) CRCL and EGFR
        self.replace_widget(self.ui.load_pages.crcl_calculator_title, self.crcl_calculator_title)
        self.replace_widget(self.ui.load_pages.age_label_1, self.age_label_1)
        self.replace_widget(self.ui.load_pages.weight_label_1, self.weight_label_1)
        self.replace_widget(self.ui.load_pages.scr_label_1, self.scr_label_1)
        self.replace_widget(self.ui.load_pages.age_1, self.age_1)
        self.replace_widget(self.ui.load_pages.weight_1, self.weight_1)
        self.replace_widget(self.ui.load_pages.unit_toggle_1, self.unit_toggle_1)
        self.replace_widget(self.ui.load_pages.scr_value_1, self.scr_value_1)
        self.replace_widget(self.ui.load_pages.crcl_male_label, self.crcl_male_label)
        self.replace_widget(self.ui.load_pages.crcl_female_label, self.crcl_female_label)
        self.replace_widget(self.ui.load_pages.crcl_male, self.crcl_male)
        self.replace_widget(self.ui.load_pages.crcl_female, self.crcl_female)

        # 2) BMI, IBW, AdjBW
        self.replace_widget(self.ui.load_pages.ibw_abw_bmi_title, self.ibw_abw_bmi_title)
        self.replace_widget(self.ui.load_pages.height_label, self.height_label)
        self.replace_widget(self.ui.load_pages.weight_label_2, self.weight_label_2)
        self.replace_widget(self.ui.load_pages.height, self.height)
        self.replace_widget(self.ui.load_pages.weight_2, self.weight_2)
        self.replace_widget(self.ui.load_pages.bmi_label, self.bmi_label)
        self.replace_widget(self.ui.load_pages.bmi, self.bmi)

        self.replace_widget(self.ui.load_pages.ibw_male_label, self.ibw_male_label)
        self.replace_widget(self.ui.load_pages.ibw_male, self.ibw_male)
        self.replace_widget(self.ui.load_pages.ibw_female_label, self.ibw_female_label)
        self.replace_widget(self.ui.load_pages.ibw_female, self.ibw_female)
        self.replace_widget(self.ui.load_pages.abw_male_label, self.abw_male_label)
        self.replace_widget(self.ui.load_pages.abw_male, self.abw_male)
        self.replace_widget(self.ui.load_pages.abw_female_label, self.abw_female_label)
        self.replace_widget(self.ui.load_pages.abw_female, self.abw_female)


        # 3) STATIC REFERENCE LIST
        self.replace_widget(self.ui.load_pages.renal_drugs_list, self.renal_drugs_list)
        self.replace_widget(self.ui.load_pages.ddi_drugs_list, self.ddi_drugs_list)
        

    
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
        # Trigger crcl and egfr calculation whenever any input changes
        self.age_1.textChanged.connect(self.run_crcl_egfr_calculation)
        self.weight_1.textChanged.connect(self.run_crcl_egfr_calculation)
        self.scr_value_1.textChanged.connect(self.run_crcl_egfr_calculation)
        self.unit_toggle_1.currentIndexChanged.connect(self.run_crcl_egfr_calculation)

        # Trigger bmi, ibw, abw calculation whenever any input changes
        self.height.textChanged.connect(self.run_bmi_ibw_abw_calculation)
        self.weight_2.textChanged.connect(self.run_bmi_ibw_abw_calculation)
    # =========================
    # CALCULATOR EVENT HANDLING LOGIC
    # =========================
    def run_crcl_egfr_calculation(self):
        print("CrCl and eGFR calculation triggered")
        # 1. Gather data from widgets
        age = self.age_1.text().strip()
        weight = self.weight_1.text().strip()
        scr = self.scr_value_1.text().strip()
        unit = self.unit_toggle_1.currentText()

        # Check if any field is empty before calling logic
        if not age or not weight or not scr:
            self.crcl_male.setText("---")
            self.crcl_female.setText("---")
            return
        
        # 2. Call external backend function
        m_result, f_result = cal_clcr_results(age, weight, scr, unit)

        # 3. Update UI based on result
        if m_result is not None:
            self.crcl_male.setText(f"{m_result} mL/min")
            self.crcl_female.setText(f"{f_result} mL/min")
            # Using your existing status helper for color feedback
            self.set_label_status(self.crcl_male, f"{m_result} mL/min", is_valid=True)
            self.set_label_status(self.crcl_female, f"{f_result} mL/min", is_valid=True)
        else:
            self.crcl_male.setText("---")
            self.crcl_female.setText("---")

    def run_bmi_ibw_abw_calculation(self):
        print("BMI, IBW, AdjBW calculation triggered")
        # 1. Gather data from widgets
        height = self.height.text().strip()
        weight = self.weight_2.text().strip()

        # Check if any field is empty before calling logic
        if not height or not weight:
            self.bmi.setText("---")
            self.ibw_male.setText("--- kg")
            self.ibw_female.setText("--- kg")
            self.abw_male.setText("--- kg")
            self.abw_female.setText("--- kg")
            return
        
        # 2. Call external backend function
        bmi_result = cal_bmi(weight, height)
        ibw_male, ibw_female, abw_male, abw_female = cal_ideal_adj_body_weight(weight, height)

        results = (bmi_result, ibw_male, ibw_female, abw_male, abw_female)


        # 3. Update UI based on result
        if all(result is not None for result in results):
            self.bmi.setText(f"{bmi_result}")
            self.ibw_male.setText(f"{ibw_male} kg")
            self.ibw_female.setText(f"{ibw_female} kg")
            self.abw_male.setText(f"{abw_male} kg")
            self.abw_female.setText(f"{abw_female} kg")
            # Using your existing status helper for color feedback
            
            obese_bmi = "obese" not in bmi_result.lower()
            self.set_label_status(self.bmi, f"{bmi_result}", is_valid=obese_bmi)

            actual_BW_largely_exceed_ibw_male = (float(weight) / ibw_male) < 1.2
            actual_BW_largely_exceed_ibw_female = (float(weight) / ibw_female) < 1.2
            self.set_label_status(self.abw_male, f"{abw_male} kg", is_valid=actual_BW_largely_exceed_ibw_male)
            self.set_label_status(self.abw_female, f"{abw_female} kg", is_valid=actual_BW_largely_exceed_ibw_female)
        else:
            self.bmi.setText("---")
            self.ibw_male.setText("--- kg")
            self.ibw_female.setText("--- kg")
            self.abw_male.setText("--- kg")
            self.abw_female.setText("--- kg")

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