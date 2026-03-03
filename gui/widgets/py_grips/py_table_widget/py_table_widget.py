from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *# Assuming your style string is named 'table_style' inside style.py
from . style import style as table_style 

class PyTableWidget(QTableWidget):
    def __init__(
        self, 
        radius = 8,
        color = "#8a95aa",
        bg_color = "#343b48",
        selection_color = "#568af2",
        header_horizontal_color = "#272c36",
        header_vertical_color = "#3c4454",
        bottom_line_color = "#3c4454",
        grid_line_color = "#2c313c",
        scroll_bar_color = "#568af2",
        scroll_bar_bg_color = "#272C36",
        scroll_bar_btn_color = "#272C36",
        context_color = "#568af2",
        index_col_color = "#FFFFFF"
    ):
        super().__init__()

        # SAVE PROPERTIES
        self._radius = radius
        self._color = color
        self._bg_color = bg_color
        self._selection_color = selection_color
        self._header_horizontal_color = header_horizontal_color
        self._header_vertical_color = header_vertical_color
        self._bottom_line_color = bottom_line_color
        self._grid_line_color = grid_line_color
        self._scroll_bar_color = scroll_bar_color
        self._scroll_bar_bg_color = scroll_bar_bg_color
        self._scroll_bar_btn_color = scroll_bar_btn_color
        self._context_color = context_color
        self._index_col_color = index_col_color

        # DEFAULT SETTINGS
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setAlternatingRowColors(False)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setShowGrid(True)
        self.setCornerButtonEnabled(True)

        # INITIAL STYLE APPLY
        self.apply_styles()

    def apply_styles(self):
        """Injects internal variables into the detailed external stylesheet"""
        style_format = table_style.format(
            _radius = self._radius,          
            _color = self._color,
            _bg_color = self._bg_color,
            _header_horizontal_color = self._header_horizontal_color,
            _header_vertical_color = self._header_vertical_color,
            _selection_color = self._selection_color,
            _bottom_line_color = self._bottom_line_color,
            _grid_line_color = self._grid_line_color,
            _scroll_bar_color = self._scroll_bar_color,
            _scroll_bar_bg_color = self._scroll_bar_bg_color,
            _scroll_bar_btn_color = self._scroll_bar_btn_color,
            _context_color = self._context_color,
            _index_col_color = self._index_col_color
        )
        self.setStyleSheet(style_format)

    def update_theme_colors(self, theme_data):
        """Standardized method to update colors from theme dictionary"""
        self._bg_color = theme_data["app_color"]["table_bg"]
        self._color = theme_data["app_color"]["text_foreground"]
        self._context_color = theme_data["app_color"]["context_color"]
        self._grid_line_color = theme_data["app_color"]["bg_one"]
        self._bottom_line_color = theme_data["app_color"]["bg_one"]
        self._header_horizontal_color = theme_data["app_color"]["dark_four"]
        self._header_vertical_color = theme_data["app_color"]["bg_three"]
        self._scroll_bar_color = theme_data["app_color"]["scroll_bar_color"]
        self._scroll_bar_bg_color = theme_data["app_color"]["scroll_bar_bg_color"]
        self._scroll_bar_btn_color = theme_data["app_color"]["dark_four"]
        self._selection_color = theme_data["app_color"]["context_color"]
        self._index_col_color = theme_data["app_color"]["index_col_color"]


        # Re-apply using the saved properties
        self.apply_styles()

    def mousePressEvent(self, event):
        """Clears selection when clicking empty area"""
        item = self.itemAt(event.pos())
        if item is None:
            self.clearSelection()
            self.setCurrentItem(None)
        super().mousePressEvent(event)