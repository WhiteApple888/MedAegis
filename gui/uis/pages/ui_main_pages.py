# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QScrollArea,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1230, 670)
        self.verticalLayout_10 = QVBoxLayout(MainPages)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)


        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"border: 1px solid black;")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area_2 = QScrollArea(self.page_2)
        self.scroll_area_2.setObjectName(u"scroll_area_2")
        self.scroll_area_2.setStyleSheet(u"")
        self.scroll_area_2.setFrameShape(QFrame.NoFrame)
        self.scroll_area_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_2.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 1206, 646))
        self.contents.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.contents)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left = QWidget(self.widget)
        self.left.setObjectName(u"left")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left.sizePolicy().hasHeightForWidth())
        self.left.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.left)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.crcl_calculator_title = QWidget(self.left)
        self.crcl_calculator_title.setObjectName(u"crcl_calculator_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.crcl_calculator_title.sizePolicy().hasHeightForWidth())
        self.crcl_calculator_title.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.crcl_calculator_title)

        self.crcl_calculator_input_output = QWidget(self.left)
        self.crcl_calculator_input_output.setObjectName(u"crcl_calculator_input_output")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(10)
        sizePolicy3.setHeightForWidth(self.crcl_calculator_input_output.sizePolicy().hasHeightForWidth())
        self.crcl_calculator_input_output.setSizePolicy(sizePolicy3)
        self.verticalLayout_2 = QVBoxLayout(self.crcl_calculator_input_output)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.crcl_calculator_input = QWidget(self.crcl_calculator_input_output)
        self.crcl_calculator_input.setObjectName(u"crcl_calculator_input")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.crcl_calculator_input.sizePolicy().hasHeightForWidth())
        self.crcl_calculator_input.setSizePolicy(sizePolicy4)
        self.formLayout_4 = QFormLayout(self.crcl_calculator_input)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.age_label_1 = QWidget(self.crcl_calculator_input)
        self.age_label_1.setObjectName(u"age_label_1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.age_label_1.sizePolicy().hasHeightForWidth())
        self.age_label_1.setSizePolicy(sizePolicy5)
        self.age_label_1.setMinimumSize(QSize(30, 0))

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.age_label_1)

        self.age_1 = QWidget(self.crcl_calculator_input)
        self.age_1.setObjectName(u"age_1")
        sizePolicy5.setHeightForWidth(self.age_1.sizePolicy().hasHeightForWidth())
        self.age_1.setSizePolicy(sizePolicy5)
        self.age_1.setMinimumSize(QSize(30, 0))

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.age_1)

        self.weight_label_1 = QWidget(self.crcl_calculator_input)
        self.weight_label_1.setObjectName(u"weight_label_1")
        sizePolicy5.setHeightForWidth(self.weight_label_1.sizePolicy().hasHeightForWidth())
        self.weight_label_1.setSizePolicy(sizePolicy5)
        self.weight_label_1.setMinimumSize(QSize(30, 0))

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.weight_label_1)

        self.weight_1 = QWidget(self.crcl_calculator_input)
        self.weight_1.setObjectName(u"weight_1")
        sizePolicy5.setHeightForWidth(self.weight_1.sizePolicy().hasHeightForWidth())
        self.weight_1.setSizePolicy(sizePolicy5)
        self.weight_1.setMinimumSize(QSize(30, 0))

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.weight_1)

        self.scr_label_units_1 = QWidget(self.crcl_calculator_input)
        self.scr_label_units_1.setObjectName(u"scr_label_units_1")
        sizePolicy5.setHeightForWidth(self.scr_label_units_1.sizePolicy().hasHeightForWidth())
        self.scr_label_units_1.setSizePolicy(sizePolicy5)
        self.scr_label_units_1.setMinimumSize(QSize(30, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.scr_label_units_1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scr_label_1 = QWidget(self.scr_label_units_1)
        self.scr_label_1.setObjectName(u"scr_label_1")
        sizePolicy5.setHeightForWidth(self.scr_label_1.sizePolicy().hasHeightForWidth())
        self.scr_label_1.setSizePolicy(sizePolicy5)
        self.scr_label_1.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_3.addWidget(self.scr_label_1)

        self.unit_toggle_1 = QWidget(self.scr_label_units_1)
        self.unit_toggle_1.setObjectName(u"unit_toggle_1")
        sizePolicy1.setHeightForWidth(self.unit_toggle_1.sizePolicy().hasHeightForWidth())
        self.unit_toggle_1.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.unit_toggle_1)


        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.scr_label_units_1)

        self.scr_value_1 = QWidget(self.crcl_calculator_input)
        self.scr_value_1.setObjectName(u"scr_value_1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.scr_value_1.sizePolicy().hasHeightForWidth())
        self.scr_value_1.setSizePolicy(sizePolicy6)

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.scr_value_1)


        self.verticalLayout_2.addWidget(self.crcl_calculator_input)

        self.crcl_calculator_output = QWidget(self.crcl_calculator_input_output)
        self.crcl_calculator_output.setObjectName(u"crcl_calculator_output")
        sizePolicy5.setHeightForWidth(self.crcl_calculator_output.sizePolicy().hasHeightForWidth())
        self.crcl_calculator_output.setSizePolicy(sizePolicy5)
        self.horizontalLayout_2 = QHBoxLayout(self.crcl_calculator_output)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.crcl_male_label = QWidget(self.crcl_calculator_output)
        self.crcl_male_label.setObjectName(u"crcl_male_label")
        sizePolicy5.setHeightForWidth(self.crcl_male_label.sizePolicy().hasHeightForWidth())
        self.crcl_male_label.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.crcl_male_label)

        self.crcl_male = QWidget(self.crcl_calculator_output)
        self.crcl_male.setObjectName(u"crcl_male")
        sizePolicy5.setHeightForWidth(self.crcl_male.sizePolicy().hasHeightForWidth())
        self.crcl_male.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.crcl_male)

        self.crcl_female_label = QWidget(self.crcl_calculator_output)
        self.crcl_female_label.setObjectName(u"crcl_female_label")
        sizePolicy5.setHeightForWidth(self.crcl_female_label.sizePolicy().hasHeightForWidth())
        self.crcl_female_label.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.crcl_female_label)

        self.crcl_female = QWidget(self.crcl_calculator_output)
        self.crcl_female.setObjectName(u"crcl_female")
        sizePolicy5.setHeightForWidth(self.crcl_female.sizePolicy().hasHeightForWidth())
        self.crcl_female.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.crcl_female)


        self.verticalLayout_2.addWidget(self.crcl_calculator_output)

        self.egfr_calculator_output = QWidget(self.crcl_calculator_input_output)
        self.egfr_calculator_output.setObjectName(u"egfr_calculator_output")
        sizePolicy5.setHeightForWidth(self.egfr_calculator_output.sizePolicy().hasHeightForWidth())
        self.egfr_calculator_output.setSizePolicy(sizePolicy5)
        self.horizontalLayout_5 = QHBoxLayout(self.egfr_calculator_output)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.egfr_male_label = QWidget(self.egfr_calculator_output)
        self.egfr_male_label.setObjectName(u"egfr_male_label")
        sizePolicy5.setHeightForWidth(self.egfr_male_label.sizePolicy().hasHeightForWidth())
        self.egfr_male_label.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.egfr_male_label)

        self.egfr_male = QWidget(self.egfr_calculator_output)
        self.egfr_male.setObjectName(u"egfr_male")
        sizePolicy5.setHeightForWidth(self.egfr_male.sizePolicy().hasHeightForWidth())
        self.egfr_male.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.egfr_male)

        self.egfr_female_label = QWidget(self.egfr_calculator_output)
        self.egfr_female_label.setObjectName(u"egfr_female_label")
        sizePolicy5.setHeightForWidth(self.egfr_female_label.sizePolicy().hasHeightForWidth())
        self.egfr_female_label.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.egfr_female_label)

        self.egfr_female = QWidget(self.egfr_calculator_output)
        self.egfr_female.setObjectName(u"egfr_female")
        sizePolicy5.setHeightForWidth(self.egfr_female.sizePolicy().hasHeightForWidth())
        self.egfr_female.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.egfr_female)


        self.verticalLayout_2.addWidget(self.egfr_calculator_output)

        self.renal_drugs_list = QWidget(self.crcl_calculator_input_output)
        self.renal_drugs_list.setObjectName(u"renal_drugs_list")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(6)
        sizePolicy7.setHeightForWidth(self.renal_drugs_list.sizePolicy().hasHeightForWidth())
        self.renal_drugs_list.setSizePolicy(sizePolicy7)

        self.verticalLayout_2.addWidget(self.renal_drugs_list)


        self.verticalLayout_5.addWidget(self.crcl_calculator_input_output)


        self.horizontalLayout.addWidget(self.left)

        self.right = QWidget(self.widget)
        self.right.setObjectName(u"right")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(3)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.right.sizePolicy().hasHeightForWidth())
        self.right.setSizePolicy(sizePolicy8)
        self.verticalLayout_11 = QVBoxLayout(self.right)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.ibw_abw_bmi = QFrame(self.right)
        self.ibw_abw_bmi.setObjectName(u"ibw_abw_bmi")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(2)
        sizePolicy9.setHeightForWidth(self.ibw_abw_bmi.sizePolicy().hasHeightForWidth())
        self.ibw_abw_bmi.setSizePolicy(sizePolicy9)
        self.ibw_abw_bmi.setFrameShape(QFrame.StyledPanel)
        self.ibw_abw_bmi.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.ibw_abw_bmi)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.ibw_abw_bmi_title = QWidget(self.ibw_abw_bmi)
        self.ibw_abw_bmi_title.setObjectName(u"ibw_abw_bmi_title")
        sizePolicy2.setHeightForWidth(self.ibw_abw_bmi_title.sizePolicy().hasHeightForWidth())
        self.ibw_abw_bmi_title.setSizePolicy(sizePolicy2)

        self.verticalLayout_26.addWidget(self.ibw_abw_bmi_title)

        self.ibw_abw_bmi_input_output = QWidget(self.ibw_abw_bmi)
        self.ibw_abw_bmi_input_output.setObjectName(u"ibw_abw_bmi_input_output")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(8)
        sizePolicy10.setHeightForWidth(self.ibw_abw_bmi_input_output.sizePolicy().hasHeightForWidth())
        self.ibw_abw_bmi_input_output.setSizePolicy(sizePolicy10)
        self.verticalLayout_25 = QVBoxLayout(self.ibw_abw_bmi_input_output)
        self.verticalLayout_25.setSpacing(2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.bmi_ibw_abw_calculator_input = QWidget(self.ibw_abw_bmi_input_output)
        self.bmi_ibw_abw_calculator_input.setObjectName(u"bmi_ibw_abw_calculator_input")
        sizePolicy5.setHeightForWidth(self.bmi_ibw_abw_calculator_input.sizePolicy().hasHeightForWidth())
        self.bmi_ibw_abw_calculator_input.setSizePolicy(sizePolicy5)
        self.gridLayout = QGridLayout(self.bmi_ibw_abw_calculator_input)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.height_label = QWidget(self.bmi_ibw_abw_calculator_input)
        self.height_label.setObjectName(u"height_label")
        sizePolicy5.setHeightForWidth(self.height_label.sizePolicy().hasHeightForWidth())
        self.height_label.setSizePolicy(sizePolicy5)
        self.height_label.setMinimumSize(QSize(30, 0))

        self.gridLayout.addWidget(self.height_label, 0, 0, 1, 1)

        self.height = QWidget(self.bmi_ibw_abw_calculator_input)
        self.height.setObjectName(u"height")
        sizePolicy5.setHeightForWidth(self.height.sizePolicy().hasHeightForWidth())
        self.height.setSizePolicy(sizePolicy5)
        self.height.setMinimumSize(QSize(30, 0))

        self.gridLayout.addWidget(self.height, 0, 1, 1, 1)

        self.weight_label_2 = QWidget(self.bmi_ibw_abw_calculator_input)
        self.weight_label_2.setObjectName(u"weight_label_2")
        sizePolicy5.setHeightForWidth(self.weight_label_2.sizePolicy().hasHeightForWidth())
        self.weight_label_2.setSizePolicy(sizePolicy5)
        self.weight_label_2.setMinimumSize(QSize(30, 0))

        self.gridLayout.addWidget(self.weight_label_2, 1, 0, 1, 1)

        self.weight_2 = QWidget(self.bmi_ibw_abw_calculator_input)
        self.weight_2.setObjectName(u"weight_2")
        sizePolicy5.setHeightForWidth(self.weight_2.sizePolicy().hasHeightForWidth())
        self.weight_2.setSizePolicy(sizePolicy5)
        self.weight_2.setMinimumSize(QSize(30, 0))

        self.gridLayout.addWidget(self.weight_2, 1, 1, 1, 1)

        self.bmi_label = QWidget(self.bmi_ibw_abw_calculator_input)
        self.bmi_label.setObjectName(u"bmi_label")
        sizePolicy5.setHeightForWidth(self.bmi_label.sizePolicy().hasHeightForWidth())
        self.bmi_label.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.bmi_label, 2, 0, 1, 1)

        self.bmi = QWidget(self.bmi_ibw_abw_calculator_input)
        self.bmi.setObjectName(u"bmi")
        sizePolicy5.setHeightForWidth(self.bmi.sizePolicy().hasHeightForWidth())
        self.bmi.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.bmi, 2, 1, 1, 1)


        self.verticalLayout_25.addWidget(self.bmi_ibw_abw_calculator_input)

        self.ibw_calculator_output = QWidget(self.ibw_abw_bmi_input_output)
        self.ibw_calculator_output.setObjectName(u"ibw_calculator_output")
        sizePolicy5.setHeightForWidth(self.ibw_calculator_output.sizePolicy().hasHeightForWidth())
        self.ibw_calculator_output.setSizePolicy(sizePolicy5)
        self.horizontalLayout_16 = QHBoxLayout(self.ibw_calculator_output)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 6)
        self.ibw_male_label = QWidget(self.ibw_calculator_output)
        self.ibw_male_label.setObjectName(u"ibw_male_label")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy11.setHorizontalStretch(2)
        sizePolicy11.setVerticalStretch(1)
        sizePolicy11.setHeightForWidth(self.ibw_male_label.sizePolicy().hasHeightForWidth())
        self.ibw_male_label.setSizePolicy(sizePolicy11)

        self.horizontalLayout_16.addWidget(self.ibw_male_label)

        self.ibw_male = QWidget(self.ibw_calculator_output)
        self.ibw_male.setObjectName(u"ibw_male")
        sizePolicy5.setHeightForWidth(self.ibw_male.sizePolicy().hasHeightForWidth())
        self.ibw_male.setSizePolicy(sizePolicy5)

        self.horizontalLayout_16.addWidget(self.ibw_male)

        self.ibw_female_label = QWidget(self.ibw_calculator_output)
        self.ibw_female_label.setObjectName(u"ibw_female_label")
        sizePolicy11.setHeightForWidth(self.ibw_female_label.sizePolicy().hasHeightForWidth())
        self.ibw_female_label.setSizePolicy(sizePolicy11)

        self.horizontalLayout_16.addWidget(self.ibw_female_label)

        self.ibw_female = QWidget(self.ibw_calculator_output)
        self.ibw_female.setObjectName(u"ibw_female")
        sizePolicy5.setHeightForWidth(self.ibw_female.sizePolicy().hasHeightForWidth())
        self.ibw_female.setSizePolicy(sizePolicy5)

        self.horizontalLayout_16.addWidget(self.ibw_female)


        self.verticalLayout_25.addWidget(self.ibw_calculator_output)

        self.abw_calculator_output = QWidget(self.ibw_abw_bmi_input_output)
        self.abw_calculator_output.setObjectName(u"abw_calculator_output")
        sizePolicy5.setHeightForWidth(self.abw_calculator_output.sizePolicy().hasHeightForWidth())
        self.abw_calculator_output.setSizePolicy(sizePolicy5)
        self.horizontalLayout_17 = QHBoxLayout(self.abw_calculator_output)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.abw_male_label = QWidget(self.abw_calculator_output)
        self.abw_male_label.setObjectName(u"abw_male_label")
        sizePolicy11.setHeightForWidth(self.abw_male_label.sizePolicy().hasHeightForWidth())
        self.abw_male_label.setSizePolicy(sizePolicy11)

        self.horizontalLayout_17.addWidget(self.abw_male_label)

        self.abw_male = QWidget(self.abw_calculator_output)
        self.abw_male.setObjectName(u"abw_male")
        sizePolicy5.setHeightForWidth(self.abw_male.sizePolicy().hasHeightForWidth())
        self.abw_male.setSizePolicy(sizePolicy5)

        self.horizontalLayout_17.addWidget(self.abw_male)

        self.abw_female_label = QWidget(self.abw_calculator_output)
        self.abw_female_label.setObjectName(u"abw_female_label")
        sizePolicy11.setHeightForWidth(self.abw_female_label.sizePolicy().hasHeightForWidth())
        self.abw_female_label.setSizePolicy(sizePolicy11)

        self.horizontalLayout_17.addWidget(self.abw_female_label)

        self.abw_female = QWidget(self.abw_calculator_output)
        self.abw_female.setObjectName(u"abw_female")
        sizePolicy5.setHeightForWidth(self.abw_female.sizePolicy().hasHeightForWidth())
        self.abw_female.setSizePolicy(sizePolicy5)

        self.horizontalLayout_17.addWidget(self.abw_female)


        self.verticalLayout_25.addWidget(self.abw_calculator_output)


        self.verticalLayout_26.addWidget(self.ibw_abw_bmi_input_output)


        self.verticalLayout_11.addWidget(self.ibw_abw_bmi)

        self.ddi_drugs_list = QFrame(self.right)
        self.ddi_drugs_list.setObjectName(u"ddi_drugs_list")
        sizePolicy9.setHeightForWidth(self.ddi_drugs_list.sizePolicy().hasHeightForWidth())
        self.ddi_drugs_list.setSizePolicy(sizePolicy9)
        self.ddi_drugs_list.setFrameShape(QFrame.StyledPanel)
        self.ddi_drugs_list.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.ddi_drugs_list)


        self.horizontalLayout.addWidget(self.right)


        self.verticalLayout.addWidget(self.widget)

        self.scroll_area_2.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area_2)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_3 = QScrollArea(self.page_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setLineWidth(0)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 274, 242))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.left_widget = QWidget(self.scrollAreaWidgetContents_3)
        self.left_widget.setObjectName(u"left_widget")
        sizePolicy8.setHeightForWidth(self.left_widget.sizePolicy().hasHeightForWidth())
        self.left_widget.setSizePolicy(sizePolicy8)
        self.verticalLayout_6 = QVBoxLayout(self.left_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.supply_tracker_title_1 = QWidget(self.left_widget)
        self.supply_tracker_title_1.setObjectName(u"supply_tracker_title_1")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(1)
        sizePolicy12.setHeightForWidth(self.supply_tracker_title_1.sizePolicy().hasHeightForWidth())
        self.supply_tracker_title_1.setSizePolicy(sizePolicy12)

        self.verticalLayout_6.addWidget(self.supply_tracker_title_1)

        self.suup = QWidget(self.left_widget)
        self.suup.setObjectName(u"suup")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(10)
        sizePolicy13.setHeightForWidth(self.suup.sizePolicy().hasHeightForWidth())
        self.suup.setSizePolicy(sizePolicy13)
        self.formLayout = QFormLayout(self.suup)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.start_date_label_2 = QWidget(self.suup)
        self.start_date_label_2.setObjectName(u"start_date_label_2")
        sizePolicy5.setHeightForWidth(self.start_date_label_2.sizePolicy().hasHeightForWidth())
        self.start_date_label_2.setSizePolicy(sizePolicy5)
        self.start_date_label_2.setMinimumSize(QSize(30, 0))
        self.start_date_label_2.setToolTipDuration(-6)
        self.start_date_label_2.setStyleSheet(u"color:red")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.start_date_label_2)

        self.start_date_2 = QWidget(self.suup)
        self.start_date_2.setObjectName(u"start_date_2")
        sizePolicy5.setHeightForWidth(self.start_date_2.sizePolicy().hasHeightForWidth())
        self.start_date_2.setSizePolicy(sizePolicy5)
        self.start_date_2.setMinimumSize(QSize(200, 0))
        self.start_date_2.setMaximumSize(QSize(16777215, 16777215))
        self.start_date_2.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.start_date_2)

        self.duration_label_2 = QWidget(self.suup)
        self.duration_label_2.setObjectName(u"duration_label_2")
        sizePolicy5.setHeightForWidth(self.duration_label_2.sizePolicy().hasHeightForWidth())
        self.duration_label_2.setSizePolicy(sizePolicy5)
        self.duration_label_2.setMinimumSize(QSize(30, 0))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.duration_label_2)

        self.duration_2 = QWidget(self.suup)
        self.duration_2.setObjectName(u"duration_2")
        sizePolicy5.setHeightForWidth(self.duration_2.sizePolicy().hasHeightForWidth())
        self.duration_2.setSizePolicy(sizePolicy5)
        self.duration_2.setMinimumSize(QSize(200, 0))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.duration_2)

        self.end_date_label_2 = QWidget(self.suup)
        self.end_date_label_2.setObjectName(u"end_date_label_2")
        sizePolicy5.setHeightForWidth(self.end_date_label_2.sizePolicy().hasHeightForWidth())
        self.end_date_label_2.setSizePolicy(sizePolicy5)
        self.end_date_label_2.setMinimumSize(QSize(30, 0))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.end_date_label_2)

        self.end_date_2 = QWidget(self.suup)
        self.end_date_2.setObjectName(u"end_date_2")
        sizePolicy5.setHeightForWidth(self.end_date_2.sizePolicy().hasHeightForWidth())
        self.end_date_2.setSizePolicy(sizePolicy5)
        self.end_date_2.setMinimumSize(QSize(200, 0))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.end_date_2)

        self.qty_1 = QWidget(self.suup)
        self.qty_1.setObjectName(u"qty_1")
        sizePolicy5.setHeightForWidth(self.qty_1.sizePolicy().hasHeightForWidth())
        self.qty_1.setSizePolicy(sizePolicy5)
        self.qty_1.setMinimumSize(QSize(200, 0))

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.qty_1)

        self.qty_label_1 = QWidget(self.suup)
        self.qty_label_1.setObjectName(u"qty_label_1")
        sizePolicy5.setHeightForWidth(self.qty_label_1.sizePolicy().hasHeightForWidth())
        self.qty_label_1.setSizePolicy(sizePolicy5)
        self.qty_label_1.setMinimumSize(QSize(30, 0))

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.qty_label_1)

        self.qty_2 = QWidget(self.suup)
        self.qty_2.setObjectName(u"qty_2")
        sizePolicy5.setHeightForWidth(self.qty_2.sizePolicy().hasHeightForWidth())
        self.qty_2.setSizePolicy(sizePolicy5)
        self.qty_2.setMinimumSize(QSize(200, 0))

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.qty_2)

        self.qty_label_2 = QWidget(self.suup)
        self.qty_label_2.setObjectName(u"qty_label_2")
        sizePolicy5.setHeightForWidth(self.qty_label_2.sizePolicy().hasHeightForWidth())
        self.qty_label_2.setSizePolicy(sizePolicy5)
        self.qty_label_2.setMinimumSize(QSize(30, 0))

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.qty_label_2)

        self.oversupplied = QWidget(self.suup)
        self.oversupplied.setObjectName(u"oversupplied")
        sizePolicy.setHeightForWidth(self.oversupplied.sizePolicy().hasHeightForWidth())
        self.oversupplied.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.oversupplied)

        self.oversupplied_label = QWidget(self.suup)
        self.oversupplied_label.setObjectName(u"oversupplied_label")
        sizePolicy5.setHeightForWidth(self.oversupplied_label.sizePolicy().hasHeightForWidth())
        self.oversupplied_label.setSizePolicy(sizePolicy5)
        self.oversupplied_label.setMinimumSize(QSize(30, 0))

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.oversupplied_label)


        self.verticalLayout_6.addWidget(self.suup)

        self.calculate_qty = QWidget(self.left_widget)
        self.calculate_qty.setObjectName(u"calculate_qty")
        sizePolicy3.setHeightForWidth(self.calculate_qty.sizePolicy().hasHeightForWidth())
        self.calculate_qty.setSizePolicy(sizePolicy3)
        self.verticalLayout_17 = QVBoxLayout(self.calculate_qty)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.input_section = QWidget(self.calculate_qty)
        self.input_section.setObjectName(u"input_section")
        sizePolicy.setHeightForWidth(self.input_section.sizePolicy().hasHeightForWidth())
        self.input_section.setSizePolicy(sizePolicy)
        self.verticalLayout_8 = QVBoxLayout(self.input_section)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.input_text = QWidget(self.input_section)
        self.input_text.setObjectName(u"input_text")
        sizePolicy7.setHeightForWidth(self.input_text.sizePolicy().hasHeightForWidth())
        self.input_text.setSizePolicy(sizePolicy7)
        self.horizontalLayout_9 = QHBoxLayout(self.input_text)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.verticalLayout_8.addWidget(self.input_text)

        self.claer_process_btns = QWidget(self.input_section)
        self.claer_process_btns.setObjectName(u"claer_process_btns")
        sizePolicy2.setHeightForWidth(self.claer_process_btns.sizePolicy().hasHeightForWidth())
        self.claer_process_btns.setSizePolicy(sizePolicy2)
        self.horizontalLayout_11 = QHBoxLayout(self.claer_process_btns)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.process_btn = QWidget(self.claer_process_btns)
        self.process_btn.setObjectName(u"process_btn")
        sizePolicy12.setHeightForWidth(self.process_btn.sizePolicy().hasHeightForWidth())
        self.process_btn.setSizePolicy(sizePolicy12)
        self.verticalLayout_18 = QVBoxLayout(self.process_btn)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")

        self.horizontalLayout_11.addWidget(self.process_btn)

        self.clear_btn = QWidget(self.claer_process_btns)
        self.clear_btn.setObjectName(u"clear_btn")
        sizePolicy12.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy12)
        self.verticalLayout_20 = QVBoxLayout(self.clear_btn)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")

        self.horizontalLayout_11.addWidget(self.clear_btn)


        self.verticalLayout_8.addWidget(self.claer_process_btns)


        self.verticalLayout_17.addWidget(self.input_section)


        self.verticalLayout_6.addWidget(self.calculate_qty)

        self.calculate_duration_title_1 = QWidget(self.left_widget)
        self.calculate_duration_title_1.setObjectName(u"calculate_duration_title_1")
        sizePolicy12.setHeightForWidth(self.calculate_duration_title_1.sizePolicy().hasHeightForWidth())
        self.calculate_duration_title_1.setSizePolicy(sizePolicy12)

        self.verticalLayout_6.addWidget(self.calculate_duration_title_1)

        self.calculate_duration = QWidget(self.left_widget)
        self.calculate_duration.setObjectName(u"calculate_duration")
        sizePolicy13.setHeightForWidth(self.calculate_duration.sizePolicy().hasHeightForWidth())
        self.calculate_duration.setSizePolicy(sizePolicy13)
        self.formLayout_3 = QFormLayout(self.calculate_duration)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.start_date_label_1 = QWidget(self.calculate_duration)
        self.start_date_label_1.setObjectName(u"start_date_label_1")
        sizePolicy5.setHeightForWidth(self.start_date_label_1.sizePolicy().hasHeightForWidth())
        self.start_date_label_1.setSizePolicy(sizePolicy5)
        self.start_date_label_1.setMinimumSize(QSize(30, 0))

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.start_date_label_1)

        self.start_date_1 = QWidget(self.calculate_duration)
        self.start_date_1.setObjectName(u"start_date_1")
        sizePolicy11.setHeightForWidth(self.start_date_1.sizePolicy().hasHeightForWidth())
        self.start_date_1.setSizePolicy(sizePolicy11)
        self.start_date_1.setMinimumSize(QSize(200, 0))

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.start_date_1)

        self.end_date_1 = QWidget(self.calculate_duration)
        self.end_date_1.setObjectName(u"end_date_1")
        sizePolicy11.setHeightForWidth(self.end_date_1.sizePolicy().hasHeightForWidth())
        self.end_date_1.setSizePolicy(sizePolicy11)
        self.end_date_1.setMinimumSize(QSize(200, 0))

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.end_date_1)

        self.duration_label_1 = QWidget(self.calculate_duration)
        self.duration_label_1.setObjectName(u"duration_label_1")
        sizePolicy5.setHeightForWidth(self.duration_label_1.sizePolicy().hasHeightForWidth())
        self.duration_label_1.setSizePolicy(sizePolicy5)
        self.duration_label_1.setMinimumSize(QSize(30, 0))

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.duration_label_1)

        self.duration_1 = QWidget(self.calculate_duration)
        self.duration_1.setObjectName(u"duration_1")
        sizePolicy11.setHeightForWidth(self.duration_1.sizePolicy().hasHeightForWidth())
        self.duration_1.setSizePolicy(sizePolicy11)
        self.duration_1.setMinimumSize(QSize(200, 0))

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.duration_1)

        self.end_date_label_1 = QWidget(self.calculate_duration)
        self.end_date_label_1.setObjectName(u"end_date_label_1")
        sizePolicy5.setHeightForWidth(self.end_date_label_1.sizePolicy().hasHeightForWidth())
        self.end_date_label_1.setSizePolicy(sizePolicy5)
        self.end_date_label_1.setMinimumSize(QSize(30, 0))

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.end_date_label_1)


        self.verticalLayout_6.addWidget(self.calculate_duration)


        self.horizontalLayout_10.addWidget(self.left_widget)

        self.right_widget = QWidget(self.scrollAreaWidgetContents_3)
        self.right_widget.setObjectName(u"right_widget")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy14.setHorizontalStretch(10)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.right_widget.sizePolicy().hasHeightForWidth())
        self.right_widget.setSizePolicy(sizePolicy14)
        self.verticalLayout_4 = QVBoxLayout(self.right_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.top_right_widget = QWidget(self.right_widget)
        self.top_right_widget.setObjectName(u"top_right_widget")
        sizePolicy.setHeightForWidth(self.top_right_widget.sizePolicy().hasHeightForWidth())
        self.top_right_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_8 = QHBoxLayout(self.top_right_widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.datawidget = QWidget(self.top_right_widget)
        self.datawidget.setObjectName(u"datawidget")
        sizePolicy.setHeightForWidth(self.datawidget.sizePolicy().hasHeightForWidth())
        self.datawidget.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.datawidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.graph = QWidget(self.datawidget)
        self.graph.setObjectName(u"graph")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(4)
        sizePolicy15.setHeightForWidth(self.graph.sizePolicy().hasHeightForWidth())
        self.graph.setSizePolicy(sizePolicy15)

        self.verticalLayout_7.addWidget(self.graph)

        self.total_table = QWidget(self.datawidget)
        self.total_table.setObjectName(u"total_table")
        sizePolicy9.setHeightForWidth(self.total_table.sizePolicy().hasHeightForWidth())
        self.total_table.setSizePolicy(sizePolicy9)

        self.verticalLayout_7.addWidget(self.total_table)


        self.horizontalLayout_8.addWidget(self.datawidget)


        self.verticalLayout_4.addWidget(self.top_right_widget)


        self.horizontalLayout_10.addWidget(self.right_widget)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_3.addWidget(self.scrollArea_3)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_12 = QVBoxLayout(self.page_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea_4 = QScrollArea(self.page_4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 74, 76))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.whole = QWidget(self.scrollAreaWidgetContents)
        self.whole.setObjectName(u"whole")
        sizePolicy.setHeightForWidth(self.whole.sizePolicy().hasHeightForWidth())
        self.whole.setSizePolicy(sizePolicy)
        self.verticalLayout_13 = QVBoxLayout(self.whole)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.right_widget_3 = QWidget(self.whole)
        self.right_widget_3.setObjectName(u"right_widget_3")
        sizePolicy5.setHeightForWidth(self.right_widget_3.sizePolicy().hasHeightForWidth())
        self.right_widget_3.setSizePolicy(sizePolicy5)
        self.horizontalLayout_12 = QHBoxLayout(self.right_widget_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.left_2 = QWidget(self.right_widget_3)
        self.left_2.setObjectName(u"left_2")
        sizePolicy1.setHeightForWidth(self.left_2.sizePolicy().hasHeightForWidth())
        self.left_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_14 = QVBoxLayout(self.left_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.parser_title = QWidget(self.left_2)
        self.parser_title.setObjectName(u"parser_title")
        sizePolicy2.setHeightForWidth(self.parser_title.sizePolicy().hasHeightForWidth())
        self.parser_title.setSizePolicy(sizePolicy2)

        self.verticalLayout_14.addWidget(self.parser_title)

        self.input_text_2 = QWidget(self.left_2)
        self.input_text_2.setObjectName(u"input_text_2")
        sizePolicy16 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy16.setHorizontalStretch(1)
        sizePolicy16.setVerticalStretch(6)
        sizePolicy16.setHeightForWidth(self.input_text_2.sizePolicy().hasHeightForWidth())
        self.input_text_2.setSizePolicy(sizePolicy16)
        self.horizontalLayout_13 = QHBoxLayout(self.input_text_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.verticalLayout_14.addWidget(self.input_text_2)

        self.claer_process_btns_2 = QWidget(self.left_2)
        self.claer_process_btns_2.setObjectName(u"claer_process_btns_2")
        sizePolicy2.setHeightForWidth(self.claer_process_btns_2.sizePolicy().hasHeightForWidth())
        self.claer_process_btns_2.setSizePolicy(sizePolicy2)
        self.horizontalLayout_14 = QHBoxLayout(self.claer_process_btns_2)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.process_btn_2 = QWidget(self.claer_process_btns_2)
        self.process_btn_2.setObjectName(u"process_btn_2")
        sizePolicy12.setHeightForWidth(self.process_btn_2.sizePolicy().hasHeightForWidth())
        self.process_btn_2.setSizePolicy(sizePolicy12)
        self.verticalLayout_19 = QVBoxLayout(self.process_btn_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")

        self.horizontalLayout_14.addWidget(self.process_btn_2)

        self.clear_btn_2 = QWidget(self.claer_process_btns_2)
        self.clear_btn_2.setObjectName(u"clear_btn_2")
        sizePolicy12.setHeightForWidth(self.clear_btn_2.sizePolicy().hasHeightForWidth())
        self.clear_btn_2.setSizePolicy(sizePolicy12)
        self.verticalLayout_21 = QVBoxLayout(self.clear_btn_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")

        self.horizontalLayout_14.addWidget(self.clear_btn_2)


        self.verticalLayout_14.addWidget(self.claer_process_btns_2)


        self.horizontalLayout_12.addWidget(self.left_2)

        self.right_2 = QWidget(self.right_widget_3)
        self.right_2.setObjectName(u"right_2")
        sizePolicy14.setHeightForWidth(self.right_2.sizePolicy().hasHeightForWidth())
        self.right_2.setSizePolicy(sizePolicy14)
        self.verticalLayout_15 = QVBoxLayout(self.right_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.chronic_med_list_title = QWidget(self.right_2)
        self.chronic_med_list_title.setObjectName(u"chronic_med_list_title")
        sizePolicy2.setHeightForWidth(self.chronic_med_list_title.sizePolicy().hasHeightForWidth())
        self.chronic_med_list_title.setSizePolicy(sizePolicy2)

        self.verticalLayout_15.addWidget(self.chronic_med_list_title)

        self.chronic_med_list = QWidget(self.right_2)
        self.chronic_med_list.setObjectName(u"chronic_med_list")
        sizePolicy17 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(20)
        sizePolicy17.setHeightForWidth(self.chronic_med_list.sizePolicy().hasHeightForWidth())
        self.chronic_med_list.setSizePolicy(sizePolicy17)

        self.verticalLayout_15.addWidget(self.chronic_med_list)

        self.prn_med_list_title = QWidget(self.right_2)
        self.prn_med_list_title.setObjectName(u"prn_med_list_title")
        sizePolicy2.setHeightForWidth(self.prn_med_list_title.sizePolicy().hasHeightForWidth())
        self.prn_med_list_title.setSizePolicy(sizePolicy2)

        self.verticalLayout_15.addWidget(self.prn_med_list_title)

        self.prn_med_list = QWidget(self.right_2)
        self.prn_med_list.setObjectName(u"prn_med_list")
        sizePolicy13.setHeightForWidth(self.prn_med_list.sizePolicy().hasHeightForWidth())
        self.prn_med_list.setSizePolicy(sizePolicy13)

        self.verticalLayout_15.addWidget(self.prn_med_list)


        self.horizontalLayout_12.addWidget(self.right_2)


        self.verticalLayout_13.addWidget(self.right_widget_3)


        self.verticalLayout_16.addWidget(self.whole)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea_4)

        self.pages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_9 = QVBoxLayout(self.page_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea_5 = QScrollArea(self.page_5)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setStyleSheet(u"")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 707, 646))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.left_widget_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.left_widget_2.setObjectName(u"left_widget_2")
        sizePolicy8.setHeightForWidth(self.left_widget_2.sizePolicy().hasHeightForWidth())
        self.left_widget_2.setSizePolicy(sizePolicy8)
        self.verticalLayout_22 = QVBoxLayout(self.left_widget_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.finder_title_pane = QWidget(self.left_widget_2)
        self.finder_title_pane.setObjectName(u"finder_title_pane")
        sizePolicy12.setHeightForWidth(self.finder_title_pane.sizePolicy().hasHeightForWidth())
        self.finder_title_pane.setSizePolicy(sizePolicy12)

        self.verticalLayout_22.addWidget(self.finder_title_pane)

        self.postal_input = QWidget(self.left_widget_2)
        self.postal_input.setObjectName(u"postal_input")
        sizePolicy13.setHeightForWidth(self.postal_input.sizePolicy().hasHeightForWidth())
        self.postal_input.setSizePolicy(sizePolicy13)
        self.formLayout_5 = QFormLayout(self.postal_input)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_5.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.postal_label_pane = QWidget(self.postal_input)
        self.postal_label_pane.setObjectName(u"postal_label_pane")
        sizePolicy5.setHeightForWidth(self.postal_label_pane.sizePolicy().hasHeightForWidth())
        self.postal_label_pane.setSizePolicy(sizePolicy5)
        self.postal_label_pane.setMinimumSize(QSize(30, 0))
        self.postal_label_pane.setToolTipDuration(-6)
        self.postal_label_pane.setStyleSheet(u"color:red")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.postal_label_pane)

        self.postal_input_pane = QWidget(self.postal_input)
        self.postal_input_pane.setObjectName(u"postal_input_pane")
        sizePolicy5.setHeightForWidth(self.postal_input_pane.sizePolicy().hasHeightForWidth())
        self.postal_input_pane.setSizePolicy(sizePolicy5)
        self.postal_input_pane.setMinimumSize(QSize(200, 0))
        self.postal_input_pane.setMaximumSize(QSize(16777215, 16777215))
        self.postal_input_pane.setStyleSheet(u"")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.postal_input_pane)


        self.verticalLayout_22.addWidget(self.postal_input)

        self.nil = QWidget(self.left_widget_2)
        self.nil.setObjectName(u"nil")
        sizePolicy2.setHeightForWidth(self.nil.sizePolicy().hasHeightForWidth())
        self.nil.setSizePolicy(sizePolicy2)
        self.verticalLayout_23 = QVBoxLayout(self.nil)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_22.addWidget(self.nil)

        self.nil_2 = QWidget(self.left_widget_2)
        self.nil_2.setObjectName(u"nil_2")
        sizePolicy3.setHeightForWidth(self.nil_2.sizePolicy().hasHeightForWidth())
        self.nil_2.setSizePolicy(sizePolicy3)
        self.formLayout_6 = QFormLayout(self.nil_2)
        self.formLayout_6.setObjectName(u"formLayout_6")

        self.verticalLayout_22.addWidget(self.nil_2)

        self.nil_4 = QWidget(self.left_widget_2)
        self.nil_4.setObjectName(u"nil_4")
        sizePolicy12.setHeightForWidth(self.nil_4.sizePolicy().hasHeightForWidth())
        self.nil_4.setSizePolicy(sizePolicy12)

        self.verticalLayout_22.addWidget(self.nil_4)

        self.nil_3 = QWidget(self.left_widget_2)
        self.nil_3.setObjectName(u"nil_3")
        sizePolicy13.setHeightForWidth(self.nil_3.sizePolicy().hasHeightForWidth())
        self.nil_3.setSizePolicy(sizePolicy13)
        self.formLayout_7 = QFormLayout(self.nil_3)
        self.formLayout_7.setObjectName(u"formLayout_7")

        self.verticalLayout_22.addWidget(self.nil_3)


        self.horizontalLayout_4.addWidget(self.left_widget_2)

        self.results_table_pane = QWidget(self.scrollAreaWidgetContents_2)
        self.results_table_pane.setObjectName(u"results_table_pane")
        sizePolicy14.setHeightForWidth(self.results_table_pane.sizePolicy().hasHeightForWidth())
        self.results_table_pane.setSizePolicy(sizePolicy14)
        self.verticalLayout_24 = QVBoxLayout(self.results_table_pane)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.results_table_pane)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_9.addWidget(self.scrollArea_5)

        self.pages.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_31 = QVBoxLayout(self.page_6)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.scrollArea_6 = QScrollArea(self.page_6)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setStyleSheet(u"")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 707, 646))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.left_widget_4 = QWidget(self.scrollAreaWidgetContents_5)
        self.left_widget_4.setObjectName(u"left_widget_4")
        sizePolicy8.setHeightForWidth(self.left_widget_4.sizePolicy().hasHeightForWidth())
        self.left_widget_4.setSizePolicy(sizePolicy8)
        self.verticalLayout_28 = QVBoxLayout(self.left_widget_4)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.mfd_title = QWidget(self.left_widget_4)
        self.mfd_title.setObjectName(u"mfd_title")
        sizePolicy18 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy18.setHorizontalStretch(6)
        sizePolicy18.setVerticalStretch(1)
        sizePolicy18.setHeightForWidth(self.mfd_title.sizePolicy().hasHeightForWidth())
        self.mfd_title.setSizePolicy(sizePolicy18)
        self.mfd_title.setCursor(QCursor(Qt.CursorShape.CrossCursor))

        self.verticalLayout_28.addWidget(self.mfd_title)

        self.mfd_coverage = QWidget(self.left_widget_4)
        self.mfd_coverage.setObjectName(u"mfd_coverage")
        sizePolicy19 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy19.setHorizontalStretch(8)
        sizePolicy19.setVerticalStretch(2)
        sizePolicy19.setHeightForWidth(self.mfd_coverage.sizePolicy().hasHeightForWidth())
        self.mfd_coverage.setSizePolicy(sizePolicy19)
        self.formLayout_11 = QFormLayout(self.mfd_coverage)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.formLayout_11.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_11.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_28.addWidget(self.mfd_coverage)

        self.mfd_exclusions = QWidget(self.left_widget_4)
        self.mfd_exclusions.setObjectName(u"mfd_exclusions")
        sizePolicy20 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy20.setHorizontalStretch(8)
        sizePolicy20.setVerticalStretch(4)
        sizePolicy20.setHeightForWidth(self.mfd_exclusions.sizePolicy().hasHeightForWidth())
        self.mfd_exclusions.setSizePolicy(sizePolicy20)
        self.formLayout_12 = QFormLayout(self.mfd_exclusions)
        self.formLayout_12.setObjectName(u"formLayout_12")

        self.verticalLayout_28.addWidget(self.mfd_exclusions)

        self.mfd_auto_switch = QWidget(self.left_widget_4)
        self.mfd_auto_switch.setObjectName(u"mfd_auto_switch")
        sizePolicy21 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy21.setHorizontalStretch(8)
        sizePolicy21.setVerticalStretch(10)
        sizePolicy21.setHeightForWidth(self.mfd_auto_switch.sizePolicy().hasHeightForWidth())
        self.mfd_auto_switch.setSizePolicy(sizePolicy21)
        self.formLayout_13 = QFormLayout(self.mfd_auto_switch)
        self.formLayout_13.setObjectName(u"formLayout_13")

        self.verticalLayout_28.addWidget(self.mfd_auto_switch)


        self.horizontalLayout_6.addWidget(self.left_widget_4)

        self.mfd_retail = QWidget(self.scrollAreaWidgetContents_5)
        self.mfd_retail.setObjectName(u"mfd_retail")
        sizePolicy22 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy22.setHorizontalStretch(2)
        sizePolicy22.setVerticalStretch(0)
        sizePolicy22.setHeightForWidth(self.mfd_retail.sizePolicy().hasHeightForWidth())
        self.mfd_retail.setSizePolicy(sizePolicy22)
        self.verticalLayout_30 = QVBoxLayout(self.mfd_retail)
        self.verticalLayout_30.setSpacing(6)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.mfd_retail)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_31.addWidget(self.scrollArea_6)

        self.pages.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_34 = QVBoxLayout(self.page_7)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.scrollArea_7 = QScrollArea(self.page_7)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setStyleSheet(u"")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 707, 646))
        self.horizontalLayout_7 = QHBoxLayout(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.left_widget_5 = QWidget(self.scrollAreaWidgetContents_6)
        self.left_widget_5.setObjectName(u"left_widget_5")
        sizePolicy8.setHeightForWidth(self.left_widget_5.sizePolicy().hasHeightForWidth())
        self.left_widget_5.setSizePolicy(sizePolicy8)
        self.verticalLayout_29 = QVBoxLayout(self.left_widget_5)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.retail_finder_title = QWidget(self.left_widget_5)
        self.retail_finder_title.setObjectName(u"retail_finder_title")
        sizePolicy12.setHeightForWidth(self.retail_finder_title.sizePolicy().hasHeightForWidth())
        self.retail_finder_title.setSizePolicy(sizePolicy12)

        self.verticalLayout_29.addWidget(self.retail_finder_title)

        self.item_name = QWidget(self.left_widget_5)
        self.item_name.setObjectName(u"item_name")
        sizePolicy13.setHeightForWidth(self.item_name.sizePolicy().hasHeightForWidth())
        self.item_name.setSizePolicy(sizePolicy13)
        self.formLayout_14 = QFormLayout(self.item_name)
        self.formLayout_14.setObjectName(u"formLayout_14")
        self.formLayout_14.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_14.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.item_name_label = QWidget(self.item_name)
        self.item_name_label.setObjectName(u"item_name_label")
        sizePolicy5.setHeightForWidth(self.item_name_label.sizePolicy().hasHeightForWidth())
        self.item_name_label.setSizePolicy(sizePolicy5)
        self.item_name_label.setMinimumSize(QSize(30, 0))
        self.item_name_label.setToolTipDuration(-6)
        self.item_name_label.setStyleSheet(u"color:red")

        self.formLayout_14.setWidget(0, QFormLayout.ItemRole.LabelRole, self.item_name_label)

        self.item_name_input = QWidget(self.item_name)
        self.item_name_input.setObjectName(u"item_name_input")
        sizePolicy5.setHeightForWidth(self.item_name_input.sizePolicy().hasHeightForWidth())
        self.item_name_input.setSizePolicy(sizePolicy5)
        self.item_name_input.setMinimumSize(QSize(200, 0))
        self.item_name_input.setMaximumSize(QSize(16777215, 16777215))
        self.item_name_input.setStyleSheet(u"")

        self.formLayout_14.setWidget(0, QFormLayout.ItemRole.FieldRole, self.item_name_input)


        self.verticalLayout_29.addWidget(self.item_name)

        self.nil_9 = QWidget(self.left_widget_5)
        self.nil_9.setObjectName(u"nil_9")
        sizePolicy2.setHeightForWidth(self.nil_9.sizePolicy().hasHeightForWidth())
        self.nil_9.setSizePolicy(sizePolicy2)
        self.verticalLayout_32 = QVBoxLayout(self.nil_9)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_29.addWidget(self.nil_9)

        self.nil_10 = QWidget(self.left_widget_5)
        self.nil_10.setObjectName(u"nil_10")
        sizePolicy3.setHeightForWidth(self.nil_10.sizePolicy().hasHeightForWidth())
        self.nil_10.setSizePolicy(sizePolicy3)
        self.formLayout_15 = QFormLayout(self.nil_10)
        self.formLayout_15.setObjectName(u"formLayout_15")

        self.verticalLayout_29.addWidget(self.nil_10)

        self.nil_11 = QWidget(self.left_widget_5)
        self.nil_11.setObjectName(u"nil_11")
        sizePolicy12.setHeightForWidth(self.nil_11.sizePolicy().hasHeightForWidth())
        self.nil_11.setSizePolicy(sizePolicy12)

        self.verticalLayout_29.addWidget(self.nil_11)

        self.nil_12 = QWidget(self.left_widget_5)
        self.nil_12.setObjectName(u"nil_12")
        sizePolicy13.setHeightForWidth(self.nil_12.sizePolicy().hasHeightForWidth())
        self.nil_12.setSizePolicy(sizePolicy13)
        self.formLayout_16 = QFormLayout(self.nil_12)
        self.formLayout_16.setObjectName(u"formLayout_16")

        self.verticalLayout_29.addWidget(self.nil_12)


        self.horizontalLayout_7.addWidget(self.left_widget_5)

        self.retail_results_table_pane = QWidget(self.scrollAreaWidgetContents_6)
        self.retail_results_table_pane.setObjectName(u"retail_results_table_pane")
        sizePolicy14.setHeightForWidth(self.retail_results_table_pane.sizePolicy().hasHeightForWidth())
        self.retail_results_table_pane.setSizePolicy(sizePolicy14)
        self.verticalLayout_33 = QVBoxLayout(self.retail_results_table_pane)
        self.verticalLayout_33.setSpacing(6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_7.addWidget(self.retail_results_table_pane)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_34.addWidget(self.scrollArea_7)

        self.pages.addWidget(self.page_7)

        self.verticalLayout_10.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To MedAegis", None))
    # retranslateUi

