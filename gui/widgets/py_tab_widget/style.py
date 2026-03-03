# STYLE
# ///////////////////////////////////////////////////////////////
style = """
QTabWidget::pane {{
    border: 1px solid {_grid_line_color};
    border-radius: {_radius}px;
    background-color: {_bg_color};
    top: -1px; /* Overlap border with tab bar */
}}

QTabBar::tab {{
    background-color: {_header_horizontal_color};
    color: {_color};
    border: 1px solid {_grid_line_color};
    border-bottom: none;
    border-top-left-radius: {_radius}px;
    border-top-right-radius: {_radius}px;
    padding: 8px 15px;
    margin-right: 2px;
}}

QTabBar::tab:hover {{
    background-color: {_header_vertical_color};
}}

QTabBar::tab:selected {{
    background-color: {_bg_color};
    color: {_selection_color};
    border-bottom: 2px solid {_selection_color};
}}

QTabBar::tab:!selected {{
    margin-top: 2px; /* Makes unselected tabs look smaller */
}}
"""