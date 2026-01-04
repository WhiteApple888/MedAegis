# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
import sys
import os
import pandas as pd
import pyqtgraph as pg


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
from . functions_main_window import *

# BACKEND LOGIC 
# ///////////////////////////////////////////////////////////////
from logic.supply_tracker import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////

class SupplyTrackerPage:
    def __init__(self, parent_ui, themes):
        # SETTINGS
        self.themes = themes
        self.ui = parent_ui # This is self.ui from SetupMainWindow
        self.current_df = None  # To store data for the crosshair
        
        # Initialize UI
        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        
        # 1) CALCULATE DURATION
        self.calculate_duration_title_1 = self.create_header(title="Duration Calculator")
        self.start_date_label_1 = self.create_label(text="Start Date")
        self.end_date_label_1 = self.create_label(text="End Date")
        self.duration_label_1 = self.create_label(text="Duration (Days)")
        self.duration_1 = self.create_label(text="Answer", color="#2CA02C")
        self.start_date_1 = self.create_datetime_edit()
        self.end_date_1 = self.create_datetime_edit()

        # 3) CALCULATE QTY
        self.calculate_qty_title_1 = self.create_header(title="Balance Calculator")
        self.duration_label_2 = self.create_label(text="Total Duration (Days)")
        self.qty_label_1 = self.create_label(text="No. of tabs/caps per day")
        self.qty_label_2 = self.create_label(text="Already Supplied")
        self.qty_label_3 = self.create_label(text="Balance to supply")
        self.qty_3 = self.create_label(text="Answer", color="#2CA02C")
        self.duration_2 = self.create_line_edit()
        self.qty_1 = self.create_line_edit()
        self.qty_2 = self.create_line_edit()
        
        # 3) CALCULATE END DATE
        self.calculate_end_date_title_1 = self.create_header(title="End Date Calculator")
        self.start_date_label_2 = self.create_label(text="Start Date")
        self.duration_label_3 = self.create_label(text="Duration (Days)")
        self.end_date_label_2 = self.create_label(text="End Date")
        self.end_date_2 = self.create_label(text="Answer", color="#2CA02C")

        self.start_date_2 = self.create_datetime_edit()
        self.duration_3 = self.create_line_edit()

        # 4) BLOOD THINNER SUPPLY TRACKER    
        self.supply_tracker_title_1 = self.create_header(title="Supply Tracker")
        # INPUT
        self.input_text = PyTextEdit(
            text = "",
            place_holder_text = "Please Insert NEHR Dispensed Records",
            radius = 8,
            border_size = 2,
        )
        self.input_text.setMinimumHeight(300)
        
        
        # PROCESS BUTTON 
        self.process_btn = PyPushButton(
            text = "PROCESS",
            bg_color = self.themes["app_color"]["green_btn"],
            bg_color_hover = self.themes["app_color"]["green_btn"],

        )
        self.process_btn.setMinimumHeight(40)
        self.process_btn.setIcon(QIcon(Functions.set_svg_icon("icon_settings.svg")))
        
        # CLEAR BUTTON 
        self.clear_btn = PyPushButton(
            text = "CLEAR",
            bg_color = self.themes["app_color"]["red"],
            bg_color_hover = self.themes["app_color"]["red"]
        )
        self.clear_btn.setMinimumHeight(40)
        self.clear_btn.setIcon(QIcon(Functions.set_svg_icon("icon_close.svg")))
        
        # TABLES
        self.total_table = self.create_styled_table(["NAME", "TOTAL QTY"])
        self.dataframe_widget = self.create_styled_table(["Date", "Medication", "Tablets", "Formulation", "Institution", "Cumulative Sum"])

        # GRAPH CONTAINER - a simple QWidget to hold our PyQtGraph
        self.graph_widget = PyTrackingGraphWidget( 
            bg_color = self.themes["app_color"]["dark_four"],
            accent_color = self.themes["app_color"]["context_color"]
            )
        
        # REPLACE DESIGNER PLACEHOLDERS
        # Targeting the object names you set in Qt Designer

        # 1) CALCULATE END DATE
        self.replace_widget(self.ui.load_pages.calculate_duration_title_1, self.calculate_duration_title_1)
        self.replace_widget(self.ui.load_pages.start_date_label_1, self.start_date_label_1)
        self.replace_widget(self.ui.load_pages.end_date_label_1, self.end_date_label_1)
        self.replace_widget(self.ui.load_pages.duration_label_1, self.duration_label_1)
        self.replace_widget(self.ui.load_pages.duration_1, self.duration_1)
        

        # PyDateTimeEdit
        self.replace_widget(self.ui.load_pages.start_date_1, self.start_date_1)
        self.replace_widget(self.ui.load_pages.end_date_1, self.end_date_1)

            
        # 2) CALCULATE QTY
        self.replace_widget(self.ui.load_pages.calculate_qty_title_1, self.calculate_qty_title_1)
        # PyLabel
        self.replace_widget(self.ui.load_pages.duration_label_2, self.duration_label_2)
        self.replace_widget(self.ui.load_pages.qty_label_1, self.qty_label_1)
        self.replace_widget(self.ui.load_pages.qty_label_2, self.qty_label_2)
        self.replace_widget(self.ui.load_pages.qty_label_3, self.qty_label_3)
        self.replace_widget(self.ui.load_pages.qty_3, self.qty_3)
        
        # PyLineEdit
        self.replace_widget(self.ui.load_pages.duration_2, self.duration_2)
        self.replace_widget(self.ui.load_pages.qty_1, self.qty_1)
        self.replace_widget(self.ui.load_pages.qty_2, self.qty_2)


        # 3) CALCULATE END DATE
        self.replace_widget(self.ui.load_pages.calculate_end_date_title_1, self.calculate_end_date_title_1)
        # PyDateTimeEdit
        self.replace_widget(self.ui.load_pages.start_date_2, self.start_date_2)            
        # PyLineEdit
        self.replace_widget(self.ui.load_pages.duration_3, self.duration_3)
        # PyLabel
        self.replace_widget(self.ui.load_pages.start_date_label_2, self.start_date_label_2)
        self.replace_widget(self.ui.load_pages.duration_label_3, self.duration_label_3)
        self.replace_widget(self.ui.load_pages.end_date_label_2, self.end_date_label_2)
        self.replace_widget(self.ui.load_pages.end_date_2, self.end_date_2)

            
            # 3) BLOOD THINNER SUPPLY TRACKER
        self.replace_widget(self.ui.load_pages.supply_tracker_title_1, self.supply_tracker_title_1)
        self.replace_widget(self.ui.load_pages.input_text, self.input_text)
        self.replace_widget(self.ui.load_pages.process_btn, self.process_btn)
        self.replace_widget(self.ui.load_pages.clear_btn, self.clear_btn)
        self.replace_widget(self.ui.load_pages.total_table, self.total_table)
        self.replace_widget(self.ui.load_pages.dataframe, self.dataframe_widget)
        self.replace_widget(self.ui.load_pages.graph, self.graph_widget)
    def create_label(self, text, color=None):
        """Factory function to create styled PyLabel widgets"""
        # If no color is provided, use the theme default
        if color is None:
            color = self.themes["app_color"]["text_labels"]
        
        label = PyLabel(
            text = text,
            radius = 8,
            color = color
        )
        label.setMinimumHeight(45)
        label.setMinimumWidth(200)
        return label
    
    def create_header(self, title):
        """
        Helper function to quickly create and add a PyTitleWidget to a layout.
        :param layout: The parent layout (QVBoxLayout or QHBoxLayout)
        :param title: The string for the title
        :param color: The accent color (default is your signature blue)
        :return: The created widget instance (in case you need to update it later)
        """
        header = PyTitleWidget(title=title)
        return header
    
    def create_line_edit(self):
        """Factory function to create styled PyLineEdit widgets"""
        line_edit = PyLineEdit(
            radius = 8,
            border_size = 2
        )
        line_edit.setMinimumHeight(45)
        # Optional: Set default to current date/time
        return line_edit
    
    def create_datetime_edit(self):
        """Factory function to create styled PyDateTimeEdit widgets"""
        date_edit = PyDateTimeEdit(
            radius = 8,
            border_size = 2,
        )
        date_edit.setMinimumHeight(45)
        date_edit.setDisplayFormat("dd-MM-yyyy")
        # Optional: Set default to current date/time
        date_edit.setDateTime(QDateTime.currentDateTime())
        return date_edit
    
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
    

    def connect_signals(self):
        self.process_btn.clicked.connect(self.handle_process)
        self.clear_btn.clicked.connect(self.clear_all)
      
        # Shortcut to copy selection for the Totals table
        self.shortcut_total = QShortcut(QKeySequence("Ctrl+C"), self.total_table)
        self.shortcut_total.setContext(Qt.WidgetWithChildrenShortcut)
        self.shortcut_total.activated.connect(lambda: MainFunctions.copy_table_selection(self.total_table))

        # Shortcut to copy selection for the Detailed dataframe table
        self.shortcut_df = QShortcut(QKeySequence("Ctrl+C"), self.dataframe_widget)
        self.shortcut_df.setContext(Qt.WidgetWithChildrenShortcut)
        self.shortcut_df.activated.connect(lambda: MainFunctions.copy_table_selection(self.dataframe_widget))

        # Duration Calculation
        self.start_date_1.dateTimeChanged.connect(self.handle_duration_calc)
        self.end_date_1.dateTimeChanged.connect(self.handle_duration_calc)

        # Trigger required qty calc when these change
        self.duration_2.textChanged.connect(self.handle_required_qty_calc)
        self.qty_1.textChanged.connect(self.handle_required_qty_calc)
        self.qty_2.textChanged.connect(self.handle_required_qty_calc)

        # End Date Calculation
        self.start_date_2.dateTimeChanged.connect(self.handle_end_date_calc)
        self.duration_3.textChanged.connect(self.handle_end_date_calc)
    
    # =========================
    # CALCULATOR EVENT HANDLING LOGIC
    # =========================
    def handle_duration_calc(self):
        """Calculates days between two dates"""
        start = self.start_date_1.date().toString("yyyy-MM-dd")
        end = self.end_date_1.date().toString("yyyy-MM-dd")
        
        # Pass those strings to your Pandas logic
        result = calculate_duration_pd(start, end)
        
        # Update the label
        if result is not None and result >= 0:
            self.set_label_status(self.duration_1, f"{result} Days", is_valid=True)
        
        else:
            self.set_label_status(self.duration_1, "Invalid", is_valid=False)

    def handle_end_date_calc(self):
        """Calculates end date from start + days"""
        # 1. Extract values
        start = self.start_date_2.date().toString("yyyy-MM-dd")
        duration = self.duration_3.text().strip()
        
        if not duration:
            self.end_date_2.setText("Invalid")
            return

        # 2. Call your pandas logic
        result = calculate_end_date_pd(start, duration)
        
        # 3. Update UI
        if result and result != "Invalid":
            self.set_label_status(self.end_date_2, result, is_valid=True)
        else:
            self.set_label_status(self.end_date_2, "Invalid", is_valid=False)
    
    def handle_required_qty_calc(self):
    # Bridge between UI and logic/supply_tracker.py
        # 1. Get raw strings from UI
        duration_text = self.duration_2.text().strip()
        daily_text = self.qty_1.text().strip()
        balance_text = self.qty_2.text().strip()
                
        # 2. Call the backend logic
        # Make sure calculate_required_qty is imported at the top of this file
        result = calculate_required_qty(daily_text, balance_text, duration_text)
        # 3. Update the UI "Answer" label
        if result is not None and result > 0 :
            self.set_label_status(self.qty_3, f"{result} tabs/caps", is_valid=True)
            
        else:
            self.set_label_status(self.qty_3, "Invalid", is_valid=False)

    def set_label_status(self, label, text, is_valid=True):
        label.setText(text)

        if is_valid == True:
            # Change to green (or your theme's success color)
            color = self.themes["app_color"]["valid_green"] 
        else:
            # Change to red
            color = self.themes["app_color"]["red"]
        # Apply the color via inline stylesheet
        label._color = color
        label.apply_styles()
    
        
    # =========================
    # GRAPH AND TABLE EVENT HANDLING LOGIC
    # =========================

    def handle_process(self):
        raw_data = self.input_text.toPlainText().strip()
        if not raw_data:
            return

        # 1. Process Data via Backend
        # Returns: (DataFrame, Dictionary of Totals)
        self.current_df, totals = process_nehr_data(raw_data)

        # 2. Update Total Table
        self.total_table.setRowCount(0)
        for row_idx, (med, qty) in enumerate(totals.items()):
            self.total_table.insertRow(row_idx)
            item_med = QTableWidgetItem(str(med))
            item_qty = QTableWidgetItem(f"{qty} tabs/caps")
            # Set alignment to Center
            item_med.setTextAlignment(Qt.AlignCenter)
            item_qty.setTextAlignment(Qt.AlignCenter)
            self.total_table.setItem(row_idx, 0, item_med)
            self.total_table.setItem(row_idx, 1, item_qty)

        # 3. Update Detailed Table
        display_cols = ["Date", "Medication", "Qty", "Formulation", "Institution", "cumulative_sum"]
        df_to_display = self.current_df[display_cols].sort_values(by="Date", ascending=False)
        self.populate_table(self.dataframe_widget, df_to_display)

        # 4. Update Graph
        self.graph_widget.display_new_graph(self.current_df)


    def populate_table(self, table_widget, df):
        table_widget.setRowCount(len(df))
        for row_idx, row_values in enumerate(df.values):
            for col_idx, value in enumerate(row_values):
                # Format date objects for display
                val_str = value.strftime('%Y-%m-%d') if isinstance(value, pd.Timestamp) else str(value)
                item = QTableWidgetItem(val_str)
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row_idx, col_idx, item)

    def clear_all(self):
        self.input_text.clear()
        self.total_table.setRowCount(0)
        self.dataframe_widget.setRowCount(0)
        self.graph_widget.display_new_graph(None)
        self.current_df = None

    