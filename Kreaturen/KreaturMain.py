# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KreaturMain.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QSplitter, QTabWidget, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_formMain(object):
    def setupUi(self, formMain):
        if not formMain.objectName():
            formMain.setObjectName(u"formMain")
        formMain.setWindowModality(Qt.WindowModality.ApplicationModal)
        formMain.resize(1062, 696)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(formMain.sizePolicy().hasHeightForWidth())
        formMain.setSizePolicy(sizePolicy)
        formMain.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.verticalLayout_3 = QVBoxLayout(formMain)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(formMain)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy2)
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(20, 20, 20, 20)
        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMaximumSize(QSize(16777215, 200))
        self.gridLayout_16 = QGridLayout(self.groupBox_7)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setVerticalSpacing(6)
        self.leQuelle = QLineEdit(self.groupBox_7)
        self.leQuelle.setObjectName(u"leQuelle")

        self.gridLayout_12.addWidget(self.leQuelle, 2, 1, 1, 3)

        self.label = QLabel(self.groupBox_7)
        self.label.setObjectName(u"label")
        self.label.setMouseTracking(True)

        self.gridLayout_12.addWidget(self.label, 1, 0, 1, 1)

        self.label_19 = QLabel(self.groupBox_7)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_12.addWidget(self.label_19, 3, 0, 1, 1)

        self.leName = QLineEdit(self.groupBox_7)
        self.leName.setObjectName(u"leName")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leName.sizePolicy().hasHeightForWidth())
        self.leName.setSizePolicy(sizePolicy3)
        self.leName.setMinimumSize(QSize(300, 0))

        self.gridLayout_12.addWidget(self.leName, 0, 1, 1, 1)

        self.cbTyp = QComboBox(self.groupBox_7)
        self.cbTyp.setObjectName(u"cbTyp")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cbTyp.sizePolicy().hasHeightForWidth())
        self.cbTyp.setSizePolicy(sizePolicy4)

        self.gridLayout_12.addWidget(self.cbTyp, 0, 5, 1, 1)

        self.laID = QLabel(self.groupBox_7)
        self.laID.setObjectName(u"laID")

        self.gridLayout_12.addWidget(self.laID, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.leAbenteuer = QLineEdit(self.groupBox_7)
        self.leAbenteuer.setObjectName(u"leAbenteuer")

        self.gridLayout_12.addWidget(self.leAbenteuer, 3, 1, 1, 3)

        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_12.addWidget(self.label_4, 2, 0, 1, 1)

        self.cbPublik = QCheckBox(self.groupBox_7)
        self.cbPublik.setObjectName(u"cbPublik")

        self.gridLayout_12.addWidget(self.cbPublik, 2, 5, 1, 1)

        self.leKurzbeschreibung = QLineEdit(self.groupBox_7)
        self.leKurzbeschreibung.setObjectName(u"leKurzbeschreibung")
        sizePolicy4.setHeightForWidth(self.leKurzbeschreibung.sizePolicy().hasHeightForWidth())
        self.leKurzbeschreibung.setSizePolicy(sizePolicy4)
        self.leKurzbeschreibung.setFrame(True)

        self.gridLayout_12.addWidget(self.leKurzbeschreibung, 1, 1, 1, 5)

        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 0))
        self.label_14.setMaximumSize(QSize(250, 16777215))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_12.addWidget(self.label_14, 0, 4, 1, 1)

        self.label_2 = QLabel(self.groupBox_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_12.addWidget(self.label_2, 0, 0, 1, 1)

        self.cbNSC = QCheckBox(self.groupBox_7)
        self.cbNSC.setObjectName(u"cbNSC")

        self.gridLayout_12.addWidget(self.cbNSC, 3, 5, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_12, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_7, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.leGSS_label = QLineEdit(self.groupBox_2)
        self.leGSS_label.setObjectName(u"leGSS_label")
        self.leGSS_label.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_3.addWidget(self.leGSS_label, 4, 8, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_8, 0, 2, 1, 1)

        self.sbINI = QSpinBox(self.groupBox_2)
        self.sbINI.setObjectName(u"sbINI")
        self.sbINI.setMaximumSize(QSize(50, 16777215))
        self.sbINI.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbINI.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbINI, 4, 3, 1, 1)

        self.sbASP = QSpinBox(self.groupBox_2)
        self.sbASP.setObjectName(u"sbASP")

        self.gridLayout_3.addWidget(self.sbASP, 3, 5, 1, 1)

        self.sbKAP = QSpinBox(self.groupBox_2)
        self.sbKAP.setObjectName(u"sbKAP")

        self.gridLayout_3.addWidget(self.sbKAP, 4, 5, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_7, 1, 4, 1, 1)

        self.label_25 = QLabel(self.groupBox_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_25, 4, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_12, 1, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_9, 1, 6, 1, 1)

        self.sbKL = QSpinBox(self.groupBox_2)
        self.sbKL.setObjectName(u"sbKL")
        self.sbKL.setMaximumSize(QSize(50, 16777215))
        self.sbKL.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbKL.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbKL, 1, 3, 1, 1)

        self.label_26 = QLabel(self.groupBox_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_26, 3, 4, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_18, 3, 0, 1, 1)

        self.sbGE = QSpinBox(self.groupBox_2)
        self.sbGE.setObjectName(u"sbGE")
        self.sbGE.setMaximumSize(QSize(50, 16777215))
        self.sbGE.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbGE.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbGE, 0, 5, 1, 1)

        self.sbKK = QSpinBox(self.groupBox_2)
        self.sbKK.setObjectName(u"sbKK")
        self.sbKK.setMaximumSize(QSize(50, 16777215))
        self.sbKK.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbKK.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbKK, 0, 7, 1, 1)

        self.label_27 = QLabel(self.groupBox_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_27, 4, 4, 1, 1)

        self.sbMR = QSpinBox(self.groupBox_2)
        self.sbMR.setObjectName(u"sbMR")
        self.sbMR.setMaximumSize(QSize(50, 16777215))
        self.sbMR.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbMR.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbMR, 5, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_24, 3, 6, 1, 1)

        self.sbIN = QSpinBox(self.groupBox_2)
        self.sbIN.setObjectName(u"sbIN")
        self.sbIN.setMaximumSize(QSize(50, 16777215))
        self.sbIN.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbIN.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbIN, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_3, 5, 4, 1, 1)

        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_17, 3, 2, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_15, 4, 2, 1, 1)

        self.sbKO = QSpinBox(self.groupBox_2)
        self.sbKO.setObjectName(u"sbKO")
        self.sbKO.setMinimumSize(QSize(0, 0))
        self.sbKO.setMaximumSize(QSize(50, 16777215))
        self.sbKO.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbKO.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbKO, 0, 1, 1, 1)

        self.sbWS = QSpinBox(self.groupBox_2)
        self.sbWS.setObjectName(u"sbWS")
        self.sbWS.setMinimumSize(QSize(0, 0))
        self.sbWS.setMaximumSize(QSize(50, 16777215))
        self.sbWS.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbWS.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbWS, 3, 1, 1, 1)

        self.line_2 = QFrame(self.groupBox_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 2, 0, 1, 9)

        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_23, 5, 6, 1, 1)

        self.sbGUP = QSpinBox(self.groupBox_2)
        self.sbGUP.setObjectName(u"sbGUP")

        self.gridLayout_3.addWidget(self.sbGUP, 5, 5, 1, 1)

        self.sbCH = QSpinBox(self.groupBox_2)
        self.sbCH.setObjectName(u"sbCH")
        self.sbCH.setMaximumSize(QSize(50, 16777215))
        self.sbCH.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbCH.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbCH, 1, 5, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_10, 0, 4, 1, 1)

        self.leGST_label = QLineEdit(self.groupBox_2)
        self.leGST_label.setObjectName(u"leGST_label")
        self.leGST_label.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_3.addWidget(self.leGST_label, 5, 8, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_13, 5, 0, 1, 1)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_16, 4, 6, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_11, 0, 6, 1, 1)

        self.sbGS = QSpinBox(self.groupBox_2)
        self.sbGS.setObjectName(u"sbGS")
        self.sbGS.setMaximumSize(QSize(50, 16777215))
        self.sbGS.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbGS.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbGS, 3, 7, 1, 1)

        self.sbWSE = QSpinBox(self.groupBox_2)
        self.sbWSE.setObjectName(u"sbWSE")
        self.sbWSE.setMaximumSize(QSize(50, 16777215))
        self.sbWSE.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbWSE.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbWSE, 4, 1, 1, 1)

        self.sbKOL = QSpinBox(self.groupBox_2)
        self.sbKOL.setObjectName(u"sbKOL")
        self.sbKOL.setMaximumSize(QSize(50, 16777215))
        self.sbKOL.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbKOL.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbKOL, 3, 3, 1, 1)

        self.sbFF = QSpinBox(self.groupBox_2)
        self.sbFF.setObjectName(u"sbFF")
        self.sbFF.setMaximumSize(QSize(50, 16777215))
        self.sbFF.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbFF.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbFF, 1, 7, 1, 1)

        self.sbMU = QSpinBox(self.groupBox_2)
        self.sbMU.setObjectName(u"sbMU")
        self.sbMU.setMaximumSize(QSize(50, 16777215))
        self.sbMU.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbMU.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbMU, 0, 3, 1, 1)

        self.sbGST = QSpinBox(self.groupBox_2)
        self.sbGST.setObjectName(u"sbGST")
        self.sbGST.setMaximumSize(QSize(50, 16777215))
        self.sbGST.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbGST.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbGST, 5, 7, 1, 1)

        self.sbGSS = QSpinBox(self.groupBox_2)
        self.sbGSS.setObjectName(u"sbGSS")
        self.sbGSS.setMaximumSize(QSize(50, 16777215))
        self.sbGSS.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sbGSS.setMinimum(-99)

        self.gridLayout_3.addWidget(self.sbGSS, 4, 7, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_3)


        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.Eigenschaften = QWidget()
        self.Eigenschaften.setObjectName(u"Eigenschaften")
        self.gridLayout_15 = QGridLayout(self.Eigenschaften)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(20, 20, 20, 20)
        self.groupBox_6 = QGroupBox(self.Eigenschaften)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy2.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy2)
        self.groupBox_6.setMaximumSize(QSize(800, 99999))
        self.groupBox_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.groupBox_6.setFlat(True)
        self.gridLayout_18 = QGridLayout(self.groupBox_6)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.treeEigenschaften = QTreeWidget(self.groupBox_6)
        self.treeEigenschaften.setObjectName(u"treeEigenschaften")
        self.treeEigenschaften.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(20)
        sizePolicy5.setHeightForWidth(self.treeEigenschaften.sizePolicy().hasHeightForWidth())
        self.treeEigenschaften.setSizePolicy(sizePolicy5)
        self.treeEigenschaften.setMinimumSize(QSize(0, 50))
        self.treeEigenschaften.setMaximumSize(QSize(16777215, 900))
        self.treeEigenschaften.setFrameShadow(QFrame.Shadow.Plain)
        self.treeEigenschaften.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.gridLayout_18.addWidget(self.treeEigenschaften, 0, 0, 1, 1)

        self.btnAddEigenschaft = QPushButton(self.groupBox_6)
        self.btnAddEigenschaft.setObjectName(u"btnAddEigenschaft")

        self.gridLayout_18.addWidget(self.btnAddEigenschaft, 2, 0, 1, 1)


        self.gridLayout_15.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Eigenschaften, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        sizePolicy2.setHeightForWidth(self.tab_4.sizePolicy().hasHeightForWidth())
        self.tab_4.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.groupBox_8 = QGroupBox(self.tab_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy2.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy2)
        self.gridLayout_8 = QGridLayout(self.groupBox_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.treeTalente = QTreeWidget(self.groupBox_8)
        self.treeTalente.setObjectName(u"treeTalente")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.treeTalente.sizePolicy().hasHeightForWidth())
        self.treeTalente.setSizePolicy(sizePolicy6)
        self.treeTalente.setMaximumSize(QSize(16777215, 200))

        self.gridLayout_8.addWidget(self.treeTalente, 0, 0, 1, 1)

        self.btnAddTalent = QPushButton(self.groupBox_8)
        self.btnAddTalent.setObjectName(u"btnAddTalent")

        self.gridLayout_8.addWidget(self.btnAddTalent, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.tab_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy2.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy2)
        self.gridLayout_10 = QGridLayout(self.groupBox_9)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.treeZauberfertigkeiten = QTreeWidget(self.groupBox_9)
        self.treeZauberfertigkeiten.setObjectName(u"treeZauberfertigkeiten")
        sizePolicy6.setHeightForWidth(self.treeZauberfertigkeiten.sizePolicy().hasHeightForWidth())
        self.treeZauberfertigkeiten.setSizePolicy(sizePolicy6)
        self.treeZauberfertigkeiten.setMaximumSize(QSize(16777215, 200))

        self.gridLayout_10.addWidget(self.treeZauberfertigkeiten, 0, 0, 1, 1)

        self.btnAddZauberfertigkeit = QPushButton(self.groupBox_9)
        self.btnAddZauberfertigkeit.setObjectName(u"btnAddZauberfertigkeit")

        self.gridLayout_10.addWidget(self.btnAddZauberfertigkeit, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        sizePolicy2.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy2)
        self.verticalLayout_6 = QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 20, 20, 20)
        self.groupBox_4 = QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.groupBox_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 98, 51))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.boxAngriffe = QWidget(self.scrollAreaWidgetContents_2)
        self.boxAngriffe.setObjectName(u"boxAngriffe")
        sizePolicy2.setHeightForWidth(self.boxAngriffe.sizePolicy().hasHeightForWidth())
        self.boxAngriffe.setSizePolicy(sizePolicy2)
        self.layoutAngriffe = QVBoxLayout(self.boxAngriffe)
        self.layoutAngriffe.setObjectName(u"layoutAngriffe")

        self.verticalLayout_4.addWidget(self.boxAngriffe)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)


        self.verticalLayout_6.addWidget(self.groupBox_4)

        self.btnAddAngriff = QPushButton(self.tab_3)
        self.btnAddAngriff.setObjectName(u"btnAddAngriff")

        self.verticalLayout_6.addWidget(self.btnAddAngriff)

        self.tabWidget.addTab(self.tab_3, "")
        self.splitter.addWidget(self.tabWidget)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 245, 702))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy2.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy2)
        self.groupBox_3.setMaximumSize(QSize(16777215, 300))
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.buttonDeleteImage = QPushButton(self.groupBox_3)
        self.buttonDeleteImage.setObjectName(u"buttonDeleteImage")

        self.gridLayout_6.addWidget(self.buttonDeleteImage, 2, 1, 1, 1)

        self.labelImage = QLabel(self.groupBox_3)
        self.labelImage.setObjectName(u"labelImage")
        self.labelImage.setMinimumSize(QSize(0, 200))
        self.labelImage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.labelImage, 1, 0, 1, 2)

        self.buttonLoadImage = QPushButton(self.groupBox_3)
        self.buttonLoadImage.setObjectName(u"buttonLoadImage")

        self.gridLayout_6.addWidget(self.buttonLoadImage, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.groupBox.setMaximumSize(QSize(16777215, 300))
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.laStatus = QLabel(self.groupBox)
        self.laStatus.setObjectName(u"laStatus")
        sizePolicy2.setHeightForWidth(self.laStatus.sizePolicy().hasHeightForWidth())
        self.laStatus.setSizePolicy(sizePolicy2)

        self.verticalLayout_8.addWidget(self.laStatus)

        self.lblWerte = QLabel(self.groupBox)
        self.lblWerte.setObjectName(u"lblWerte")
        sizePolicy2.setHeightForWidth(self.lblWerte.sizePolicy().hasHeightForWidth())
        self.lblWerte.setSizePolicy(sizePolicy2)
        self.lblWerte.setTextFormat(Qt.TextFormat.RichText)
        self.lblWerte.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lblWerte.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.lblWerte)

        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.verticalLayout_7 = QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btnLogin = QPushButton(self.widget_3)
        self.btnLogin.setObjectName(u"btnLogin")

        self.verticalLayout_7.addWidget(self.btnLogin)

        self.btnDBLaden = QPushButton(self.widget_3)
        self.btnDBLaden.setObjectName(u"btnDBLaden")

        self.verticalLayout_7.addWidget(self.btnDBLaden)

        self.btnDBSpeichern = QPushButton(self.widget_3)
        self.btnDBSpeichern.setObjectName(u"btnDBSpeichern")

        self.verticalLayout_7.addWidget(self.btnDBSpeichern)


        self.verticalLayout_8.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy2.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy2)
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.checkEditierbar = QCheckBox(self.groupBox_5)
        self.checkEditierbar.setObjectName(u"checkEditierbar")
        self.checkEditierbar.setEnabled(False)

        self.gridLayout_7.addWidget(self.checkEditierbar, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 4, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.scrollArea)

        self.verticalLayout_3.addWidget(self.splitter)

        self.widget_6 = QWidget(formMain)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(633, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.buttonLoad = QPushButton(self.widget_6)
        self.buttonLoad.setObjectName(u"buttonLoad")

        self.horizontalLayout_2.addWidget(self.buttonLoad)

        self.buttonQuicksave = QPushButton(self.widget_6)
        self.buttonQuicksave.setObjectName(u"buttonQuicksave")

        self.horizontalLayout_2.addWidget(self.buttonQuicksave)

        self.buttonSave = QPushButton(self.widget_6)
        self.buttonSave.setObjectName(u"buttonSave")

        self.horizontalLayout_2.addWidget(self.buttonSave)

        self.btnExport = QPushButton(self.widget_6)
        self.btnExport.setObjectName(u"btnExport")
        self.btnExport.setEnabled(True)
        self.btnExport.setMinimumSize(QSize(100, 0))
        self.btnExport.setMaximumSize(QSize(16777214, 16777215))

        self.horizontalLayout_2.addWidget(self.btnExport)


        self.verticalLayout_3.addWidget(self.widget_6)

        QWidget.setTabOrder(self.leName, self.leKurzbeschreibung)
        QWidget.setTabOrder(self.leKurzbeschreibung, self.cbTyp)
        QWidget.setTabOrder(self.cbTyp, self.sbKO)
        QWidget.setTabOrder(self.sbKO, self.sbIN)
        QWidget.setTabOrder(self.sbIN, self.sbMU)
        QWidget.setTabOrder(self.sbMU, self.sbKL)
        QWidget.setTabOrder(self.sbKL, self.sbGE)
        QWidget.setTabOrder(self.sbGE, self.sbCH)
        QWidget.setTabOrder(self.sbCH, self.sbKK)
        QWidget.setTabOrder(self.sbKK, self.sbFF)
        QWidget.setTabOrder(self.sbFF, self.sbWS)
        QWidget.setTabOrder(self.sbWS, self.sbWSE)
        QWidget.setTabOrder(self.sbWSE, self.sbMR)
        QWidget.setTabOrder(self.sbMR, self.sbKOL)
        QWidget.setTabOrder(self.sbKOL, self.sbINI)
        QWidget.setTabOrder(self.sbINI, self.sbASP)
        QWidget.setTabOrder(self.sbASP, self.sbKAP)
        QWidget.setTabOrder(self.sbKAP, self.sbGUP)
        QWidget.setTabOrder(self.sbGUP, self.sbGS)
        QWidget.setTabOrder(self.sbGS, self.sbGSS)
        QWidget.setTabOrder(self.sbGSS, self.leGSS_label)
        QWidget.setTabOrder(self.leGSS_label, self.sbGST)
        QWidget.setTabOrder(self.sbGST, self.leGST_label)
        QWidget.setTabOrder(self.leGST_label, self.checkEditierbar)
        QWidget.setTabOrder(self.checkEditierbar, self.buttonDeleteImage)
        QWidget.setTabOrder(self.buttonDeleteImage, self.buttonLoadImage)

        self.retranslateUi(formMain)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(formMain)
    # setupUi

    def retranslateUi(self, formMain):
        formMain.setWindowTitle(QCoreApplication.translate("formMain", u"Sephrasto - Kreatur erstellen", None))
        self.tabWidget.setProperty(u"class", QCoreApplication.translate("formMain", u"tabNavigation", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("formMain", u"Allgemein", None))
        self.leQuelle.setPlaceholderText(QCoreApplication.translate("formMain", u"Quelle", None))
        self.label.setText(QCoreApplication.translate("formMain", u"Kurzbeschreibung", None))
#if QT_CONFIG(tooltip)
        self.label_19.setToolTip(QCoreApplication.translate("formMain", u"<html><head/><body><p>Liste von Abk\u00fcrzungen der<a href=\"https://ilaris-online.de/app/abenteuers/\"><span style=\" text-decoration: underline; color:#0000ff;\">Abenteuer</span></a> in denen die Kreatur vorkommt (durch Komma getrennt). Nicht existierende Abenteuer werden automatisch erstellt.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("formMain", u"Abenteuer", None))
        self.leName.setPlaceholderText(QCoreApplication.translate("formMain", u"Name (erforderlich)", None))
        self.laID.setText(QCoreApplication.translate("formMain", u"ID: ", None))
        self.leAbenteuer.setText("")
        self.leAbenteuer.setPlaceholderText(QCoreApplication.translate("formMain", u"Durch Komma getrennte Abk\u00fcrzungen", None))
        self.label_4.setText(QCoreApplication.translate("formMain", u"Quelle", None))
#if QT_CONFIG(tooltip)
        self.cbPublik.setToolTip(QCoreApplication.translate("formMain", u"<html><head/><body><p>Ver\u00f6ffentliche Kreaturen sind online f\u00fcr alle sichtbar und sollten einzigartig im Namen sein. Mit der Ver\u00f6ffentlichung erm\u00f6glichst du zudem anderen die Kreatur zu bearbeiten.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cbPublik.setText(QCoreApplication.translate("formMain", u"\u00d6ffentlich", None))
        self.leKurzbeschreibung.setPlaceholderText(QCoreApplication.translate("formMain", u"Kompakte Beschreibung der Kreatur (erforderlich)", None))
        self.label_14.setText(QCoreApplication.translate("formMain", u"<html><head/><body><p><span style=\" font-weight:600;\">Typ</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("formMain", u"<html><head/><body><p><span style=\" font-weight:600;\">Name</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.cbNSC.setToolTip(QCoreApplication.translate("formMain", u"<html><head/><body><p>Kreaturen werden dann als NSCs gekennzeichnet, wenn ihre Beschreibung eher f\u00fcr ein Individuum (zB Helme Hafax) als f\u00fcr eine ganze Gruppe einer Art oder eines Archetypen gilt (zB Erfahrener Heerf\u00fchrer). Als Faustregel: Bestimmter Artikel -&gt; NSC, unbestimmter Artikel -&gt; kein NSC.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cbNSC.setText(QCoreApplication.translate("formMain", u"NSC", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("formMain", u"Werte", None))
        self.leGSS_label.setPlaceholderText(QCoreApplication.translate("formMain", u"Schwimmend", None))
        self.label_8.setText(QCoreApplication.translate("formMain", u"MU", None))
        self.label_7.setText(QCoreApplication.translate("formMain", u"CH", None))
        self.label_25.setText(QCoreApplication.translate("formMain", u"WS*", None))
        self.label_12.setText(QCoreApplication.translate("formMain", u"KL", None))
        self.label_9.setText(QCoreApplication.translate("formMain", u"FF", None))
        self.label_26.setText(QCoreApplication.translate("formMain", u"AsP", None))
        self.label_5.setText(QCoreApplication.translate("formMain", u"KO", None))
        self.label_18.setText(QCoreApplication.translate("formMain", u"WS", None))
        self.label_27.setText(QCoreApplication.translate("formMain", u"KaP", None))
        self.label_24.setText(QCoreApplication.translate("formMain", u"GS", None))
        self.label_3.setText(QCoreApplication.translate("formMain", u"GuP", None))
        self.label_17.setText(QCoreApplication.translate("formMain", u"Koloss", None))
        self.label_15.setText(QCoreApplication.translate("formMain", u"INI", None))
        self.label_23.setText(QCoreApplication.translate("formMain", u"GS 3", None))
        self.label_10.setText(QCoreApplication.translate("formMain", u"GE", None))
        self.leGST_label.setPlaceholderText(QCoreApplication.translate("formMain", u"Fliegend", None))
        self.label_6.setText(QCoreApplication.translate("formMain", u"IN", None))
        self.label_13.setText(QCoreApplication.translate("formMain", u"MR", None))
        self.label_16.setText(QCoreApplication.translate("formMain", u"GS 2", None))
        self.label_11.setText(QCoreApplication.translate("formMain", u"KK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("formMain", u"Beschreibung und Attribute", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("formMain", u"Eigenschaften", None))
        ___qtreewidgetitem = self.treeEigenschaften.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("formMain", u"Text", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("formMain", u"Kategorie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("formMain", u"Name", None));
        self.btnAddEigenschaft.setText(QCoreApplication.translate("formMain", u"Hinzuf\u00fcgen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Eigenschaften), QCoreApplication.translate("formMain", u"Eigenschaften", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("formMain", u"Freie Talente", None))
        ___qtreewidgetitem1 = self.treeTalente.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("formMain", u"Text", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("formMain", u"PW", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("formMain", u"Talent", None));
        self.btnAddTalent.setText(QCoreApplication.translate("formMain", u"Hinzuf\u00fcgen", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("formMain", u"\u00dcbernat\u00fcrlich", None))
        ___qtreewidgetitem2 = self.treeZauberfertigkeiten.headerItem()
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("formMain", u"Zauber/Liturgien", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("formMain", u"PW", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("formMain", u"Fertigkeit", None));
        self.btnAddZauberfertigkeit.setText(QCoreApplication.translate("formMain", u"Hinzuf\u00fcgen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("formMain", u"Fertigkeiten", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("formMain", u"Angriffe", None))
        self.scrollArea_2.setProperty(u"class", QCoreApplication.translate("formMain", u"transparent", None))
        self.btnAddAngriff.setText(QCoreApplication.translate("formMain", u"Hinzuf\u00fcgen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("formMain", u"Angriffe", None))
        self.scrollArea.setProperty(u"class", QCoreApplication.translate("formMain", u"transparent", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("formMain", u"Bild", None))
        self.buttonDeleteImage.setText(QCoreApplication.translate("formMain", u"Bild L\u00f6schen", None))
        self.labelImage.setText(QCoreApplication.translate("formMain", u"Bild-Aufl\u00f6sung: 193x254 px\n"
"(wird automatisch angepasst)", None))
        self.buttonLoadImage.setText(QCoreApplication.translate("formMain", u"Bild Laden", None))
        self.groupBox.setTitle(QCoreApplication.translate("formMain", u"ilaris-online.de", None))
        self.laStatus.setText(QCoreApplication.translate("formMain", u"Angemeldet: ", None))
        self.lblWerte.setText(QCoreApplication.translate("formMain", u"<html><head/><body><p><br/></p></body></html>", None))
        self.btnLogin.setText(QCoreApplication.translate("formMain", u"Anmelden", None))
        self.btnDBLaden.setText(QCoreApplication.translate("formMain", u"Aus Datenbank Laden", None))
        self.btnDBSpeichern.setText(QCoreApplication.translate("formMain", u"In Datenbank Speichern", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("formMain", u"Einstellungen", None))
        self.checkEditierbar.setText(QCoreApplication.translate("formMain", u"Zus\u00e4tzliche Infok\u00e4sten", None))
        self.buttonLoad.setText(QCoreApplication.translate("formMain", u"Laden", None))
        self.buttonQuicksave.setText(QCoreApplication.translate("formMain", u"Speichern", None))
        self.buttonSave.setText(QCoreApplication.translate("formMain", u"Speichern unter...", None))
        self.btnExport.setText(QCoreApplication.translate("formMain", u"Export", None))
    # retranslateUi

