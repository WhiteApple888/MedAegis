from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

class PyTitleWidget(QWidget):
    def __init__(
        self,
        title="DASHBOARD TITLE",
        radius=8,
        bg_color="#272c36",       
        title_color="#dce1ec",
        context_color="#007AFF",  
        title_size=14
    ):
        super().__init__()

        # SAVE PROPERTIES (To retain them during theme updates)
        self._radius = radius
        self._title_size = title_size
        self._title_text = title.upper()

        # LAYOUT
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(5, 5, 5, 5) 
        
        # CONTAINER
        self.container = QFrame()
        self.container.setObjectName("Container")
        self.container_layout = QHBoxLayout(self.container)
        self.container_layout.setContentsMargins(10, 8, 10, 8)
        
        # LEFT ACCENT BAR
        self.accent_bar = QFrame()
        self.accent_bar.setObjectName("AccentBar")
        self.accent_bar.setFixedWidth(4)
        self.accent_bar.setFixedHeight(18) 
        
        # TITLE LABEL
        self.label_title = QLabel(self._title_text)
        self.label_title.setObjectName("Title")

        # ADD TO LAYOUTS
        self.container_layout.addWidget(self.accent_bar)
        self.container_layout.addWidget(self.label_title)
        self.container_layout.addStretch() 
        self.layout.addWidget(self.container)

        # INITIAL STYLE APPLY
        self.apply_styles(bg_color, title_color, context_color)

    def apply_styles(self, bg, color, accent):
        """Centralized method to apply stylesheet without losing formatting"""
        style = f"""
        #Container {{
            background-color: {bg};
            border-radius: {self._radius}px;
        }}
        #Title {{
            color: {color};
            font-size: {self._title_size}pt;
            font-weight: bold;
            background: transparent;
            padding-left: 5px;
        }}
        #AccentBar {{
            background-color: {accent};
            border-radius: 2px;
        }}
        """
        self.setStyleSheet(style)

    def set_title(self, title):
        self._title_text = title.upper()
        self.label_title.setText(self._title_text)

    def update_theme_colors(self, theme_data):
        """Grab colors and re-apply using the helper method"""
        bg_color = theme_data["app_color"]["dark_four"]
        title_color = theme_data["app_color"]["text_title"]
        context_color = theme_data["app_color"]["context_color"]

        # This now retains your radius and font settings
        self.apply_styles(bg_color, title_color, context_color)

        