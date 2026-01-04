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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLayout, QScrollArea, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1192, 863)
        self.verticalLayout_10 = QVBoxLayout(MainPages)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
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
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area_2 = QScrollArea(self.page_2)
        self.scroll_area_2.setObjectName(u"scroll_area_2")
        self.scroll_area_2.setStyleSheet(u"background: transparent;")
        self.scroll_area_2.setFrameShape(QFrame.NoFrame)
        self.scroll_area_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_2.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 1172, 843))
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
        self.result_male_label_1 = QWidget(self.crcl_calculator_output)
        self.result_male_label_1.setObjectName(u"result_male_label_1")
        sizePolicy5.setHeightForWidth(self.result_male_label_1.sizePolicy().hasHeightForWidth())
        self.result_male_label_1.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.result_male_label_1)

        self.val_male_1 = QWidget(self.crcl_calculator_output)
        self.val_male_1.setObjectName(u"val_male_1")
        sizePolicy5.setHeightForWidth(self.val_male_1.sizePolicy().hasHeightForWidth())
        self.val_male_1.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.val_male_1)

        self.result_female_label_1 = QWidget(self.crcl_calculator_output)
        self.result_female_label_1.setObjectName(u"result_female_label_1")
        sizePolicy5.setHeightForWidth(self.result_female_label_1.sizePolicy().hasHeightForWidth())
        self.result_female_label_1.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.result_female_label_1)

        self.val_female_1 = QWidget(self.crcl_calculator_output)
        self.val_female_1.setObjectName(u"val_female_1")
        sizePolicy5.setHeightForWidth(self.val_female_1.sizePolicy().hasHeightForWidth())
        self.val_female_1.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.val_female_1)


        self.verticalLayout_2.addWidget(self.crcl_calculator_output)

        self.widget_2 = QWidget(self.crcl_calculator_input_output)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(6)
        sizePolicy7.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy7)

        self.verticalLayout_2.addWidget(self.widget_2)


        self.verticalLayout_5.addWidget(self.crcl_calculator_input_output)


        self.horizontalLayout.addWidget(self.left)

        self.right = QWidget(self.widget)
        self.right.setObjectName(u"right")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(3)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.right.sizePolicy().hasHeightForWidth())
        self.right.setSizePolicy(sizePolicy8)

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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1170, 841))
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
        self.calculate_duration_title_1 = QWidget(self.left_widget)
        self.calculate_duration_title_1.setObjectName(u"calculate_duration_title_1")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(1)
        sizePolicy9.setHeightForWidth(self.calculate_duration_title_1.sizePolicy().hasHeightForWidth())
        self.calculate_duration_title_1.setSizePolicy(sizePolicy9)

        self.verticalLayout_6.addWidget(self.calculate_duration_title_1)

        self.calculate_duration = QWidget(self.left_widget)
        self.calculate_duration.setObjectName(u"calculate_duration")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(10)
        sizePolicy10.setHeightForWidth(self.calculate_duration.sizePolicy().hasHeightForWidth())
        self.calculate_duration.setSizePolicy(sizePolicy10)
        self.formLayout = QFormLayout(self.calculate_duration)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.start_date_label_1 = QWidget(self.calculate_duration)
        self.start_date_label_1.setObjectName(u"start_date_label_1")
        sizePolicy5.setHeightForWidth(self.start_date_label_1.sizePolicy().hasHeightForWidth())
        self.start_date_label_1.setSizePolicy(sizePolicy5)
        self.start_date_label_1.setMinimumSize(QSize(30, 0))
        self.start_date_label_1.setToolTipDuration(-6)
        self.start_date_label_1.setStyleSheet(u"color:red")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.start_date_label_1)

        self.start_date_1 = QWidget(self.calculate_duration)
        self.start_date_1.setObjectName(u"start_date_1")
        sizePolicy5.setHeightForWidth(self.start_date_1.sizePolicy().hasHeightForWidth())
        self.start_date_1.setSizePolicy(sizePolicy5)
        self.start_date_1.setMinimumSize(QSize(200, 0))
        self.start_date_1.setMaximumSize(QSize(16777215, 16777215))
        self.start_date_1.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.start_date_1)

        self.end_date_label_1 = QWidget(self.calculate_duration)
        self.end_date_label_1.setObjectName(u"end_date_label_1")
        sizePolicy5.setHeightForWidth(self.end_date_label_1.sizePolicy().hasHeightForWidth())
        self.end_date_label_1.setSizePolicy(sizePolicy5)
        self.end_date_label_1.setMinimumSize(QSize(30, 0))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.end_date_label_1)

        self.end_date_1 = QWidget(self.calculate_duration)
        self.end_date_1.setObjectName(u"end_date_1")
        sizePolicy5.setHeightForWidth(self.end_date_1.sizePolicy().hasHeightForWidth())
        self.end_date_1.setSizePolicy(sizePolicy5)
        self.end_date_1.setMinimumSize(QSize(200, 0))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.end_date_1)

        self.duration_label_1 = QWidget(self.calculate_duration)
        self.duration_label_1.setObjectName(u"duration_label_1")
        sizePolicy5.setHeightForWidth(self.duration_label_1.sizePolicy().hasHeightForWidth())
        self.duration_label_1.setSizePolicy(sizePolicy5)
        self.duration_label_1.setMinimumSize(QSize(30, 0))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.duration_label_1)

        self.duration_1 = QWidget(self.calculate_duration)
        self.duration_1.setObjectName(u"duration_1")
        sizePolicy5.setHeightForWidth(self.duration_1.sizePolicy().hasHeightForWidth())
        self.duration_1.setSizePolicy(sizePolicy5)
        self.duration_1.setMinimumSize(QSize(200, 0))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.duration_1)


        self.verticalLayout_6.addWidget(self.calculate_duration)

        self.calculate_qty_title_1 = QWidget(self.left_widget)
        self.calculate_qty_title_1.setObjectName(u"calculate_qty_title_1")
        sizePolicy2.setHeightForWidth(self.calculate_qty_title_1.sizePolicy().hasHeightForWidth())
        self.calculate_qty_title_1.setSizePolicy(sizePolicy2)
        self.verticalLayout_11 = QVBoxLayout(self.calculate_qty_title_1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_6.addWidget(self.calculate_qty_title_1)

        self.calculate_qty = QWidget(self.left_widget)
        self.calculate_qty.setObjectName(u"calculate_qty")
        sizePolicy3.setHeightForWidth(self.calculate_qty.sizePolicy().hasHeightForWidth())
        self.calculate_qty.setSizePolicy(sizePolicy3)
        self.formLayout_2 = QFormLayout(self.calculate_qty)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.qty_label_1 = QWidget(self.calculate_qty)
        self.qty_label_1.setObjectName(u"qty_label_1")
        sizePolicy5.setHeightForWidth(self.qty_label_1.sizePolicy().hasHeightForWidth())
        self.qty_label_1.setSizePolicy(sizePolicy5)
        self.qty_label_1.setMinimumSize(QSize(30, 0))

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.qty_label_1)

        self.qty_1 = QWidget(self.calculate_qty)
        self.qty_1.setObjectName(u"qty_1")
        sizePolicy5.setHeightForWidth(self.qty_1.sizePolicy().hasHeightForWidth())
        self.qty_1.setSizePolicy(sizePolicy5)
        self.qty_1.setMinimumSize(QSize(200, 0))

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.qty_1)

        self.qty_label_2 = QWidget(self.calculate_qty)
        self.qty_label_2.setObjectName(u"qty_label_2")
        sizePolicy5.setHeightForWidth(self.qty_label_2.sizePolicy().hasHeightForWidth())
        self.qty_label_2.setSizePolicy(sizePolicy5)
        self.qty_label_2.setMinimumSize(QSize(30, 0))

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.qty_label_2)

        self.qty_label_3 = QWidget(self.calculate_qty)
        self.qty_label_3.setObjectName(u"qty_label_3")
        sizePolicy5.setHeightForWidth(self.qty_label_3.sizePolicy().hasHeightForWidth())
        self.qty_label_3.setSizePolicy(sizePolicy5)
        self.qty_label_3.setMinimumSize(QSize(30, 0))

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.qty_label_3)

        self.qty_3 = QWidget(self.calculate_qty)
        self.qty_3.setObjectName(u"qty_3")
        sizePolicy5.setHeightForWidth(self.qty_3.sizePolicy().hasHeightForWidth())
        self.qty_3.setSizePolicy(sizePolicy5)
        self.qty_3.setMinimumSize(QSize(200, 0))

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.qty_3)

        self.qty_2 = QWidget(self.calculate_qty)
        self.qty_2.setObjectName(u"qty_2")
        sizePolicy5.setHeightForWidth(self.qty_2.sizePolicy().hasHeightForWidth())
        self.qty_2.setSizePolicy(sizePolicy5)
        self.qty_2.setMinimumSize(QSize(200, 0))

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.qty_2)

        self.duration_label_2 = QWidget(self.calculate_qty)
        self.duration_label_2.setObjectName(u"duration_label_2")
        sizePolicy5.setHeightForWidth(self.duration_label_2.sizePolicy().hasHeightForWidth())
        self.duration_label_2.setSizePolicy(sizePolicy5)
        self.duration_label_2.setMinimumSize(QSize(30, 0))

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.duration_label_2)

        self.duration_2 = QWidget(self.calculate_qty)
        self.duration_2.setObjectName(u"duration_2")
        sizePolicy5.setHeightForWidth(self.duration_2.sizePolicy().hasHeightForWidth())
        self.duration_2.setSizePolicy(sizePolicy5)
        self.duration_2.setMinimumSize(QSize(200, 0))

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.duration_2)


        self.verticalLayout_6.addWidget(self.calculate_qty)

        self.calculate_end_date_title_1 = QWidget(self.left_widget)
        self.calculate_end_date_title_1.setObjectName(u"calculate_end_date_title_1")
        sizePolicy9.setHeightForWidth(self.calculate_end_date_title_1.sizePolicy().hasHeightForWidth())
        self.calculate_end_date_title_1.setSizePolicy(sizePolicy9)

        self.verticalLayout_6.addWidget(self.calculate_end_date_title_1)

        self.calculate_end_date_1 = QWidget(self.left_widget)
        self.calculate_end_date_1.setObjectName(u"calculate_end_date_1")
        sizePolicy10.setHeightForWidth(self.calculate_end_date_1.sizePolicy().hasHeightForWidth())
        self.calculate_end_date_1.setSizePolicy(sizePolicy10)
        self.formLayout_3 = QFormLayout(self.calculate_end_date_1)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.start_date_label_2 = QWidget(self.calculate_end_date_1)
        self.start_date_label_2.setObjectName(u"start_date_label_2")
        sizePolicy5.setHeightForWidth(self.start_date_label_2.sizePolicy().hasHeightForWidth())
        self.start_date_label_2.setSizePolicy(sizePolicy5)
        self.start_date_label_2.setMinimumSize(QSize(30, 0))

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.start_date_label_2)

        self.start_date_2 = QWidget(self.calculate_end_date_1)
        self.start_date_2.setObjectName(u"start_date_2")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy11.setHorizontalStretch(2)
        sizePolicy11.setVerticalStretch(1)
        sizePolicy11.setHeightForWidth(self.start_date_2.sizePolicy().hasHeightForWidth())
        self.start_date_2.setSizePolicy(sizePolicy11)
        self.start_date_2.setMinimumSize(QSize(200, 0))

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.start_date_2)

        self.duration_label_3 = QWidget(self.calculate_end_date_1)
        self.duration_label_3.setObjectName(u"duration_label_3")
        sizePolicy5.setHeightForWidth(self.duration_label_3.sizePolicy().hasHeightForWidth())
        self.duration_label_3.setSizePolicy(sizePolicy5)
        self.duration_label_3.setMinimumSize(QSize(30, 0))

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.duration_label_3)

        self.duration_3 = QWidget(self.calculate_end_date_1)
        self.duration_3.setObjectName(u"duration_3")
        sizePolicy11.setHeightForWidth(self.duration_3.sizePolicy().hasHeightForWidth())
        self.duration_3.setSizePolicy(sizePolicy11)
        self.duration_3.setMinimumSize(QSize(200, 0))

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.duration_3)

        self.end_date_label_2 = QWidget(self.calculate_end_date_1)
        self.end_date_label_2.setObjectName(u"end_date_label_2")
        sizePolicy5.setHeightForWidth(self.end_date_label_2.sizePolicy().hasHeightForWidth())
        self.end_date_label_2.setSizePolicy(sizePolicy5)
        self.end_date_label_2.setMinimumSize(QSize(30, 0))

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.end_date_label_2)

        self.end_date_2 = QWidget(self.calculate_end_date_1)
        self.end_date_2.setObjectName(u"end_date_2")
        sizePolicy11.setHeightForWidth(self.end_date_2.sizePolicy().hasHeightForWidth())
        self.end_date_2.setSizePolicy(sizePolicy11)
        self.end_date_2.setMinimumSize(QSize(200, 0))

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.end_date_2)


        self.verticalLayout_6.addWidget(self.calculate_end_date_1)


        self.horizontalLayout_10.addWidget(self.left_widget)

        self.right_widget = QWidget(self.scrollAreaWidgetContents_3)
        self.right_widget.setObjectName(u"right_widget")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy12.setHorizontalStretch(10)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.right_widget.sizePolicy().hasHeightForWidth())
        self.right_widget.setSizePolicy(sizePolicy12)
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
        self.input_section = QWidget(self.top_right_widget)
        self.input_section.setObjectName(u"input_section")
        sizePolicy.setHeightForWidth(self.input_section.sizePolicy().hasHeightForWidth())
        self.input_section.setSizePolicy(sizePolicy)
        self.verticalLayout_8 = QVBoxLayout(self.input_section)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.supply_tracker_title_1 = QWidget(self.input_section)
        self.supply_tracker_title_1.setObjectName(u"supply_tracker_title_1")
        sizePolicy.setHeightForWidth(self.supply_tracker_title_1.sizePolicy().hasHeightForWidth())
        self.supply_tracker_title_1.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.supply_tracker_title_1)

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
        sizePolicy9.setHeightForWidth(self.process_btn.sizePolicy().hasHeightForWidth())
        self.process_btn.setSizePolicy(sizePolicy9)
        self.verticalLayout_18 = QVBoxLayout(self.process_btn)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")

        self.horizontalLayout_11.addWidget(self.process_btn)

        self.clear_btn = QWidget(self.claer_process_btns)
        self.clear_btn.setObjectName(u"clear_btn")
        sizePolicy9.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy9)
        self.verticalLayout_20 = QVBoxLayout(self.clear_btn)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")

        self.horizontalLayout_11.addWidget(self.clear_btn)


        self.verticalLayout_8.addWidget(self.claer_process_btns)


        self.horizontalLayout_8.addWidget(self.input_section)

        self.datawidget = QWidget(self.top_right_widget)
        self.datawidget.setObjectName(u"datawidget")
        sizePolicy.setHeightForWidth(self.datawidget.sizePolicy().hasHeightForWidth())
        self.datawidget.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QVBoxLayout(self.datawidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.total_table = QWidget(self.datawidget)
        self.total_table.setObjectName(u"total_table")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(6)
        sizePolicy13.setHeightForWidth(self.total_table.sizePolicy().hasHeightForWidth())
        self.total_table.setSizePolicy(sizePolicy13)

        self.verticalLayout_9.addWidget(self.total_table)

        self.dataframe = QWidget(self.datawidget)
        self.dataframe.setObjectName(u"dataframe")
        sizePolicy3.setHeightForWidth(self.dataframe.sizePolicy().hasHeightForWidth())
        self.dataframe.setSizePolicy(sizePolicy3)

        self.verticalLayout_9.addWidget(self.dataframe)


        self.horizontalLayout_8.addWidget(self.datawidget)


        self.verticalLayout_4.addWidget(self.top_right_widget)

        self.graph = QWidget(self.right_widget)
        self.graph.setObjectName(u"graph")
        sizePolicy.setHeightForWidth(self.graph.sizePolicy().hasHeightForWidth())
        self.graph.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.graph)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.graph)


        self.horizontalLayout_10.addWidget(self.right_widget)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_3.addWidget(self.scrollArea_3)

        self.pages.addWidget(self.page_3)

        self.verticalLayout_10.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To MedAegis", None))
    # retranslateUi

