from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
import pyqtgraph as pg
import pandas as pd
import numpy as np

class PyTrackingGraphWidget(QWidget):
    def __init__(
        self,
        bg_color = "#21252D",
        accent_color = "#568af2",
        text_color = "#8A95AA", # Added for axis labels
        parent = None
    ):
        super().__init__(parent)

        # 1. SETUP LAYOUT
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)

        # 2. INTERNAL STORAGE (Save properties for re-application)
        self._bg_color = bg_color
        self._accent_color = accent_color
        self._text_color = text_color
        self._current_df = None

        # 3. RUN SETUP
        self.setup_graph()

    def setup_graph(self):
        """Initializes PyQtGraph with Date Axis and Crosshair"""
        self.plot_widget = pg.PlotWidget(axisItems={'bottom': pg.DateAxisItem()})
        
        # Crosshair setup
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.label = pg.TextItem(anchor=(1.1, 1.1), fill=(0, 0, 0, 150))
        
        for item in [self.vLine, self.hLine, self.label]:
            item.setVisible(False)
            self.plot_widget.addItem(item, ignoreBounds=True)

        self.layout.addWidget(self.plot_widget)
        
        # Apply initial theme
        self.apply_styles()
        
        # Mouse Proxy
        self.proxy = pg.SignalProxy(self.plot_widget.scene().sigMouseMoved, rateLimit=60, slot=self.update_crosshair)

    def apply_styles(self):
        """Applies the colors to the pyqtgraph components manually"""
        # Background
        self.plot_widget.setBackground(self._bg_color)
        
        # Grid and Axes
        self.plot_widget.showGrid(x=False, y=False, alpha=0.3)
        styles = {'color': self._text_color, 'font-size': '10pt'}
        self.plot_widget.getAxis('left').setLabel('Quantity', **styles)
        self.plot_widget.getAxis('bottom').setLabel('Date', **styles)
        self.plot_widget.getAxis('left').setPen(self._text_color)
        self.plot_widget.getAxis('bottom').setPen(self._text_color)
        self.plot_widget.getAxis('left').setTextPen(self._text_color)
        self.plot_widget.getAxis('bottom').setTextPen(self._text_color)

        # Crosshair Pen
        crosshair_pen = pg.mkPen(color=self._accent_color, width=1, style=Qt.DashLine)
        self.vLine.setPen(crosshair_pen)
        self.hLine.setPen(crosshair_pen)
        self.label.setColor(self._text_color)

        if self._bg_color.lower() in ["#ffffff", "#f5f7ff", "#f5f5f5"]:
            # Light Mode: Light grey background box for the tooltip
            self.label = pg.TextItem(anchor=(1.1, 1.1), fill=(132, 124, 248, 200), color='w')
        else:
            # Dark Mode: Darker background box for the tooltip
            self.label = pg.TextItem(anchor=(1.1, 1.1), fill=(0, 0, 0, 150))

    def update_theme_colors(self, theme_data):
        """Standardized method to update colors from theme dictionary"""
        # Extract colors from theme_data
        self._bg_color = theme_data["app_color"]["tracking_graph_bg"]
        self._text_color = theme_data["app_color"]["text_labels"]
        self._accent_color = theme_data["app_color"]["context_color"]

        # Re-apply styles
        self.apply_styles()
        
        # Refresh the graph if data exists to update the legend and line colors if needed
        if self._current_df is not None:
            self.display_new_graph(self._current_df)

    def display_new_graph(self, df):
        """Standardized method to plot data"""
        self.plot_widget.clear()
        if df is not None:
            df = df.sort_values("Timestamp").reset_index(drop=True)
        self._current_df = df
        
        # Re-add items after clear
        self.plot_widget.addItem(self.vLine, ignoreBounds=True)
        self.plot_widget.addItem(self.hLine, ignoreBounds=True)
        self.plot_widget.addItem(self.label, ignoreBounds=True)

        # Optional: You could also pull these line colors from your theme_data
        colors = ['#FF5555', '#55FF55', '#00CEFF', '#FFFF55']
        
        if df is not None and not df.empty:
            # Plot Graph 1: Target Required (The 'Ideal' Ceiling)
            x_data = df['Date'].astype('int64') // 10**9
            self.plot_widget.plot(
                x=x_data,
                y=df['Target_Required'].values,
                name="Target Supply",
                pen=pg.mkPen(color='r', width=2.5, style=Qt.DotLine), 
                symbol=None, symbolSize=10, symbolBrush='r'
        )
            self.plot_widget.plot(
               x=x_data,
               y=df['Patient_Stock'].values,
               name="Actual Stock",
               pen=pg.mkPen(color=self._accent_color, width=2.5),
               fillLevel=0,
               brush=(86, 138, 242, 50) # Light blue fill under the curve
        )      

            # for i, (medication, group) in enumerate(df.groupby("Medication")):
            #     color = colors[i % len(colors)]
            #     self.plot_widget.plot(
            #         x=group['Timestamp'].values,
            #         y=group['cumulative_sum'].values,
            #         name=medication,
            #         pen=pg.mkPen(color=color, width=2.5),
            #         symbol='o', symbolSize=10, symbolBrush=color
            #     )
            # self.plot_widget.autoRange(padding=0.2)

    def update_crosshair(self, event):
        """Handles internal mouse movement and data snapping"""
        pos = event[0]
        if self.plot_widget.sceneBoundingRect().contains(pos):
            mouse_point = self.plot_widget.getViewBox().mapSceneToView(pos)
            
            if self._current_df is not None and not self._current_df.empty:
                idx = (self._current_df['Timestamp'] - mouse_point.x()).abs().idxmin()
                row = self._current_df.iloc[idx] # Use iloc for safer indexing
                
                self.vLine.setVisible(True)
                self.hLine.setVisible(True)
                self.label.setVisible(True)
                
                self.vLine.setPos(row['Timestamp'])
                self.hLine.setPos(row['Patient_Stock'])

                # Logic for Conditional Coloring
                oversupply_status = str(row['Oversupplied']).strip()
                if oversupply_status.lower() == "yes":
                    oversupply_text = f'<span style="color: #FF5555;">Oversupply: {oversupply_status}</span>'

                else:
                    oversupply_text = f"Oversupply: {oversupply_status}"

                content = f"Date: {row['Date'].strftime('%d-%b-%Y')}<br>" \
                            f"{oversupply_text}<br>" \
                            f"Patient Stock:{row['Patient_Stock']}<br>" \
                            f"Target Level:{row['Target_Required']}<br>" \
                            f"Qty given this day:{row['Qty']}<br>" \
                            f"Institutions: {row['Institution']}"
                            # f"Total Sum: {row['cumulative_sum']}\n"\
                            #  {row['Formulation']}\n" \
                
                self.label.setHtml(content) #set as html 
                # self.label.setText(content)
                self.label.setAnchor((1.1, 1.1))
                self.label.setPos(mouse_point.x(), mouse_point.y())
                return
            
    def add_today_crossmark(self, df):
        if df is None or df.empty or 'Date' not in df.columns:
            return
        
        try:
            # 1. Get today's date (normalized to midnight)
            today = pd.Timestamp.now().normalize()

            # 2. Find the integer index (row number) where Date == Today
            # We use .values to avoid index-alignment issues
            today_df = df[df['Date'] == today]

            if not today_df.empty:
                idx = today_df.index[0]
                y_val = today_df.at[idx, 'Patient_Stock']
                x_val = df.at[idx, 'Timestamp']

                # Create the Cross Marker
                self.plot_widget.plot(
                    [x_val], [y_val],
                    pen=None,
                    symbol='x', 
                    symbolSize=20,
                    symbolPen=pg.mkPen(color='#FF5555', width=3)
                )
                
                target_required = today_df.at[idx, 'Target_Required']
                balance_to_supply = int(np.ceil(max(0, target_required - y_val)))
                # Add the Text Label
                label = pg.TextItem(
                    text=f"Today:\n Patient stock: {int(np.ceil(y_val))}\n Balance to supply: {balance_to_supply}",
                    color="#FF5555", 
                    anchor=(0.5, 1.4)
                )
                label.setPos(x_val, y_val)
                self.plot_widget.addItem(label)
            
            else:
                # If today is not in the range, we do nothing (no marking)
                print("Today's date is outside the tracked range. No marker added.")
            
        except Exception as e:
            print(f"Marker Error: {e}")

        self.vLine.setVisible(False)
        self.hLine.setVisible(False)
        self.label.setVisible(False)