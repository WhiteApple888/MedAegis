from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
# STYLE STRING (Moved outside or inside class for organization)
# ///////////////////////////////////////////////////////////////
style = '''
QTextEdit {{
    background-color: {_bg_color};
    border-radius: {_radius}px;
    border: {_border_size}px solid {_bg_color};
    padding: 5px;
    selection-color: {_selection_color};
    selection-background-color: {_context_color};
    color: {_color};
    font-family: "Segoe UI";
    font-size: 12pt;
}}
QTextEdit:focus {{
    border: {_border_size}px solid {_context_color};
    background-color: {_bg_color_active};
}}
QAbstractScrollArea QWidget {{
    background-color: transparent;
    border-radius: {_radius}px;
}}
QScrollBar:horizontal {{
    border: none;
    background: {_scroll_bar_bg_color};
    height: 8px;
    margin: 0px;
    border-radius: 0px;
}}
QScrollBar::handle:horizontal {{
    background: {_scroll_bar_color};
    min-width: 25px;
    border-radius: 4px;
}}
QScrollBar:vertical {{
    border: none;
    background: {_scroll_bar_bg_color};
    width: 8px;
    margin: 0px;
    border-radius: 0px;
}}
QScrollBar::handle:vertical {{  
    background: {_scroll_bar_color};
    min-height: 25px;
    border-radius: 4px;
}}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal,
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    width: 0px;
    height: 0px;
}}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal,
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
    background: none;
}}
'''

class PyTextEdit(QTextEdit):
    def __init__(
        self, 
        text = "",
        place_holder_text = "Input",
        radius = 8,
        border_size = 2,
        color = "#8A95AA",
        selection_color = "#8A95AA",
        bg_color = "#1e2229",
        bg_color_active = "#1b1e23",
        scroll_bar_color = "#3B82F6",
        scroll_bar_bg_color = "#272C36",
        scroll_bar_btn_color = "#272C36",
        context_color = "#568af2"
    ):
        super().__init__()

        # SAVE PROPERTIES
        self._radius = radius
        self._border_size = border_size
        self._color = color
        self._selection_color = selection_color
        self._bg_color = bg_color
        self._bg_color_active = bg_color_active
        self._scroll_bar_color = scroll_bar_color
        self._scroll_bar_bg_color = scroll_bar_bg_color
        self._scroll_bar_btn_color = scroll_bar_btn_color
        self._context_color = context_color
        self._place_holder_text = place_holder_text
        
        # INITIAL SETUP
        if text:
            self.setPlainText(text)
        self.setPlaceholderText(self._place_holder_text)

        # APPLY INITIAL STYLE
        self.apply_styles()

    # FOCUS EVENTS
    def focusInEvent(self, event):
        self.setPlaceholderText("")
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.setPlaceholderText(self._place_holder_text)
        super().focusOutEvent(event)

    # REFACTORED APPLY STYLES
    def apply_styles(self):
        style_format = style.format(
            _radius = self._radius,
            _border_size = self._border_size,           
            _color = self._color,
            _selection_color = self._selection_color,
            _bg_color = self._bg_color,
            _bg_color_active = self._bg_color_active,
            _scroll_bar_color = self._scroll_bar_color,
            _scroll_bar_bg_color = self._scroll_bar_bg_color,
            _scroll_bar_btn_color = self._scroll_bar_btn_color,
            _context_color = self._context_color
        )
        self.setStyleSheet(style_format)

    # THEME UPDATE METHOD
    def update_theme_colors(self, theme_data):
        """Update colors based on theme dictionary"""
        self._bg_color = theme_data["app_color"]["text_edit_bg"]
        self._bg_color_active = theme_data["app_color"]["text_edit_bg_active"]
        self._color = theme_data["app_color"]["text_foreground"]
        self._context_color = theme_data["app_color"]["context_color"]
        self._scroll_bar_color = theme_data["app_color"]["scroll_bar_color"]
        self._scroll_bar_bg_color = theme_data["app_color"]["scroll_bar_bg_color"]
        self._scroll_bar_btn_color = theme_data["app_color"]["dark_four"]
        
        # Re-apply using internal state
        self.apply_styles()