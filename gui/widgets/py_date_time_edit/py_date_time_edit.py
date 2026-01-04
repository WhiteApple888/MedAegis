from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
# STYLE STRING
# ///////////////////////////////////////////////////////////////
style = '''
QDateTimeEdit {{
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
QDateTimeEdit:focus {{
    border: {_border_size}px solid {_context_color};
    background-color: {_bg_color_active};
}}
QDateTimeEdit::drop-down {{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 25px; 
    border-left-width: 1px;
    border-left-color: {_bg_color_active};
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}}
QDateTimeEdit::down-arrow {{
    background-color: {_context_color};
    width: 8px;
    height: 8px;
    border-radius: 4px;
}}
'''

class PyDateTimeEdit(QDateTimeEdit):
    def __init__(
        self, 
        datetime = None,
        radius = 8,
        border_size = 2,
        color = "#dce1ec",
        selection_color = "#dce1ec",
        bg_color = "#1b1e23",
        bg_color_active = "#1B1E23",
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
        self._context_color = context_color

        # INITIAL SETUP
        if datetime:
            self.setDateTime(datetime)
        else:
            self.setDateTime(QDateTime.currentDateTime())

        # SET CALENDAR POPUP
        self.setCalendarPopup(True)
        
        # APPLY INITIAL STYLE
        self.apply_styles()

    def apply_styles(self):
        # 1. Format and Apply Main Stylesheet
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

        # 2. Update Internal Calendar Widget Styles
        self.setup_calendar_style()

    def setup_calendar_style(self):
        calendar = self.calendarWidget()
        
        # Calendar Background and Main Color
        calendar.setStyleSheet(f"""
            QCalendarWidget QWidget {{ background-color: {self._bg_color}; color: {self._color}; }}
            QCalendarWidget QAbstractItemView:enabled {{
                selection-background-color: {self._context_color};
                selection-color: {self._selection_color};
            }}
        """)
        
        # Reset Weekday formats (Removes the default Red for weekends)
        char_format = QTextCharFormat()
        char_format.setForeground(QColor(self._color))
        calendar.setWeekdayTextFormat(Qt.Saturday, char_format)
        calendar.setWeekdayTextFormat(Qt.Sunday, char_format)
        calendar.setGridVisible(False)

    def update_theme_colors(self, theme_data):
        """Standardized theme update method"""
        self._bg_color = theme_data["app_color"]["dark_one"]
        self._bg_color_active = theme_data["app_color"]["dark_one"]
        self._color = theme_data["app_color"]["text_labels"]
        self._context_color = theme_data["app_color"]["context_color"]
        
        # Re-apply all styles
        self.apply_styles()