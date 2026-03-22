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
from logic.nehr_recon import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
cols_to_show = ['Date', 'Status', 'Medication', 'Dosing instructions', 'Date &/or Qty', 'Institution', 'End Date']
class NEHRListParserPage:
    def __init__(self, parent_ui, themes):
        self.themes = themes
        self.ui = parent_ui 
        
        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        # 1. CREATE CUSTOM WIDGETS
        self.parser_title = self.create_header(title="NEHR Med List Parser")
        self.chronic_med_list_title = self.create_header(title="Chronic Medications")
        self.prn_med_list_title = self.create_header(title="PRN Medications")
        
        # 2. CREATE MEDICATION LIST INPUT FIELD
        self.input_text = PyTextEdit(
            text = "",
            place_holder_text = "Insert NEHR Records (ORDERED ONLY)",
            radius = 8,
            border_size = 2,
        )
        self.input_text.setMinimumHeight(300)
        # 3. CREATE PROCESS BUTTON 
        self.process_btn = PyPushButton(
            text = "PROCESS",
            bg_color = self.themes["app_color"]["green_btn"],
            bg_color_hover = self.themes["app_color"]["green_btn"],

        )
        self.process_btn.setMinimumHeight(40)
        self.process_btn.setIcon(QIcon(Functions.set_svg_icon("icon_settings.svg")))
        
        # 4. CREATE CLEAR BUTTON 
        self.clear_btn = PyPushButton(
            text = "CLEAR",
            bg_color = self.themes["app_color"]["red"],
            bg_color_hover = self.themes["app_color"]["red"]
        )
        self.clear_btn.setMinimumHeight(40)
        self.clear_btn.setIcon(QIcon(Functions.set_svg_icon("icon_close.svg")))
        

        # 5. CHRONIC AND PRN TABLE - initialized empty
        
        self.chronic_table = self.create_styled_table(cols_to_show)
        self.prn_table = self.create_styled_table(cols_to_show)
        
        # # 6. TAB Container - initialized empty
        # self.tabs_container = PyTabWidget()
        # self.tabs_container.addTab(self.chronic_table, "Chronic Meds")
        # self.tabs_container.addTab(self.prn_table, "PRN / As Needed")

        # 2. REPLACE DESIGNER PLACEHOLDERS
        # Ensure these object names exist in your .ui file/SetupMainWindow
        self.replace_widget(self.ui.load_pages.parser_title, self.parser_title)
        self.replace_widget(self.ui.load_pages.input_text_2, self.input_text)
        self.replace_widget(self.ui.load_pages.process_btn_2, self.process_btn)
        self.replace_widget(self.ui.load_pages.clear_btn_2, self.clear_btn)
        self.replace_widget(self.ui.load_pages.chronic_med_list_title, self.chronic_med_list_title)
        self.replace_widget(self.ui.load_pages.chronic_med_list, self.chronic_table)
        self.replace_widget(self.ui.load_pages.prn_med_list_title, self.prn_med_list_title)
        self.replace_widget(self.ui.load_pages.prn_med_list, self.prn_table)
        # self.replace_widget(self.ui.load_pages.medication_lists, self.tabs_container)

    def connect_signals(self):
        self.process_btn.clicked.connect(self.handle_process)
        self.clear_btn.clicked.connect(self.clear_all)
        # Single shortcut tied to the whole page
        self.copy_shortcut = QShortcut(QKeySequence("Ctrl+C"), self.ui.load_pages.pages) 
        self.copy_shortcut.activated.connect(self.handle_copy_shortcut)
    
    def handle_copy_shortcut(self):
    # Determine which table is visible based on the current tab index
        focused_widget = QApplication.focusWidget()
        if isinstance(focused_widget, QTableWidget):
            MainFunctions.copy_table_selection(focused_widget)

    # =========================
    # CALCULATOR EVENT HANDLING LOGIC
    # =========================
    
    def handle_process(self):
        raw_data = self.input_text.toPlainText().strip()
        if not raw_data:
            return

        # 1. Run your Backend Logic
        try:
            df_chronic, df_prn = compile_med_list(raw_data)
            
            # 2. Populate Chronic Table
            self.populate_med_table(self.chronic_table, df_chronic)
            
            # 3. Populate PRN Table
            self.populate_med_table(self.prn_table, df_prn)
            
            # Update tab labels with counts
            self.chronic_med_list_title.label_title.setText(f"Chronic Medications ({len(df_chronic)})")
            self.prn_med_list_title.label_title.setText(f"PRN Medications ({len(df_prn)})")
            
        except Exception as e:
            print(f"Error parsing data: {e}")

    def populate_med_table(self, table_widget, df):
        """Helper to fill QTableWidget from DataFrame"""
        table_widget.setRowCount(0)
        table_widget.setRowCount(len(df))
        cell_font = QFont()
        cell_font.setPointSize(12)

        # Get today's date for comparison (midnight)
        today = pd.Timestamp.now().normalize()

        for row_idx, row in df.iterrows():
            is_expired = False
            try:
                end_date_val = row.get('End Date')
                if pd.notna(end_date_val):
                    if pd.to_datetime(end_date_val) < today:
                        is_expired = True
            except:
                pass

            for col_idx, col_name in enumerate(cols_to_show):
                val = str(row[col_name]) if pd.notna(row[col_name]) else ""
                # Format date to string if it's a timestamp
                item = QTableWidgetItem()
                item.setFont(cell_font)
                item.setToolTip(val)

                # Handle Date Formatting
                if col_name in ['Date', 'End Date']:
                    try:
                        date_obj = pd.to_datetime(val)
                        val = date_obj.strftime('%d-%m-%Y')
                        item.setText(val)

                    except:
                        item.setText("")
                else:
                    item.setText(val)
            
                if is_expired:
                    item.setForeground(QBrush(QColor(self.themes["app_color"]["red"])))

                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                table_widget.setItem(row_idx, col_idx, item)
        # After the loop finishes populating the data:
        header = table_widget.horizontalHeader()

        # 1. Set the default behavior for all columns to 'ResizeToContents' or 'Interactive'
        header.setSectionResizeMode(QHeaderView.Interactive)

        # 2. Define specific widths or behaviors
        # Columns are 0: Date, 1: End Date, 2: Status, 3: Medication, 4: Dosing, 5: Institution
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents) # Date fits text
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents) # Status fits text
        header.setSectionResizeMode(2, QHeaderView.Interactive) # Medication interactive
        header.setSectionResizeMode(3, QHeaderView.Stretch) # Dosing Instructions fits text
        header.setSectionResizeMode(4, QHeaderView.Interactive) # Date &/or Qty interactive 
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents) # Institution interactive 
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents) # End Date fits text 
        table_widget.setColumnWidth(2, 250) # Set Medication to 200px
        table_widget.setColumnWidth(3, 900) # Set Dosing Instructions to 800px
        table_widget.setColumnWidth(4, 100) # Set Date &/or Qty to 100
        table_widget.resizeRowsToContents()

    def clear_all(self):
        self.input_text.clear()
        self.chronic_table.setRowCount(0)
        self.prn_table.setRowCount(0)
        self.chronic_med_list_title.label_title.setText("Chronic Meds")
        self.prn_med_list_title.label_title.setText("PRN Medications")


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
        table.setWordWrap(True)
        
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