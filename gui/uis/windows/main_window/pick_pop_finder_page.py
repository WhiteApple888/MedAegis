# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from .functions_main_window import *

# BACKEND LOGIC 
# ///////////////////////////////////////////////////////////////
from logic.pickpopfinder import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////

class PickPopFinderPage:
    def __init__(self, parent_ui, themes):
        self.themes = themes
        self.ui = parent_ui 
        
        # Paths to your CSV files
        self.sg_postal_path = 'pickpopfindercsv/SG_postal.csv'
        self.station_path = 'pickpopfindercsv/stations.csv'

        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        # 1. CREATE CUSTOM WIDGETS
        self.finder_title = self.create_header(title="Nearest Station Finder")
        self.postal_label = self.create_label("Enter Postal Code", minh=45, minw=150)
        self.postal_input = self.create_line_edit("e.g. 681820", minh=45, minw=200)
        
        # We use a Table to display the Top results clearly
        self.results_table = self.create_styled_table(["Station Name", "Description", "Opening Hours", "Postal Code", "Estimated Distance (m)"]) #EMPTY

        # 2. REPLACE DESIGNER PLACEHOLDERS
        # Ensure these object names exist in your .ui file/SetupMainWindow
        self.replace_widget(self.ui.load_pages.finder_title_pane, self.finder_title)
        self.replace_widget(self.ui.load_pages.postal_label_pane, self.postal_label)
        self.replace_widget(self.ui.load_pages.postal_input_pane, self.postal_input)
        self.replace_widget(self.ui.load_pages.results_table_pane, self.results_table)

    def connect_signals(self):
        # Trigger search when text changes or when user presses Enter
        self.postal_input.textChanged.connect(self.run_station_search)
        # Shortcut to copy selection for the Totals table
        self.shortcut_total = QShortcut(QKeySequence("Ctrl+C"), self.results_table)
        self.shortcut_total.setContext(Qt.WidgetWithChildrenShortcut)
        self.shortcut_total.activated.connect(lambda: MainFunctions.copy_table_selection(self.results_table))

    def run_station_search(self):
        user_postal = self.postal_input.text().strip()

        # Validation: Singapore postal codes are 6 digits
        if len(user_postal) != 6 or not user_postal.isdigit():
            self.results_table.setRowCount(0)
            return

        # Call Backend
        try:
            result = get_nearest(user_postal, self.sg_postal_path, self.station_path)

            if isinstance(result, str): # Error message returned
                print(result) 
                self.results_table.setRowCount(0)
            else:
                self.display_results(result)
        except Exception as e:
            print(f"Search Error: {e}")

    def display_results(self, df):
        """Populates the QTableWidget with DataFrame content"""
        # Select columns to show
        display_cols = ['locker_station_name', 'locker_station_description', 'opening_hours', 'postal_code', 'estimated_dist_km']
        
        self.results_table.setColumnCount(len(display_cols))
        self.results_table.setHorizontalHeaderLabels(["Station Name", "Description", "Opening Hours", "Postal Code", "Estimated Distance (m)"])
        self.results_table.setRowCount(len(df))

        for row_idx, row in df.iterrows():
            # Reset index logic for display
            actual_row = df.index.get_loc(row_idx)
            for col_idx, col_name in enumerate(display_cols):
                item = QTableWidgetItem(str(row[col_name]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled) # Read-only
                self.results_table.setItem(actual_row, col_idx, item)
        
        self.results_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # --- HELPERS (Reusing your style pattern) ---
    def create_header(self, title):
        header = PyTitleWidget(title=title)
        return header
    
    def create_label(self, text, color=None, minh=45, minw=200):
        """Factory function to create styled PyLabel widgets"""
        # If no color is provided, use the theme default
        if color is None:
            color = self.themes["app_color"]["text_labels"]
        
        label = PyLabel(text = text, radius = 8, color = color)
        label.setMinimumHeight(minh)
        label.setMinimumWidth(minw)
        return label

    def create_line_edit(self, place_holder_text, minh=45, minw=125):
        line_edit = PyLineEdit(radius=8, border_size=2, place_holder_text=place_holder_text)
        line_edit.setMinimumHeight(minh)
        line_edit.setMinimumWidth(minw)
        return line_edit

    def create_styled_table(self, columns):
        table = PyTableWidget()
        table.setColumnCount(len(columns))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setFocusPolicy(Qt.ClickFocus)
        for i, name in enumerate(columns):
            item = QTableWidgetItem(name)
            item.setTextAlignment(Qt.AlignCenter)
            table.setHorizontalHeaderItem(i, item)
        return table

    def replace_widget(self, old_widget, new_widget):
        """ Replaces a Designer widget with a custom one while keeping layout index """
        if old_widget and old_widget.parentWidget():
            layout = old_widget.parentWidget().layout()
            if layout:
                # 1. HANDLE FORM LAYOUT
                if isinstance(layout, QFormLayout):
                    row, role = layout.getWidgetPosition(old_widget)
                    layout.removeWidget(old_widget)
                    old_widget.deleteLater()
                    layout.setWidget(row, role, new_widget)
                    # new_widget.setMinimumSize(QSize(0, 0))
                    new_widget.setMaximumSize(QSize(16777215, 16777215)) # This is the "Ignored" maximum
                
                # 2. HANDLE GRID LAYOUT
                elif isinstance(layout, QGridLayout):
                    # Find the index of the widget in the grid
                    idx = layout.indexOf(old_widget)
                    # Get the location: (row, column, rowSpan, columnSpan)
                    location = layout.getItemPosition(idx)
                
                    layout.removeWidget(old_widget)
                    old_widget.deleteLater()
                
                    # Re-insert with the exact same coordinates and spanning
                    layout.addWidget(new_widget, *location)
                    new_widget.setMinimumSize(QSize(0, 0))
                    new_widget.setMaximumSize(QSize(16777215, 16777215)) # This is the "Ignored" maximum

                # 3. HANDLE BOX LAYOUT (Vertical / Horizontal)
                else:
                    index = layout.indexOf(old_widget) # This checks if it's in the field column
                    stretch = 0
                    if hasattr(layout, "stretch"):
                        stretch = layout.stretch(index)
                
                    new_widget.setSizePolicy(old_widget.sizePolicy()) # Map size policy
                    layout.removeWidget(old_widget)
                    old_widget.deleteLater()
                    layout.insertWidget(index, new_widget, stretch) # Map size policy