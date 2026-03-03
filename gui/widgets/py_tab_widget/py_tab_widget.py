from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
# Assuming your style string is named 'tab_style' inside style.py
from .style import style as tab_style 

class PyTabWidget(QTabWidget):
    def __init__(
        self, 
        radius = 8,
        color = "#8a95aa",
        bg_color = "#343b48",
        selection_color = "#568af2",
        header_horizontal_color = "#272c36",
        header_vertical_color = "#3c4454",
        grid_line_color = "#2c313c"
    ):
        super().__init__()

        # SAVE PROPERTIES
        self._radius = radius
        self._color = color
        self._bg_color = bg_color
        self._selection_color = selection_color
        self._header_horizontal_color = header_horizontal_color
        self._header_vertical_color = header_vertical_color
        self._grid_line_color = grid_line_color

        # INITIAL STYLE APPLY
        self.apply_styles()

    def apply_styles(self):
        # Using the style string defined above
        style_format = tab_style.format(
            _radius = self._radius,          
            _color = self._color,
            _bg_color = self._bg_color,
            _header_horizontal_color = self._header_horizontal_color,
            _header_vertical_color = self._header_vertical_color,
            _selection_color = self._selection_color,
            _grid_line_color = self._grid_line_color
        )
        self.setStyleSheet(style_format)

    def update_theme_colors(self, theme_data):
        """Syncs with your existing theme dictionary"""
        self._bg_color = theme_data["app_color"]["table_bg"]
        self._color = theme_data["app_color"]["text_foreground"]
        self._grid_line_color = theme_data["app_color"]["bg_one"]
        self._header_horizontal_color = theme_data["app_color"]["dark_four"]
        self._header_vertical_color = theme_data["app_color"]["bg_three"]
        self._selection_color = theme_data["app_color"]["context_color"]

        self.apply_styles()