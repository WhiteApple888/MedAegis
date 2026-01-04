from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QPushButton {{
    border: none;
    padding-left: 14px;
    padding-right: 5px;
    color: {_color};
    border-radius: {_radius}px;   
    background-color: {_bg_color};
    font-family: "Segoe UI";
    font-size: 10pt;
}}
QPushButton:hover {{
    background-color: {_bg_color_hover};
}}
QPushButton:pressed {{  
    background-color: {_bg_color_pressed};
}}
'''

# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyPushButton(QPushButton):
    def __init__(
        self, 
        text = "Push Button",
        radius = 20,
        color = "white",
        bg_color = "#272C36",
        bg_color_hover = "#6C99f4",
        bg_color_pressed = "#272C36",
        parent = None,
    ):
        super().__init__()

        # SAVE PROPERTIES (To retain them during theme updates)
        self._text = text
        self._radius = radius
        self._color = color
        self._bg_color = bg_color
        self._bg_color_hover = bg_color_hover
        self._bg_color_pressed = bg_color_pressed

        # BASIC CONFIG
        self.setText(self._text)
        if parent is not None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # INITIAL STYLE APPLY
        self.apply_styles()

    def apply_styles(self):
        """Centralized method to apply stylesheet using internal attributes"""
        custom_style = style.format(
            _color = self._color,
            _radius = self._radius,
            _bg_color = self._bg_color,
            _bg_color_hover = self._bg_color_hover,
            _bg_color_pressed = self._bg_color_pressed
        )
        self.setStyleSheet(custom_style)

    def update_theme_colors(self, theme_data):
        """Standardized method to update colors from theme dictionary"""
        self._bg_color_pressed = theme_data["app_color"]["dark_four"]

        # Re-apply using the saved properties
        self.apply_styles()


        #muted blue: #A5B4FC