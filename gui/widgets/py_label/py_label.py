from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

# STYLE
# ///////////////////////////////////////////////////////////////
label_style = '''
QLabel {{
    background-color: {_bg_color};
    color: {_color};
    border-radius: {_radius}px;
    padding-left: 10px;
    padding-right: 10px;
    font-family: "Segoe UI";
    font-size: {_font_size}pt;
    font-weight: {_font_weight};
}}
'''

# PY LABEL
# ///////////////////////////////////////////////////////////////
class PyLabel(QLabel):
    def __init__(
        self, 
        text = "Custom Label",
        radius = 0,
        color = "#8A95AA",
        bg_color = "#1B1E23",
        font_size = 12,
        font_weight = "normal",
        alignment = Qt.AlignLeft | Qt.AlignVCenter
    ):
        super().__init__()

        # SAVE PROPERTIES
        self._radius = radius
        self._color = color
        self._bg_color = bg_color
        self._font_size = font_size
        self._font_weight = font_weight

        # PARAMETERS
        if text:
            self.setText(text)
        self.setAlignment(alignment)

        # INITIAL STYLE APPLY
        self.apply_styles()

        self.is_error = False  # Add this flag
        self._original_color = color # Store the initial color

    def set_error(self, state, error_color="#FF5555"):
        """Sets the label to error state (red) or back to normal"""
        self.is_error = state
        if state:
            self._color = error_color
        else:
            # We will let the theme update handle reverting to standard
            self._color = self._original_color
        self.apply_styles()

    # APPLY STYLESHEET
    # ///////////////////////////////////////////////////////////////
    def apply_styles(self):
        style_format = label_style.format(
            _radius = self._radius,
            _color = self._color,
            _bg_color = self._bg_color,
            _font_size = self._font_size,
            _font_weight = self._font_weight
        )
        self.setStyleSheet(style_format)

    # THEME UPDATE METHOD
    # ///////////////////////////////////////////////////////////////
    def update_theme_colors(self, theme_data):
        # If the background isn't transparent, update it to the app's secondary color
        if self._bg_color != "transparent":
            self._bg_color = theme_data["app_color"]["dark_one"]

        # Usually, labels either take the 'white' color or a specific context color
        if self._color.upper() == "#8A95AA":
                self._color = theme_data["app_color"]["text_labels"]

        elif self._color.upper() == "#334155":
            self._color = theme_data["app_color"]["text_labels"]

        if self.is_error:
            self._color = theme_data["app_color"]["red"]

        self.apply_styles()