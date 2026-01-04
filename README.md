# Med Aegis

**Med Aegis** is a comprehensive pharmacy management application designed to streamline daily pharmacy operations. It consolidates clinical calculators and medication tracking tools into a single, user-friendly platform.
* **UI Versatility**: Optimized for both **Dark and Light mode** interfaces.
---

## 🚀 Key Features
### 🧪 Clinical Calculators
* **Creatinine Clearance Calculator**: Implementation of the **Cockroft-Gault formula** with flexible unit conversions ($μmol/L$, $mg/dL$, $mg/mL$).

### 📦 Supply Management Suite
* **Supply Tracker**: Automated parsing of NEHR dispensed history via copy-paste. Generates interactive graphs and tabular summaries for quick identification of oversupply.
* **Duration Calculator**: Precise treatment duration calculation between specified dates.
* **Balance Calculator**: Automated calculation of remaining supply quantities.
* **End Date Calculator**: Determination of treatment completion dates based on start date and duration.

---
## 🛠️ Running application
* **Run via line terminal**: python main.py
* **Run via executable**: python build_exe_slim.py then click main.exe

## ⚙️ Technical Architecture

* **Backend**: Python 3.10, Regular Expression Engine, and Pandas for robust data processing.
* **Frontend**: Built with **PySide6 (Qt)** and **PyQtChart** for high-performance data visualization.
* **Security**: **Fully offline operation**. All data processing occurs locally on the user's machine, ensuring total data privacy and eliminating network vulnerabilities.

---

## ✒️ Credits
Special thanks to **WANDERSON M.PIMENTA** for the [PyOneDark Template](https://github.com/Wanderson-Magalhaes/PyOneDark_Qt_Widgets_Modern_GUI). This application utilizes an adapted version of his modern UI framework to provide a professional user experience.
