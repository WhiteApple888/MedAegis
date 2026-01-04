from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QLineEdit {{
    background-color: {_bg_color};
    border-radius: {_radius}px;
    border: {_border_size}px solid transparent;
    padding-left: 10px;
    padding-right: 10px;
    selection-color: {_selection_color};
    selection-background-color: {_context_color};
    color: {_color};
    font-family: "Segoe UI";
    font-size: 10pt;
}}
QLineEdit:focus {{
    border: {_border_size}px solid {_context_color};
    background-color: {_bg_color_active};
}}
'''

class PyLineEdit(QLineEdit):
    def __init__(
        self, 
        text = "",
        place_holder_text = "",
        radius = 8,
        border_size = 2,
        color = "#dce1ec",
        selection_color = "#FFF",
        bg_color = "#1b1e23",
        bg_color_active = "#1B1E23",
        context_color = "#568af2"
    ):
        super().__init__()

        # SAVE PROPERTIES (Internal State)
        self._radius = radius
        self._border_size = border_size
        self._color = color
        self._selection_color = selection_color
        self._bg_color = bg_color
        self._bg_color_active = bg_color_active
        self._context_color = context_color

        # PARAMETERS
        if text:
            self.setText(text)
        if place_holder_text:
            self.setPlaceholderText(place_holder_text)

        # INITIAL STYLE APPLY
        self.apply_styles()

    # APPLY STYLESHEET
    # ///////////////////////////////////////////////////////////////
    def apply_styles(self):
        style_format = style.format(
            _radius = self._radius,
            _border_size = self._border_size,           
            _color = self._color,
            _selection_color = self._selection_color,
            _bg_color = self._bg_color,
            _bg_color_active = self._bg_color_active,
            _context_color = self._context_color
        )
        self.setStyleSheet(style_format)

    # THEME UPDATE METHOD
    # ///////////////////////////////////////////////////////////////
    def update_theme_colors(self, theme_data):
        """Standardized method to update colors from theme dictionary"""
        self._bg_color = theme_data["app_color"]["dark_one"]
        self._bg_color_active = theme_data["app_color"]["dark_one"]
        self._color = theme_data["app_color"]["text_active"]
        self._context_color = theme_data["app_color"]["context_color"]

        # Re-apply using the saved properties
        self.apply_styles()