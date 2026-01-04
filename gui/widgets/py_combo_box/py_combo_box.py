from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QComboBox {{
    background-color: {_bg_color};
    border-radius: {_radius}px;
    border: {_border_size}px solid transparent;
    padding-left: 10px;
    padding-right: 10px;
    color: {_color};
    font-family: "Segoe UI";
    font-size: 10pt;
}}
QComboBox:hover {{
    border: {_border_size}px solid {_context_color};
}}
QComboBox::down-arrow {{
    image: none;
    background-color: {_bg_color};
    width: 8px;
    height: 8px;
    border-radius: 4px;
    margin-right: 15px;
}}
QComboBox::down-arrow {{
    width: 8px;
    height: 8px;
    border-radius: 4px;
    margin-right: 15px;
}}
QComboBox QAbstractItemView {{
    color: {_color};
    background-color: {_bg_color};
    padding: 10px;
    selection-background-color: {_context_color};
    border: none;
    outline: none;
}}
'''

class PyComboBox(QComboBox):
    def __init__(
        self, 
        items=[],
        radius = 8,
        border_size = 2,
        color = "#dce1ec",
        bg_color = "#272C36",
        context_color = "#568af2"
    ):
        super().__init__()

        # SAVE PROPERTIES
        self._radius = radius
        self._border_size = border_size
        self._color = color
        self._bg_color = bg_color
        self._context_color = context_color

        # PARAMETERS
        self.setMinimumHeight(45)
        if items:
            self.addItems(items)

        # INITIAL STYLE APPLY
        self.apply_styles()

    def apply_styles(self):
        style_format = style.format(
            _radius = self._radius,
            _border_size = self._border_size,           
            _color = self._color,
            _bg_color = self._bg_color,
            _context_color = self._context_color
        )
        self.setStyleSheet(style_format)

    def update_theme_colors(self, theme_data):
        """Standardized method to update colors from theme dictionary"""
        self._bg_color = theme_data["app_color"]["dark_four"] # Matches your request
        self._color = theme_data["app_color"]["white"]
        self._context_color = theme_data["app_color"]["context_color"]

        self.apply_styles()