# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_framepvtITx.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import resources_rc
import resources_rc
import resources_rc
import resources_rc
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1110, 756)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"*{ \n"
"	border:none;\n"
"	background-color:transparent;\n"
"	background: transparent;\n"
"	padding:0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #f3f5f7;\n"
"}\n"
"\n"
"#leftMenuSubContainer{\n"
"	background-color: #58aaec;\n"
"}\n"
"\n"
"#frame QPushButton{\n"
"	text-align: left;\n"
"	padding: 4px 5px;\n"
"}\n"
"\n"
"#frame_2 QPushButton{\n"
"	text-align: left;\n"
"	padding: 4px 23px;\n"
"	border-top-left-radius:0px;\n"
"	border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"#frame_3 QPushButton{\n"
"	text-align: left;\n"
"	padding: 0px 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"#dCards1 {\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"\n"
"}\n"
"\n"
"#dImageContainer {\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"#dCards2 {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"#rCards1 {\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	\n"
"}\n"
"\n"
"#rCards2 {\n"
"	borde"
                        "r-radius: 20px;\n"
"}\n"
"\n"
"#sCards1 {\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	\n"
"}\n"
"\n"
"#sCards2 {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#blueFrame1 {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#whiteFrame1 {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#blueFrame2 {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#whiteFrame2 {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#blueFrame3 {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#whiteFrame3 {\n"
"	border-radius: 20px;\n"
"}\n"
"#blueFrame4 {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#whiteFrame4 {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#blueFrame5 {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#whiteFrame5 {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#blueFrame6 {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#whiteFrame6 {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QCustomSlideMenu(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainMenuContainer = QWidget(self.centralwidget)
        self.mainMenuContainer.setObjectName(u"mainMenuContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainMenuContainer.sizePolicy().hasHeightForWidth())
        self.mainMenuContainer.setSizePolicy(sizePolicy2)
        self.mainMenuContainer.setMaximumSize(QSize(16777215, 16777215))
        self.mainMenuContainer.setSizeIncrement(QSize(0, 0))
        self.mainMenuContainer.setStyleSheet(u"background-color: #f3f5f7;")
        self.verticalLayout_5 = QVBoxLayout(self.mainMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainMenuContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setStyleSheet(u"background-color: rgb(20, 113, 201);")
        self.horizontalLayout_3 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.menuBtn = QPushButton(self.frame_5)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/white/svg/menu-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.menuBtn)


        self.horizontalLayout_3.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_4 = QFrame(self.headerContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.labelAchi = QLabel(self.frame_4)
        self.labelAchi.setObjectName(u"labelAchi")
        font = QFont()
        font.setFamily(u"Open Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.labelAchi.setFont(font)
        self.labelAchi.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.labelAchi)


        self.horizontalLayout_3.addWidget(self.frame_4, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainMenuContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.mainBodyContent.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        sizePolicy1.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy1)
        self.leftMenuContainer.setMinimumSize(QSize(0, 0))
        self.leftMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.leftMenuContainer.setStyleSheet(u"background-color: rgb(88, 170, 236);")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_303 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_303.setSpacing(0)
        self.verticalLayout_303.setObjectName(u"verticalLayout_303")
        self.verticalLayout_303.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBtnContainer = QFrame(self.leftMenuSubContainer)
        self.leftMenuBtnContainer.setObjectName(u"leftMenuBtnContainer")
        sizePolicy2.setHeightForWidth(self.leftMenuBtnContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuBtnContainer.setSizePolicy(sizePolicy2)
        self.leftMenuBtnContainer.setMaximumSize(QSize(16777215, 16777215))
        self.leftMenuBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.leftMenuBtnContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_304 = QVBoxLayout(self.leftMenuBtnContainer)
        self.verticalLayout_304.setSpacing(7)
        self.verticalLayout_304.setObjectName(u"verticalLayout_304")
        self.verticalLayout_304.setContentsMargins(0, 10, 0, 10)
        self.frame_2 = QFrame(self.leftMenuBtnContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_305 = QVBoxLayout(self.frame_2)
        self.verticalLayout_305.setSpacing(0)
        self.verticalLayout_305.setObjectName(u"verticalLayout_305")
        self.verticalLayout_305.setContentsMargins(0, 0, 0, 0)
        self.leftMenuDiagnosisBtn = QPushButton(self.frame_2)
        self.leftMenuDiagnosisBtn.setObjectName(u"leftMenuDiagnosisBtn")
        sizePolicy1.setHeightForWidth(self.leftMenuDiagnosisBtn.sizePolicy().hasHeightForWidth())
        self.leftMenuDiagnosisBtn.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Open Sans")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.leftMenuDiagnosisBtn.setFont(font1)
        self.leftMenuDiagnosisBtn.setStyleSheet(u"background-color: rgb(20, 113, 201);\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/black/svg/stethoscope-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.leftMenuDiagnosisBtn.setIcon(icon1)
        self.leftMenuDiagnosisBtn.setIconSize(QSize(28, 28))

        self.verticalLayout_305.addWidget(self.leftMenuDiagnosisBtn)

        self.leftMenuRecordsBtn = QPushButton(self.frame_2)
        self.leftMenuRecordsBtn.setObjectName(u"leftMenuRecordsBtn")
        sizePolicy1.setHeightForWidth(self.leftMenuRecordsBtn.sizePolicy().hasHeightForWidth())
        self.leftMenuRecordsBtn.setSizePolicy(sizePolicy1)
        self.leftMenuRecordsBtn.setFont(font1)
        self.leftMenuRecordsBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/black/svg/file-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.leftMenuRecordsBtn.setIcon(icon2)
        self.leftMenuRecordsBtn.setIconSize(QSize(28, 28))

        self.verticalLayout_305.addWidget(self.leftMenuRecordsBtn)

        self.leftMenuSummaryBtn = QPushButton(self.frame_2)
        self.leftMenuSummaryBtn.setObjectName(u"leftMenuSummaryBtn")
        sizePolicy1.setHeightForWidth(self.leftMenuSummaryBtn.sizePolicy().hasHeightForWidth())
        self.leftMenuSummaryBtn.setSizePolicy(sizePolicy1)
        self.leftMenuSummaryBtn.setFont(font1)
        self.leftMenuSummaryBtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/black/svg/chart-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.leftMenuSummaryBtn.setIcon(icon3)
        self.leftMenuSummaryBtn.setIconSize(QSize(28, 28))

        self.verticalLayout_305.addWidget(self.leftMenuSummaryBtn)

        self.leftMenuVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_305.addItem(self.leftMenuVSpacer)

        self.leftMenuLogoutBtn = QPushButton(self.frame_2)
        self.leftMenuLogoutBtn.setObjectName(u"leftMenuLogoutBtn")
        self.leftMenuLogoutBtn.setFont(font1)
        self.leftMenuLogoutBtn.setStyleSheet(u"padding: 5px 30px 5px 30px;")
        icon4 = QIcon()
        icon4.addFile(u":/black/svg/log-out-outlined-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.leftMenuLogoutBtn.setIcon(icon4)
        self.leftMenuLogoutBtn.setIconSize(QSize(28, 28))

        self.verticalLayout_305.addWidget(self.leftMenuLogoutBtn)


        self.verticalLayout_304.addWidget(self.frame_2)


        self.verticalLayout_303.addWidget(self.leftMenuBtnContainer)


        self.verticalLayout_2.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout_2.addWidget(self.leftMenuContainer)

        self.mainPages = QStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        font2 = QFont()
        font2.setPointSize(5)
        self.mainPages.setFont(font2)
        self.mainPages.setStyleSheet(u"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(88, 169, 235);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"   background: rgb(88, 169, 235);\n"
"    min-width: 25px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"     background: rgb(20, 113, 201);\n"
"    width: 20px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(20, 113, 201);\n"
"    width: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:"
                        "horizontal\n"
"{\n"
"    background: rgb(20, 113, 201);\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(20, 113, 201);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"    background: rgb(88, 169, 235);\n"
"    min-height: 25px;\n"
"    border-radius: 0px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(20, 113, 201);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"     background: rgb(20, 113, 201);\n"
"     height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"     background: n"
                        "one;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"     background: rgb(20, 113, 201);\n"
"} \n"
"")
        self.diagnosisPages = QWidget()
        self.diagnosisPages.setObjectName(u"diagnosisPages")
        self.diagnosisPages.setStyleSheet(u"color:#000;")
        self.verticalLayout_17 = QVBoxLayout(self.diagnosisPages)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.diagnosisStackedWidget = QStackedWidget(self.diagnosisPages)
        self.diagnosisStackedWidget.setObjectName(u"diagnosisStackedWidget")
        self.diagnosisFrontPage = QWidget()
        self.diagnosisFrontPage.setObjectName(u"diagnosisFrontPage")
        self.verticalLayout_11 = QVBoxLayout(self.diagnosisFrontPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.diagnosisCardsFrame = QWidget(self.diagnosisFrontPage)
        self.diagnosisCardsFrame.setObjectName(u"diagnosisCardsFrame")
        self.diagnosisCardsFrame.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.diagnosisCardsFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, 40, 50, 40)
        self.dCards1 = QFrame(self.diagnosisCardsFrame)
        self.dCards1.setObjectName(u"dCards1")
        self.dCards1.setStyleSheet(u"background-color: rgb(138, 191, 238);")
        self.dCards1.setFrameShape(QFrame.StyledPanel)
        self.dCards1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.dCards1)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.dCards2 = QFrame(self.dCards1)
        self.dCards2.setObjectName(u"dCards2")
        self.dCards2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000;")
        self.dCards2.setFrameShape(QFrame.StyledPanel)
        self.dCards2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.dCards2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(9, -1, -1, -1)
        self.dMainContainer = QFrame(self.dCards2)
        self.dMainContainer.setObjectName(u"dMainContainer")
        self.dMainContainer.setFrameShape(QFrame.StyledPanel)
        self.dMainContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.dMainContainer)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(20, 20, 20, 20)
        self.recAuthframe1_2 = QFrame(self.dMainContainer)
        self.recAuthframe1_2.setObjectName(u"recAuthframe1_2")
        self.recAuthframe1_2.setFrameShape(QFrame.StyledPanel)
        self.recAuthframe1_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.recAuthframe1_2)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(38, -1, 31, -1)
        self.label_7 = QLabel(self.recAuthframe1_2)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setFamily(u"Open Sans")
        font3.setPointSize(28)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_7.setWordWrap(True)

        self.verticalLayout_51.addWidget(self.label_7)


        self.verticalLayout_22.addWidget(self.recAuthframe1_2)

        self.recAuthframe2_2 = QFrame(self.dMainContainer)
        self.recAuthframe2_2.setObjectName(u"recAuthframe2_2")
        font4 = QFont()
        font4.setPointSize(18)
        self.recAuthframe2_2.setFont(font4)
        self.recAuthframe2_2.setFrameShape(QFrame.StyledPanel)
        self.recAuthframe2_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.recAuthframe2_2)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(40, 15, 40, -1)
        self.label_9 = QLabel(self.recAuthframe2_2)
        self.label_9.setObjectName(u"label_9")
        font5 = QFont()
        font5.setFamily(u"Open Sans")
        font5.setPointSize(18)
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_9.setWordWrap(True)

        self.horizontalLayout_88.addWidget(self.label_9)


        self.verticalLayout_22.addWidget(self.recAuthframe2_2)

        self.dBottomContainer = QFrame(self.dMainContainer)
        self.dBottomContainer.setObjectName(u"dBottomContainer")
        self.dBottomContainer.setFrameShape(QFrame.StyledPanel)
        self.dBottomContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.dBottomContainer)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.dTakeBtn = QPushButton(self.dBottomContainer)
        self.dTakeBtn.setObjectName(u"dTakeBtn")
        font6 = QFont()
        font6.setFamily(u"Open Sans")
        font6.setPointSize(16)
        font6.setBold(True)
        font6.setWeight(75)
        self.dTakeBtn.setFont(font6)
        self.dTakeBtn.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color: #FFF;\n"
"padding: 5px 20px 5px 20px;\n"
"border-radius: 15px;")

        self.verticalLayout_61.addWidget(self.dTakeBtn)


        self.verticalLayout_22.addWidget(self.dBottomContainer, 0, Qt.AlignHCenter)


        self.horizontalLayout_20.addWidget(self.dMainContainer)


        self.horizontalLayout_19.addWidget(self.dCards2)

        self.dImageContainer_2 = QWidget(self.dCards1)
        self.dImageContainer_2.setObjectName(u"dImageContainer_2")
        self.verticalLayout_10 = QVBoxLayout(self.dImageContainer_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.dImage_2 = QLabel(self.dImageContainer_2)
        self.dImage_2.setObjectName(u"dImage_2")
        self.dImage_2.setPixmap(QPixmap(u":/images/images/diagnosisPicture_1.png"))
        self.dImage_2.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.dImage_2)


        self.horizontalLayout_19.addWidget(self.dImageContainer_2)


        self.horizontalLayout_7.addWidget(self.dCards1)


        self.verticalLayout_11.addWidget(self.diagnosisCardsFrame)

        self.diagnosisStackedWidget.addWidget(self.diagnosisFrontPage)
        self.diagnosisProfilePage = QWidget()
        self.diagnosisProfilePage.setObjectName(u"diagnosisProfilePage")
        self.verticalLayout_228 = QVBoxLayout(self.diagnosisProfilePage)
        self.verticalLayout_228.setObjectName(u"verticalLayout_228")
        self.profileProgressContainer = QWidget(self.diagnosisProfilePage)
        self.profileProgressContainer.setObjectName(u"profileProgressContainer")
        sizePolicy1.setHeightForWidth(self.profileProgressContainer.sizePolicy().hasHeightForWidth())
        self.profileProgressContainer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_50 = QHBoxLayout(self.profileProgressContainer)
        self.horizontalLayout_50.setSpacing(6)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.pPExitBtnContainer = QFrame(self.profileProgressContainer)
        self.pPExitBtnContainer.setObjectName(u"pPExitBtnContainer")
        self.pPExitBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.pPExitBtnContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.pPExitBtnContainer)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.pPExitBtn = QPushButton(self.pPExitBtnContainer)
        self.pPExitBtn.setObjectName(u"pPExitBtn")
        icon5 = QIcon()
        icon5.addFile(u":/black/svg/arrow-left-black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pPExitBtn.setIcon(icon5)
        self.pPExitBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_55.addWidget(self.pPExitBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_50.addWidget(self.pPExitBtnContainer, 0, Qt.AlignLeft)

        self.pPProgressContainer = QFrame(self.profileProgressContainer)
        self.pPProgressContainer.setObjectName(u"pPProgressContainer")
        self.pPProgressContainer.setFrameShape(QFrame.StyledPanel)
        self.pPProgressContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.pPProgressContainer)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.pPProgress = QLabel(self.pPProgressContainer)
        self.pPProgress.setObjectName(u"pPProgress")
        sizePolicy2.setHeightForWidth(self.pPProgress.sizePolicy().hasHeightForWidth())
        self.pPProgress.setSizePolicy(sizePolicy2)
        self.pPProgress.setMinimumSize(QSize(680, 45))
        self.pPProgress.setMaximumSize(QSize(680, 45))
        self.pPProgress.setSizeIncrement(QSize(0, 0))
        font7 = QFont()
        font7.setPointSize(100)
        font7.setBold(False)
        font7.setWeight(50)
        self.pPProgress.setFont(font7)
        self.pPProgress.setFrameShadow(QFrame.Plain)
        self.pPProgress.setPixmap(QPixmap(u":/progressBarImages/images/progress1.png"))
        self.pPProgress.setScaledContents(True)
        self.pPProgress.setWordWrap(False)

        self.horizontalLayout_56.addWidget(self.pPProgress, 0, Qt.AlignVCenter)


        self.horizontalLayout_50.addWidget(self.pPProgressContainer, 0, Qt.AlignHCenter)

        self.pPExitBtn2 = QPushButton(self.profileProgressContainer)
        self.pPExitBtn2.setObjectName(u"pPExitBtn2")
        self.pPExitBtn2.setEnabled(False)

        self.horizontalLayout_50.addWidget(self.pPExitBtn2)


        self.verticalLayout_228.addWidget(self.profileProgressContainer)

        self.pMarginContainer = QFrame(self.diagnosisProfilePage)
        self.pMarginContainer.setObjectName(u"pMarginContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pMarginContainer.sizePolicy().hasHeightForWidth())
        self.pMarginContainer.setSizePolicy(sizePolicy3)
        self.pMarginContainer.setFrameShape(QFrame.StyledPanel)
        self.pMarginContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_182 = QVBoxLayout(self.pMarginContainer)
        self.verticalLayout_182.setObjectName(u"verticalLayout_182")
        self.verticalLayout_182.setContentsMargins(70, 0, 70, 10)
        self.pBlueCard = QFrame(self.pMarginContainer)
        self.pBlueCard.setObjectName(u"pBlueCard")
        self.pBlueCard.setStyleSheet(u"background-color:#58AAEC;\n"
"border-radius: 15px;")
        self.pBlueCard.setFrameShape(QFrame.StyledPanel)
        self.pBlueCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_183 = QVBoxLayout(self.pBlueCard)
        self.verticalLayout_183.setSpacing(0)
        self.verticalLayout_183.setObjectName(u"verticalLayout_183")
        self.verticalLayout_183.setContentsMargins(10, 0, 0, 0)
        self.pWhiteCard = QFrame(self.pBlueCard)
        self.pWhiteCard.setObjectName(u"pWhiteCard")
        self.pWhiteCard.setStyleSheet(u"background-color:#FFF;\n"
"border-radius: 15px;")
        self.pWhiteCard.setFrameShape(QFrame.StyledPanel)
        self.pWhiteCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_184 = QVBoxLayout(self.pWhiteCard)
        self.verticalLayout_184.setObjectName(u"verticalLayout_184")
        self.verticalLayout_184.setContentsMargins(5, 5, 5, 5)
        self.pScrollArea = QScrollArea(self.pWhiteCard)
        self.pScrollArea.setObjectName(u"pScrollArea")
        self.pScrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.pScrollArea.setWidgetResizable(True)
        self.pScrollAreaContents = QWidget()
        self.pScrollAreaContents.setObjectName(u"pScrollAreaContents")
        self.pScrollAreaContents.setGeometry(QRect(0, 0, 838, 633))
        self.pScrollAreaContents.setStyleSheet(u" QLineEdit, QTextEdit, QComboBox, QDateEdit {\n"
"	border: 1px solid #D9D9D9;\n"
"border-radius: 5px\n"
" }")
        self.verticalLayout_220 = QVBoxLayout(self.pScrollAreaContents)
        self.verticalLayout_220.setSpacing(0)
        self.verticalLayout_220.setObjectName(u"verticalLayout_220")
        self.verticalLayout_220.setContentsMargins(0, 0, 0, 0)
        self.pTopLabelContainer = QFrame(self.pScrollAreaContents)
        self.pTopLabelContainer.setObjectName(u"pTopLabelContainer")
        self.pTopLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.pTopLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_221 = QVBoxLayout(self.pTopLabelContainer)
        self.verticalLayout_221.setSpacing(0)
        self.verticalLayout_221.setObjectName(u"verticalLayout_221")
        self.verticalLayout_221.setContentsMargins(20, 15, 20, 10)
        self.pTopLabel = QLabel(self.pTopLabelContainer)
        self.pTopLabel.setObjectName(u"pTopLabel")
        font8 = QFont()
        font8.setFamily(u"Raleway")
        font8.setPointSize(20)
        font8.setBold(True)
        font8.setWeight(75)
        self.pTopLabel.setFont(font8)

        self.verticalLayout_221.addWidget(self.pTopLabel)

        self.label_8 = QLabel(self.pTopLabelContainer)
        self.label_8.setObjectName(u"label_8")
        font9 = QFont()
        font9.setFamily(u"Open Sans")
        font9.setPointSize(10)
        self.label_8.setFont(font9)

        self.verticalLayout_221.addWidget(self.label_8)


        self.verticalLayout_220.addWidget(self.pTopLabelContainer)

        self.pUserDetailsContainer = QFrame(self.pScrollAreaContents)
        self.pUserDetailsContainer.setObjectName(u"pUserDetailsContainer")
        self.pUserDetailsContainer.setMinimumSize(QSize(0, 0))
        self.pUserDetailsContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_222 = QVBoxLayout(self.pUserDetailsContainer)
        self.verticalLayout_222.setSpacing(0)
        self.verticalLayout_222.setObjectName(u"verticalLayout_222")
        self.verticalLayout_222.setContentsMargins(35, 0, 35, 0)
        self.pUserDetailsTopContainer = QFrame(self.pUserDetailsContainer)
        self.pUserDetailsTopContainer.setObjectName(u"pUserDetailsTopContainer")
        self.pUserDetailsTopContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsTopContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.pUserDetailsTopContainer)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsTopBodyContainer = QFrame(self.pUserDetailsTopContainer)
        self.pUserDetailsTopBodyContainer.setObjectName(u"pUserDetailsTopBodyContainer")
        self.pUserDetailsTopBodyContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsTopBodyContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.pUserDetailsTopBodyContainer)
        self.horizontalLayout_13.setSpacing(100)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 5)
        self.pUserDetailsLnameContainer = QFrame(self.pUserDetailsTopBodyContainer)
        self.pUserDetailsLnameContainer.setObjectName(u"pUserDetailsLnameContainer")
        self.pUserDetailsLnameContainer.setMinimumSize(QSize(0, 0))
        self.pUserDetailsLnameContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsLnameContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_223 = QVBoxLayout(self.pUserDetailsLnameContainer)
        self.verticalLayout_223.setSpacing(0)
        self.verticalLayout_223.setObjectName(u"verticalLayout_223")
        self.verticalLayout_223.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsLnameLabelContainer = QFrame(self.pUserDetailsLnameContainer)
        self.pUserDetailsLnameLabelContainer.setObjectName(u"pUserDetailsLnameLabelContainer")
        self.pUserDetailsLnameLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsLnameLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_226 = QVBoxLayout(self.pUserDetailsLnameLabelContainer)
        self.verticalLayout_226.setSpacing(0)
        self.verticalLayout_226.setObjectName(u"verticalLayout_226")
        self.verticalLayout_226.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsLnameLabel = QLabel(self.pUserDetailsLnameLabelContainer)
        self.pUserDetailsLnameLabel.setObjectName(u"pUserDetailsLnameLabel")
        font10 = QFont()
        font10.setFamily(u"Open Sans Semibold")
        font10.setPointSize(14)
        font10.setBold(True)
        font10.setWeight(75)
        self.pUserDetailsLnameLabel.setFont(font10)

        self.verticalLayout_226.addWidget(self.pUserDetailsLnameLabel)


        self.verticalLayout_223.addWidget(self.pUserDetailsLnameLabelContainer)

        self.pUserDetailsLnameLineEditContainer = QFrame(self.pUserDetailsLnameContainer)
        self.pUserDetailsLnameLineEditContainer.setObjectName(u"pUserDetailsLnameLineEditContainer")
        self.pUserDetailsLnameLineEditContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsLnameLineEditContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_230 = QVBoxLayout(self.pUserDetailsLnameLineEditContainer)
        self.verticalLayout_230.setSpacing(0)
        self.verticalLayout_230.setObjectName(u"verticalLayout_230")
        self.verticalLayout_230.setContentsMargins(0, 5, 0, 0)
        self.pUserDetailsLnameLineEdit = QLineEdit(self.pUserDetailsLnameLineEditContainer)
        self.pUserDetailsLnameLineEdit.setObjectName(u"pUserDetailsLnameLineEdit")
        self.pUserDetailsLnameLineEdit.setMinimumSize(QSize(0, 50))
        font11 = QFont()
        font11.setFamily(u"Open Sans")
        font11.setPointSize(12)
        self.pUserDetailsLnameLineEdit.setFont(font11)

        self.verticalLayout_230.addWidget(self.pUserDetailsLnameLineEdit)


        self.verticalLayout_223.addWidget(self.pUserDetailsLnameLineEditContainer)


        self.horizontalLayout_13.addWidget(self.pUserDetailsLnameContainer)

        self.pUserDetailsFnameContainer = QFrame(self.pUserDetailsTopBodyContainer)
        self.pUserDetailsFnameContainer.setObjectName(u"pUserDetailsFnameContainer")
        self.pUserDetailsFnameContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsFnameContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_224 = QVBoxLayout(self.pUserDetailsFnameContainer)
        self.verticalLayout_224.setSpacing(0)
        self.verticalLayout_224.setObjectName(u"verticalLayout_224")
        self.verticalLayout_224.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsFnameLabelContainer = QFrame(self.pUserDetailsFnameContainer)
        self.pUserDetailsFnameLabelContainer.setObjectName(u"pUserDetailsFnameLabelContainer")
        self.pUserDetailsFnameLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsFnameLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_227 = QVBoxLayout(self.pUserDetailsFnameLabelContainer)
        self.verticalLayout_227.setSpacing(0)
        self.verticalLayout_227.setObjectName(u"verticalLayout_227")
        self.verticalLayout_227.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsFnameLabel = QLabel(self.pUserDetailsFnameLabelContainer)
        self.pUserDetailsFnameLabel.setObjectName(u"pUserDetailsFnameLabel")
        self.pUserDetailsFnameLabel.setFont(font10)

        self.verticalLayout_227.addWidget(self.pUserDetailsFnameLabel)


        self.verticalLayout_224.addWidget(self.pUserDetailsFnameLabelContainer)

        self.pUserDetailsFnameLineEditContainer = QFrame(self.pUserDetailsFnameContainer)
        self.pUserDetailsFnameLineEditContainer.setObjectName(u"pUserDetailsFnameLineEditContainer")
        self.pUserDetailsFnameLineEditContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsFnameLineEditContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_231 = QVBoxLayout(self.pUserDetailsFnameLineEditContainer)
        self.verticalLayout_231.setSpacing(0)
        self.verticalLayout_231.setObjectName(u"verticalLayout_231")
        self.verticalLayout_231.setContentsMargins(0, 5, 0, 0)
        self.pUserDetailsFnameLineEdit = QLineEdit(self.pUserDetailsFnameLineEditContainer)
        self.pUserDetailsFnameLineEdit.setObjectName(u"pUserDetailsFnameLineEdit")
        self.pUserDetailsFnameLineEdit.setMinimumSize(QSize(0, 50))
        self.pUserDetailsFnameLineEdit.setFont(font11)

        self.verticalLayout_231.addWidget(self.pUserDetailsFnameLineEdit)


        self.verticalLayout_224.addWidget(self.pUserDetailsFnameLineEditContainer)


        self.horizontalLayout_13.addWidget(self.pUserDetailsFnameContainer)

        self.pUserDetailsMnameContainer = QFrame(self.pUserDetailsTopBodyContainer)
        self.pUserDetailsMnameContainer.setObjectName(u"pUserDetailsMnameContainer")
        self.pUserDetailsMnameContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsMnameContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_225 = QVBoxLayout(self.pUserDetailsMnameContainer)
        self.verticalLayout_225.setSpacing(0)
        self.verticalLayout_225.setObjectName(u"verticalLayout_225")
        self.verticalLayout_225.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsMnameLabelContainer = QFrame(self.pUserDetailsMnameContainer)
        self.pUserDetailsMnameLabelContainer.setObjectName(u"pUserDetailsMnameLabelContainer")
        self.pUserDetailsMnameLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsMnameLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_229 = QVBoxLayout(self.pUserDetailsMnameLabelContainer)
        self.verticalLayout_229.setSpacing(0)
        self.verticalLayout_229.setObjectName(u"verticalLayout_229")
        self.verticalLayout_229.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsMnameLabel = QLabel(self.pUserDetailsMnameLabelContainer)
        self.pUserDetailsMnameLabel.setObjectName(u"pUserDetailsMnameLabel")
        self.pUserDetailsMnameLabel.setFont(font10)

        self.verticalLayout_229.addWidget(self.pUserDetailsMnameLabel)


        self.verticalLayout_225.addWidget(self.pUserDetailsMnameLabelContainer)

        self.pUserDetailsMnameLineEditContainer = QFrame(self.pUserDetailsMnameContainer)
        self.pUserDetailsMnameLineEditContainer.setObjectName(u"pUserDetailsMnameLineEditContainer")
        self.pUserDetailsMnameLineEditContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsMnameLineEditContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_232 = QVBoxLayout(self.pUserDetailsMnameLineEditContainer)
        self.verticalLayout_232.setSpacing(0)
        self.verticalLayout_232.setObjectName(u"verticalLayout_232")
        self.verticalLayout_232.setContentsMargins(0, 5, 0, 0)
        self.pUserDetailsMnameLineEdit = QLineEdit(self.pUserDetailsMnameLineEditContainer)
        self.pUserDetailsMnameLineEdit.setObjectName(u"pUserDetailsMnameLineEdit")
        self.pUserDetailsMnameLineEdit.setMinimumSize(QSize(0, 50))
        self.pUserDetailsMnameLineEdit.setFont(font11)

        self.verticalLayout_232.addWidget(self.pUserDetailsMnameLineEdit)


        self.verticalLayout_225.addWidget(self.pUserDetailsMnameLineEditContainer)


        self.horizontalLayout_13.addWidget(self.pUserDetailsMnameContainer)


        self.verticalLayout_52.addWidget(self.pUserDetailsTopBodyContainer)

        self.pUserDetailsTopErrorContainer = QFrame(self.pUserDetailsTopContainer)
        self.pUserDetailsTopErrorContainer.setObjectName(u"pUserDetailsTopErrorContainer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pUserDetailsTopErrorContainer.sizePolicy().hasHeightForWidth())
        self.pUserDetailsTopErrorContainer.setSizePolicy(sizePolicy4)
        font12 = QFont()
        font12.setFamily(u"Open Sans")
        self.pUserDetailsTopErrorContainer.setFont(font12)
        self.pUserDetailsTopErrorContainer.setStyleSheet(u"color: rgb(255, 0, 0)")
        self.pUserDetailsTopErrorContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsTopErrorContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.pUserDetailsTopErrorContainer)
        self.horizontalLayout_14.setSpacing(100)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lnameErrorLabel = QLabel(self.pUserDetailsTopErrorContainer)
        self.lnameErrorLabel.setObjectName(u"lnameErrorLabel")
        self.lnameErrorLabel.setFont(font12)

        self.horizontalLayout_14.addWidget(self.lnameErrorLabel)

        self.fnameErrorLabel = QLabel(self.pUserDetailsTopErrorContainer)
        self.fnameErrorLabel.setObjectName(u"fnameErrorLabel")
        self.fnameErrorLabel.setFont(font12)

        self.horizontalLayout_14.addWidget(self.fnameErrorLabel)

        self.mnameErrorLabel = QLabel(self.pUserDetailsTopErrorContainer)
        self.mnameErrorLabel.setObjectName(u"mnameErrorLabel")
        self.mnameErrorLabel.setFont(font12)

        self.horizontalLayout_14.addWidget(self.mnameErrorLabel)


        self.verticalLayout_52.addWidget(self.pUserDetailsTopErrorContainer)


        self.verticalLayout_222.addWidget(self.pUserDetailsTopContainer)

        self.pUserDetailsMidContainer = QFrame(self.pUserDetailsContainer)
        self.pUserDetailsMidContainer.setObjectName(u"pUserDetailsMidContainer")
        self.pUserDetailsMidContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsMidContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_233 = QVBoxLayout(self.pUserDetailsMidContainer)
        self.verticalLayout_233.setSpacing(0)
        self.verticalLayout_233.setObjectName(u"verticalLayout_233")
        self.verticalLayout_233.setContentsMargins(0, 15, 0, 0)
        self.pUserDetailsMidBodyContainer = QFrame(self.pUserDetailsMidContainer)
        self.pUserDetailsMidBodyContainer.setObjectName(u"pUserDetailsMidBodyContainer")
        self.pUserDetailsMidBodyContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsMidBodyContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.pUserDetailsMidBodyContainer)
        self.horizontalLayout_15.setSpacing(60)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 5)
        self.pUserDetailsBirthdateContainer = QFrame(self.pUserDetailsMidBodyContainer)
        self.pUserDetailsBirthdateContainer.setObjectName(u"pUserDetailsBirthdateContainer")
        self.pUserDetailsBirthdateContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsBirthdateContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_234 = QVBoxLayout(self.pUserDetailsBirthdateContainer)
        self.verticalLayout_234.setSpacing(0)
        self.verticalLayout_234.setObjectName(u"verticalLayout_234")
        self.verticalLayout_234.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsBirthdateLabelContainer = QFrame(self.pUserDetailsBirthdateContainer)
        self.pUserDetailsBirthdateLabelContainer.setObjectName(u"pUserDetailsBirthdateLabelContainer")
        self.pUserDetailsBirthdateLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsBirthdateLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_240 = QVBoxLayout(self.pUserDetailsBirthdateLabelContainer)
        self.verticalLayout_240.setSpacing(0)
        self.verticalLayout_240.setObjectName(u"verticalLayout_240")
        self.verticalLayout_240.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsBirthdateLabel = QLabel(self.pUserDetailsBirthdateLabelContainer)
        self.pUserDetailsBirthdateLabel.setObjectName(u"pUserDetailsBirthdateLabel")
        self.pUserDetailsBirthdateLabel.setFont(font10)

        self.verticalLayout_240.addWidget(self.pUserDetailsBirthdateLabel)

        self.pUserDetailsBirthdateFormatLabel = QLabel(self.pUserDetailsBirthdateLabelContainer)
        self.pUserDetailsBirthdateFormatLabel.setObjectName(u"pUserDetailsBirthdateFormatLabel")

        self.verticalLayout_240.addWidget(self.pUserDetailsBirthdateFormatLabel)


        self.verticalLayout_234.addWidget(self.pUserDetailsBirthdateLabelContainer)

        self.pUserDetailsBirthdateDateEditContainer = QFrame(self.pUserDetailsBirthdateContainer)
        self.pUserDetailsBirthdateDateEditContainer.setObjectName(u"pUserDetailsBirthdateDateEditContainer")
        self.pUserDetailsBirthdateDateEditContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsBirthdateDateEditContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_249 = QVBoxLayout(self.pUserDetailsBirthdateDateEditContainer)
        self.verticalLayout_249.setSpacing(0)
        self.verticalLayout_249.setObjectName(u"verticalLayout_249")
        self.verticalLayout_249.setContentsMargins(0, 5, 0, 0)
        self.pUserDetailsBirthdateDateEdit = QDateEdit(self.pUserDetailsBirthdateDateEditContainer)
        self.pUserDetailsBirthdateDateEdit.setObjectName(u"pUserDetailsBirthdateDateEdit")
        self.pUserDetailsBirthdateDateEdit.setMinimumSize(QSize(150, 50))
        self.pUserDetailsBirthdateDateEdit.setFont(font11)
        self.pUserDetailsBirthdateDateEdit.setInputMethodHints(Qt.ImhNone)
        self.pUserDetailsBirthdateDateEdit.setAlignment(Qt.AlignCenter)
        self.pUserDetailsBirthdateDateEdit.setProperty("showGroupSeparator", False)
        self.pUserDetailsBirthdateDateEdit.setCalendarPopup(True)

        self.verticalLayout_249.addWidget(self.pUserDetailsBirthdateDateEdit)


        self.verticalLayout_234.addWidget(self.pUserDetailsBirthdateDateEditContainer)


        self.horizontalLayout_15.addWidget(self.pUserDetailsBirthdateContainer)

        self.pUserDetailsAgeContainer = QFrame(self.pUserDetailsMidBodyContainer)
        self.pUserDetailsAgeContainer.setObjectName(u"pUserDetailsAgeContainer")
        self.pUserDetailsAgeContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsAgeContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_241 = QVBoxLayout(self.pUserDetailsAgeContainer)
        self.verticalLayout_241.setSpacing(0)
        self.verticalLayout_241.setObjectName(u"verticalLayout_241")
        self.verticalLayout_241.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsAgeLabelContainer = QFrame(self.pUserDetailsAgeContainer)
        self.pUserDetailsAgeLabelContainer.setObjectName(u"pUserDetailsAgeLabelContainer")
        self.pUserDetailsAgeLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsAgeLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_248 = QVBoxLayout(self.pUserDetailsAgeLabelContainer)
        self.verticalLayout_248.setSpacing(0)
        self.verticalLayout_248.setObjectName(u"verticalLayout_248")
        self.verticalLayout_248.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsAgeLabel = QLabel(self.pUserDetailsAgeLabelContainer)
        self.pUserDetailsAgeLabel.setObjectName(u"pUserDetailsAgeLabel")
        self.pUserDetailsAgeLabel.setFont(font10)

        self.verticalLayout_248.addWidget(self.pUserDetailsAgeLabel)


        self.verticalLayout_241.addWidget(self.pUserDetailsAgeLabelContainer)

        self.pUserDetailsAgeLineEditContainer = QFrame(self.pUserDetailsAgeContainer)
        self.pUserDetailsAgeLineEditContainer.setObjectName(u"pUserDetailsAgeLineEditContainer")
        self.pUserDetailsAgeLineEditContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsAgeLineEditContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_299 = QVBoxLayout(self.pUserDetailsAgeLineEditContainer)
        self.verticalLayout_299.setSpacing(0)
        self.verticalLayout_299.setObjectName(u"verticalLayout_299")
        self.verticalLayout_299.setContentsMargins(0, 5, 0, 0)
        self.pUserDetailsAgeLineEdit = QLineEdit(self.pUserDetailsAgeLineEditContainer)
        self.pUserDetailsAgeLineEdit.setObjectName(u"pUserDetailsAgeLineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pUserDetailsAgeLineEdit.sizePolicy().hasHeightForWidth())
        self.pUserDetailsAgeLineEdit.setSizePolicy(sizePolicy5)
        self.pUserDetailsAgeLineEdit.setMinimumSize(QSize(0, 50))
        self.pUserDetailsAgeLineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.pUserDetailsAgeLineEdit.setFont(font11)
        self.pUserDetailsAgeLineEdit.setStyleSheet(u"background-color: rgb(234, 234, 234);")

        self.verticalLayout_299.addWidget(self.pUserDetailsAgeLineEdit)


        self.verticalLayout_241.addWidget(self.pUserDetailsAgeLineEditContainer)


        self.horizontalLayout_15.addWidget(self.pUserDetailsAgeContainer)

        self.pUserDetailsSexContainer = QFrame(self.pUserDetailsMidBodyContainer)
        self.pUserDetailsSexContainer.setObjectName(u"pUserDetailsSexContainer")
        self.pUserDetailsSexContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsSexContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_237 = QVBoxLayout(self.pUserDetailsSexContainer)
        self.verticalLayout_237.setSpacing(0)
        self.verticalLayout_237.setObjectName(u"verticalLayout_237")
        self.verticalLayout_237.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsSexLabelContainer = QFrame(self.pUserDetailsSexContainer)
        self.pUserDetailsSexLabelContainer.setObjectName(u"pUserDetailsSexLabelContainer")
        self.pUserDetailsSexLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsSexLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_242 = QVBoxLayout(self.pUserDetailsSexLabelContainer)
        self.verticalLayout_242.setSpacing(0)
        self.verticalLayout_242.setObjectName(u"verticalLayout_242")
        self.verticalLayout_242.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsSexLabel = QLabel(self.pUserDetailsSexLabelContainer)
        self.pUserDetailsSexLabel.setObjectName(u"pUserDetailsSexLabel")
        self.pUserDetailsSexLabel.setFont(font10)

        self.verticalLayout_242.addWidget(self.pUserDetailsSexLabel)


        self.verticalLayout_237.addWidget(self.pUserDetailsSexLabelContainer)

        self.pUserDetailsSexCbContainer = QFrame(self.pUserDetailsSexContainer)
        self.pUserDetailsSexCbContainer.setObjectName(u"pUserDetailsSexCbContainer")
        self.pUserDetailsSexCbContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsSexCbContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_247 = QVBoxLayout(self.pUserDetailsSexCbContainer)
        self.verticalLayout_247.setSpacing(0)
        self.verticalLayout_247.setObjectName(u"verticalLayout_247")
        self.verticalLayout_247.setContentsMargins(0, 5, 0, 0)
        self.pUserDetailsSexCb = QComboBox(self.pUserDetailsSexCbContainer)
        self.pUserDetailsSexCb.addItem("")
        self.pUserDetailsSexCb.addItem("")
        self.pUserDetailsSexCb.addItem("")
        self.pUserDetailsSexCb.setObjectName(u"pUserDetailsSexCb")
        self.pUserDetailsSexCb.setMinimumSize(QSize(70, 50))
        self.pUserDetailsSexCb.setFont(font11)
        self.pUserDetailsSexCb.setStyleSheet(u"padding-left: 7px")
        self.pUserDetailsSexCb.setEditable(False)

        self.verticalLayout_247.addWidget(self.pUserDetailsSexCb)


        self.verticalLayout_237.addWidget(self.pUserDetailsSexCbContainer)


        self.horizontalLayout_15.addWidget(self.pUserDetailsSexContainer)

        self.pUserDetailsCivilContainer = QFrame(self.pUserDetailsMidBodyContainer)
        self.pUserDetailsCivilContainer.setObjectName(u"pUserDetailsCivilContainer")
        self.pUserDetailsCivilContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsCivilContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_235 = QVBoxLayout(self.pUserDetailsCivilContainer)
        self.verticalLayout_235.setSpacing(0)
        self.verticalLayout_235.setObjectName(u"verticalLayout_235")
        self.verticalLayout_235.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsCivilLabelContainer = QFrame(self.pUserDetailsCivilContainer)
        self.pUserDetailsCivilLabelContainer.setObjectName(u"pUserDetailsCivilLabelContainer")
        self.pUserDetailsCivilLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsCivilLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_243 = QVBoxLayout(self.pUserDetailsCivilLabelContainer)
        self.verticalLayout_243.setSpacing(0)
        self.verticalLayout_243.setObjectName(u"verticalLayout_243")
        self.verticalLayout_243.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsCivilLabel = QLabel(self.pUserDetailsCivilLabelContainer)
        self.pUserDetailsCivilLabel.setObjectName(u"pUserDetailsCivilLabel")
        self.pUserDetailsCivilLabel.setFont(font10)

        self.verticalLayout_243.addWidget(self.pUserDetailsCivilLabel)


        self.verticalLayout_235.addWidget(self.pUserDetailsCivilLabelContainer)

        self.pUserDetailsCivilCbContainer = QFrame(self.pUserDetailsCivilContainer)
        self.pUserDetailsCivilCbContainer.setObjectName(u"pUserDetailsCivilCbContainer")
        self.pUserDetailsCivilCbContainer.setMinimumSize(QSize(0, 0))
        self.pUserDetailsCivilCbContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsCivilCbContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_246 = QVBoxLayout(self.pUserDetailsCivilCbContainer)
        self.verticalLayout_246.setSpacing(0)
        self.verticalLayout_246.setObjectName(u"verticalLayout_246")
        self.verticalLayout_246.setContentsMargins(0, 5, 0, 0)
        self.pUserDetailsCivilCb = QComboBox(self.pUserDetailsCivilCbContainer)
        self.pUserDetailsCivilCb.addItem("")
        self.pUserDetailsCivilCb.addItem("")
        self.pUserDetailsCivilCb.addItem("")
        self.pUserDetailsCivilCb.addItem("")
        self.pUserDetailsCivilCb.addItem("")
        self.pUserDetailsCivilCb.setObjectName(u"pUserDetailsCivilCb")
        self.pUserDetailsCivilCb.setMinimumSize(QSize(100, 50))
        self.pUserDetailsCivilCb.setFont(font11)
        self.pUserDetailsCivilCb.setStyleSheet(u"padding-left: 7px")

        self.verticalLayout_246.addWidget(self.pUserDetailsCivilCb)


        self.verticalLayout_235.addWidget(self.pUserDetailsCivilCbContainer)


        self.horizontalLayout_15.addWidget(self.pUserDetailsCivilContainer)

        self.pUserDetailsContactContainer = QFrame(self.pUserDetailsMidBodyContainer)
        self.pUserDetailsContactContainer.setObjectName(u"pUserDetailsContactContainer")
        self.pUserDetailsContactContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsContactContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_236 = QVBoxLayout(self.pUserDetailsContactContainer)
        self.verticalLayout_236.setSpacing(0)
        self.verticalLayout_236.setObjectName(u"verticalLayout_236")
        self.verticalLayout_236.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsContactLabelContainer = QFrame(self.pUserDetailsContactContainer)
        self.pUserDetailsContactLabelContainer.setObjectName(u"pUserDetailsContactLabelContainer")
        self.pUserDetailsContactLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsContactLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_244 = QVBoxLayout(self.pUserDetailsContactLabelContainer)
        self.verticalLayout_244.setSpacing(0)
        self.verticalLayout_244.setObjectName(u"verticalLayout_244")
        self.verticalLayout_244.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsContactLabel = QLabel(self.pUserDetailsContactLabelContainer)
        self.pUserDetailsContactLabel.setObjectName(u"pUserDetailsContactLabel")
        self.pUserDetailsContactLabel.setFont(font10)

        self.verticalLayout_244.addWidget(self.pUserDetailsContactLabel)


        self.verticalLayout_236.addWidget(self.pUserDetailsContactLabelContainer)

        self.pUserDetailsContactLineEditContainer = QFrame(self.pUserDetailsContactContainer)
        self.pUserDetailsContactLineEditContainer.setObjectName(u"pUserDetailsContactLineEditContainer")
        self.pUserDetailsContactLineEditContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsContactLineEditContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_245 = QVBoxLayout(self.pUserDetailsContactLineEditContainer)
        self.verticalLayout_245.setSpacing(0)
        self.verticalLayout_245.setObjectName(u"verticalLayout_245")
        self.verticalLayout_245.setContentsMargins(0, 5, 0, 0)
        self.pUserDetailsContactLineEdit = QLineEdit(self.pUserDetailsContactLineEditContainer)
        self.pUserDetailsContactLineEdit.setObjectName(u"pUserDetailsContactLineEdit")
        sizePolicy5.setHeightForWidth(self.pUserDetailsContactLineEdit.sizePolicy().hasHeightForWidth())
        self.pUserDetailsContactLineEdit.setSizePolicy(sizePolicy5)
        self.pUserDetailsContactLineEdit.setMinimumSize(QSize(150, 50))
        self.pUserDetailsContactLineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.pUserDetailsContactLineEdit.setFont(font11)

        self.verticalLayout_245.addWidget(self.pUserDetailsContactLineEdit)


        self.verticalLayout_236.addWidget(self.pUserDetailsContactLineEditContainer)


        self.horizontalLayout_15.addWidget(self.pUserDetailsContactContainer)

        self.horizontalLayout_15.setStretch(0, 3)
        self.horizontalLayout_15.setStretch(1, 1)
        self.horizontalLayout_15.setStretch(2, 2)
        self.horizontalLayout_15.setStretch(3, 4)
        self.horizontalLayout_15.setStretch(4, 4)

        self.verticalLayout_233.addWidget(self.pUserDetailsMidBodyContainer)

        self.pUserDetailsMidErrorContainer = QFrame(self.pUserDetailsMidContainer)
        self.pUserDetailsMidErrorContainer.setObjectName(u"pUserDetailsMidErrorContainer")
        sizePolicy4.setHeightForWidth(self.pUserDetailsMidErrorContainer.sizePolicy().hasHeightForWidth())
        self.pUserDetailsMidErrorContainer.setSizePolicy(sizePolicy4)
        self.pUserDetailsMidErrorContainer.setStyleSheet(u"color: rgb(255, 0, 0)")
        self.pUserDetailsMidErrorContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsMidErrorContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.pUserDetailsMidErrorContainer)
        self.horizontalLayout_16.setSpacing(60)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.birthdateErrorLabel = QLabel(self.pUserDetailsMidErrorContainer)
        self.birthdateErrorLabel.setObjectName(u"birthdateErrorLabel")
        self.birthdateErrorLabel.setMinimumSize(QSize(150, 0))
        self.birthdateErrorLabel.setFont(font12)

        self.horizontalLayout_16.addWidget(self.birthdateErrorLabel)

        self.ageErrorLabel = QLabel(self.pUserDetailsMidErrorContainer)
        self.ageErrorLabel.setObjectName(u"ageErrorLabel")
        self.ageErrorLabel.setFont(font12)

        self.horizontalLayout_16.addWidget(self.ageErrorLabel)

        self.sexErrorLabel = QLabel(self.pUserDetailsMidErrorContainer)
        self.sexErrorLabel.setObjectName(u"sexErrorLabel")
        self.sexErrorLabel.setFont(font12)

        self.horizontalLayout_16.addWidget(self.sexErrorLabel)

        self.civilErrorLabel = QLabel(self.pUserDetailsMidErrorContainer)
        self.civilErrorLabel.setObjectName(u"civilErrorLabel")
        self.civilErrorLabel.setFont(font12)

        self.horizontalLayout_16.addWidget(self.civilErrorLabel)

        self.contactErrorLabel = QLabel(self.pUserDetailsMidErrorContainer)
        self.contactErrorLabel.setObjectName(u"contactErrorLabel")
        self.contactErrorLabel.setFont(font12)

        self.horizontalLayout_16.addWidget(self.contactErrorLabel)

        self.horizontalLayout_16.setStretch(0, 3)
        self.horizontalLayout_16.setStretch(1, 1)
        self.horizontalLayout_16.setStretch(2, 2)
        self.horizontalLayout_16.setStretch(3, 4)
        self.horizontalLayout_16.setStretch(4, 4)

        self.verticalLayout_233.addWidget(self.pUserDetailsMidErrorContainer)


        self.verticalLayout_222.addWidget(self.pUserDetailsMidContainer)

        self.pUserDetailsBottomContainer = QFrame(self.pUserDetailsContainer)
        self.pUserDetailsBottomContainer.setObjectName(u"pUserDetailsBottomContainer")
        self.pUserDetailsBottomContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsBottomContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_238 = QVBoxLayout(self.pUserDetailsBottomContainer)
        self.verticalLayout_238.setSpacing(0)
        self.verticalLayout_238.setObjectName(u"verticalLayout_238")
        self.verticalLayout_238.setContentsMargins(0, 15, 0, 0)
        self.pUserDetailsBottomBodyContainer = QFrame(self.pUserDetailsBottomContainer)
        self.pUserDetailsBottomBodyContainer.setObjectName(u"pUserDetailsBottomBodyContainer")
        self.pUserDetailsBottomBodyContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsBottomBodyContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_300 = QVBoxLayout(self.pUserDetailsBottomBodyContainer)
        self.verticalLayout_300.setSpacing(0)
        self.verticalLayout_300.setObjectName(u"verticalLayout_300")
        self.verticalLayout_300.setContentsMargins(0, 0, 0, 5)
        self.userDetailsAddressLabelContainer = QFrame(self.pUserDetailsBottomBodyContainer)
        self.userDetailsAddressLabelContainer.setObjectName(u"userDetailsAddressLabelContainer")
        self.userDetailsAddressLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.userDetailsAddressLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_239 = QVBoxLayout(self.userDetailsAddressLabelContainer)
        self.verticalLayout_239.setSpacing(0)
        self.verticalLayout_239.setObjectName(u"verticalLayout_239")
        self.verticalLayout_239.setContentsMargins(0, 0, 0, 0)
        self.pUserDetailsAddressLabel = QLabel(self.userDetailsAddressLabelContainer)
        self.pUserDetailsAddressLabel.setObjectName(u"pUserDetailsAddressLabel")
        font13 = QFont()
        font13.setFamily(u"Open Sans")
        font13.setPointSize(14)
        font13.setBold(True)
        font13.setWeight(75)
        self.pUserDetailsAddressLabel.setFont(font13)

        self.verticalLayout_239.addWidget(self.pUserDetailsAddressLabel)


        self.verticalLayout_300.addWidget(self.userDetailsAddressLabelContainer)

        self.userDetailsAddressTextEditContainer = QFrame(self.pUserDetailsBottomBodyContainer)
        self.userDetailsAddressTextEditContainer.setObjectName(u"userDetailsAddressTextEditContainer")
        self.userDetailsAddressTextEditContainer.setFrameShape(QFrame.StyledPanel)
        self.userDetailsAddressTextEditContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_250 = QVBoxLayout(self.userDetailsAddressTextEditContainer)
        self.verticalLayout_250.setSpacing(0)
        self.verticalLayout_250.setObjectName(u"verticalLayout_250")
        self.verticalLayout_250.setContentsMargins(0, 5, 0, 0)
        self.pUserDetailsAddressTextEdit = QTextEdit(self.userDetailsAddressTextEditContainer)
        self.pUserDetailsAddressTextEdit.setObjectName(u"pUserDetailsAddressTextEdit")
        self.pUserDetailsAddressTextEdit.setMinimumSize(QSize(0, 60))
        self.pUserDetailsAddressTextEdit.setFont(font11)

        self.verticalLayout_250.addWidget(self.pUserDetailsAddressTextEdit)


        self.verticalLayout_300.addWidget(self.userDetailsAddressTextEditContainer)


        self.verticalLayout_238.addWidget(self.pUserDetailsBottomBodyContainer)

        self.pUserDetailsBottomErrorContainer = QFrame(self.pUserDetailsBottomContainer)
        self.pUserDetailsBottomErrorContainer.setObjectName(u"pUserDetailsBottomErrorContainer")
        sizePolicy4.setHeightForWidth(self.pUserDetailsBottomErrorContainer.sizePolicy().hasHeightForWidth())
        self.pUserDetailsBottomErrorContainer.setSizePolicy(sizePolicy4)
        self.pUserDetailsBottomErrorContainer.setStyleSheet(u"color: rgb(255, 0, 0)")
        self.pUserDetailsBottomErrorContainer.setFrameShape(QFrame.StyledPanel)
        self.pUserDetailsBottomErrorContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_301 = QVBoxLayout(self.pUserDetailsBottomErrorContainer)
        self.verticalLayout_301.setSpacing(0)
        self.verticalLayout_301.setObjectName(u"verticalLayout_301")
        self.verticalLayout_301.setContentsMargins(0, 0, 0, 0)
        self.addressErrorLabel = QLabel(self.pUserDetailsBottomErrorContainer)
        self.addressErrorLabel.setObjectName(u"addressErrorLabel")
        self.addressErrorLabel.setFont(font12)

        self.verticalLayout_301.addWidget(self.addressErrorLabel)


        self.verticalLayout_238.addWidget(self.pUserDetailsBottomErrorContainer)


        self.verticalLayout_222.addWidget(self.pUserDetailsBottomContainer)


        self.verticalLayout_220.addWidget(self.pUserDetailsContainer)

        self.pMidLabelContainer = QFrame(self.pScrollAreaContents)
        self.pMidLabelContainer.setObjectName(u"pMidLabelContainer")
        self.pMidLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.pMidLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_251 = QVBoxLayout(self.pMidLabelContainer)
        self.verticalLayout_251.setObjectName(u"verticalLayout_251")
        self.verticalLayout_251.setContentsMargins(20, 15, 20, 16)
        self.pMidLabel = QLabel(self.pMidLabelContainer)
        self.pMidLabel.setObjectName(u"pMidLabel")
        font14 = QFont()
        font14.setFamily(u"Raleway")
        font14.setPointSize(18)
        font14.setBold(True)
        font14.setWeight(75)
        self.pMidLabel.setFont(font14)

        self.verticalLayout_251.addWidget(self.pMidLabel)


        self.verticalLayout_220.addWidget(self.pMidLabelContainer)

        self.pEmergencyContainer = QFrame(self.pScrollAreaContents)
        self.pEmergencyContainer.setObjectName(u"pEmergencyContainer")
        self.pEmergencyContainer.setMinimumSize(QSize(0, 0))
        self.pEmergencyContainer.setFrameShape(QFrame.StyledPanel)
        self.pEmergencyContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_254 = QVBoxLayout(self.pEmergencyContainer)
        self.verticalLayout_254.setSpacing(0)
        self.verticalLayout_254.setObjectName(u"verticalLayout_254")
        self.verticalLayout_254.setContentsMargins(35, 0, 35, 0)
        self.pEmergencyBodyContainer = QFrame(self.pEmergencyContainer)
        self.pEmergencyBodyContainer.setObjectName(u"pEmergencyBodyContainer")
        self.pEmergencyBodyContainer.setFrameShape(QFrame.StyledPanel)
        self.pEmergencyBodyContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.pEmergencyBodyContainer)
        self.horizontalLayout_17.setSpacing(70)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 5)
        self.emergencyNameContainer = QFrame(self.pEmergencyBodyContainer)
        self.emergencyNameContainer.setObjectName(u"emergencyNameContainer")
        self.emergencyNameContainer.setFrameShape(QFrame.StyledPanel)
        self.emergencyNameContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_255 = QVBoxLayout(self.emergencyNameContainer)
        self.verticalLayout_255.setSpacing(0)
        self.verticalLayout_255.setObjectName(u"verticalLayout_255")
        self.verticalLayout_255.setContentsMargins(0, 0, 0, 0)
        self.emergencyNameLabelContainer = QFrame(self.emergencyNameContainer)
        self.emergencyNameLabelContainer.setObjectName(u"emergencyNameLabelContainer")
        self.emergencyNameLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.emergencyNameLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_257 = QVBoxLayout(self.emergencyNameLabelContainer)
        self.verticalLayout_257.setSpacing(0)
        self.verticalLayout_257.setObjectName(u"verticalLayout_257")
        self.verticalLayout_257.setContentsMargins(0, 0, 0, 0)
        self.emergencyNameLabel = QLabel(self.emergencyNameLabelContainer)
        self.emergencyNameLabel.setObjectName(u"emergencyNameLabel")
        self.emergencyNameLabel.setFont(font10)

        self.verticalLayout_257.addWidget(self.emergencyNameLabel)


        self.verticalLayout_255.addWidget(self.emergencyNameLabelContainer)

        self.emergencyNameLineEditContainer = QFrame(self.emergencyNameContainer)
        self.emergencyNameLineEditContainer.setObjectName(u"emergencyNameLineEditContainer")
        self.emergencyNameLineEditContainer.setFrameShape(QFrame.StyledPanel)
        self.emergencyNameLineEditContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_262 = QVBoxLayout(self.emergencyNameLineEditContainer)
        self.verticalLayout_262.setSpacing(0)
        self.verticalLayout_262.setObjectName(u"verticalLayout_262")
        self.verticalLayout_262.setContentsMargins(0, 5, 0, 0)
        self.emergencyNameLineEdit = QLineEdit(self.emergencyNameLineEditContainer)
        self.emergencyNameLineEdit.setObjectName(u"emergencyNameLineEdit")
        self.emergencyNameLineEdit.setMinimumSize(QSize(0, 50))
        self.emergencyNameLineEdit.setFont(font11)

        self.verticalLayout_262.addWidget(self.emergencyNameLineEdit)


        self.verticalLayout_255.addWidget(self.emergencyNameLineEditContainer)


        self.horizontalLayout_17.addWidget(self.emergencyNameContainer)

        self.emergencyRelationContainer = QFrame(self.pEmergencyBodyContainer)
        self.emergencyRelationContainer.setObjectName(u"emergencyRelationContainer")
        self.emergencyRelationContainer.setFrameShape(QFrame.StyledPanel)
        self.emergencyRelationContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_256 = QVBoxLayout(self.emergencyRelationContainer)
        self.verticalLayout_256.setSpacing(0)
        self.verticalLayout_256.setObjectName(u"verticalLayout_256")
        self.verticalLayout_256.setContentsMargins(0, 0, 0, 0)
        self.emergencyRelationLabelContainer = QFrame(self.emergencyRelationContainer)
        self.emergencyRelationLabelContainer.setObjectName(u"emergencyRelationLabelContainer")
        self.emergencyRelationLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.emergencyRelationLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_258 = QVBoxLayout(self.emergencyRelationLabelContainer)
        self.verticalLayout_258.setSpacing(0)
        self.verticalLayout_258.setObjectName(u"verticalLayout_258")
        self.verticalLayout_258.setContentsMargins(0, 0, 0, 0)
        self.emergencyRelationLabel = QLabel(self.emergencyRelationLabelContainer)
        self.emergencyRelationLabel.setObjectName(u"emergencyRelationLabel")
        font15 = QFont()
        font15.setFamily(u"Open Sans Semibold")
        font15.setPointSize(12)
        font15.setBold(True)
        font15.setWeight(75)
        self.emergencyRelationLabel.setFont(font15)

        self.verticalLayout_258.addWidget(self.emergencyRelationLabel)


        self.verticalLayout_256.addWidget(self.emergencyRelationLabelContainer)

        self.emergencyRelationLineEditContainer = QFrame(self.emergencyRelationContainer)
        self.emergencyRelationLineEditContainer.setObjectName(u"emergencyRelationLineEditContainer")
        self.emergencyRelationLineEditContainer.setFrameShape(QFrame.StyledPanel)
        self.emergencyRelationLineEditContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_260 = QVBoxLayout(self.emergencyRelationLineEditContainer)
        self.verticalLayout_260.setSpacing(0)
        self.verticalLayout_260.setObjectName(u"verticalLayout_260")
        self.verticalLayout_260.setContentsMargins(0, 5, 0, 0)
        self.emergencyRelationLineEdit = QLineEdit(self.emergencyRelationLineEditContainer)
        self.emergencyRelationLineEdit.setObjectName(u"emergencyRelationLineEdit")
        self.emergencyRelationLineEdit.setMinimumSize(QSize(0, 50))
        self.emergencyRelationLineEdit.setFont(font12)

        self.verticalLayout_260.addWidget(self.emergencyRelationLineEdit)


        self.verticalLayout_256.addWidget(self.emergencyRelationLineEditContainer)


        self.horizontalLayout_17.addWidget(self.emergencyRelationContainer)

        self.emergencyNumberContainer = QFrame(self.pEmergencyBodyContainer)
        self.emergencyNumberContainer.setObjectName(u"emergencyNumberContainer")
        self.emergencyNumberContainer.setFrameShape(QFrame.StyledPanel)
        self.emergencyNumberContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_259 = QVBoxLayout(self.emergencyNumberContainer)
        self.verticalLayout_259.setSpacing(0)
        self.verticalLayout_259.setObjectName(u"verticalLayout_259")
        self.verticalLayout_259.setContentsMargins(0, 0, 0, 0)
        self.emergencyContactLabelContainer = QFrame(self.emergencyNumberContainer)
        self.emergencyContactLabelContainer.setObjectName(u"emergencyContactLabelContainer")
        self.emergencyContactLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.emergencyContactLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_261 = QVBoxLayout(self.emergencyContactLabelContainer)
        self.verticalLayout_261.setSpacing(0)
        self.verticalLayout_261.setObjectName(u"verticalLayout_261")
        self.verticalLayout_261.setContentsMargins(0, 0, 0, 0)
        self.emergencyContactLabel = QLabel(self.emergencyContactLabelContainer)
        self.emergencyContactLabel.setObjectName(u"emergencyContactLabel")
        self.emergencyContactLabel.setFont(font15)

        self.verticalLayout_261.addWidget(self.emergencyContactLabel)


        self.verticalLayout_259.addWidget(self.emergencyContactLabelContainer)

        self.emergencyContactLineEditContainer = QFrame(self.emergencyNumberContainer)
        self.emergencyContactLineEditContainer.setObjectName(u"emergencyContactLineEditContainer")
        self.emergencyContactLineEditContainer.setFrameShape(QFrame.StyledPanel)
        self.emergencyContactLineEditContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_302 = QVBoxLayout(self.emergencyContactLineEditContainer)
        self.verticalLayout_302.setSpacing(0)
        self.verticalLayout_302.setObjectName(u"verticalLayout_302")
        self.verticalLayout_302.setContentsMargins(0, 5, 0, 0)
        self.emergencyContactLineEdit = QLineEdit(self.emergencyContactLineEditContainer)
        self.emergencyContactLineEdit.setObjectName(u"emergencyContactLineEdit")
        self.emergencyContactLineEdit.setMinimumSize(QSize(0, 50))
        self.emergencyContactLineEdit.setFont(font12)

        self.verticalLayout_302.addWidget(self.emergencyContactLineEdit)


        self.verticalLayout_259.addWidget(self.emergencyContactLineEditContainer)


        self.horizontalLayout_17.addWidget(self.emergencyNumberContainer)

        self.horizontalLayout_17.setStretch(0, 50)
        self.horizontalLayout_17.setStretch(1, 25)
        self.horizontalLayout_17.setStretch(2, 25)

        self.verticalLayout_254.addWidget(self.pEmergencyBodyContainer)

        self.pEmergencyErrorContainer = QFrame(self.pEmergencyContainer)
        self.pEmergencyErrorContainer.setObjectName(u"pEmergencyErrorContainer")
        sizePolicy4.setHeightForWidth(self.pEmergencyErrorContainer.sizePolicy().hasHeightForWidth())
        self.pEmergencyErrorContainer.setSizePolicy(sizePolicy4)
        self.pEmergencyErrorContainer.setStyleSheet(u"color: rgb(255, 0, 0)")
        self.pEmergencyErrorContainer.setFrameShape(QFrame.StyledPanel)
        self.pEmergencyErrorContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.pEmergencyErrorContainer)
        self.horizontalLayout_18.setSpacing(70)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.emergencyNameErrorLabel = QLabel(self.pEmergencyErrorContainer)
        self.emergencyNameErrorLabel.setObjectName(u"emergencyNameErrorLabel")

        self.horizontalLayout_18.addWidget(self.emergencyNameErrorLabel)

        self.emergencyRelationErrorLabel = QLabel(self.pEmergencyErrorContainer)
        self.emergencyRelationErrorLabel.setObjectName(u"emergencyRelationErrorLabel")

        self.horizontalLayout_18.addWidget(self.emergencyRelationErrorLabel)

        self.emergencyContactErrorLabel = QLabel(self.pEmergencyErrorContainer)
        self.emergencyContactErrorLabel.setObjectName(u"emergencyContactErrorLabel")

        self.horizontalLayout_18.addWidget(self.emergencyContactErrorLabel)

        self.horizontalLayout_18.setStretch(0, 50)
        self.horizontalLayout_18.setStretch(1, 25)
        self.horizontalLayout_18.setStretch(2, 25)

        self.verticalLayout_254.addWidget(self.pEmergencyErrorContainer)


        self.verticalLayout_220.addWidget(self.pEmergencyContainer)

        self.pBottomContainer = QFrame(self.pScrollAreaContents)
        self.pBottomContainer.setObjectName(u"pBottomContainer")
        self.pBottomContainer.setMinimumSize(QSize(0, 0))
        self.pBottomContainer.setFrameShape(QFrame.StyledPanel)
        self.pBottomContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_252 = QVBoxLayout(self.pBottomContainer)
        self.verticalLayout_252.setSpacing(0)
        self.verticalLayout_252.setObjectName(u"verticalLayout_252")
        self.verticalLayout_252.setContentsMargins(20, 20, 20, 20)
        self.pBottomLineContainer = QFrame(self.pBottomContainer)
        self.pBottomLineContainer.setObjectName(u"pBottomLineContainer")
        self.pBottomLineContainer.setFrameShape(QFrame.StyledPanel)
        self.pBottomLineContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_253 = QVBoxLayout(self.pBottomLineContainer)
        self.verticalLayout_253.setSpacing(0)
        self.verticalLayout_253.setObjectName(u"verticalLayout_253")
        self.verticalLayout_253.setContentsMargins(0, 0, 0, 10)
        self.pBottomLine = QFrame(self.pBottomLineContainer)
        self.pBottomLine.setObjectName(u"pBottomLine")
        self.pBottomLine.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.pBottomLine.setFrameShape(QFrame.HLine)
        self.pBottomLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_253.addWidget(self.pBottomLine)


        self.verticalLayout_252.addWidget(self.pBottomLineContainer, 0, Qt.AlignTop)

        self.pBottomBtnContainer = QFrame(self.pBottomContainer)
        self.pBottomBtnContainer.setObjectName(u"pBottomBtnContainer")
        self.pBottomBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.pBottomBtnContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.pBottomBtnContainer)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.pBottomNextBtn = QPushButton(self.pBottomBtnContainer)
        self.pBottomNextBtn.setObjectName(u"pBottomNextBtn")
        self.pBottomNextBtn.setFont(font13)
        self.pBottomNextBtn.setStyleSheet(u"background-color:rgb(56, 166, 255);\n"
"padding: 3px 23px 3px 23px;\n"
"border-radius: 15px;\n"
"color: #fff;")

        self.horizontalLayout_69.addWidget(self.pBottomNextBtn)


        self.verticalLayout_252.addWidget(self.pBottomBtnContainer, 0, Qt.AlignRight)


        self.verticalLayout_220.addWidget(self.pBottomContainer)

        self.pScrollArea.setWidget(self.pScrollAreaContents)

        self.verticalLayout_184.addWidget(self.pScrollArea)


        self.verticalLayout_183.addWidget(self.pWhiteCard)


        self.verticalLayout_182.addWidget(self.pBlueCard)


        self.verticalLayout_228.addWidget(self.pMarginContainer)

        self.diagnosisStackedWidget.addWidget(self.diagnosisProfilePage)
        self.diagnosisSymptomsPage = QWidget()
        self.diagnosisSymptomsPage.setObjectName(u"diagnosisSymptomsPage")
        self.verticalLayout_34 = QVBoxLayout(self.diagnosisSymptomsPage)
        self.verticalLayout_34.setSpacing(6)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(9, 9, 9, 9)
        self.symptomProgressContainer = QWidget(self.diagnosisSymptomsPage)
        self.symptomProgressContainer.setObjectName(u"symptomProgressContainer")
        sizePolicy1.setHeightForWidth(self.symptomProgressContainer.sizePolicy().hasHeightForWidth())
        self.symptomProgressContainer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_38 = QHBoxLayout(self.symptomProgressContainer)
        self.horizontalLayout_38.setSpacing(6)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.symPExitBtnContainer = QFrame(self.symptomProgressContainer)
        self.symPExitBtnContainer.setObjectName(u"symPExitBtnContainer")
        self.symPExitBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.symPExitBtnContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.symPExitBtnContainer)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.symPExitBtn = QPushButton(self.symPExitBtnContainer)
        self.symPExitBtn.setObjectName(u"symPExitBtn")
        self.symPExitBtn.setIcon(icon5)
        self.symPExitBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_39.addWidget(self.symPExitBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_38.addWidget(self.symPExitBtnContainer, 0, Qt.AlignLeft)

        self.symPProgressContainer = QFrame(self.symptomProgressContainer)
        self.symPProgressContainer.setObjectName(u"symPProgressContainer")
        self.symPProgressContainer.setFrameShape(QFrame.StyledPanel)
        self.symPProgressContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.symPProgressContainer)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.symPProgress = QLabel(self.symPProgressContainer)
        self.symPProgress.setObjectName(u"symPProgress")
        sizePolicy2.setHeightForWidth(self.symPProgress.sizePolicy().hasHeightForWidth())
        self.symPProgress.setSizePolicy(sizePolicy2)
        self.symPProgress.setMinimumSize(QSize(680, 45))
        self.symPProgress.setMaximumSize(QSize(680, 45))
        self.symPProgress.setSizeIncrement(QSize(0, 0))
        self.symPProgress.setFont(font7)
        self.symPProgress.setFrameShadow(QFrame.Plain)
        self.symPProgress.setPixmap(QPixmap(u":/progressBarImages/images/progress2.png"))
        self.symPProgress.setScaledContents(True)
        self.symPProgress.setWordWrap(False)

        self.horizontalLayout_47.addWidget(self.symPProgress, 0, Qt.AlignVCenter)


        self.horizontalLayout_38.addWidget(self.symPProgressContainer, 0, Qt.AlignHCenter)

        self.symPExitBtn2 = QPushButton(self.symptomProgressContainer)
        self.symPExitBtn2.setObjectName(u"symPExitBtn2")
        self.symPExitBtn2.setEnabled(False)

        self.horizontalLayout_38.addWidget(self.symPExitBtn2)


        self.verticalLayout_34.addWidget(self.symptomProgressContainer)

        self.symMarginContainer = QFrame(self.diagnosisSymptomsPage)
        self.symMarginContainer.setObjectName(u"symMarginContainer")
        sizePolicy3.setHeightForWidth(self.symMarginContainer.sizePolicy().hasHeightForWidth())
        self.symMarginContainer.setSizePolicy(sizePolicy3)
        self.symMarginContainer.setFrameShape(QFrame.StyledPanel)
        self.symMarginContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_185 = QVBoxLayout(self.symMarginContainer)
        self.verticalLayout_185.setObjectName(u"verticalLayout_185")
        self.verticalLayout_185.setContentsMargins(70, 0, 70, 9)
        self.symBlueCard = QFrame(self.symMarginContainer)
        self.symBlueCard.setObjectName(u"symBlueCard")
        self.symBlueCard.setStyleSheet(u"background-color:#58AAEC;\n"
"border-radius: 15px;")
        self.symBlueCard.setFrameShape(QFrame.StyledPanel)
        self.symBlueCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_186 = QVBoxLayout(self.symBlueCard)
        self.verticalLayout_186.setSpacing(0)
        self.verticalLayout_186.setObjectName(u"verticalLayout_186")
        self.verticalLayout_186.setContentsMargins(10, 0, 0, 0)
        self.sympWhiteCard = QFrame(self.symBlueCard)
        self.sympWhiteCard.setObjectName(u"sympWhiteCard")
        self.sympWhiteCard.setStyleSheet(u"background-color:#FFF;\n"
"border-radius: 15px;")
        self.sympWhiteCard.setFrameShape(QFrame.StyledPanel)
        self.sympWhiteCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_187 = QVBoxLayout(self.sympWhiteCard)
        self.verticalLayout_187.setObjectName(u"verticalLayout_187")
        self.verticalLayout_187.setContentsMargins(5, 5, 5, 5)
        self.symScrollArea = QScrollArea(self.sympWhiteCard)
        self.symScrollArea.setObjectName(u"symScrollArea")
        self.symScrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.symScrollArea.setWidgetResizable(True)
        self.symScrollAreaContents = QWidget()
        self.symScrollAreaContents.setObjectName(u"symScrollAreaContents")
        self.symScrollAreaContents.setGeometry(QRect(0, 0, 694, 566))
        self.symScrollAreaContents.setStyleSheet(u" QLineEdit, QTextEdit, QComboBox, QDateEdit {\n"
"	border: 1px solid #D9D9D9;\n"
"border-radius: 5px\n"
" }")
        self.verticalLayout_35 = QVBoxLayout(self.symScrollAreaContents)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.symMainContainer = QFrame(self.symScrollAreaContents)
        self.symMainContainer.setObjectName(u"symMainContainer")
        sizePolicy3.setHeightForWidth(self.symMainContainer.sizePolicy().hasHeightForWidth())
        self.symMainContainer.setSizePolicy(sizePolicy3)
        self.symMainContainer.setFrameShape(QFrame.StyledPanel)
        self.symMainContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.symMainContainer)
        self.horizontalLayout_57.setSpacing(30)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.symLeftContainer = QFrame(self.symMainContainer)
        self.symLeftContainer.setObjectName(u"symLeftContainer")
        self.symLeftContainer.setFrameShape(QFrame.StyledPanel)
        self.symLeftContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.symLeftContainer)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.symLabelContainer = QFrame(self.symLeftContainer)
        self.symLabelContainer.setObjectName(u"symLabelContainer")
        self.symLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.symLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.symLabelContainer)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(20, 15, 20, 10)
        self.symTopLabel = QLabel(self.symLabelContainer)
        self.symTopLabel.setObjectName(u"symTopLabel")
        self.symTopLabel.setFont(font14)

        self.verticalLayout_37.addWidget(self.symTopLabel)


        self.verticalLayout_36.addWidget(self.symLabelContainer)

        self.symSearchContainer = QFrame(self.symLeftContainer)
        self.symSearchContainer.setObjectName(u"symSearchContainer")
        self.symSearchContainer.setFrameShape(QFrame.StyledPanel)
        self.symSearchContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.symSearchContainer)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(35, 10, 20, 10)
        self.symSearchIcon = QPushButton(self.symSearchContainer)
        self.symSearchIcon.setObjectName(u"symSearchIcon")

        self.horizontalLayout_58.addWidget(self.symSearchIcon)

        self.symSearchLineEdit = QLineEdit(self.symSearchContainer)
        self.symSearchLineEdit.setObjectName(u"symSearchLineEdit")

        self.horizontalLayout_58.addWidget(self.symSearchLineEdit)


        self.verticalLayout_36.addWidget(self.symSearchContainer)

        self.symSymptomsContainer = QFrame(self.symLeftContainer)
        self.symSymptomsContainer.setObjectName(u"symSymptomsContainer")
        self.symSymptomsContainer.setStyleSheet(u"#symptomContainer{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}")
        self.symSymptomsContainer.setFrameShape(QFrame.StyledPanel)
        self.symSymptomsContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.symSymptomsContainer)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(35, 0, 0, 0)
        self.symptomContainer = QFrame(self.symSymptomsContainer)
        self.symptomContainer.setObjectName(u"symptomContainer")
        self.symptomContainer.setStyleSheet(u"#symptomContainer{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}")
        self.symptomContainer.setFrameShape(QFrame.StyledPanel)
        self.symptomContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.symptomContainer)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.symptomScrollArea = QScrollArea(self.symptomContainer)
        self.symptomScrollArea.setObjectName(u"symptomScrollArea")
        self.symptomScrollArea.setWidgetResizable(True)
        self.symptomScrollAreaContents = QWidget()
        self.symptomScrollAreaContents.setObjectName(u"symptomScrollAreaContents")
        self.symptomScrollAreaContents.setGeometry(QRect(0, 0, 110, 352))
        self.verticalLayout_44 = QVBoxLayout(self.symptomScrollAreaContents)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.symptomEntryContainer1 = QFrame(self.symptomScrollAreaContents)
        self.symptomEntryContainer1.setObjectName(u"symptomEntryContainer1")
        self.symptomEntryContainer1.setFrameShape(QFrame.StyledPanel)
        self.symptomEntryContainer1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.symptomEntryContainer1)
        self.verticalLayout_45.setSpacing(3)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 5)
        self.symCbContainer1 = QFrame(self.symptomEntryContainer1)
        self.symCbContainer1.setObjectName(u"symCbContainer1")
        self.symCbContainer1.setFrameShape(QFrame.StyledPanel)
        self.symCbContainer1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.symCbContainer1)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.symCb1 = QCheckBox(self.symCbContainer1)
        self.symCb1.setObjectName(u"symCb1")

        self.verticalLayout_48.addWidget(self.symCb1)


        self.verticalLayout_45.addWidget(self.symCbContainer1)

        self.symDescContainer1 = QFrame(self.symptomEntryContainer1)
        self.symDescContainer1.setObjectName(u"symDescContainer1")
        self.symDescContainer1.setFrameShape(QFrame.StyledPanel)
        self.symDescContainer1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.symDescContainer1)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(20, 0, 20, 0)
        self.symDesc1 = QLabel(self.symDescContainer1)
        self.symDesc1.setObjectName(u"symDesc1")
        self.symDesc1.setWordWrap(True)

        self.verticalLayout_47.addWidget(self.symDesc1)


        self.verticalLayout_45.addWidget(self.symDescContainer1)

        self.symLineContainer1 = QFrame(self.symptomEntryContainer1)
        self.symLineContainer1.setObjectName(u"symLineContainer1")
        self.symLineContainer1.setFrameShape(QFrame.StyledPanel)
        self.symLineContainer1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.symLineContainer1)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(-1, 0, -1, 0)
        self.symLine1 = QFrame(self.symLineContainer1)
        self.symLine1.setObjectName(u"symLine1")
        self.symLine1.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.symLine1.setFrameShape(QFrame.HLine)
        self.symLine1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_46.addWidget(self.symLine1)


        self.verticalLayout_45.addWidget(self.symLineContainer1)


        self.verticalLayout_44.addWidget(self.symptomEntryContainer1)

        self.symptomEntryContainer2 = QFrame(self.symptomScrollAreaContents)
        self.symptomEntryContainer2.setObjectName(u"symptomEntryContainer2")
        self.symptomEntryContainer2.setFrameShape(QFrame.StyledPanel)
        self.symptomEntryContainer2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.symptomEntryContainer2)
        self.verticalLayout_53.setSpacing(3)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 5)
        self.symCbContainer2 = QFrame(self.symptomEntryContainer2)
        self.symCbContainer2.setObjectName(u"symCbContainer2")
        self.symCbContainer2.setFrameShape(QFrame.StyledPanel)
        self.symCbContainer2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.symCbContainer2)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.symCb2 = QCheckBox(self.symCbContainer2)
        self.symCb2.setObjectName(u"symCb2")

        self.verticalLayout_54.addWidget(self.symCb2)


        self.verticalLayout_53.addWidget(self.symCbContainer2)

        self.symDescContainer2 = QFrame(self.symptomEntryContainer2)
        self.symDescContainer2.setObjectName(u"symDescContainer2")
        self.symDescContainer2.setFrameShape(QFrame.StyledPanel)
        self.symDescContainer2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.symDescContainer2)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(20, 0, 20, 0)
        self.symDesc2 = QLabel(self.symDescContainer2)
        self.symDesc2.setObjectName(u"symDesc2")
        self.symDesc2.setWordWrap(True)

        self.verticalLayout_55.addWidget(self.symDesc2)


        self.verticalLayout_53.addWidget(self.symDescContainer2)

        self.symLineContainer2 = QFrame(self.symptomEntryContainer2)
        self.symLineContainer2.setObjectName(u"symLineContainer2")
        self.symLineContainer2.setFrameShape(QFrame.StyledPanel)
        self.symLineContainer2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.symLineContainer2)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(-1, 0, -1, 0)
        self.symLine2 = QFrame(self.symLineContainer2)
        self.symLine2.setObjectName(u"symLine2")
        self.symLine2.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.symLine2.setFrameShape(QFrame.HLine)
        self.symLine2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_56.addWidget(self.symLine2)


        self.verticalLayout_53.addWidget(self.symLineContainer2)


        self.verticalLayout_44.addWidget(self.symptomEntryContainer2)

        self.symptomEntryContainer3 = QFrame(self.symptomScrollAreaContents)
        self.symptomEntryContainer3.setObjectName(u"symptomEntryContainer3")
        self.symptomEntryContainer3.setFrameShape(QFrame.StyledPanel)
        self.symptomEntryContainer3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.symptomEntryContainer3)
        self.verticalLayout_57.setSpacing(3)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 5)
        self.symCbContainer2_2 = QFrame(self.symptomEntryContainer3)
        self.symCbContainer2_2.setObjectName(u"symCbContainer2_2")
        self.symCbContainer2_2.setFrameShape(QFrame.StyledPanel)
        self.symCbContainer2_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.symCbContainer2_2)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.symCb3 = QCheckBox(self.symCbContainer2_2)
        self.symCb3.setObjectName(u"symCb3")

        self.verticalLayout_58.addWidget(self.symCb3)


        self.verticalLayout_57.addWidget(self.symCbContainer2_2)

        self.symDescContainer3 = QFrame(self.symptomEntryContainer3)
        self.symDescContainer3.setObjectName(u"symDescContainer3")
        self.symDescContainer3.setFrameShape(QFrame.StyledPanel)
        self.symDescContainer3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.symDescContainer3)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(20, 0, 20, 0)
        self.symDesc3 = QLabel(self.symDescContainer3)
        self.symDesc3.setObjectName(u"symDesc3")
        self.symDesc3.setWordWrap(True)

        self.verticalLayout_59.addWidget(self.symDesc3)


        self.verticalLayout_57.addWidget(self.symDescContainer3)

        self.symLineContainer2_2 = QFrame(self.symptomEntryContainer3)
        self.symLineContainer2_2.setObjectName(u"symLineContainer2_2")
        self.symLineContainer2_2.setFrameShape(QFrame.StyledPanel)
        self.symLineContainer2_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.symLineContainer2_2)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(-1, 0, -1, 0)
        self.symLine3 = QFrame(self.symLineContainer2_2)
        self.symLine3.setObjectName(u"symLine3")
        self.symLine3.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.symLine3.setFrameShape(QFrame.HLine)
        self.symLine3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_60.addWidget(self.symLine3)


        self.verticalLayout_57.addWidget(self.symLineContainer2_2)


        self.verticalLayout_44.addWidget(self.symptomEntryContainer3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_44.addItem(self.verticalSpacer_3)

        self.symptomScrollArea.setWidget(self.symptomScrollAreaContents)

        self.verticalLayout_41.addWidget(self.symptomScrollArea)


        self.verticalLayout_38.addWidget(self.symptomContainer)


        self.verticalLayout_36.addWidget(self.symSymptomsContainer)

        self.symSelectedContainer = QFrame(self.symLeftContainer)
        self.symSelectedContainer.setObjectName(u"symSelectedContainer")
        self.symSelectedContainer.setStyleSheet(u"")
        self.symSelectedContainer.setFrameShape(QFrame.StyledPanel)
        self.symSelectedContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.symSelectedContainer)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(35, 10, 0, 0)
        self.selectedContainer = QFrame(self.symSelectedContainer)
        self.selectedContainer.setObjectName(u"selectedContainer")
        self.selectedContainer.setStyleSheet(u"#selectedContainer{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}")
        self.selectedContainer.setFrameShape(QFrame.StyledPanel)
        self.selectedContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.selectedContainer)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.selectedScrollArea = QScrollArea(self.selectedContainer)
        self.selectedScrollArea.setObjectName(u"selectedScrollArea")
        self.selectedScrollArea.setWidgetResizable(True)
        self.selectedScrollAreaContents = QWidget()
        self.selectedScrollAreaContents.setObjectName(u"selectedScrollAreaContents")
        self.selectedScrollAreaContents.setGeometry(QRect(0, 0, 100, 30))
        self.selectedScrollArea.setWidget(self.selectedScrollAreaContents)

        self.verticalLayout_40.addWidget(self.selectedScrollArea)


        self.verticalLayout_39.addWidget(self.selectedContainer)


        self.verticalLayout_36.addWidget(self.symSelectedContainer)

        self.verticalLayout_36.setStretch(0, 1)
        self.verticalLayout_36.setStretch(2, 4)
        self.verticalLayout_36.setStretch(3, 2)

        self.horizontalLayout_57.addWidget(self.symLeftContainer)

        self.symRightContainer = QFrame(self.symMainContainer)
        self.symRightContainer.setObjectName(u"symRightContainer")
        self.symRightContainer.setFrameShape(QFrame.StyledPanel)
        self.symRightContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.symRightContainer)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(30, -1, 20, -1)
        self.symBodyComboBox = QComboBox(self.symRightContainer)
        self.symBodyComboBox.addItem("")
        self.symBodyComboBox.addItem("")
        self.symBodyComboBox.addItem("")
        self.symBodyComboBox.addItem("")
        self.symBodyComboBox.addItem("")
        self.symBodyComboBox.addItem("")
        self.symBodyComboBox.setObjectName(u"symBodyComboBox")

        self.verticalLayout_43.addWidget(self.symBodyComboBox)

        self.symImageContainer = QFrame(self.symRightContainer)
        self.symImageContainer.setObjectName(u"symImageContainer")
        self.symImageContainer.setFrameShape(QFrame.StyledPanel)
        self.symImageContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.symImageContainer)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.symImage = QLabel(self.symImageContainer)
        self.symImage.setObjectName(u"symImage")
        sizePolicy1.setHeightForWidth(self.symImage.sizePolicy().hasHeightForWidth())
        self.symImage.setSizePolicy(sizePolicy1)
        self.symImage.setMinimumSize(QSize(350, 420))
        self.symImage.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_42.addWidget(self.symImage)


        self.verticalLayout_43.addWidget(self.symImageContainer)


        self.horizontalLayout_57.addWidget(self.symRightContainer)

        self.horizontalLayout_57.setStretch(0, 60)
        self.horizontalLayout_57.setStretch(1, 40)

        self.verticalLayout_35.addWidget(self.symMainContainer)

        self.symBottomContainer = QFrame(self.symScrollAreaContents)
        self.symBottomContainer.setObjectName(u"symBottomContainer")
        self.symBottomContainer.setMinimumSize(QSize(0, 0))
        self.symBottomContainer.setFrameShape(QFrame.StyledPanel)
        self.symBottomContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_263 = QVBoxLayout(self.symBottomContainer)
        self.verticalLayout_263.setSpacing(0)
        self.verticalLayout_263.setObjectName(u"verticalLayout_263")
        self.verticalLayout_263.setContentsMargins(20, 20, 20, 20)
        self.symBottomLineContainer = QFrame(self.symBottomContainer)
        self.symBottomLineContainer.setObjectName(u"symBottomLineContainer")
        self.symBottomLineContainer.setFrameShape(QFrame.StyledPanel)
        self.symBottomLineContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_264 = QVBoxLayout(self.symBottomLineContainer)
        self.verticalLayout_264.setSpacing(0)
        self.verticalLayout_264.setObjectName(u"verticalLayout_264")
        self.verticalLayout_264.setContentsMargins(0, 0, 0, 10)
        self.symBottomLine = QFrame(self.symBottomLineContainer)
        self.symBottomLine.setObjectName(u"symBottomLine")
        self.symBottomLine.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.symBottomLine.setFrameShape(QFrame.HLine)
        self.symBottomLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_264.addWidget(self.symBottomLine)


        self.verticalLayout_263.addWidget(self.symBottomLineContainer, 0, Qt.AlignTop)

        self.symBottomBtnContainer = QFrame(self.symBottomContainer)
        self.symBottomBtnContainer.setObjectName(u"symBottomBtnContainer")
        self.symBottomBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.symBottomBtnContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.symBottomBtnContainer)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.symBottomNextBtn = QPushButton(self.symBottomBtnContainer)
        self.symBottomNextBtn.setObjectName(u"symBottomNextBtn")
        self.symBottomNextBtn.setFont(font13)
        self.symBottomNextBtn.setStyleSheet(u"background-color:rgb(56, 166, 255);\n"
"padding: 3px 23px 3px 23px;\n"
"border-radius: 15px;\n"
"color: #fff;")

        self.horizontalLayout_71.addWidget(self.symBottomNextBtn)


        self.verticalLayout_263.addWidget(self.symBottomBtnContainer, 0, Qt.AlignRight)


        self.verticalLayout_35.addWidget(self.symBottomContainer)

        self.symScrollArea.setWidget(self.symScrollAreaContents)

        self.verticalLayout_187.addWidget(self.symScrollArea)


        self.verticalLayout_186.addWidget(self.sympWhiteCard)


        self.verticalLayout_185.addWidget(self.symBlueCard)


        self.verticalLayout_34.addWidget(self.symMarginContainer)

        self.diagnosisStackedWidget.addWidget(self.diagnosisSymptomsPage)
        self.diagnosisInterviewPage = QWidget()
        self.diagnosisInterviewPage.setObjectName(u"diagnosisInterviewPage")
        self.verticalLayout_12 = QVBoxLayout(self.diagnosisInterviewPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.iProgressContainer = QWidget(self.diagnosisInterviewPage)
        self.iProgressContainer.setObjectName(u"iProgressContainer")
        sizePolicy1.setHeightForWidth(self.iProgressContainer.sizePolicy().hasHeightForWidth())
        self.iProgressContainer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_26 = QHBoxLayout(self.iProgressContainer)
        self.horizontalLayout_26.setSpacing(6)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.iPExitBtnContainer = QFrame(self.iProgressContainer)
        self.iPExitBtnContainer.setObjectName(u"iPExitBtnContainer")
        self.iPExitBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.iPExitBtnContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.iPExitBtnContainer)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.iPExitBtn = QPushButton(self.iPExitBtnContainer)
        self.iPExitBtn.setObjectName(u"iPExitBtn")
        self.iPExitBtn.setIcon(icon5)
        self.iPExitBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.iPExitBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_26.addWidget(self.iPExitBtnContainer, 0, Qt.AlignLeft)

        self.iPProgressContainer = QFrame(self.iProgressContainer)
        self.iPProgressContainer.setObjectName(u"iPProgressContainer")
        self.iPProgressContainer.setFrameShape(QFrame.StyledPanel)
        self.iPProgressContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.iPProgressContainer)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.iPProgress = QLabel(self.iPProgressContainer)
        self.iPProgress.setObjectName(u"iPProgress")
        sizePolicy2.setHeightForWidth(self.iPProgress.sizePolicy().hasHeightForWidth())
        self.iPProgress.setSizePolicy(sizePolicy2)
        self.iPProgress.setMinimumSize(QSize(680, 45))
        self.iPProgress.setMaximumSize(QSize(680, 45))
        self.iPProgress.setSizeIncrement(QSize(0, 0))
        self.iPProgress.setFont(font7)
        self.iPProgress.setFrameShadow(QFrame.Plain)
        self.iPProgress.setPixmap(QPixmap(u":/progressBarImages/images/progress3.png"))
        self.iPProgress.setScaledContents(True)
        self.iPProgress.setWordWrap(False)

        self.horizontalLayout_28.addWidget(self.iPProgress, 0, Qt.AlignVCenter)


        self.horizontalLayout_26.addWidget(self.iPProgressContainer, 0, Qt.AlignHCenter)

        self.iPExitBtn2 = QPushButton(self.iProgressContainer)
        self.iPExitBtn2.setObjectName(u"iPExitBtn2")
        self.iPExitBtn2.setEnabled(False)

        self.horizontalLayout_26.addWidget(self.iPExitBtn2)


        self.verticalLayout_12.addWidget(self.iProgressContainer)

        self.iMarginContainer = QFrame(self.diagnosisInterviewPage)
        self.iMarginContainer.setObjectName(u"iMarginContainer")
        sizePolicy3.setHeightForWidth(self.iMarginContainer.sizePolicy().hasHeightForWidth())
        self.iMarginContainer.setSizePolicy(sizePolicy3)
        self.iMarginContainer.setFrameShape(QFrame.StyledPanel)
        self.iMarginContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_188 = QVBoxLayout(self.iMarginContainer)
        self.verticalLayout_188.setObjectName(u"verticalLayout_188")
        self.verticalLayout_188.setContentsMargins(70, 0, 70, 9)
        self.iBlueCard = QFrame(self.iMarginContainer)
        self.iBlueCard.setObjectName(u"iBlueCard")
        self.iBlueCard.setStyleSheet(u"background-color:#58AAEC;\n"
"border-radius: 15px;")
        self.iBlueCard.setFrameShape(QFrame.StyledPanel)
        self.iBlueCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_189 = QVBoxLayout(self.iBlueCard)
        self.verticalLayout_189.setSpacing(0)
        self.verticalLayout_189.setObjectName(u"verticalLayout_189")
        self.verticalLayout_189.setContentsMargins(10, 0, 0, 0)
        self.iWhiteCard = QFrame(self.iBlueCard)
        self.iWhiteCard.setObjectName(u"iWhiteCard")
        self.iWhiteCard.setStyleSheet(u"background-color:#FFF;\n"
"border-radius: 15px;")
        self.iWhiteCard.setFrameShape(QFrame.StyledPanel)
        self.iWhiteCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.iWhiteCard)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.iScrollArea = QScrollArea(self.iWhiteCard)
        self.iScrollArea.setObjectName(u"iScrollArea")
        self.iScrollArea.setMinimumSize(QSize(0, 0))
        self.iScrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.iScrollArea.setWidgetResizable(True)
        self.iScrollAreaContents = QWidget()
        self.iScrollAreaContents.setObjectName(u"iScrollAreaContents")
        self.iScrollAreaContents.setGeometry(QRect(0, 0, 566, 527))
        self.iScrollAreaContents.setStyleSheet(u" QLineEdit, QTextEdit, QComboBox, QDateEdit {\n"
"	border: 1px solid #D9D9D9;\n"
"border-radius: 5px\n"
" }")
        self.verticalLayout_15 = QVBoxLayout(self.iScrollAreaContents)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.iTopContainer = QFrame(self.iScrollAreaContents)
        self.iTopContainer.setObjectName(u"iTopContainer")
        self.iTopContainer.setFrameShape(QFrame.StyledPanel)
        self.iTopContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.iTopContainer)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(20, 15, 20, 10)
        self.label = QLabel(self.iTopContainer)
        self.label.setObjectName(u"label")
        self.label.setFont(font14)

        self.verticalLayout_16.addWidget(self.label)

        self.label_2 = QLabel(self.iTopContainer)
        self.label_2.setObjectName(u"label_2")
        font16 = QFont()
        font16.setFamily(u"Open Sans")
        font16.setPointSize(10)
        font16.setBold(False)
        font16.setWeight(50)
        self.label_2.setFont(font16)

        self.verticalLayout_16.addWidget(self.label_2)

        self.frame_8 = QFrame(self.iTopContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_8)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 10, 0, 0)
        self.line = QFrame(self.frame_8)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"border: 1px solid;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_24.addWidget(self.line)


        self.verticalLayout_16.addWidget(self.frame_8)


        self.verticalLayout_15.addWidget(self.iTopContainer)

        self.iInterviewContainer = QFrame(self.iScrollAreaContents)
        self.iInterviewContainer.setObjectName(u"iInterviewContainer")
        sizePolicy3.setHeightForWidth(self.iInterviewContainer.sizePolicy().hasHeightForWidth())
        self.iInterviewContainer.setSizePolicy(sizePolicy3)
        self.iInterviewContainer.setFrameShape(QFrame.StyledPanel)
        self.iInterviewContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.iInterviewContainer)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(30, 0, 30, 0)
        self.iInterviewScrollArea = QScrollArea(self.iInterviewContainer)
        self.iInterviewScrollArea.setObjectName(u"iInterviewScrollArea")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.iInterviewScrollArea.sizePolicy().hasHeightForWidth())
        self.iInterviewScrollArea.setSizePolicy(sizePolicy6)
        self.iInterviewScrollArea.setMinimumSize(QSize(0, 350))
        self.iInterviewScrollArea.setWidgetResizable(True)
        self.iInterviewScrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.iInterviewScrollAreaContents = QWidget()
        self.iInterviewScrollAreaContents.setObjectName(u"iInterviewScrollAreaContents")
        self.iInterviewScrollAreaContents.setGeometry(QRect(0, 0, 116, 1174))
        self.verticalLayout_28 = QVBoxLayout(self.iInterviewScrollAreaContents)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.symptomEntryContainer = QFrame(self.iInterviewScrollAreaContents)
        self.symptomEntryContainer.setObjectName(u"symptomEntryContainer")
        sizePolicy1.setHeightForWidth(self.symptomEntryContainer.sizePolicy().hasHeightForWidth())
        self.symptomEntryContainer.setSizePolicy(sizePolicy1)
        self.symptomEntryContainer.setFrameShape(QFrame.StyledPanel)
        self.symptomEntryContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_159 = QVBoxLayout(self.symptomEntryContainer)
        self.verticalLayout_159.setSpacing(3)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.verticalLayout_159.setContentsMargins(0, 0, 0, 5)
        self.iCbContainer = QFrame(self.symptomEntryContainer)
        self.iCbContainer.setObjectName(u"iCbContainer")
        self.iCbContainer.setFrameShape(QFrame.StyledPanel)
        self.iCbContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_160 = QVBoxLayout(self.iCbContainer)
        self.verticalLayout_160.setSpacing(0)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.verticalLayout_160.setContentsMargins(0, 0, 0, 0)
        self.isymCb = QCheckBox(self.iCbContainer)
        self.isymCb.setObjectName(u"isymCb")
        font17 = QFont()
        font17.setFamily(u"Open Sans")
        font17.setPointSize(10)
        font17.setBold(True)
        font17.setWeight(75)
        self.isymCb.setFont(font17)

        self.verticalLayout_160.addWidget(self.isymCb)


        self.verticalLayout_159.addWidget(self.iCbContainer)

        self.iDescContainer1 = QFrame(self.symptomEntryContainer)
        self.iDescContainer1.setObjectName(u"iDescContainer1")
        self.iDescContainer1.setFrameShape(QFrame.StyledPanel)
        self.iDescContainer1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.iDescContainer1)
        self.verticalLayout_161.setSpacing(0)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(20, 0, 20, 0)
        self.iDesc1 = QLabel(self.iDescContainer1)
        self.iDesc1.setObjectName(u"iDesc1")
        self.iDesc1.setFont(font12)
        self.iDesc1.setWordWrap(True)

        self.verticalLayout_161.addWidget(self.iDesc1)


        self.verticalLayout_159.addWidget(self.iDescContainer1)

        self.iLineContainer1 = QFrame(self.symptomEntryContainer)
        self.iLineContainer1.setObjectName(u"iLineContainer1")
        self.iLineContainer1.setFrameShape(QFrame.StyledPanel)
        self.iLineContainer1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_162 = QVBoxLayout(self.iLineContainer1)
        self.verticalLayout_162.setSpacing(0)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(-1, 5, -1, 5)
        self.isymLine1 = QFrame(self.iLineContainer1)
        self.isymLine1.setObjectName(u"isymLine1")
        self.isymLine1.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.isymLine1.setFrameShape(QFrame.HLine)
        self.isymLine1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_162.addWidget(self.isymLine1)


        self.verticalLayout_159.addWidget(self.iLineContainer1)


        self.verticalLayout_28.addWidget(self.symptomEntryContainer)

        self.symptomEntryContainer_3 = QFrame(self.iInterviewScrollAreaContents)
        self.symptomEntryContainer_3.setObjectName(u"symptomEntryContainer_3")
        sizePolicy1.setHeightForWidth(self.symptomEntryContainer_3.sizePolicy().hasHeightForWidth())
        self.symptomEntryContainer_3.setSizePolicy(sizePolicy1)
        self.symptomEntryContainer_3.setFrameShape(QFrame.StyledPanel)
        self.symptomEntryContainer_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_167 = QVBoxLayout(self.symptomEntryContainer_3)
        self.verticalLayout_167.setSpacing(3)
        self.verticalLayout_167.setObjectName(u"verticalLayout_167")
        self.verticalLayout_167.setContentsMargins(0, 0, 0, 5)
        self.iCbContainer_3 = QFrame(self.symptomEntryContainer_3)
        self.iCbContainer_3.setObjectName(u"iCbContainer_3")
        self.iCbContainer_3.setFrameShape(QFrame.StyledPanel)
        self.iCbContainer_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_190 = QVBoxLayout(self.iCbContainer_3)
        self.verticalLayout_190.setSpacing(0)
        self.verticalLayout_190.setObjectName(u"verticalLayout_190")
        self.verticalLayout_190.setContentsMargins(0, 0, 0, 0)
        self.isymCb_3 = QCheckBox(self.iCbContainer_3)
        self.isymCb_3.setObjectName(u"isymCb_3")
        self.isymCb_3.setFont(font17)

        self.verticalLayout_190.addWidget(self.isymCb_3)


        self.verticalLayout_167.addWidget(self.iCbContainer_3)

        self.iDescContainer1_3 = QFrame(self.symptomEntryContainer_3)
        self.iDescContainer1_3.setObjectName(u"iDescContainer1_3")
        self.iDescContainer1_3.setFrameShape(QFrame.StyledPanel)
        self.iDescContainer1_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_191 = QVBoxLayout(self.iDescContainer1_3)
        self.verticalLayout_191.setSpacing(0)
        self.verticalLayout_191.setObjectName(u"verticalLayout_191")
        self.verticalLayout_191.setContentsMargins(20, 0, 20, 0)
        self.iDesc1_3 = QLabel(self.iDescContainer1_3)
        self.iDesc1_3.setObjectName(u"iDesc1_3")
        self.iDesc1_3.setFont(font12)
        self.iDesc1_3.setWordWrap(True)

        self.verticalLayout_191.addWidget(self.iDesc1_3)


        self.verticalLayout_167.addWidget(self.iDescContainer1_3)

        self.iLineContainer1_3 = QFrame(self.symptomEntryContainer_3)
        self.iLineContainer1_3.setObjectName(u"iLineContainer1_3")
        self.iLineContainer1_3.setFrameShape(QFrame.StyledPanel)
        self.iLineContainer1_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_192 = QVBoxLayout(self.iLineContainer1_3)
        self.verticalLayout_192.setSpacing(0)
        self.verticalLayout_192.setObjectName(u"verticalLayout_192")
        self.verticalLayout_192.setContentsMargins(-1, 5, -1, 5)
        self.isymLine1_3 = QFrame(self.iLineContainer1_3)
        self.isymLine1_3.setObjectName(u"isymLine1_3")
        self.isymLine1_3.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.isymLine1_3.setFrameShape(QFrame.HLine)
        self.isymLine1_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_192.addWidget(self.isymLine1_3)


        self.verticalLayout_167.addWidget(self.iLineContainer1_3)


        self.verticalLayout_28.addWidget(self.symptomEntryContainer_3)

        self.symptomEntryContainer_8 = QFrame(self.iInterviewScrollAreaContents)
        self.symptomEntryContainer_8.setObjectName(u"symptomEntryContainer_8")
        sizePolicy1.setHeightForWidth(self.symptomEntryContainer_8.sizePolicy().hasHeightForWidth())
        self.symptomEntryContainer_8.setSizePolicy(sizePolicy1)
        self.symptomEntryContainer_8.setFrameShape(QFrame.StyledPanel)
        self.symptomEntryContainer_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_209 = QVBoxLayout(self.symptomEntryContainer_8)
        self.verticalLayout_209.setSpacing(3)
        self.verticalLayout_209.setObjectName(u"verticalLayout_209")
        self.verticalLayout_209.setContentsMargins(0, 0, 0, 5)
        self.iCbContainer_8 = QFrame(self.symptomEntryContainer_8)
        self.iCbContainer_8.setObjectName(u"iCbContainer_8")
        self.iCbContainer_8.setFrameShape(QFrame.StyledPanel)
        self.iCbContainer_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_210 = QVBoxLayout(self.iCbContainer_8)
        self.verticalLayout_210.setSpacing(0)
        self.verticalLayout_210.setObjectName(u"verticalLayout_210")
        self.verticalLayout_210.setContentsMargins(0, 0, 0, 0)
        self.isymCb_8 = QCheckBox(self.iCbContainer_8)
        self.isymCb_8.setObjectName(u"isymCb_8")
        self.isymCb_8.setFont(font17)

        self.verticalLayout_210.addWidget(self.isymCb_8)


        self.verticalLayout_209.addWidget(self.iCbContainer_8)

        self.iDescContainer1_8 = QFrame(self.symptomEntryContainer_8)
        self.iDescContainer1_8.setObjectName(u"iDescContainer1_8")
        self.iDescContainer1_8.setFrameShape(QFrame.StyledPanel)
        self.iDescContainer1_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_211 = QVBoxLayout(self.iDescContainer1_8)
        self.verticalLayout_211.setSpacing(0)
        self.verticalLayout_211.setObjectName(u"verticalLayout_211")
        self.verticalLayout_211.setContentsMargins(20, 0, 20, 0)
        self.iDesc1_8 = QLabel(self.iDescContainer1_8)
        self.iDesc1_8.setObjectName(u"iDesc1_8")
        self.iDesc1_8.setFont(font12)
        self.iDesc1_8.setWordWrap(True)

        self.verticalLayout_211.addWidget(self.iDesc1_8)


        self.verticalLayout_209.addWidget(self.iDescContainer1_8)

        self.iLineContainer1_8 = QFrame(self.symptomEntryContainer_8)
        self.iLineContainer1_8.setObjectName(u"iLineContainer1_8")
        self.iLineContainer1_8.setFrameShape(QFrame.StyledPanel)
        self.iLineContainer1_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_212 = QVBoxLayout(self.iLineContainer1_8)
        self.verticalLayout_212.setSpacing(0)
        self.verticalLayout_212.setObjectName(u"verticalLayout_212")
        self.verticalLayout_212.setContentsMargins(-1, 5, -1, 5)
        self.isymLine1_8 = QFrame(self.iLineContainer1_8)
        self.isymLine1_8.setObjectName(u"isymLine1_8")
        self.isymLine1_8.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.isymLine1_8.setFrameShape(QFrame.HLine)
        self.isymLine1_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_212.addWidget(self.isymLine1_8)


        self.verticalLayout_209.addWidget(self.iLineContainer1_8)


        self.verticalLayout_28.addWidget(self.symptomEntryContainer_8)

        self.symptomEntryContainer_9 = QFrame(self.iInterviewScrollAreaContents)
        self.symptomEntryContainer_9.setObjectName(u"symptomEntryContainer_9")
        sizePolicy1.setHeightForWidth(self.symptomEntryContainer_9.sizePolicy().hasHeightForWidth())
        self.symptomEntryContainer_9.setSizePolicy(sizePolicy1)
        self.symptomEntryContainer_9.setFrameShape(QFrame.StyledPanel)
        self.symptomEntryContainer_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_213 = QVBoxLayout(self.symptomEntryContainer_9)
        self.verticalLayout_213.setSpacing(3)
        self.verticalLayout_213.setObjectName(u"verticalLayout_213")
        self.verticalLayout_213.setContentsMargins(0, 0, 0, 5)
        self.iCbContainer_9 = QFrame(self.symptomEntryContainer_9)
        self.iCbContainer_9.setObjectName(u"iCbContainer_9")
        self.iCbContainer_9.setFrameShape(QFrame.StyledPanel)
        self.iCbContainer_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_214 = QVBoxLayout(self.iCbContainer_9)
        self.verticalLayout_214.setSpacing(0)
        self.verticalLayout_214.setObjectName(u"verticalLayout_214")
        self.verticalLayout_214.setContentsMargins(0, 0, 0, 0)
        self.isymCb_9 = QCheckBox(self.iCbContainer_9)
        self.isymCb_9.setObjectName(u"isymCb_9")
        self.isymCb_9.setFont(font17)

        self.verticalLayout_214.addWidget(self.isymCb_9)


        self.verticalLayout_213.addWidget(self.iCbContainer_9)

        self.iDescContainer1_9 = QFrame(self.symptomEntryContainer_9)
        self.iDescContainer1_9.setObjectName(u"iDescContainer1_9")
        self.iDescContainer1_9.setFrameShape(QFrame.StyledPanel)
        self.iDescContainer1_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_215 = QVBoxLayout(self.iDescContainer1_9)
        self.verticalLayout_215.setSpacing(0)
        self.verticalLayout_215.setObjectName(u"verticalLayout_215")
        self.verticalLayout_215.setContentsMargins(20, 0, 20, 0)
        self.iDesc1_9 = QLabel(self.iDescContainer1_9)
        self.iDesc1_9.setObjectName(u"iDesc1_9")
        self.iDesc1_9.setFont(font12)
        self.iDesc1_9.setWordWrap(True)

        self.verticalLayout_215.addWidget(self.iDesc1_9)


        self.verticalLayout_213.addWidget(self.iDescContainer1_9)

        self.iLineContainer1_9 = QFrame(self.symptomEntryContainer_9)
        self.iLineContainer1_9.setObjectName(u"iLineContainer1_9")
        self.iLineContainer1_9.setFrameShape(QFrame.StyledPanel)
        self.iLineContainer1_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_216 = QVBoxLayout(self.iLineContainer1_9)
        self.verticalLayout_216.setSpacing(0)
        self.verticalLayout_216.setObjectName(u"verticalLayout_216")
        self.verticalLayout_216.setContentsMargins(-1, 5, -1, 5)
        self.isymLine1_9 = QFrame(self.iLineContainer1_9)
        self.isymLine1_9.setObjectName(u"isymLine1_9")
        self.isymLine1_9.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.isymLine1_9.setFrameShape(QFrame.HLine)
        self.isymLine1_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_216.addWidget(self.isymLine1_9)


        self.verticalLayout_213.addWidget(self.iLineContainer1_9)


        self.verticalLayout_28.addWidget(self.symptomEntryContainer_9)

        self.symptomEntryContainer_7 = QFrame(self.iInterviewScrollAreaContents)
        self.symptomEntryContainer_7.setObjectName(u"symptomEntryContainer_7")
        sizePolicy1.setHeightForWidth(self.symptomEntryContainer_7.sizePolicy().hasHeightForWidth())
        self.symptomEntryContainer_7.setSizePolicy(sizePolicy1)
        self.symptomEntryContainer_7.setFrameShape(QFrame.StyledPanel)
        self.symptomEntryContainer_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_205 = QVBoxLayout(self.symptomEntryContainer_7)
        self.verticalLayout_205.setSpacing(3)
        self.verticalLayout_205.setObjectName(u"verticalLayout_205")
        self.verticalLayout_205.setContentsMargins(0, 0, 0, 5)
        self.iCbContainer_7 = QFrame(self.symptomEntryContainer_7)
        self.iCbContainer_7.setObjectName(u"iCbContainer_7")
        self.iCbContainer_7.setFrameShape(QFrame.StyledPanel)
        self.iCbContainer_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_206 = QVBoxLayout(self.iCbContainer_7)
        self.verticalLayout_206.setSpacing(0)
        self.verticalLayout_206.setObjectName(u"verticalLayout_206")
        self.verticalLayout_206.setContentsMargins(0, 0, 0, 0)
        self.isymCb_7 = QCheckBox(self.iCbContainer_7)
        self.isymCb_7.setObjectName(u"isymCb_7")
        self.isymCb_7.setFont(font17)

        self.verticalLayout_206.addWidget(self.isymCb_7)


        self.verticalLayout_205.addWidget(self.iCbContainer_7)

        self.iDescContainer1_7 = QFrame(self.symptomEntryContainer_7)
        self.iDescContainer1_7.setObjectName(u"iDescContainer1_7")
        self.iDescContainer1_7.setFrameShape(QFrame.StyledPanel)
        self.iDescContainer1_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_207 = QVBoxLayout(self.iDescContainer1_7)
        self.verticalLayout_207.setSpacing(0)
        self.verticalLayout_207.setObjectName(u"verticalLayout_207")
        self.verticalLayout_207.setContentsMargins(20, 0, 20, 0)
        self.iDesc1_7 = QLabel(self.iDescContainer1_7)
        self.iDesc1_7.setObjectName(u"iDesc1_7")
        self.iDesc1_7.setFont(font12)
        self.iDesc1_7.setWordWrap(True)

        self.verticalLayout_207.addWidget(self.iDesc1_7)


        self.verticalLayout_205.addWidget(self.iDescContainer1_7)

        self.iLineContainer1_7 = QFrame(self.symptomEntryContainer_7)
        self.iLineContainer1_7.setObjectName(u"iLineContainer1_7")
        self.iLineContainer1_7.setFrameShape(QFrame.StyledPanel)
        self.iLineContainer1_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_208 = QVBoxLayout(self.iLineContainer1_7)
        self.verticalLayout_208.setSpacing(0)
        self.verticalLayout_208.setObjectName(u"verticalLayout_208")
        self.verticalLayout_208.setContentsMargins(-1, 5, -1, 5)
        self.isymLine1_7 = QFrame(self.iLineContainer1_7)
        self.isymLine1_7.setObjectName(u"isymLine1_7")
        self.isymLine1_7.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.isymLine1_7.setFrameShape(QFrame.HLine)
        self.isymLine1_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_208.addWidget(self.isymLine1_7)


        self.verticalLayout_205.addWidget(self.iLineContainer1_7)


        self.verticalLayout_28.addWidget(self.symptomEntryContainer_7)

        self.symptomEntryContainer_6 = QFrame(self.iInterviewScrollAreaContents)
        self.symptomEntryContainer_6.setObjectName(u"symptomEntryContainer_6")
        sizePolicy1.setHeightForWidth(self.symptomEntryContainer_6.sizePolicy().hasHeightForWidth())
        self.symptomEntryContainer_6.setSizePolicy(sizePolicy1)
        self.symptomEntryContainer_6.setFrameShape(QFrame.StyledPanel)
        self.symptomEntryContainer_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_201 = QVBoxLayout(self.symptomEntryContainer_6)
        self.verticalLayout_201.setSpacing(3)
        self.verticalLayout_201.setObjectName(u"verticalLayout_201")
        self.verticalLayout_201.setContentsMargins(0, 0, 0, 5)
        self.iCbContainer_6 = QFrame(self.symptomEntryContainer_6)
        self.iCbContainer_6.setObjectName(u"iCbContainer_6")
        self.iCbContainer_6.setFrameShape(QFrame.StyledPanel)
        self.iCbContainer_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_202 = QVBoxLayout(self.iCbContainer_6)
        self.verticalLayout_202.setSpacing(0)
        self.verticalLayout_202.setObjectName(u"verticalLayout_202")
        self.verticalLayout_202.setContentsMargins(0, 0, 0, 0)
        self.isymCb_6 = QCheckBox(self.iCbContainer_6)
        self.isymCb_6.setObjectName(u"isymCb_6")
        self.isymCb_6.setFont(font17)

        self.verticalLayout_202.addWidget(self.isymCb_6)


        self.verticalLayout_201.addWidget(self.iCbContainer_6)

        self.iDescContainer1_6 = QFrame(self.symptomEntryContainer_6)
        self.iDescContainer1_6.setObjectName(u"iDescContainer1_6")
        self.iDescContainer1_6.setFrameShape(QFrame.StyledPanel)
        self.iDescContainer1_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_203 = QVBoxLayout(self.iDescContainer1_6)
        self.verticalLayout_203.setSpacing(0)
        self.verticalLayout_203.setObjectName(u"verticalLayout_203")
        self.verticalLayout_203.setContentsMargins(20, 0, 20, 0)
        self.iDesc1_6 = QLabel(self.iDescContainer1_6)
        self.iDesc1_6.setObjectName(u"iDesc1_6")
        self.iDesc1_6.setFont(font12)
        self.iDesc1_6.setWordWrap(True)

        self.verticalLayout_203.addWidget(self.iDesc1_6)


        self.verticalLayout_201.addWidget(self.iDescContainer1_6)

        self.iLineContainer1_6 = QFrame(self.symptomEntryContainer_6)
        self.iLineContainer1_6.setObjectName(u"iLineContainer1_6")
        self.iLineContainer1_6.setFrameShape(QFrame.StyledPanel)
        self.iLineContainer1_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_204 = QVBoxLayout(self.iLineContainer1_6)
        self.verticalLayout_204.setSpacing(0)
        self.verticalLayout_204.setObjectName(u"verticalLayout_204")
        self.verticalLayout_204.setContentsMargins(-1, 5, -1, 5)
        self.isymLine1_6 = QFrame(self.iLineContainer1_6)
        self.isymLine1_6.setObjectName(u"isymLine1_6")
        self.isymLine1_6.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.isymLine1_6.setFrameShape(QFrame.HLine)
        self.isymLine1_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_204.addWidget(self.isymLine1_6)


        self.verticalLayout_201.addWidget(self.iLineContainer1_6)


        self.verticalLayout_28.addWidget(self.symptomEntryContainer_6)

        self.symptomEntryContainer_5 = QFrame(self.iInterviewScrollAreaContents)
        self.symptomEntryContainer_5.setObjectName(u"symptomEntryContainer_5")
        sizePolicy1.setHeightForWidth(self.symptomEntryContainer_5.sizePolicy().hasHeightForWidth())
        self.symptomEntryContainer_5.setSizePolicy(sizePolicy1)
        self.symptomEntryContainer_5.setFrameShape(QFrame.StyledPanel)
        self.symptomEntryContainer_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_197 = QVBoxLayout(self.symptomEntryContainer_5)
        self.verticalLayout_197.setSpacing(3)
        self.verticalLayout_197.setObjectName(u"verticalLayout_197")
        self.verticalLayout_197.setContentsMargins(0, 0, 0, 5)
        self.iCbContainer_5 = QFrame(self.symptomEntryContainer_5)
        self.iCbContainer_5.setObjectName(u"iCbContainer_5")
        self.iCbContainer_5.setFrameShape(QFrame.StyledPanel)
        self.iCbContainer_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_198 = QVBoxLayout(self.iCbContainer_5)
        self.verticalLayout_198.setSpacing(0)
        self.verticalLayout_198.setObjectName(u"verticalLayout_198")
        self.verticalLayout_198.setContentsMargins(0, 0, 0, 0)
        self.isymCb_5 = QCheckBox(self.iCbContainer_5)
        self.isymCb_5.setObjectName(u"isymCb_5")
        self.isymCb_5.setFont(font17)

        self.verticalLayout_198.addWidget(self.isymCb_5)


        self.verticalLayout_197.addWidget(self.iCbContainer_5)

        self.iDescContainer1_5 = QFrame(self.symptomEntryContainer_5)
        self.iDescContainer1_5.setObjectName(u"iDescContainer1_5")
        self.iDescContainer1_5.setFrameShape(QFrame.StyledPanel)
        self.iDescContainer1_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_199 = QVBoxLayout(self.iDescContainer1_5)
        self.verticalLayout_199.setSpacing(0)
        self.verticalLayout_199.setObjectName(u"verticalLayout_199")
        self.verticalLayout_199.setContentsMargins(20, 0, 20, 0)
        self.iDesc1_5 = QLabel(self.iDescContainer1_5)
        self.iDesc1_5.setObjectName(u"iDesc1_5")
        self.iDesc1_5.setFont(font12)
        self.iDesc1_5.setWordWrap(True)

        self.verticalLayout_199.addWidget(self.iDesc1_5)


        self.verticalLayout_197.addWidget(self.iDescContainer1_5)

        self.iLineContainer1_5 = QFrame(self.symptomEntryContainer_5)
        self.iLineContainer1_5.setObjectName(u"iLineContainer1_5")
        self.iLineContainer1_5.setFrameShape(QFrame.StyledPanel)
        self.iLineContainer1_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_200 = QVBoxLayout(self.iLineContainer1_5)
        self.verticalLayout_200.setSpacing(0)
        self.verticalLayout_200.setObjectName(u"verticalLayout_200")
        self.verticalLayout_200.setContentsMargins(-1, 5, -1, 5)
        self.isymLine1_5 = QFrame(self.iLineContainer1_5)
        self.isymLine1_5.setObjectName(u"isymLine1_5")
        self.isymLine1_5.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.isymLine1_5.setFrameShape(QFrame.HLine)
        self.isymLine1_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_200.addWidget(self.isymLine1_5)


        self.verticalLayout_197.addWidget(self.iLineContainer1_5)


        self.verticalLayout_28.addWidget(self.symptomEntryContainer_5)

        self.symptomEntryContainer_4 = QFrame(self.iInterviewScrollAreaContents)
        self.symptomEntryContainer_4.setObjectName(u"symptomEntryContainer_4")
        sizePolicy1.setHeightForWidth(self.symptomEntryContainer_4.sizePolicy().hasHeightForWidth())
        self.symptomEntryContainer_4.setSizePolicy(sizePolicy1)
        self.symptomEntryContainer_4.setFrameShape(QFrame.StyledPanel)
        self.symptomEntryContainer_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_193 = QVBoxLayout(self.symptomEntryContainer_4)
        self.verticalLayout_193.setSpacing(3)
        self.verticalLayout_193.setObjectName(u"verticalLayout_193")
        self.verticalLayout_193.setContentsMargins(0, 0, 0, 5)
        self.iCbContainer_4 = QFrame(self.symptomEntryContainer_4)
        self.iCbContainer_4.setObjectName(u"iCbContainer_4")
        self.iCbContainer_4.setFrameShape(QFrame.StyledPanel)
        self.iCbContainer_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_194 = QVBoxLayout(self.iCbContainer_4)
        self.verticalLayout_194.setSpacing(0)
        self.verticalLayout_194.setObjectName(u"verticalLayout_194")
        self.verticalLayout_194.setContentsMargins(0, 0, 0, 0)
        self.isymCb_4 = QCheckBox(self.iCbContainer_4)
        self.isymCb_4.setObjectName(u"isymCb_4")
        self.isymCb_4.setFont(font17)

        self.verticalLayout_194.addWidget(self.isymCb_4)


        self.verticalLayout_193.addWidget(self.iCbContainer_4)

        self.iDescContainer1_4 = QFrame(self.symptomEntryContainer_4)
        self.iDescContainer1_4.setObjectName(u"iDescContainer1_4")
        self.iDescContainer1_4.setFrameShape(QFrame.StyledPanel)
        self.iDescContainer1_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_195 = QVBoxLayout(self.iDescContainer1_4)
        self.verticalLayout_195.setSpacing(0)
        self.verticalLayout_195.setObjectName(u"verticalLayout_195")
        self.verticalLayout_195.setContentsMargins(20, 0, 20, 0)
        self.iDesc1_4 = QLabel(self.iDescContainer1_4)
        self.iDesc1_4.setObjectName(u"iDesc1_4")
        self.iDesc1_4.setFont(font12)
        self.iDesc1_4.setWordWrap(True)

        self.verticalLayout_195.addWidget(self.iDesc1_4)


        self.verticalLayout_193.addWidget(self.iDescContainer1_4)

        self.iLineContainer1_4 = QFrame(self.symptomEntryContainer_4)
        self.iLineContainer1_4.setObjectName(u"iLineContainer1_4")
        self.iLineContainer1_4.setFrameShape(QFrame.StyledPanel)
        self.iLineContainer1_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_196 = QVBoxLayout(self.iLineContainer1_4)
        self.verticalLayout_196.setSpacing(0)
        self.verticalLayout_196.setObjectName(u"verticalLayout_196")
        self.verticalLayout_196.setContentsMargins(-1, 5, -1, 5)
        self.isymLine1_4 = QFrame(self.iLineContainer1_4)
        self.isymLine1_4.setObjectName(u"isymLine1_4")
        self.isymLine1_4.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.isymLine1_4.setFrameShape(QFrame.HLine)
        self.isymLine1_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_196.addWidget(self.isymLine1_4)


        self.verticalLayout_193.addWidget(self.iLineContainer1_4)


        self.verticalLayout_28.addWidget(self.symptomEntryContainer_4)

        self.symptomEntryContainer_2 = QFrame(self.iInterviewScrollAreaContents)
        self.symptomEntryContainer_2.setObjectName(u"symptomEntryContainer_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.symptomEntryContainer_2.sizePolicy().hasHeightForWidth())
        self.symptomEntryContainer_2.setSizePolicy(sizePolicy7)
        self.symptomEntryContainer_2.setFrameShape(QFrame.StyledPanel)
        self.symptomEntryContainer_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_163 = QVBoxLayout(self.symptomEntryContainer_2)
        self.verticalLayout_163.setSpacing(3)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.verticalLayout_163.setContentsMargins(0, 0, 0, 5)
        self.iCbContainer_2 = QFrame(self.symptomEntryContainer_2)
        self.iCbContainer_2.setObjectName(u"iCbContainer_2")
        self.iCbContainer_2.setFrameShape(QFrame.StyledPanel)
        self.iCbContainer_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_164 = QVBoxLayout(self.iCbContainer_2)
        self.verticalLayout_164.setSpacing(0)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.verticalLayout_164.setContentsMargins(0, 0, 0, 0)
        self.isymCb_2 = QCheckBox(self.iCbContainer_2)
        self.isymCb_2.setObjectName(u"isymCb_2")
        self.isymCb_2.setFont(font17)

        self.verticalLayout_164.addWidget(self.isymCb_2)


        self.verticalLayout_163.addWidget(self.iCbContainer_2)

        self.iDescContainer1_2 = QFrame(self.symptomEntryContainer_2)
        self.iDescContainer1_2.setObjectName(u"iDescContainer1_2")
        self.iDescContainer1_2.setFrameShape(QFrame.StyledPanel)
        self.iDescContainer1_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_165 = QVBoxLayout(self.iDescContainer1_2)
        self.verticalLayout_165.setSpacing(0)
        self.verticalLayout_165.setObjectName(u"verticalLayout_165")
        self.verticalLayout_165.setContentsMargins(20, 0, 20, 0)
        self.iDesc1_2 = QLabel(self.iDescContainer1_2)
        self.iDesc1_2.setObjectName(u"iDesc1_2")
        self.iDesc1_2.setFont(font12)
        self.iDesc1_2.setWordWrap(True)

        self.verticalLayout_165.addWidget(self.iDesc1_2)


        self.verticalLayout_163.addWidget(self.iDescContainer1_2)

        self.iLineContainer1_2 = QFrame(self.symptomEntryContainer_2)
        self.iLineContainer1_2.setObjectName(u"iLineContainer1_2")
        self.iLineContainer1_2.setFrameShape(QFrame.StyledPanel)
        self.iLineContainer1_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_166 = QVBoxLayout(self.iLineContainer1_2)
        self.verticalLayout_166.setSpacing(0)
        self.verticalLayout_166.setObjectName(u"verticalLayout_166")
        self.verticalLayout_166.setContentsMargins(-1, 5, -1, 5)
        self.isymLine1_2 = QFrame(self.iLineContainer1_2)
        self.isymLine1_2.setObjectName(u"isymLine1_2")
        self.isymLine1_2.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.isymLine1_2.setFrameShape(QFrame.HLine)
        self.isymLine1_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_166.addWidget(self.isymLine1_2)


        self.verticalLayout_163.addWidget(self.iLineContainer1_2)


        self.verticalLayout_28.addWidget(self.symptomEntryContainer_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_2)

        self.iInterviewScrollArea.setWidget(self.iInterviewScrollAreaContents)

        self.verticalLayout_27.addWidget(self.iInterviewScrollArea)


        self.verticalLayout_15.addWidget(self.iInterviewContainer)

        self.frame_10 = QFrame(self.iScrollAreaContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_10)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(20, 20, 20, 20)
        self.iBottomLineContainer = QFrame(self.frame_10)
        self.iBottomLineContainer.setObjectName(u"iBottomLineContainer")
        self.iBottomLineContainer.setFrameShape(QFrame.StyledPanel)
        self.iBottomLineContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_265 = QVBoxLayout(self.iBottomLineContainer)
        self.verticalLayout_265.setSpacing(0)
        self.verticalLayout_265.setObjectName(u"verticalLayout_265")
        self.verticalLayout_265.setContentsMargins(0, 0, 0, 10)
        self.iBottomLine = QFrame(self.iBottomLineContainer)
        self.iBottomLine.setObjectName(u"iBottomLine")
        self.iBottomLine.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.iBottomLine.setFrameShape(QFrame.HLine)
        self.iBottomLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_265.addWidget(self.iBottomLine)


        self.verticalLayout_25.addWidget(self.iBottomLineContainer, 0, Qt.AlignTop)

        self.iBottomBtnContainer = QFrame(self.frame_10)
        self.iBottomBtnContainer.setObjectName(u"iBottomBtnContainer")
        self.iBottomBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.iBottomBtnContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.iBottomBtnContainer)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.iBottomNextBtn = QPushButton(self.iBottomBtnContainer)
        self.iBottomNextBtn.setObjectName(u"iBottomNextBtn")
        self.iBottomNextBtn.setFont(font13)
        self.iBottomNextBtn.setStyleSheet(u"background-color:rgb(56, 166, 255);\n"
"padding: 3px 23px 3px 23px;\n"
"border-radius: 15px;\n"
"color: #fff;")

        self.horizontalLayout_72.addWidget(self.iBottomNextBtn)


        self.verticalLayout_25.addWidget(self.iBottomBtnContainer, 0, Qt.AlignRight)


        self.verticalLayout_15.addWidget(self.frame_10)

        self.iScrollArea.setWidget(self.iScrollAreaContents)

        self.verticalLayout_13.addWidget(self.iScrollArea)


        self.verticalLayout_189.addWidget(self.iWhiteCard)


        self.verticalLayout_188.addWidget(self.iBlueCard)


        self.verticalLayout_12.addWidget(self.iMarginContainer)

        self.diagnosisStackedWidget.addWidget(self.diagnosisInterviewPage)
        self.diagnosisValidationPage = QWidget()
        self.diagnosisValidationPage.setObjectName(u"diagnosisValidationPage")
        self.verticalLayout_19 = QVBoxLayout(self.diagnosisValidationPage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.validationProgressContainer = QWidget(self.diagnosisValidationPage)
        self.validationProgressContainer.setObjectName(u"validationProgressContainer")
        sizePolicy1.setHeightForWidth(self.validationProgressContainer.sizePolicy().hasHeightForWidth())
        self.validationProgressContainer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_34 = QHBoxLayout(self.validationProgressContainer)
        self.horizontalLayout_34.setSpacing(6)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.vPExitBtnContainer = QFrame(self.validationProgressContainer)
        self.vPExitBtnContainer.setObjectName(u"vPExitBtnContainer")
        self.vPExitBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.vPExitBtnContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.vPExitBtnContainer)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.vPExitBtn = QPushButton(self.vPExitBtnContainer)
        self.vPExitBtn.setObjectName(u"vPExitBtn")
        self.vPExitBtn.setIcon(icon5)
        self.vPExitBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_35.addWidget(self.vPExitBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_34.addWidget(self.vPExitBtnContainer, 0, Qt.AlignLeft)

        self.vPProgessContainer = QFrame(self.validationProgressContainer)
        self.vPProgessContainer.setObjectName(u"vPProgessContainer")
        self.vPProgessContainer.setFrameShape(QFrame.StyledPanel)
        self.vPProgessContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.vPProgessContainer)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.vPProgess = QLabel(self.vPProgessContainer)
        self.vPProgess.setObjectName(u"vPProgess")
        sizePolicy2.setHeightForWidth(self.vPProgess.sizePolicy().hasHeightForWidth())
        self.vPProgess.setSizePolicy(sizePolicy2)
        self.vPProgess.setMinimumSize(QSize(680, 45))
        self.vPProgess.setMaximumSize(QSize(680, 45))
        self.vPProgess.setSizeIncrement(QSize(0, 0))
        self.vPProgess.setFont(font7)
        self.vPProgess.setFrameShadow(QFrame.Plain)
        self.vPProgess.setPixmap(QPixmap(u":/progressBarImages/images/progress4.png"))
        self.vPProgess.setScaledContents(True)
        self.vPProgess.setWordWrap(False)

        self.horizontalLayout_36.addWidget(self.vPProgess, 0, Qt.AlignVCenter)


        self.horizontalLayout_34.addWidget(self.vPProgessContainer, 0, Qt.AlignHCenter)

        self.vPExitBtn2 = QPushButton(self.validationProgressContainer)
        self.vPExitBtn2.setObjectName(u"vPExitBtn2")
        self.vPExitBtn2.setEnabled(False)

        self.horizontalLayout_34.addWidget(self.vPExitBtn2)


        self.verticalLayout_19.addWidget(self.validationProgressContainer, 0, Qt.AlignTop)

        self.vMarginContainer = QFrame(self.diagnosisValidationPage)
        self.vMarginContainer.setObjectName(u"vMarginContainer")
        sizePolicy3.setHeightForWidth(self.vMarginContainer.sizePolicy().hasHeightForWidth())
        self.vMarginContainer.setSizePolicy(sizePolicy3)
        self.vMarginContainer.setFrameShape(QFrame.StyledPanel)
        self.vMarginContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.vMarginContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(70, 0, 70, 10)
        self.vBlueCard = QFrame(self.vMarginContainer)
        self.vBlueCard.setObjectName(u"vBlueCard")
        self.vBlueCard.setStyleSheet(u"background-color:#58AAEC;\n"
"border-radius: 15px;")
        self.vBlueCard.setFrameShape(QFrame.StyledPanel)
        self.vBlueCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.vBlueCard)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(10, 0, 0, 0)
        self.vWhiteCard = QFrame(self.vBlueCard)
        self.vWhiteCard.setObjectName(u"vWhiteCard")
        self.vWhiteCard.setStyleSheet(u"background-color:#FFF;\n"
"border-radius: 15px;")
        self.vWhiteCard.setFrameShape(QFrame.StyledPanel)
        self.vWhiteCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.vWhiteCard)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(5, 5, 5, 5)
        self.vScrollArea = QScrollArea(self.vWhiteCard)
        self.vScrollArea.setObjectName(u"vScrollArea")
        self.vScrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.vScrollArea.setWidgetResizable(True)
        self.vScrollAreaContents = QWidget()
        self.vScrollAreaContents.setObjectName(u"vScrollAreaContents")
        self.vScrollAreaContents.setGeometry(QRect(0, 0, 520, 1076))
        self.vScrollAreaContents.setStyleSheet(u"#vPatientDetailsOutlinedContainer, #vEmergencyOutlinedContainer, #vSymptomsOutlinedContainer{border: 1px solid gray;}")
        self.verticalLayout_30 = QVBoxLayout(self.vScrollAreaContents)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.vTopContainer = QFrame(self.vScrollAreaContents)
        self.vTopContainer.setObjectName(u"vTopContainer")
        self.vTopContainer.setMinimumSize(QSize(0, 0))
        self.vTopContainer.setFrameShape(QFrame.StyledPanel)
        self.vTopContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.vTopContainer)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(20, 15, 40, 10)
        self.vTopLabelContainer = QFrame(self.vTopContainer)
        self.vTopLabelContainer.setObjectName(u"vTopLabelContainer")
        self.vTopLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.vTopLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.vTopLabelContainer)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.vTopLabel = QLabel(self.vTopLabelContainer)
        self.vTopLabel.setObjectName(u"vTopLabel")
        self.vTopLabel.setFont(font14)

        self.verticalLayout_31.addWidget(self.vTopLabel, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_37.addWidget(self.vTopLabelContainer, 0, Qt.AlignLeft|Qt.AlignTop)

        self.vTopBtnContainer = QFrame(self.vTopContainer)
        self.vTopBtnContainer.setObjectName(u"vTopBtnContainer")
        self.vTopBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.vTopBtnContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.vTopBtnContainer)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.vTopEditBtn = QPushButton(self.vTopBtnContainer)
        self.vTopEditBtn.setObjectName(u"vTopEditBtn")
        self.vTopEditBtn.setFont(font17)
        self.vTopEditBtn.setStyleSheet(u"background-color: #FFF;\n"
"border: 1px solid #38A6FF;\n"
"color:#38A6FF;\n"
"padding: 5px 15px 5px 15px;\n"
"border-radius: 15px;\n"
"\n"
"")

        self.verticalLayout_32.addWidget(self.vTopEditBtn)


        self.horizontalLayout_37.addWidget(self.vTopBtnContainer, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_30.addWidget(self.vTopContainer)

        self.vPatientDetailsContainer = QFrame(self.vScrollAreaContents)
        self.vPatientDetailsContainer.setObjectName(u"vPatientDetailsContainer")
        self.vPatientDetailsContainer.setMinimumSize(QSize(0, 0))
        self.vPatientDetailsContainer.setStyleSheet(u"")
        self.vPatientDetailsContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.vPatientDetailsContainer)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(30, 0, 30, 0)
        self.vPatientDetailsOutlinedContainer = QFrame(self.vPatientDetailsContainer)
        self.vPatientDetailsOutlinedContainer.setObjectName(u"vPatientDetailsOutlinedContainer")
        self.vPatientDetailsOutlinedContainer.setStyleSheet(u"")
        self.vPatientDetailsOutlinedContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsOutlinedContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.vPatientDetailsOutlinedContainer)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(20, 10, 20, 0)
        self.vPatientDetailsTopContainer = QFrame(self.vPatientDetailsOutlinedContainer)
        self.vPatientDetailsTopContainer.setObjectName(u"vPatientDetailsTopContainer")
        self.vPatientDetailsTopContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsTopContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.vPatientDetailsTopContainer)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 15)
        self.vPatientDetailsNameHeadingContainer = QFrame(self.vPatientDetailsTopContainer)
        self.vPatientDetailsNameHeadingContainer.setObjectName(u"vPatientDetailsNameHeadingContainer")
        self.vPatientDetailsNameHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsNameHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.vPatientDetailsNameHeadingContainer)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsNameHeading = QLabel(self.vPatientDetailsNameHeadingContainer)
        self.vPatientDetailsNameHeading.setObjectName(u"vPatientDetailsNameHeading")
        self.vPatientDetailsNameHeading.setFont(font17)

        self.verticalLayout_77.addWidget(self.vPatientDetailsNameHeading, 0, Qt.AlignBottom)


        self.verticalLayout_76.addWidget(self.vPatientDetailsNameHeadingContainer)

        self.vPatientDetailsNameLabelContainer = QFrame(self.vPatientDetailsTopContainer)
        self.vPatientDetailsNameLabelContainer.setObjectName(u"vPatientDetailsNameLabelContainer")
        self.vPatientDetailsNameLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsNameLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.vPatientDetailsNameLabelContainer)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsNameLabel = QLabel(self.vPatientDetailsNameLabelContainer)
        self.vPatientDetailsNameLabel.setObjectName(u"vPatientDetailsNameLabel")
        self.vPatientDetailsNameLabel.setFont(font12)

        self.verticalLayout_78.addWidget(self.vPatientDetailsNameLabel, 0, Qt.AlignTop)


        self.verticalLayout_76.addWidget(self.vPatientDetailsNameLabelContainer)


        self.verticalLayout_97.addWidget(self.vPatientDetailsTopContainer)

        self.vPatientDetailsMidContainer = QFrame(self.vPatientDetailsOutlinedContainer)
        self.vPatientDetailsMidContainer.setObjectName(u"vPatientDetailsMidContainer")
        self.vPatientDetailsMidContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsMidContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.vPatientDetailsMidContainer)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 15)
        self.vPatientDetailsBirthdateContainer = QFrame(self.vPatientDetailsMidContainer)
        self.vPatientDetailsBirthdateContainer.setObjectName(u"vPatientDetailsBirthdateContainer")
        self.vPatientDetailsBirthdateContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsBirthdateContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.vPatientDetailsBirthdateContainer)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsBirthdateHeadingContainer = QFrame(self.vPatientDetailsBirthdateContainer)
        self.vPatientDetailsBirthdateHeadingContainer.setObjectName(u"vPatientDetailsBirthdateHeadingContainer")
        self.vPatientDetailsBirthdateHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsBirthdateHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.vPatientDetailsBirthdateHeadingContainer)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsBirthdateHeading = QLabel(self.vPatientDetailsBirthdateHeadingContainer)
        self.vPatientDetailsBirthdateHeading.setObjectName(u"vPatientDetailsBirthdateHeading")
        self.vPatientDetailsBirthdateHeading.setFont(font17)

        self.verticalLayout_80.addWidget(self.vPatientDetailsBirthdateHeading)


        self.verticalLayout_79.addWidget(self.vPatientDetailsBirthdateHeadingContainer)

        self.vPatientDetailsBirthdateLabelContainer = QFrame(self.vPatientDetailsBirthdateContainer)
        self.vPatientDetailsBirthdateLabelContainer.setObjectName(u"vPatientDetailsBirthdateLabelContainer")
        self.vPatientDetailsBirthdateLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsBirthdateLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.vPatientDetailsBirthdateLabelContainer)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsBirthdateLabel = QLabel(self.vPatientDetailsBirthdateLabelContainer)
        self.vPatientDetailsBirthdateLabel.setObjectName(u"vPatientDetailsBirthdateLabel")
        self.vPatientDetailsBirthdateLabel.setFont(font12)

        self.verticalLayout_81.addWidget(self.vPatientDetailsBirthdateLabel)


        self.verticalLayout_79.addWidget(self.vPatientDetailsBirthdateLabelContainer)


        self.horizontalLayout_40.addWidget(self.vPatientDetailsBirthdateContainer, 0, Qt.AlignLeft)

        self.vPatientDetailsAgeContainer = QFrame(self.vPatientDetailsMidContainer)
        self.vPatientDetailsAgeContainer.setObjectName(u"vPatientDetailsAgeContainer")
        self.vPatientDetailsAgeContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsAgeContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.vPatientDetailsAgeContainer)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsAgeHeadingContainer = QFrame(self.vPatientDetailsAgeContainer)
        self.vPatientDetailsAgeHeadingContainer.setObjectName(u"vPatientDetailsAgeHeadingContainer")
        self.vPatientDetailsAgeHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsAgeHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.vPatientDetailsAgeHeadingContainer)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsAgeHeading = QLabel(self.vPatientDetailsAgeHeadingContainer)
        self.vPatientDetailsAgeHeading.setObjectName(u"vPatientDetailsAgeHeading")
        self.vPatientDetailsAgeHeading.setFont(font17)

        self.verticalLayout_83.addWidget(self.vPatientDetailsAgeHeading)


        self.verticalLayout_82.addWidget(self.vPatientDetailsAgeHeadingContainer)

        self.vPatientDetailsAgeLabelContainer = QFrame(self.vPatientDetailsAgeContainer)
        self.vPatientDetailsAgeLabelContainer.setObjectName(u"vPatientDetailsAgeLabelContainer")
        self.vPatientDetailsAgeLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsAgeLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.vPatientDetailsAgeLabelContainer)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsAgeLabel = QLabel(self.vPatientDetailsAgeLabelContainer)
        self.vPatientDetailsAgeLabel.setObjectName(u"vPatientDetailsAgeLabel")
        self.vPatientDetailsAgeLabel.setFont(font12)

        self.verticalLayout_84.addWidget(self.vPatientDetailsAgeLabel)


        self.verticalLayout_82.addWidget(self.vPatientDetailsAgeLabelContainer)


        self.horizontalLayout_40.addWidget(self.vPatientDetailsAgeContainer, 0, Qt.AlignHCenter)

        self.vPatientDetailsSexContainer = QFrame(self.vPatientDetailsMidContainer)
        self.vPatientDetailsSexContainer.setObjectName(u"vPatientDetailsSexContainer")
        self.vPatientDetailsSexContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsSexContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.vPatientDetailsSexContainer)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsSexHeadingContainer = QFrame(self.vPatientDetailsSexContainer)
        self.vPatientDetailsSexHeadingContainer.setObjectName(u"vPatientDetailsSexHeadingContainer")
        self.vPatientDetailsSexHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsSexHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.vPatientDetailsSexHeadingContainer)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsSexHeading = QLabel(self.vPatientDetailsSexHeadingContainer)
        self.vPatientDetailsSexHeading.setObjectName(u"vPatientDetailsSexHeading")
        self.vPatientDetailsSexHeading.setFont(font17)

        self.verticalLayout_86.addWidget(self.vPatientDetailsSexHeading)


        self.verticalLayout_85.addWidget(self.vPatientDetailsSexHeadingContainer)

        self.vPatientDetailsSexLabelContainer = QFrame(self.vPatientDetailsSexContainer)
        self.vPatientDetailsSexLabelContainer.setObjectName(u"vPatientDetailsSexLabelContainer")
        self.vPatientDetailsSexLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsSexLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.vPatientDetailsSexLabelContainer)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsSexLabel = QLabel(self.vPatientDetailsSexLabelContainer)
        self.vPatientDetailsSexLabel.setObjectName(u"vPatientDetailsSexLabel")
        self.vPatientDetailsSexLabel.setFont(font12)

        self.verticalLayout_87.addWidget(self.vPatientDetailsSexLabel)


        self.verticalLayout_85.addWidget(self.vPatientDetailsSexLabelContainer)


        self.horizontalLayout_40.addWidget(self.vPatientDetailsSexContainer, 0, Qt.AlignHCenter)

        self.vPatientDetailsCivilContainer = QFrame(self.vPatientDetailsMidContainer)
        self.vPatientDetailsCivilContainer.setObjectName(u"vPatientDetailsCivilContainer")
        self.vPatientDetailsCivilContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsCivilContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.vPatientDetailsCivilContainer)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsCivilHeadingContainer = QFrame(self.vPatientDetailsCivilContainer)
        self.vPatientDetailsCivilHeadingContainer.setObjectName(u"vPatientDetailsCivilHeadingContainer")
        self.vPatientDetailsCivilHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsCivilHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.vPatientDetailsCivilHeadingContainer)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsCivilHeading = QLabel(self.vPatientDetailsCivilHeadingContainer)
        self.vPatientDetailsCivilHeading.setObjectName(u"vPatientDetailsCivilHeading")
        self.vPatientDetailsCivilHeading.setFont(font17)

        self.verticalLayout_89.addWidget(self.vPatientDetailsCivilHeading)


        self.verticalLayout_88.addWidget(self.vPatientDetailsCivilHeadingContainer)

        self.vPatientDetailsCivilLabelContainer = QFrame(self.vPatientDetailsCivilContainer)
        self.vPatientDetailsCivilLabelContainer.setObjectName(u"vPatientDetailsCivilLabelContainer")
        self.vPatientDetailsCivilLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsCivilLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.vPatientDetailsCivilLabelContainer)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsCivilLabel = QLabel(self.vPatientDetailsCivilLabelContainer)
        self.vPatientDetailsCivilLabel.setObjectName(u"vPatientDetailsCivilLabel")
        self.vPatientDetailsCivilLabel.setFont(font12)

        self.verticalLayout_90.addWidget(self.vPatientDetailsCivilLabel)


        self.verticalLayout_88.addWidget(self.vPatientDetailsCivilLabelContainer)


        self.horizontalLayout_40.addWidget(self.vPatientDetailsCivilContainer, 0, Qt.AlignHCenter)

        self.vPatientDetailsContactContainer = QFrame(self.vPatientDetailsMidContainer)
        self.vPatientDetailsContactContainer.setObjectName(u"vPatientDetailsContactContainer")
        self.vPatientDetailsContactContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsContactContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.vPatientDetailsContactContainer)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsContactHeadingContainer = QFrame(self.vPatientDetailsContactContainer)
        self.vPatientDetailsContactHeadingContainer.setObjectName(u"vPatientDetailsContactHeadingContainer")
        self.vPatientDetailsContactHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsContactHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.vPatientDetailsContactHeadingContainer)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsContactHeading = QLabel(self.vPatientDetailsContactHeadingContainer)
        self.vPatientDetailsContactHeading.setObjectName(u"vPatientDetailsContactHeading")
        self.vPatientDetailsContactHeading.setFont(font17)

        self.verticalLayout_92.addWidget(self.vPatientDetailsContactHeading)


        self.verticalLayout_91.addWidget(self.vPatientDetailsContactHeadingContainer)

        self.vPatientDetailsContactLabelContainer = QFrame(self.vPatientDetailsContactContainer)
        self.vPatientDetailsContactLabelContainer.setObjectName(u"vPatientDetailsContactLabelContainer")
        self.vPatientDetailsContactLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsContactLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.vPatientDetailsContactLabelContainer)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsContactLabel = QLabel(self.vPatientDetailsContactLabelContainer)
        self.vPatientDetailsContactLabel.setObjectName(u"vPatientDetailsContactLabel")
        self.vPatientDetailsContactLabel.setFont(font12)

        self.verticalLayout_93.addWidget(self.vPatientDetailsContactLabel)


        self.verticalLayout_91.addWidget(self.vPatientDetailsContactLabelContainer)


        self.horizontalLayout_40.addWidget(self.vPatientDetailsContactContainer, 0, Qt.AlignRight)


        self.verticalLayout_97.addWidget(self.vPatientDetailsMidContainer)

        self.vPatientDetailsBottomContainer = QFrame(self.vPatientDetailsOutlinedContainer)
        self.vPatientDetailsBottomContainer.setObjectName(u"vPatientDetailsBottomContainer")
        self.vPatientDetailsBottomContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsBottomContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.vPatientDetailsBottomContainer)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 15)
        self.vPatientDetailsAddressHeadingContainer = QFrame(self.vPatientDetailsBottomContainer)
        self.vPatientDetailsAddressHeadingContainer.setObjectName(u"vPatientDetailsAddressHeadingContainer")
        self.vPatientDetailsAddressHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsAddressHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.vPatientDetailsAddressHeadingContainer)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsAddressHeading = QLabel(self.vPatientDetailsAddressHeadingContainer)
        self.vPatientDetailsAddressHeading.setObjectName(u"vPatientDetailsAddressHeading")
        self.vPatientDetailsAddressHeading.setFont(font17)

        self.verticalLayout_95.addWidget(self.vPatientDetailsAddressHeading)


        self.verticalLayout_94.addWidget(self.vPatientDetailsAddressHeadingContainer, 0, Qt.AlignBottom)

        self.vPatientDetailsAddressLabelContainer = QFrame(self.vPatientDetailsBottomContainer)
        self.vPatientDetailsAddressLabelContainer.setObjectName(u"vPatientDetailsAddressLabelContainer")
        self.vPatientDetailsAddressLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.vPatientDetailsAddressLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.vPatientDetailsAddressLabelContainer)
        self.verticalLayout_96.setSpacing(9)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.vPatientDetailsAddressLabel = QLabel(self.vPatientDetailsAddressLabelContainer)
        self.vPatientDetailsAddressLabel.setObjectName(u"vPatientDetailsAddressLabel")

        self.verticalLayout_96.addWidget(self.vPatientDetailsAddressLabel, 0, Qt.AlignTop)


        self.verticalLayout_94.addWidget(self.vPatientDetailsAddressLabelContainer)


        self.verticalLayout_97.addWidget(self.vPatientDetailsBottomContainer)


        self.verticalLayout_33.addWidget(self.vPatientDetailsOutlinedContainer)


        self.verticalLayout_30.addWidget(self.vPatientDetailsContainer)

        self.vMidContainer = QFrame(self.vScrollAreaContents)
        self.vMidContainer.setObjectName(u"vMidContainer")
        self.vMidContainer.setMinimumSize(QSize(0, 0))
        self.vMidContainer.setFrameShape(QFrame.StyledPanel)
        self.vMidContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.vMidContainer)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(20, 15, 40, 10)
        self.vMidLabel = QLabel(self.vMidContainer)
        self.vMidLabel.setObjectName(u"vMidLabel")
        self.vMidLabel.setFont(font14)

        self.verticalLayout_98.addWidget(self.vMidLabel, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_30.addWidget(self.vMidContainer)

        self.vEmergencyContainer = QFrame(self.vScrollAreaContents)
        self.vEmergencyContainer.setObjectName(u"vEmergencyContainer")
        self.vEmergencyContainer.setMinimumSize(QSize(0, 0))
        self.vEmergencyContainer.setFrameShape(QFrame.StyledPanel)
        self.vEmergencyContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.vEmergencyContainer)
        self.verticalLayout_99.setSpacing(0)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(30, 0, 30, 0)
        self.vEmergencyOutlinedContainer = QFrame(self.vEmergencyContainer)
        self.vEmergencyOutlinedContainer.setObjectName(u"vEmergencyOutlinedContainer")
        self.vEmergencyOutlinedContainer.setFrameShape(QFrame.StyledPanel)
        self.vEmergencyOutlinedContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.vEmergencyOutlinedContainer)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(20, 10, 20, 10)
        self.vEmergencyNameContainer = QFrame(self.vEmergencyOutlinedContainer)
        self.vEmergencyNameContainer.setObjectName(u"vEmergencyNameContainer")
        self.vEmergencyNameContainer.setFrameShape(QFrame.StyledPanel)
        self.vEmergencyNameContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.vEmergencyNameContainer)
        self.verticalLayout_100.setSpacing(0)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.vEmergencyNameHeadingContainer = QFrame(self.vEmergencyNameContainer)
        self.vEmergencyNameHeadingContainer.setObjectName(u"vEmergencyNameHeadingContainer")
        self.vEmergencyNameHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.vEmergencyNameHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.vEmergencyNameHeadingContainer)
        self.verticalLayout_103.setSpacing(0)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.vEmergencyNameHeading = QLabel(self.vEmergencyNameHeadingContainer)
        self.vEmergencyNameHeading.setObjectName(u"vEmergencyNameHeading")
        self.vEmergencyNameHeading.setFont(font17)

        self.verticalLayout_103.addWidget(self.vEmergencyNameHeading, 0, Qt.AlignBottom)


        self.verticalLayout_100.addWidget(self.vEmergencyNameHeadingContainer, 0, Qt.AlignBottom)

        self.vEmergencyNameLabelContainer = QFrame(self.vEmergencyNameContainer)
        self.vEmergencyNameLabelContainer.setObjectName(u"vEmergencyNameLabelContainer")
        self.vEmergencyNameLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.vEmergencyNameLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.vEmergencyNameLabelContainer)
        self.verticalLayout_106.setSpacing(0)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.vEmergencyNameLabel = QLabel(self.vEmergencyNameLabelContainer)
        self.vEmergencyNameLabel.setObjectName(u"vEmergencyNameLabel")
        self.vEmergencyNameLabel.setFont(font12)

        self.verticalLayout_106.addWidget(self.vEmergencyNameLabel, 0, Qt.AlignTop)


        self.verticalLayout_100.addWidget(self.vEmergencyNameLabelContainer, 0, Qt.AlignTop)


        self.horizontalLayout_41.addWidget(self.vEmergencyNameContainer)

        self.vEmergencyRelationContainer = QFrame(self.vEmergencyOutlinedContainer)
        self.vEmergencyRelationContainer.setObjectName(u"vEmergencyRelationContainer")
        self.vEmergencyRelationContainer.setFrameShape(QFrame.StyledPanel)
        self.vEmergencyRelationContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.vEmergencyRelationContainer)
        self.verticalLayout_101.setSpacing(0)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.vEmergencyRelationHeadingContainer = QFrame(self.vEmergencyRelationContainer)
        self.vEmergencyRelationHeadingContainer.setObjectName(u"vEmergencyRelationHeadingContainer")
        self.vEmergencyRelationHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.vEmergencyRelationHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.vEmergencyRelationHeadingContainer)
        self.verticalLayout_104.setSpacing(0)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.vEmergencyRelationHeading = QLabel(self.vEmergencyRelationHeadingContainer)
        self.vEmergencyRelationHeading.setObjectName(u"vEmergencyRelationHeading")
        self.vEmergencyRelationHeading.setFont(font17)

        self.verticalLayout_104.addWidget(self.vEmergencyRelationHeading, 0, Qt.AlignBottom)


        self.verticalLayout_101.addWidget(self.vEmergencyRelationHeadingContainer, 0, Qt.AlignBottom)

        self.vEmergencyRelationLabelContainer = QFrame(self.vEmergencyRelationContainer)
        self.vEmergencyRelationLabelContainer.setObjectName(u"vEmergencyRelationLabelContainer")
        self.vEmergencyRelationLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.vEmergencyRelationLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.vEmergencyRelationLabelContainer)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.vEmergencyRelationLabel = QLabel(self.vEmergencyRelationLabelContainer)
        self.vEmergencyRelationLabel.setObjectName(u"vEmergencyRelationLabel")
        self.vEmergencyRelationLabel.setFont(font12)

        self.verticalLayout_107.addWidget(self.vEmergencyRelationLabel)


        self.verticalLayout_101.addWidget(self.vEmergencyRelationLabelContainer, 0, Qt.AlignTop)


        self.horizontalLayout_41.addWidget(self.vEmergencyRelationContainer)

        self.vEmergencyContactContainer = QFrame(self.vEmergencyOutlinedContainer)
        self.vEmergencyContactContainer.setObjectName(u"vEmergencyContactContainer")
        self.vEmergencyContactContainer.setFrameShape(QFrame.StyledPanel)
        self.vEmergencyContactContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.vEmergencyContactContainer)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.vEmergencyContactHeadingContainer = QFrame(self.vEmergencyContactContainer)
        self.vEmergencyContactHeadingContainer.setObjectName(u"vEmergencyContactHeadingContainer")
        self.vEmergencyContactHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.vEmergencyContactHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.vEmergencyContactHeadingContainer)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.vEmergencyContactHeading = QLabel(self.vEmergencyContactHeadingContainer)
        self.vEmergencyContactHeading.setObjectName(u"vEmergencyContactHeading")
        self.vEmergencyContactHeading.setFont(font17)

        self.verticalLayout_105.addWidget(self.vEmergencyContactHeading)


        self.verticalLayout_102.addWidget(self.vEmergencyContactHeadingContainer, 0, Qt.AlignBottom)

        self.vEmergencyContactLabelContainer = QFrame(self.vEmergencyContactContainer)
        self.vEmergencyContactLabelContainer.setObjectName(u"vEmergencyContactLabelContainer")
        self.vEmergencyContactLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.vEmergencyContactLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.vEmergencyContactLabelContainer)
        self.verticalLayout_108.setSpacing(0)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.vEmergencyContactLabel = QLabel(self.vEmergencyContactLabelContainer)
        self.vEmergencyContactLabel.setObjectName(u"vEmergencyContactLabel")
        self.vEmergencyContactLabel.setFont(font12)

        self.verticalLayout_108.addWidget(self.vEmergencyContactLabel)


        self.verticalLayout_102.addWidget(self.vEmergencyContactLabelContainer, 0, Qt.AlignTop)


        self.horizontalLayout_41.addWidget(self.vEmergencyContactContainer)


        self.verticalLayout_99.addWidget(self.vEmergencyOutlinedContainer)


        self.verticalLayout_30.addWidget(self.vEmergencyContainer)

        self.vMidContainer2 = QFrame(self.vScrollAreaContents)
        self.vMidContainer2.setObjectName(u"vMidContainer2")
        self.vMidContainer2.setMinimumSize(QSize(0, 0))
        self.vMidContainer2.setFrameShape(QFrame.StyledPanel)
        self.vMidContainer2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.vMidContainer2)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(20, 15, 40, 10)
        self.vMidLabelContainer = QFrame(self.vMidContainer2)
        self.vMidLabelContainer.setObjectName(u"vMidLabelContainer")
        self.vMidLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.vMidLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.vMidLabelContainer)
        self.verticalLayout_109.setSpacing(0)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.vMidLabel2 = QLabel(self.vMidLabelContainer)
        self.vMidLabel2.setObjectName(u"vMidLabel2")
        self.vMidLabel2.setFont(font14)

        self.verticalLayout_109.addWidget(self.vMidLabel2, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_42.addWidget(self.vMidLabelContainer, 0, Qt.AlignLeft|Qt.AlignTop)

        self.vMidBtnContainer = QFrame(self.vMidContainer2)
        self.vMidBtnContainer.setObjectName(u"vMidBtnContainer")
        self.vMidBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.vMidBtnContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.vMidBtnContainer)
        self.verticalLayout_110.setSpacing(0)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.vMidEditBtn = QPushButton(self.vMidBtnContainer)
        self.vMidEditBtn.setObjectName(u"vMidEditBtn")
        self.vMidEditBtn.setFont(font17)
        self.vMidEditBtn.setStyleSheet(u"background-color: #FFF;\n"
"border: 1px solid #38A6FF;\n"
"color:#38A6FF;\n"
"padding: 5px 15px 5px 15px;\n"
"border-radius: 15px;\n"
"\n"
"")

        self.verticalLayout_110.addWidget(self.vMidEditBtn)


        self.horizontalLayout_42.addWidget(self.vMidBtnContainer, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_30.addWidget(self.vMidContainer2)

        self.vSymptomsContainer = QFrame(self.vScrollAreaContents)
        self.vSymptomsContainer.setObjectName(u"vSymptomsContainer")
        self.vSymptomsContainer.setMinimumSize(QSize(0, 150))
        self.vSymptomsContainer.setFrameShape(QFrame.StyledPanel)
        self.vSymptomsContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.vSymptomsContainer)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(30, 0, 30, 0)
        self.vSymptomsSymptomsOutlinedContainer = QFrame(self.vSymptomsContainer)
        self.vSymptomsSymptomsOutlinedContainer.setObjectName(u"vSymptomsSymptomsOutlinedContainer")
        self.vSymptomsSymptomsOutlinedContainer.setFrameShape(QFrame.StyledPanel)
        self.vSymptomsSymptomsOutlinedContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.vSymptomsSymptomsOutlinedContainer)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(20, 10, 20, 0)
        self.vSymptomsSymptomsListWidget = QListWidget(self.vSymptomsSymptomsOutlinedContainer)
        QListWidgetItem(self.vSymptomsSymptomsListWidget)
        QListWidgetItem(self.vSymptomsSymptomsListWidget)
        QListWidgetItem(self.vSymptomsSymptomsListWidget)
        QListWidgetItem(self.vSymptomsSymptomsListWidget)
        QListWidgetItem(self.vSymptomsSymptomsListWidget)
        QListWidgetItem(self.vSymptomsSymptomsListWidget)
        self.vSymptomsSymptomsListWidget.setObjectName(u"vSymptomsSymptomsListWidget")
        self.vSymptomsSymptomsListWidget.setStyleSheet(u"")
        self.vSymptomsSymptomsListWidget.setAlternatingRowColors(False)
        self.vSymptomsSymptomsListWidget.setWordWrap(True)

        self.horizontalLayout_43.addWidget(self.vSymptomsSymptomsListWidget)


        self.verticalLayout_111.addWidget(self.vSymptomsSymptomsOutlinedContainer)


        self.verticalLayout_30.addWidget(self.vSymptomsContainer)

        self.vBottomContainer = QFrame(self.vScrollAreaContents)
        self.vBottomContainer.setObjectName(u"vBottomContainer")
        self.vBottomContainer.setMinimumSize(QSize(0, 0))
        self.vBottomContainer.setFrameShape(QFrame.StyledPanel)
        self.vBottomContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.vBottomContainer)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(20, 20, 20, 20)
        self.vBottomLineContainer = QFrame(self.vBottomContainer)
        self.vBottomLineContainer.setObjectName(u"vBottomLineContainer")
        self.vBottomLineContainer.setFrameShape(QFrame.StyledPanel)
        self.vBottomLineContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.vBottomLineContainer)
        self.verticalLayout_113.setSpacing(0)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 10)
        self.vBottomLine = QFrame(self.vBottomLineContainer)
        self.vBottomLine.setObjectName(u"vBottomLine")
        self.vBottomLine.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.vBottomLine.setFrameShape(QFrame.HLine)
        self.vBottomLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_113.addWidget(self.vBottomLine)


        self.verticalLayout_112.addWidget(self.vBottomLineContainer, 0, Qt.AlignTop)

        self.vBottomNextBtnContainer = QFrame(self.vBottomContainer)
        self.vBottomNextBtnContainer.setObjectName(u"vBottomNextBtnContainer")
        self.vBottomNextBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.vBottomNextBtnContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.vBottomNextBtnContainer)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.vBottomNextBtn = QPushButton(self.vBottomNextBtnContainer)
        self.vBottomNextBtn.setObjectName(u"vBottomNextBtn")
        self.vBottomNextBtn.setFont(font13)
        self.vBottomNextBtn.setStyleSheet(u"background-color:rgb(56, 166, 255);\n"
"padding: 3px 23px 3px 23px;\n"
"border-radius: 15px;\n"
"color: #fff;")

        self.horizontalLayout_44.addWidget(self.vBottomNextBtn)


        self.verticalLayout_112.addWidget(self.vBottomNextBtnContainer, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_30.addWidget(self.vBottomContainer, 0, Qt.AlignTop)

        self.frame_32 = QFrame(self.vScrollAreaContents)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 150))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.verticalLayout_30.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.vScrollAreaContents)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 150))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)

        self.verticalLayout_30.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.vScrollAreaContents)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 150))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.verticalLayout_30.addWidget(self.frame_34)

        self.vScrollArea.setWidget(self.vScrollAreaContents)

        self.verticalLayout_29.addWidget(self.vScrollArea)


        self.verticalLayout_21.addWidget(self.vWhiteCard)


        self.verticalLayout_20.addWidget(self.vBlueCard)


        self.verticalLayout_19.addWidget(self.vMarginContainer)

        self.diagnosisStackedWidget.addWidget(self.diagnosisValidationPage)
        self.diagnosisResultPage = QWidget()
        self.diagnosisResultPage.setObjectName(u"diagnosisResultPage")
        self.verticalLayout_18 = QVBoxLayout(self.diagnosisResultPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.resultProgressContainer = QWidget(self.diagnosisResultPage)
        self.resultProgressContainer.setObjectName(u"resultProgressContainer")
        sizePolicy1.setHeightForWidth(self.resultProgressContainer.sizePolicy().hasHeightForWidth())
        self.resultProgressContainer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_51 = QHBoxLayout(self.resultProgressContainer)
        self.horizontalLayout_51.setSpacing(6)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.resPExitBtnContainer = QFrame(self.resultProgressContainer)
        self.resPExitBtnContainer.setObjectName(u"resPExitBtnContainer")
        self.resPExitBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.resPExitBtnContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.resPExitBtnContainer)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.resPExitBtn = QPushButton(self.resPExitBtnContainer)
        self.resPExitBtn.setObjectName(u"resPExitBtn")
        self.resPExitBtn.setIcon(icon5)
        self.resPExitBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_52.addWidget(self.resPExitBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_51.addWidget(self.resPExitBtnContainer, 0, Qt.AlignLeft)

        self.resPProgressContainer = QFrame(self.resultProgressContainer)
        self.resPProgressContainer.setObjectName(u"resPProgressContainer")
        self.resPProgressContainer.setFrameShape(QFrame.StyledPanel)
        self.resPProgressContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.resPProgressContainer)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.resPProgress = QLabel(self.resPProgressContainer)
        self.resPProgress.setObjectName(u"resPProgress")
        sizePolicy2.setHeightForWidth(self.resPProgress.sizePolicy().hasHeightForWidth())
        self.resPProgress.setSizePolicy(sizePolicy2)
        self.resPProgress.setMinimumSize(QSize(680, 45))
        self.resPProgress.setMaximumSize(QSize(680, 45))
        self.resPProgress.setSizeIncrement(QSize(0, 0))
        self.resPProgress.setFont(font7)
        self.resPProgress.setFrameShadow(QFrame.Plain)
        self.resPProgress.setPixmap(QPixmap(u":/progressBarImages/images/progress5.png"))
        self.resPProgress.setScaledContents(True)
        self.resPProgress.setWordWrap(False)

        self.horizontalLayout_53.addWidget(self.resPProgress, 0, Qt.AlignVCenter)


        self.horizontalLayout_51.addWidget(self.resPProgressContainer, 0, Qt.AlignHCenter)

        self.resPExitBtn2 = QPushButton(self.resultProgressContainer)
        self.resPExitBtn2.setObjectName(u"resPExitBtn2")
        self.resPExitBtn2.setEnabled(False)

        self.horizontalLayout_51.addWidget(self.resPExitBtn2)


        self.verticalLayout_18.addWidget(self.resultProgressContainer)

        self.resMarginContainer = QFrame(self.diagnosisResultPage)
        self.resMarginContainer.setObjectName(u"resMarginContainer")
        sizePolicy3.setHeightForWidth(self.resMarginContainer.sizePolicy().hasHeightForWidth())
        self.resMarginContainer.setSizePolicy(sizePolicy3)
        self.resMarginContainer.setFrameShape(QFrame.StyledPanel)
        self.resMarginContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.resMarginContainer)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(70, 0, 70, 10)
        self.resBlueCard = QFrame(self.resMarginContainer)
        self.resBlueCard.setObjectName(u"resBlueCard")
        self.resBlueCard.setStyleSheet(u"background-color:#58AAEC;\n"
"border-radius: 15px;")
        self.resBlueCard.setFrameShape(QFrame.StyledPanel)
        self.resBlueCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.resBlueCard)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(10, 0, 0, 0)
        self.resWhiteCard = QFrame(self.resBlueCard)
        self.resWhiteCard.setObjectName(u"resWhiteCard")
        self.resWhiteCard.setStyleSheet(u"background-color:#FFF;\n"
"border-radius: 15px;")
        self.resWhiteCard.setFrameShape(QFrame.StyledPanel)
        self.resWhiteCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.resWhiteCard)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(5, 5, 5, 5)
        self.resScrollArea = QScrollArea(self.resWhiteCard)
        self.resScrollArea.setObjectName(u"resScrollArea")
        self.resScrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.resScrollArea.setWidgetResizable(True)
        self.resScrollAreaContents = QWidget()
        self.resScrollAreaContents.setObjectName(u"resScrollAreaContents")
        self.resScrollAreaContents.setGeometry(QRect(0, 0, 520, 796))
        self.resScrollAreaContents.setStyleSheet(u"#resResultOutlinedContainer, #resUserDetailsOutlinedContainer{border: 1px solid gray;}")
        self.verticalLayout_117 = QVBoxLayout(self.resScrollAreaContents)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.resTopContainer = QFrame(self.resScrollAreaContents)
        self.resTopContainer.setObjectName(u"resTopContainer")
        self.resTopContainer.setMinimumSize(QSize(0, 0))
        self.resTopContainer.setFrameShape(QFrame.StyledPanel)
        self.resTopContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.resTopContainer)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(20, 15, 40, 10)
        self.resTopLabelContainer = QFrame(self.resTopContainer)
        self.resTopLabelContainer.setObjectName(u"resTopLabelContainer")
        self.resTopLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.resTopLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_118 = QVBoxLayout(self.resTopLabelContainer)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.resTopLabel = QLabel(self.resTopLabelContainer)
        self.resTopLabel.setObjectName(u"resTopLabel")
        self.resTopLabel.setFont(font14)

        self.verticalLayout_118.addWidget(self.resTopLabel, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_45.addWidget(self.resTopLabelContainer, 0, Qt.AlignLeft|Qt.AlignTop)

        self.resTopBtnContainer = QFrame(self.resTopContainer)
        self.resTopBtnContainer.setObjectName(u"resTopBtnContainer")
        self.resTopBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.resTopBtnContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.resTopBtnContainer)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(-1, 0, -1, 0)
        self.resTopPrintBtn = QPushButton(self.resTopBtnContainer)
        self.resTopPrintBtn.setObjectName(u"resTopPrintBtn")
        self.resTopPrintBtn.setFont(font17)
        self.resTopPrintBtn.setStyleSheet(u"background-color: #FFF;\n"
"border: 1px solid #38A6FF;\n"
"color:#38A6FF;\n"
"padding: 4px 10px 4px 10px;\n"
"border-radius: 14px;\n"
"\n"
"")

        self.horizontalLayout_54.addWidget(self.resTopPrintBtn)

        self.resTopDownloadBtn = QPushButton(self.resTopBtnContainer)
        self.resTopDownloadBtn.setObjectName(u"resTopDownloadBtn")
        self.resTopDownloadBtn.setFont(font17)
        self.resTopDownloadBtn.setStyleSheet(u"background-color: #FFF;\n"
"border: 1px solid #38A6FF;\n"
"color:#38A6FF;\n"
"padding: 4px 25px 4px 25px;\n"
"border-radius:14px;\n"
"\n"
"")

        self.horizontalLayout_54.addWidget(self.resTopDownloadBtn)


        self.horizontalLayout_45.addWidget(self.resTopBtnContainer, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_117.addWidget(self.resTopContainer)

        self.resUserDetailsContainer = QFrame(self.resScrollAreaContents)
        self.resUserDetailsContainer.setObjectName(u"resUserDetailsContainer")
        self.resUserDetailsContainer.setMinimumSize(QSize(0, 0))
        self.resUserDetailsContainer.setStyleSheet(u"")
        self.resUserDetailsContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.resUserDetailsContainer)
        self.verticalLayout_120.setSpacing(0)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(30, 0, 30, 10)
        self.resUserDetailsOutlinedContainer = QFrame(self.resUserDetailsContainer)
        self.resUserDetailsOutlinedContainer.setObjectName(u"resUserDetailsOutlinedContainer")
        self.resUserDetailsOutlinedContainer.setStyleSheet(u"")
        self.resUserDetailsOutlinedContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsOutlinedContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_121 = QVBoxLayout(self.resUserDetailsOutlinedContainer)
        self.verticalLayout_121.setSpacing(0)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(20, 10, 20, 0)
        self.resUserDetailsTopContainer = QFrame(self.resUserDetailsOutlinedContainer)
        self.resUserDetailsTopContainer.setObjectName(u"resUserDetailsTopContainer")
        self.resUserDetailsTopContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsTopContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_122 = QVBoxLayout(self.resUserDetailsTopContainer)
        self.verticalLayout_122.setSpacing(0)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 0, 0, 15)
        self.resUserDetailsNameHeadingContainer = QFrame(self.resUserDetailsTopContainer)
        self.resUserDetailsNameHeadingContainer.setObjectName(u"resUserDetailsNameHeadingContainer")
        self.resUserDetailsNameHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsNameHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.resUserDetailsNameHeadingContainer)
        self.verticalLayout_123.setSpacing(0)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsNameHeading = QLabel(self.resUserDetailsNameHeadingContainer)
        self.resUserDetailsNameHeading.setObjectName(u"resUserDetailsNameHeading")
        self.resUserDetailsNameHeading.setFont(font17)

        self.verticalLayout_123.addWidget(self.resUserDetailsNameHeading, 0, Qt.AlignBottom)


        self.verticalLayout_122.addWidget(self.resUserDetailsNameHeadingContainer)

        self.resUserDetailsNameLabelContainer = QFrame(self.resUserDetailsTopContainer)
        self.resUserDetailsNameLabelContainer.setObjectName(u"resUserDetailsNameLabelContainer")
        self.resUserDetailsNameLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsNameLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.resUserDetailsNameLabelContainer)
        self.verticalLayout_124.setSpacing(0)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsNameLabel = QLabel(self.resUserDetailsNameLabelContainer)
        self.resUserDetailsNameLabel.setObjectName(u"resUserDetailsNameLabel")
        self.resUserDetailsNameLabel.setFont(font12)

        self.verticalLayout_124.addWidget(self.resUserDetailsNameLabel, 0, Qt.AlignTop)


        self.verticalLayout_122.addWidget(self.resUserDetailsNameLabelContainer)


        self.verticalLayout_121.addWidget(self.resUserDetailsTopContainer)

        self.resUserDetailsMidContainer = QFrame(self.resUserDetailsOutlinedContainer)
        self.resUserDetailsMidContainer.setObjectName(u"resUserDetailsMidContainer")
        self.resUserDetailsMidContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsMidContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.resUserDetailsMidContainer)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 15)
        self.resUserDetailsBirthdateContainer = QFrame(self.resUserDetailsMidContainer)
        self.resUserDetailsBirthdateContainer.setObjectName(u"resUserDetailsBirthdateContainer")
        self.resUserDetailsBirthdateContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsBirthdateContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_125 = QVBoxLayout(self.resUserDetailsBirthdateContainer)
        self.verticalLayout_125.setSpacing(0)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsBirthdateHeadingContainer = QFrame(self.resUserDetailsBirthdateContainer)
        self.resUserDetailsBirthdateHeadingContainer.setObjectName(u"resUserDetailsBirthdateHeadingContainer")
        self.resUserDetailsBirthdateHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsBirthdateHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_126 = QVBoxLayout(self.resUserDetailsBirthdateHeadingContainer)
        self.verticalLayout_126.setSpacing(0)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsBirthdateHeading = QLabel(self.resUserDetailsBirthdateHeadingContainer)
        self.resUserDetailsBirthdateHeading.setObjectName(u"resUserDetailsBirthdateHeading")
        self.resUserDetailsBirthdateHeading.setFont(font17)

        self.verticalLayout_126.addWidget(self.resUserDetailsBirthdateHeading)


        self.verticalLayout_125.addWidget(self.resUserDetailsBirthdateHeadingContainer)

        self.resUserDetailsBirthdateLabelContainer = QFrame(self.resUserDetailsBirthdateContainer)
        self.resUserDetailsBirthdateLabelContainer.setObjectName(u"resUserDetailsBirthdateLabelContainer")
        self.resUserDetailsBirthdateLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsBirthdateLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.resUserDetailsBirthdateLabelContainer)
        self.verticalLayout_127.setSpacing(0)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsBirthdateLabel = QLabel(self.resUserDetailsBirthdateLabelContainer)
        self.resUserDetailsBirthdateLabel.setObjectName(u"resUserDetailsBirthdateLabel")
        self.resUserDetailsBirthdateLabel.setFont(font12)

        self.verticalLayout_127.addWidget(self.resUserDetailsBirthdateLabel)


        self.verticalLayout_125.addWidget(self.resUserDetailsBirthdateLabelContainer)


        self.horizontalLayout_46.addWidget(self.resUserDetailsBirthdateContainer, 0, Qt.AlignLeft)

        self.resUserDetailsAgeContainer = QFrame(self.resUserDetailsMidContainer)
        self.resUserDetailsAgeContainer.setObjectName(u"resUserDetailsAgeContainer")
        self.resUserDetailsAgeContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsAgeContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_128 = QVBoxLayout(self.resUserDetailsAgeContainer)
        self.verticalLayout_128.setSpacing(0)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.verticalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsAgeHeadingContainer = QFrame(self.resUserDetailsAgeContainer)
        self.resUserDetailsAgeHeadingContainer.setObjectName(u"resUserDetailsAgeHeadingContainer")
        self.resUserDetailsAgeHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsAgeHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_129 = QVBoxLayout(self.resUserDetailsAgeHeadingContainer)
        self.verticalLayout_129.setSpacing(0)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.verticalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsAgeHeading = QLabel(self.resUserDetailsAgeHeadingContainer)
        self.resUserDetailsAgeHeading.setObjectName(u"resUserDetailsAgeHeading")
        self.resUserDetailsAgeHeading.setFont(font17)

        self.verticalLayout_129.addWidget(self.resUserDetailsAgeHeading)


        self.verticalLayout_128.addWidget(self.resUserDetailsAgeHeadingContainer)

        self.resUserDetailsAgeLabelContainer = QFrame(self.resUserDetailsAgeContainer)
        self.resUserDetailsAgeLabelContainer.setObjectName(u"resUserDetailsAgeLabelContainer")
        self.resUserDetailsAgeLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsAgeLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_130 = QVBoxLayout(self.resUserDetailsAgeLabelContainer)
        self.verticalLayout_130.setSpacing(0)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.verticalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsAgeLabel = QLabel(self.resUserDetailsAgeLabelContainer)
        self.resUserDetailsAgeLabel.setObjectName(u"resUserDetailsAgeLabel")
        self.resUserDetailsAgeLabel.setFont(font12)

        self.verticalLayout_130.addWidget(self.resUserDetailsAgeLabel)


        self.verticalLayout_128.addWidget(self.resUserDetailsAgeLabelContainer)


        self.horizontalLayout_46.addWidget(self.resUserDetailsAgeContainer, 0, Qt.AlignHCenter)

        self.resUserDetailsSexContainer = QFrame(self.resUserDetailsMidContainer)
        self.resUserDetailsSexContainer.setObjectName(u"resUserDetailsSexContainer")
        self.resUserDetailsSexContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsSexContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_131 = QVBoxLayout(self.resUserDetailsSexContainer)
        self.verticalLayout_131.setSpacing(0)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsSexHeadingContainer = QFrame(self.resUserDetailsSexContainer)
        self.resUserDetailsSexHeadingContainer.setObjectName(u"resUserDetailsSexHeadingContainer")
        self.resUserDetailsSexHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsSexHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_132 = QVBoxLayout(self.resUserDetailsSexHeadingContainer)
        self.verticalLayout_132.setSpacing(0)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsSexHeadingContainer_2 = QLabel(self.resUserDetailsSexHeadingContainer)
        self.resUserDetailsSexHeadingContainer_2.setObjectName(u"resUserDetailsSexHeadingContainer_2")
        self.resUserDetailsSexHeadingContainer_2.setFont(font17)

        self.verticalLayout_132.addWidget(self.resUserDetailsSexHeadingContainer_2)


        self.verticalLayout_131.addWidget(self.resUserDetailsSexHeadingContainer)

        self.resUserDetailsSexLabelContainer = QFrame(self.resUserDetailsSexContainer)
        self.resUserDetailsSexLabelContainer.setObjectName(u"resUserDetailsSexLabelContainer")
        self.resUserDetailsSexLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsSexLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_133 = QVBoxLayout(self.resUserDetailsSexLabelContainer)
        self.verticalLayout_133.setSpacing(0)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsSexLabel = QLabel(self.resUserDetailsSexLabelContainer)
        self.resUserDetailsSexLabel.setObjectName(u"resUserDetailsSexLabel")
        self.resUserDetailsSexLabel.setFont(font12)

        self.verticalLayout_133.addWidget(self.resUserDetailsSexLabel)


        self.verticalLayout_131.addWidget(self.resUserDetailsSexLabelContainer)


        self.horizontalLayout_46.addWidget(self.resUserDetailsSexContainer, 0, Qt.AlignHCenter)

        self.resUserDetailsCivilContainer = QFrame(self.resUserDetailsMidContainer)
        self.resUserDetailsCivilContainer.setObjectName(u"resUserDetailsCivilContainer")
        self.resUserDetailsCivilContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsCivilContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_134 = QVBoxLayout(self.resUserDetailsCivilContainer)
        self.verticalLayout_134.setSpacing(0)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.verticalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsCivilHeadingContainer = QFrame(self.resUserDetailsCivilContainer)
        self.resUserDetailsCivilHeadingContainer.setObjectName(u"resUserDetailsCivilHeadingContainer")
        self.resUserDetailsCivilHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsCivilHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.resUserDetailsCivilHeadingContainer)
        self.verticalLayout_135.setSpacing(0)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsCivilHeading = QLabel(self.resUserDetailsCivilHeadingContainer)
        self.resUserDetailsCivilHeading.setObjectName(u"resUserDetailsCivilHeading")
        self.resUserDetailsCivilHeading.setFont(font17)

        self.verticalLayout_135.addWidget(self.resUserDetailsCivilHeading)


        self.verticalLayout_134.addWidget(self.resUserDetailsCivilHeadingContainer)

        self.resUserDetailsCivilLabelContainer = QFrame(self.resUserDetailsCivilContainer)
        self.resUserDetailsCivilLabelContainer.setObjectName(u"resUserDetailsCivilLabelContainer")
        self.resUserDetailsCivilLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsCivilLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.resUserDetailsCivilLabelContainer)
        self.verticalLayout_136.setSpacing(0)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsCivilLabel = QLabel(self.resUserDetailsCivilLabelContainer)
        self.resUserDetailsCivilLabel.setObjectName(u"resUserDetailsCivilLabel")
        self.resUserDetailsCivilLabel.setFont(font12)

        self.verticalLayout_136.addWidget(self.resUserDetailsCivilLabel)


        self.verticalLayout_134.addWidget(self.resUserDetailsCivilLabelContainer)


        self.horizontalLayout_46.addWidget(self.resUserDetailsCivilContainer, 0, Qt.AlignHCenter)

        self.resUserDetailsContactContainer = QFrame(self.resUserDetailsMidContainer)
        self.resUserDetailsContactContainer.setObjectName(u"resUserDetailsContactContainer")
        self.resUserDetailsContactContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsContactContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_137 = QVBoxLayout(self.resUserDetailsContactContainer)
        self.verticalLayout_137.setSpacing(0)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsContactHeadingContainer = QFrame(self.resUserDetailsContactContainer)
        self.resUserDetailsContactHeadingContainer.setObjectName(u"resUserDetailsContactHeadingContainer")
        self.resUserDetailsContactHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsContactHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_138 = QVBoxLayout(self.resUserDetailsContactHeadingContainer)
        self.verticalLayout_138.setSpacing(0)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsContactHeading = QLabel(self.resUserDetailsContactHeadingContainer)
        self.resUserDetailsContactHeading.setObjectName(u"resUserDetailsContactHeading")
        self.resUserDetailsContactHeading.setFont(font17)

        self.verticalLayout_138.addWidget(self.resUserDetailsContactHeading)


        self.verticalLayout_137.addWidget(self.resUserDetailsContactHeadingContainer)

        self.resUserDetailsContactLabelContainer = QFrame(self.resUserDetailsContactContainer)
        self.resUserDetailsContactLabelContainer.setObjectName(u"resUserDetailsContactLabelContainer")
        self.resUserDetailsContactLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsContactLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.resUserDetailsContactLabelContainer)
        self.verticalLayout_139.setSpacing(0)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsContactLabel = QLabel(self.resUserDetailsContactLabelContainer)
        self.resUserDetailsContactLabel.setObjectName(u"resUserDetailsContactLabel")
        self.resUserDetailsContactLabel.setFont(font12)

        self.verticalLayout_139.addWidget(self.resUserDetailsContactLabel)


        self.verticalLayout_137.addWidget(self.resUserDetailsContactLabelContainer)


        self.horizontalLayout_46.addWidget(self.resUserDetailsContactContainer, 0, Qt.AlignRight)


        self.verticalLayout_121.addWidget(self.resUserDetailsMidContainer)

        self.resUserDetailsBottomContainer = QFrame(self.resUserDetailsOutlinedContainer)
        self.resUserDetailsBottomContainer.setObjectName(u"resUserDetailsBottomContainer")
        self.resUserDetailsBottomContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsBottomContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.resUserDetailsBottomContainer)
        self.verticalLayout_140.setSpacing(0)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_140.setContentsMargins(0, 0, 0, 15)
        self.resUserDetailsAddressHeadingContainer = QFrame(self.resUserDetailsBottomContainer)
        self.resUserDetailsAddressHeadingContainer.setObjectName(u"resUserDetailsAddressHeadingContainer")
        self.resUserDetailsAddressHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsAddressHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_141 = QVBoxLayout(self.resUserDetailsAddressHeadingContainer)
        self.verticalLayout_141.setSpacing(0)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.verticalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsAddressHeading = QLabel(self.resUserDetailsAddressHeadingContainer)
        self.resUserDetailsAddressHeading.setObjectName(u"resUserDetailsAddressHeading")
        self.resUserDetailsAddressHeading.setFont(font17)

        self.verticalLayout_141.addWidget(self.resUserDetailsAddressHeading)


        self.verticalLayout_140.addWidget(self.resUserDetailsAddressHeadingContainer, 0, Qt.AlignBottom)

        self.resUserDetailsAddressLabelContainer = QFrame(self.resUserDetailsBottomContainer)
        self.resUserDetailsAddressLabelContainer.setObjectName(u"resUserDetailsAddressLabelContainer")
        self.resUserDetailsAddressLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.resUserDetailsAddressLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_142 = QVBoxLayout(self.resUserDetailsAddressLabelContainer)
        self.verticalLayout_142.setSpacing(9)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.resUserDetailsAddressLabel = QLabel(self.resUserDetailsAddressLabelContainer)
        self.resUserDetailsAddressLabel.setObjectName(u"resUserDetailsAddressLabel")

        self.verticalLayout_142.addWidget(self.resUserDetailsAddressLabel, 0, Qt.AlignTop)


        self.verticalLayout_140.addWidget(self.resUserDetailsAddressLabelContainer)


        self.verticalLayout_121.addWidget(self.resUserDetailsBottomContainer)


        self.verticalLayout_120.addWidget(self.resUserDetailsOutlinedContainer)


        self.verticalLayout_117.addWidget(self.resUserDetailsContainer)

        self.resResultContainer = QFrame(self.resScrollAreaContents)
        self.resResultContainer.setObjectName(u"resResultContainer")
        self.resResultContainer.setMinimumSize(QSize(0, 0))
        self.resResultContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_156 = QVBoxLayout(self.resResultContainer)
        self.verticalLayout_156.setSpacing(0)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.verticalLayout_156.setContentsMargins(30, 0, 30, 0)
        self.resResultOutlinedContainer = QFrame(self.resResultContainer)
        self.resResultOutlinedContainer.setObjectName(u"resResultOutlinedContainer")
        self.resResultOutlinedContainer.setStyleSheet(u"")
        self.resResultOutlinedContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultOutlinedContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.resResultOutlinedContainer)
        self.verticalLayout_119.setSpacing(0)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(20, 10, 20, 10)
        self.resResultTopContainer = QFrame(self.resResultOutlinedContainer)
        self.resResultTopContainer.setObjectName(u"resResultTopContainer")
        self.resResultTopContainer.setMinimumSize(QSize(0, 0))
        self.resResultTopContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultTopContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.resResultTopContainer)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.resResultTopPredictionContainer = QFrame(self.resResultTopContainer)
        self.resResultTopPredictionContainer.setObjectName(u"resResultTopPredictionContainer")
        self.resResultTopPredictionContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultTopPredictionContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_176 = QVBoxLayout(self.resResultTopPredictionContainer)
        self.verticalLayout_176.setSpacing(0)
        self.verticalLayout_176.setObjectName(u"verticalLayout_176")
        self.verticalLayout_176.setContentsMargins(0, 0, 5, 0)
        self.resResultPredictionHeadingContainer = QFrame(self.resResultTopPredictionContainer)
        self.resResultPredictionHeadingContainer.setObjectName(u"resResultPredictionHeadingContainer")
        self.resResultPredictionHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultPredictionHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_178 = QVBoxLayout(self.resResultPredictionHeadingContainer)
        self.verticalLayout_178.setSpacing(0)
        self.verticalLayout_178.setObjectName(u"verticalLayout_178")
        self.verticalLayout_178.setContentsMargins(0, 0, 0, 0)
        self.resResultPredictionHeading = QLabel(self.resResultPredictionHeadingContainer)
        self.resResultPredictionHeading.setObjectName(u"resResultPredictionHeading")
        self.resResultPredictionHeading.setFont(font17)

        self.verticalLayout_178.addWidget(self.resResultPredictionHeading)


        self.verticalLayout_176.addWidget(self.resResultPredictionHeadingContainer)

        self.resResultPredictionLabelContainer = QFrame(self.resResultTopPredictionContainer)
        self.resResultPredictionLabelContainer.setObjectName(u"resResultPredictionLabelContainer")
        self.resResultPredictionLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultPredictionLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_179 = QVBoxLayout(self.resResultPredictionLabelContainer)
        self.verticalLayout_179.setSpacing(0)
        self.verticalLayout_179.setObjectName(u"verticalLayout_179")
        self.verticalLayout_179.setContentsMargins(25, 0, 0, 0)
        self.resResultPredictionLabel = QLabel(self.resResultPredictionLabelContainer)
        self.resResultPredictionLabel.setObjectName(u"resResultPredictionLabel")
        font18 = QFont()
        font18.setFamily(u"Open Sans")
        font18.setPointSize(18)
        font18.setBold(True)
        font18.setWeight(75)
        self.resResultPredictionLabel.setFont(font18)

        self.verticalLayout_179.addWidget(self.resResultPredictionLabel)


        self.verticalLayout_176.addWidget(self.resResultPredictionLabelContainer)


        self.horizontalLayout_49.addWidget(self.resResultTopPredictionContainer)

        self.resResultTopConfidenceContainer = QFrame(self.resResultTopContainer)
        self.resResultTopConfidenceContainer.setObjectName(u"resResultTopConfidenceContainer")
        self.resResultTopConfidenceContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultTopConfidenceContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_177 = QVBoxLayout(self.resResultTopConfidenceContainer)
        self.verticalLayout_177.setSpacing(0)
        self.verticalLayout_177.setObjectName(u"verticalLayout_177")
        self.verticalLayout_177.setContentsMargins(0, 0, 5, 0)
        self.resResultConfidenceHeadingContainer = QFrame(self.resResultTopConfidenceContainer)
        self.resResultConfidenceHeadingContainer.setObjectName(u"resResultConfidenceHeadingContainer")
        self.resResultConfidenceHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultConfidenceHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_180 = QVBoxLayout(self.resResultConfidenceHeadingContainer)
        self.verticalLayout_180.setSpacing(0)
        self.verticalLayout_180.setObjectName(u"verticalLayout_180")
        self.verticalLayout_180.setContentsMargins(0, 0, 0, 0)
        self.resResultConfidenceHeading = QLabel(self.resResultConfidenceHeadingContainer)
        self.resResultConfidenceHeading.setObjectName(u"resResultConfidenceHeading")
        self.resResultConfidenceHeading.setFont(font17)

        self.verticalLayout_180.addWidget(self.resResultConfidenceHeading)


        self.verticalLayout_177.addWidget(self.resResultConfidenceHeadingContainer, 0, Qt.AlignTop)

        self.resResultConfidenceLabelContainer = QFrame(self.resResultTopConfidenceContainer)
        self.resResultConfidenceLabelContainer.setObjectName(u"resResultConfidenceLabelContainer")
        self.resResultConfidenceLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultConfidenceLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_181 = QVBoxLayout(self.resResultConfidenceLabelContainer)
        self.verticalLayout_181.setSpacing(0)
        self.verticalLayout_181.setObjectName(u"verticalLayout_181")
        self.verticalLayout_181.setContentsMargins(25, 0, 0, 0)
        self.resResultConfidenceLabel = QLabel(self.resResultConfidenceLabelContainer)
        self.resResultConfidenceLabel.setObjectName(u"resResultConfidenceLabel")

        self.verticalLayout_181.addWidget(self.resResultConfidenceLabel)


        self.verticalLayout_177.addWidget(self.resResultConfidenceLabelContainer, 0, Qt.AlignTop)


        self.horizontalLayout_49.addWidget(self.resResultTopConfidenceContainer)

        self.horizontalLayout_49.setStretch(0, 80)
        self.horizontalLayout_49.setStretch(1, 20)

        self.verticalLayout_119.addWidget(self.resResultTopContainer)

        self.resResultTopLineContainer = QFrame(self.resResultOutlinedContainer)
        self.resResultTopLineContainer.setObjectName(u"resResultTopLineContainer")
        self.resResultTopLineContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultTopLineContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_172 = QVBoxLayout(self.resResultTopLineContainer)
        self.verticalLayout_172.setObjectName(u"verticalLayout_172")
        self.verticalLayout_172.setContentsMargins(40, 10, 40, 10)
        self.resResultTopLine = QFrame(self.resResultTopLineContainer)
        self.resResultTopLine.setObjectName(u"resResultTopLine")
        self.resResultTopLine.setMinimumSize(QSize(0, 4))
        self.resResultTopLine.setStyleSheet(u"border: 0.5px solid #FFF;\n"
"border-style: inset;\n"
"background-color: rgb(0, 0, 0);")
        self.resResultTopLine.setFrameShape(QFrame.HLine)
        self.resResultTopLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_172.addWidget(self.resResultTopLine)


        self.verticalLayout_119.addWidget(self.resResultTopLineContainer)

        self.resResultCauseContainer = QFrame(self.resResultOutlinedContainer)
        self.resResultCauseContainer.setObjectName(u"resResultCauseContainer")
        self.resResultCauseContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultCauseContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_168 = QVBoxLayout(self.resResultCauseContainer)
        self.verticalLayout_168.setSpacing(0)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.verticalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.resResultCauseLabelContainer = QFrame(self.resResultCauseContainer)
        self.resResultCauseLabelContainer.setObjectName(u"resResultCauseLabelContainer")
        self.resResultCauseLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultCauseLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_169 = QVBoxLayout(self.resResultCauseLabelContainer)
        self.verticalLayout_169.setSpacing(0)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.verticalLayout_169.setContentsMargins(0, 0, 0, 0)
        self.resResultCauseLabel = QLabel(self.resResultCauseLabelContainer)
        self.resResultCauseLabel.setObjectName(u"resResultCauseLabel")
        self.resResultCauseLabel.setFont(font17)

        self.verticalLayout_169.addWidget(self.resResultCauseLabel)


        self.verticalLayout_168.addWidget(self.resResultCauseLabelContainer)

        self.resResultCauseListWidgetContainer = QFrame(self.resResultCauseContainer)
        self.resResultCauseListWidgetContainer.setObjectName(u"resResultCauseListWidgetContainer")
        sizePolicy3.setHeightForWidth(self.resResultCauseListWidgetContainer.sizePolicy().hasHeightForWidth())
        self.resResultCauseListWidgetContainer.setSizePolicy(sizePolicy3)
        self.resResultCauseListWidgetContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultCauseListWidgetContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_170 = QVBoxLayout(self.resResultCauseListWidgetContainer)
        self.verticalLayout_170.setSpacing(0)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.verticalLayout_170.setContentsMargins(20, 10, 20, 0)
        self.resResultCauseListWidget = QListWidget(self.resResultCauseListWidgetContainer)
        QListWidgetItem(self.resResultCauseListWidget)
        QListWidgetItem(self.resResultCauseListWidget)
        QListWidgetItem(self.resResultCauseListWidget)
        QListWidgetItem(self.resResultCauseListWidget)
        QListWidgetItem(self.resResultCauseListWidget)
        self.resResultCauseListWidget.setObjectName(u"resResultCauseListWidget")
        self.resResultCauseListWidget.setMinimumSize(QSize(0, 150))
        self.resResultCauseListWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.resResultCauseListWidget.setAutoScroll(False)
        self.resResultCauseListWidget.setSpacing(3)
        self.resResultCauseListWidget.setWordWrap(True)

        self.verticalLayout_170.addWidget(self.resResultCauseListWidget)


        self.verticalLayout_168.addWidget(self.resResultCauseListWidgetContainer)


        self.verticalLayout_119.addWidget(self.resResultCauseContainer)

        self.resResultMidLineContainer = QFrame(self.resResultOutlinedContainer)
        self.resResultMidLineContainer.setObjectName(u"resResultMidLineContainer")
        self.resResultMidLineContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultMidLineContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_171 = QVBoxLayout(self.resResultMidLineContainer)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.verticalLayout_171.setContentsMargins(40, 10, 40, 10)
        self.resResultMidLine = QFrame(self.resResultMidLineContainer)
        self.resResultMidLine.setObjectName(u"resResultMidLine")
        self.resResultMidLine.setMinimumSize(QSize(0, 4))
        self.resResultMidLine.setStyleSheet(u"border: 0.5px solid #FFF;\n"
"border-style: inset;\n"
"background-color: rgb(0, 0, 0);")
        self.resResultMidLine.setFrameShape(QFrame.HLine)
        self.resResultMidLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_171.addWidget(self.resResultMidLine)


        self.verticalLayout_119.addWidget(self.resResultMidLineContainer)

        self.resResultActionContainer = QFrame(self.resResultOutlinedContainer)
        self.resResultActionContainer.setObjectName(u"resResultActionContainer")
        self.resResultActionContainer.setMinimumSize(QSize(0, 0))
        self.resResultActionContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultActionContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_173 = QVBoxLayout(self.resResultActionContainer)
        self.verticalLayout_173.setSpacing(0)
        self.verticalLayout_173.setObjectName(u"verticalLayout_173")
        self.verticalLayout_173.setContentsMargins(0, 0, 0, 0)
        self.resResultActionLabelContainer = QFrame(self.resResultActionContainer)
        self.resResultActionLabelContainer.setObjectName(u"resResultActionLabelContainer")
        self.resResultActionLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultActionLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_174 = QVBoxLayout(self.resResultActionLabelContainer)
        self.verticalLayout_174.setSpacing(0)
        self.verticalLayout_174.setObjectName(u"verticalLayout_174")
        self.verticalLayout_174.setContentsMargins(0, 0, 0, 0)
        self.resResultActionLabel = QLabel(self.resResultActionLabelContainer)
        self.resResultActionLabel.setObjectName(u"resResultActionLabel")
        self.resResultActionLabel.setFont(font17)

        self.verticalLayout_174.addWidget(self.resResultActionLabel)


        self.verticalLayout_173.addWidget(self.resResultActionLabelContainer)

        self.resResultActionListWidgetContainer = QFrame(self.resResultActionContainer)
        self.resResultActionListWidgetContainer.setObjectName(u"resResultActionListWidgetContainer")
        self.resResultActionListWidgetContainer.setFrameShape(QFrame.StyledPanel)
        self.resResultActionListWidgetContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_175 = QVBoxLayout(self.resResultActionListWidgetContainer)
        self.verticalLayout_175.setSpacing(0)
        self.verticalLayout_175.setObjectName(u"verticalLayout_175")
        self.verticalLayout_175.setContentsMargins(20, 10, 20, 0)
        self.resResultActionListWidget = QListWidget(self.resResultActionListWidgetContainer)
        QListWidgetItem(self.resResultActionListWidget)
        QListWidgetItem(self.resResultActionListWidget)
        QListWidgetItem(self.resResultActionListWidget)
        QListWidgetItem(self.resResultActionListWidget)
        QListWidgetItem(self.resResultActionListWidget)
        self.resResultActionListWidget.setObjectName(u"resResultActionListWidget")
        self.resResultActionListWidget.setMinimumSize(QSize(0, 150))
        self.resResultActionListWidget.setAutoScroll(False)
        self.resResultActionListWidget.setSpacing(3)
        self.resResultActionListWidget.setWordWrap(True)

        self.verticalLayout_175.addWidget(self.resResultActionListWidget)


        self.verticalLayout_173.addWidget(self.resResultActionListWidgetContainer)


        self.verticalLayout_119.addWidget(self.resResultActionContainer)


        self.verticalLayout_156.addWidget(self.resResultOutlinedContainer)


        self.verticalLayout_117.addWidget(self.resResultContainer)

        self.resBottomContainer = QFrame(self.resScrollAreaContents)
        self.resBottomContainer.setObjectName(u"resBottomContainer")
        self.resBottomContainer.setMinimumSize(QSize(0, 0))
        self.resBottomContainer.setFrameShape(QFrame.StyledPanel)
        self.resBottomContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_157 = QVBoxLayout(self.resBottomContainer)
        self.verticalLayout_157.setSpacing(0)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.verticalLayout_157.setContentsMargins(20, 20, 20, 20)
        self.resBottomLineContainer = QFrame(self.resBottomContainer)
        self.resBottomLineContainer.setObjectName(u"resBottomLineContainer")
        self.resBottomLineContainer.setFrameShape(QFrame.StyledPanel)
        self.resBottomLineContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_158 = QVBoxLayout(self.resBottomLineContainer)
        self.verticalLayout_158.setSpacing(0)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.verticalLayout_158.setContentsMargins(0, 0, 0, 10)
        self.resBottomLine = QFrame(self.resBottomLineContainer)
        self.resBottomLine.setObjectName(u"resBottomLine")
        self.resBottomLine.setStyleSheet(u"border: 0.5px solid rgb(161, 161, 161);\n"
"border-style: inset;")
        self.resBottomLine.setFrameShape(QFrame.HLine)
        self.resBottomLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_158.addWidget(self.resBottomLine)


        self.verticalLayout_157.addWidget(self.resBottomLineContainer, 0, Qt.AlignTop)

        self.resBottomBtnContainer = QFrame(self.resBottomContainer)
        self.resBottomBtnContainer.setObjectName(u"resBottomBtnContainer")
        self.resBottomBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.resBottomBtnContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.resBottomBtnContainer)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(-1, 0, -1, 0)
        self.resBottomCloseBtn = QPushButton(self.resBottomBtnContainer)
        self.resBottomCloseBtn.setObjectName(u"resBottomCloseBtn")
        self.resBottomCloseBtn.setFont(font13)
        self.resBottomCloseBtn.setStyleSheet(u"background-color: #FFF;\n"
"border: 1px solid #38A6FF;\n"
"color:#38A6FF;\n"
"padding: 3px 23px 3px 23px;\n"
"border-radius: 15px;\n"
"\n"
"")

        self.horizontalLayout_48.addWidget(self.resBottomCloseBtn)

        self.resBottomSaveBtn = QPushButton(self.resBottomBtnContainer)
        self.resBottomSaveBtn.setObjectName(u"resBottomSaveBtn")
        self.resBottomSaveBtn.setFont(font13)
        self.resBottomSaveBtn.setStyleSheet(u"background-color:rgb(56, 166, 255);\n"
"padding: 3px 23px 3px 23px;\n"
"border-radius: 15px;\n"
"color: #fff;")

        self.horizontalLayout_48.addWidget(self.resBottomSaveBtn)


        self.verticalLayout_157.addWidget(self.resBottomBtnContainer, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_117.addWidget(self.resBottomContainer, 0, Qt.AlignTop)

        self.resScrollArea.setWidget(self.resScrollAreaContents)

        self.verticalLayout_116.addWidget(self.resScrollArea)


        self.verticalLayout_115.addWidget(self.resWhiteCard)


        self.verticalLayout_114.addWidget(self.resBlueCard)


        self.verticalLayout_18.addWidget(self.resMarginContainer)

        self.diagnosisStackedWidget.addWidget(self.diagnosisResultPage)

        self.verticalLayout_17.addWidget(self.diagnosisStackedWidget)

        self.mainPages.addWidget(self.diagnosisPages)
        self.recordsPages = QWidget()
        self.recordsPages.setObjectName(u"recordsPages")
        self.verticalLayout_8 = QVBoxLayout(self.recordsPages)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.recordsStackedWidget = QStackedWidget(self.recordsPages)
        self.recordsStackedWidget.setObjectName(u"recordsStackedWidget")
        self.recordsAuthPage = QWidget()
        self.recordsAuthPage.setObjectName(u"recordsAuthPage")
        self.verticalLayout_6 = QVBoxLayout(self.recordsAuthPage)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(50, 40, 50, 40)
        self.recordsCardsFrame = QWidget(self.recordsAuthPage)
        self.recordsCardsFrame.setObjectName(u"recordsCardsFrame")
        self.recordsCardsFrame.setStyleSheet(u"#recBlueCard {\n"
"	border-radius: 20px;\n"
"}\n"
"#recWhiteCard {\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.recordsCardsFrame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.recBlueCard = QFrame(self.recordsCardsFrame)
        self.recBlueCard.setObjectName(u"recBlueCard")
        self.recBlueCard.setStyleSheet(u"background-color: rgb(189, 223, 255);")
        self.recBlueCard.setFrameShape(QFrame.StyledPanel)
        self.recBlueCard.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.recBlueCard)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.recImageContainer = QWidget(self.recBlueCard)
        self.recImageContainer.setObjectName(u"recImageContainer")
        self.recImageContainer.setStyleSheet(u"")
        self.verticalLayout_23 = QVBoxLayout(self.recImageContainer)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.recImage = QLabel(self.recImageContainer)
        self.recImage.setObjectName(u"recImage")
        self.recImage.setStyleSheet(u"")
        self.recImage.setPixmap(QPixmap(u":/images/images/recordsPicture.png"))
        self.recImage.setScaledContents(True)
        self.recImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.recImage)


        self.horizontalLayout_10.addWidget(self.recImageContainer)

        self.recWhiteCard = QFrame(self.recBlueCard)
        self.recWhiteCard.setObjectName(u"recWhiteCard")
        self.recWhiteCard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.recWhiteCard.setFrameShape(QFrame.StyledPanel)
        self.recWhiteCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.recWhiteCard)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(40, 40, 40, 40)
        self.recAuthContent = QWidget(self.recWhiteCard)
        self.recAuthContent.setObjectName(u"recAuthContent")
        self.recAuthContent.setStyleSheet(u" QLineEdit {\n"
"	border: 1px solid #D9D9D9;\n"
"	border-radius: 5px\n"
" }")
        self.verticalLayout_49 = QVBoxLayout(self.recAuthContent)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.recAuthframe1 = QFrame(self.recAuthContent)
        self.recAuthframe1.setObjectName(u"recAuthframe1")
        self.recAuthframe1.setFrameShape(QFrame.StyledPanel)
        self.recAuthframe1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.recAuthframe1)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(38, -1, 31, -1)
        self.label_3 = QLabel(self.recAuthframe1)
        self.label_3.setObjectName(u"label_3")
        font19 = QFont()
        font19.setFamily(u"Open Sans")
        font19.setPointSize(25)
        font19.setBold(True)
        font19.setWeight(75)
        self.label_3.setFont(font19)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_3.setWordWrap(True)

        self.verticalLayout_50.addWidget(self.label_3)


        self.verticalLayout_49.addWidget(self.recAuthframe1)

        self.recAuthframe2 = QFrame(self.recAuthContent)
        self.recAuthframe2.setObjectName(u"recAuthframe2")
        self.recAuthframe2.setFrameShape(QFrame.StyledPanel)
        self.recAuthframe2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.recAuthframe2)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(9, 15, 25, -1)
        self.label_4 = QLabel(self.recAuthframe2)
        self.label_4.setObjectName(u"label_4")
        font20 = QFont()
        font20.setFamily(u"Open Sans")
        font20.setPointSize(16)
        self.label_4.setFont(font20)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_4.setWordWrap(True)

        self.horizontalLayout_59.addWidget(self.label_4)


        self.verticalLayout_49.addWidget(self.recAuthframe2)

        self.recAuthframe3 = QFrame(self.recAuthContent)
        self.recAuthframe3.setObjectName(u"recAuthframe3")
        self.recAuthframe3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.recAuthframe3.setFrameShape(QFrame.StyledPanel)
        self.recAuthframe3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.recAuthframe3)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(9, -1, -1, 0)
        self.recAuthCheckBox = QCheckBox(self.recAuthframe3)
        self.recAuthCheckBox.setObjectName(u"recAuthCheckBox")
        font21 = QFont()
        font21.setFamily(u"Open Sans SemiBold")
        font21.setPointSize(14)
        font21.setBold(False)
        font21.setWeight(50)
        self.recAuthCheckBox.setFont(font21)

        self.horizontalLayout_60.addWidget(self.recAuthCheckBox)


        self.verticalLayout_49.addWidget(self.recAuthframe3, 0, Qt.AlignHCenter)

        self.recAuthframe4 = QFrame(self.recAuthContent)
        self.recAuthframe4.setObjectName(u"recAuthframe4")
        self.recAuthframe4.setFont(font4)
        self.recAuthframe4.setFrameShape(QFrame.StyledPanel)
        self.recAuthframe4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.recAuthframe4)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(20, 0, 20, 0)
        self.recAuthPasswordLbl = QLabel(self.recAuthframe4)
        self.recAuthPasswordLbl.setObjectName(u"recAuthPasswordLbl")
        font22 = QFont()
        font22.setFamily(u"Open Sans SemiBold")
        font22.setPointSize(14)
        self.recAuthPasswordLbl.setFont(font22)
        self.recAuthPasswordLbl.setLayoutDirection(Qt.LeftToRight)
        self.recAuthPasswordLbl.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.recAuthPasswordLbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.recAuthPasswordLbl.setWordWrap(False)

        self.verticalLayout_62.addWidget(self.recAuthPasswordLbl)

        self.recAuthPasswordLineEdit = QLineEdit(self.recAuthframe4)
        self.recAuthPasswordLineEdit.setObjectName(u"recAuthPasswordLineEdit")
        self.recAuthPasswordLineEdit.setFont(font4)

        self.verticalLayout_62.addWidget(self.recAuthPasswordLineEdit, 0, Qt.AlignTop)


        self.verticalLayout_49.addWidget(self.recAuthframe4, 0, Qt.AlignVCenter)

        self.recAuthframe5 = QFrame(self.recAuthContent)
        self.recAuthframe5.setObjectName(u"recAuthframe5")
        self.recAuthframe5.setFrameShape(QFrame.StyledPanel)
        self.recAuthframe5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.recAuthframe5)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.recAuthSubmitBtn = QPushButton(self.recAuthframe5)
        self.recAuthSubmitBtn.setObjectName(u"recAuthSubmitBtn")
        self.recAuthSubmitBtn.setFont(font13)
        self.recAuthSubmitBtn.setStyleSheet(u"background-color:rgb(56, 166, 255);\n"
"padding: 3px 23px 3px 23px;\n"
"border-radius: 15px;\n"
"color: #fff;")

        self.horizontalLayout_61.addWidget(self.recAuthSubmitBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_49.addWidget(self.recAuthframe5)


        self.verticalLayout_14.addWidget(self.recAuthContent)


        self.horizontalLayout_10.addWidget(self.recWhiteCard)


        self.horizontalLayout_9.addWidget(self.recBlueCard)


        self.verticalLayout_6.addWidget(self.recordsCardsFrame)

        self.recordsStackedWidget.addWidget(self.recordsAuthPage)
        self.recordsSearchPage = QWidget()
        self.recordsSearchPage.setObjectName(u"recordsSearchPage")
        self.verticalLayout_7 = QVBoxLayout(self.recordsSearchPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.recSearchContent = QWidget(self.recordsSearchPage)
        self.recSearchContent.setObjectName(u"recSearchContent")
        sizePolicy1.setHeightForWidth(self.recSearchContent.sizePolicy().hasHeightForWidth())
        self.recSearchContent.setSizePolicy(sizePolicy1)
        self.horizontalLayout_62 = QHBoxLayout(self.recSearchContent)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.recExitBtn1Frame = QFrame(self.recSearchContent)
        self.recExitBtn1Frame.setObjectName(u"recExitBtn1Frame")
        self.recExitBtn1Frame.setFrameShape(QFrame.StyledPanel)
        self.recExitBtn1Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.recExitBtn1Frame)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(15, 20, 15, 0)
        self.recExitBtn1 = QPushButton(self.recExitBtn1Frame)
        self.recExitBtn1.setObjectName(u"recExitBtn1")
        self.recExitBtn1.setIcon(icon5)
        self.recExitBtn1.setIconSize(QSize(24, 24))

        self.horizontalLayout_63.addWidget(self.recExitBtn1, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_62.addWidget(self.recExitBtn1Frame)

        self.recSearchCards = QFrame(self.recSearchContent)
        self.recSearchCards.setObjectName(u"recSearchCards")
        sizePolicy2.setHeightForWidth(self.recSearchCards.sizePolicy().hasHeightForWidth())
        self.recSearchCards.setSizePolicy(sizePolicy2)
        self.recSearchCards.setStyleSheet(u"#recSearchBlueCard {\n"
"	border-radius: 20px;\n"
"}\n"
"#recSearchWhiteCard {\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.recSearchCards.setFrameShape(QFrame.StyledPanel)
        self.recSearchCards.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.recSearchCards)
        self.verticalLayout_63.setSpacing(9)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(15, 20, 60, 20)
        self.recSearchBlueCard = QFrame(self.recSearchCards)
        self.recSearchBlueCard.setObjectName(u"recSearchBlueCard")
        self.recSearchBlueCard.setStyleSheet(u"background-color: rgb(20, 113, 201);\n"
"background-color: rgb(88, 169, 235);\n"
"")
        self.recSearchBlueCard.setFrameShape(QFrame.StyledPanel)
        self.recSearchBlueCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.recSearchBlueCard)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(10, 0, 0, 0)
        self.recSearchWhiteCard = QFrame(self.recSearchBlueCard)
        self.recSearchWhiteCard.setObjectName(u"recSearchWhiteCard")
        self.recSearchWhiteCard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.recSearchWhiteCard.setFrameShape(QFrame.StyledPanel)
        self.recSearchWhiteCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.recSearchWhiteCard)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(30, 10, 30, 10)
        self.recSearchMainLabelContainer = QFrame(self.recSearchWhiteCard)
        self.recSearchMainLabelContainer.setObjectName(u"recSearchMainLabelContainer")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.recSearchMainLabelContainer.sizePolicy().hasHeightForWidth())
        self.recSearchMainLabelContainer.setSizePolicy(sizePolicy8)
        self.recSearchMainLabelContainer.setStyleSheet(u"")
        self.recSearchMainLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.recSearchMainLabelContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.recSearchMainLabelContainer)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.recSearchMainLabel = QLabel(self.recSearchMainLabelContainer)
        self.recSearchMainLabel.setObjectName(u"recSearchMainLabel")
        font23 = QFont()
        font23.setFamily(u"Raleway SemiBold")
        font23.setPointSize(23)
        font23.setBold(False)
        font23.setWeight(50)
        self.recSearchMainLabel.setFont(font23)
        self.recSearchMainLabel.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_64.addWidget(self.recSearchMainLabel, 0, Qt.AlignTop)


        self.verticalLayout_26.addWidget(self.recSearchMainLabelContainer)

        self.recSearchBarFrameContainer = QFrame(self.recSearchWhiteCard)
        self.recSearchBarFrameContainer.setObjectName(u"recSearchBarFrameContainer")
        self.recSearchBarFrameContainer.setFrameShape(QFrame.StyledPanel)
        self.recSearchBarFrameContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.recSearchBarFrameContainer)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(30, 0, 30, 0)
        self.recSearchBarFrame = QFrame(self.recSearchBarFrameContainer)
        self.recSearchBarFrame.setObjectName(u"recSearchBarFrame")
        self.recSearchBarFrame.setStyleSheet(u"\n"
"background-color: #FFF;\n"
"border-radius:5px;\n"
"border:1px solid rgb(0, 0, 0);\n"
"\n"
"\n"
"")
        self.recSearchBarFrame.setFrameShape(QFrame.StyledPanel)
        self.recSearchBarFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.recSearchBarFrame)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(15, 7, 7, 7)
        self.recSearchPushButton = QPushButton(self.recSearchBarFrame)
        self.recSearchPushButton.setObjectName(u"recSearchPushButton")
        self.recSearchPushButton.setStyleSheet(u"color: rgb(170, 170, 255);\n"
"background-color: #FFF;\n"
"border: 1px solid #FFF;")
        icon6 = QIcon()
        icon6.addFile(u":/black/svg/search-gray.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recSearchPushButton.setIcon(icon6)

        self.horizontalLayout_65.addWidget(self.recSearchPushButton)

        self.recSearchBar = QLineEdit(self.recSearchBarFrame)
        self.recSearchBar.setObjectName(u"recSearchBar")
        font24 = QFont()
        font24.setPointSize(12)
        self.recSearchBar.setFont(font24)
        self.recSearchBar.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: #FFF;\n"
"border: #FFF;\n"
"\n"
"")

        self.horizontalLayout_65.addWidget(self.recSearchBar)


        self.verticalLayout_65.addWidget(self.recSearchBarFrame)


        self.verticalLayout_26.addWidget(self.recSearchBarFrameContainer, 0, Qt.AlignTop)

        self.recSearchTableContainer = QFrame(self.recSearchWhiteCard)
        self.recSearchTableContainer.setObjectName(u"recSearchTableContainer")
        sizePolicy3.setHeightForWidth(self.recSearchTableContainer.sizePolicy().hasHeightForWidth())
        self.recSearchTableContainer.setSizePolicy(sizePolicy3)
        self.recSearchTableContainer.setFrameShape(QFrame.StyledPanel)
        self.recSearchTableContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.recSearchTableContainer)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.recSearchTableFrame = QFrame(self.recSearchTableContainer)
        self.recSearchTableFrame.setObjectName(u"recSearchTableFrame")
        self.recSearchTableFrame.setFrameShape(QFrame.StyledPanel)
        self.recSearchTableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.recSearchTableFrame)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.recSearchTable = QTableWidget(self.recSearchTableFrame)
        if (self.recSearchTable.columnCount() < 5):
            self.recSearchTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.recSearchTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.recSearchTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.recSearchTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.recSearchTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.recSearchTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.recSearchTable.rowCount() < 8):
            self.recSearchTable.setRowCount(8)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.recSearchTable.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.recSearchTable.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.recSearchTable.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.recSearchTable.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.recSearchTable.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.recSearchTable.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.recSearchTable.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.recSearchTable.setVerticalHeaderItem(7, __qtablewidgetitem12)
        self.recSearchTable.setObjectName(u"recSearchTable")
        sizePolicy2.setHeightForWidth(self.recSearchTable.sizePolicy().hasHeightForWidth())
        self.recSearchTable.setSizePolicy(sizePolicy2)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(255, 255, 255, 128))
        brush1.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.recSearchTable.setPalette(palette)
        self.recSearchTable.setStyleSheet(u"\n"
"QTableWidget {	\n"
"	padding: 0px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(20, 113, 201);\n"
"	border: 1px solid rgb(20, 113, 201);\n"
"}\n"
"QTableWidget::item{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QHeaderView::section{\n"
"	Background-color: rgb(20, 113, 201);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(20, 113, 201);\n"
"	background-color: rgb(20, 113, 201);\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.recSearchTable.setFrameShape(QFrame.NoFrame)
        self.recSearchTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.recSearchTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.recSearchTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.recSearchTable.setAlternatingRowColors(False)
        self.recSearchTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.recSearchTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.recSearchTable.setShowGrid(True)
        self.recSearchTable.setGridStyle(Qt.SolidLine)
        self.recSearchTable.setSortingEnabled(False)
        self.recSearchTable.horizontalHeader().setVisible(False)
        self.recSearchTable.horizontalHeader().setCascadingSectionResizes(True)
        self.recSearchTable.horizontalHeader().setDefaultSectionSize(180)
        self.recSearchTable.horizontalHeader().setHighlightSections(True)
        self.recSearchTable.horizontalHeader().setStretchLastSection(True)
        self.recSearchTable.verticalHeader().setVisible(False)
        self.recSearchTable.verticalHeader().setCascadingSectionResizes(False)
        self.recSearchTable.verticalHeader().setHighlightSections(False)
        self.recSearchTable.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_67.addWidget(self.recSearchTable)


        self.verticalLayout_66.addWidget(self.recSearchTableFrame)


        self.verticalLayout_26.addWidget(self.recSearchTableContainer)


        self.verticalLayout_64.addWidget(self.recSearchWhiteCard)


        self.verticalLayout_63.addWidget(self.recSearchBlueCard)


        self.horizontalLayout_62.addWidget(self.recSearchCards)


        self.verticalLayout_7.addWidget(self.recSearchContent)

        self.recordsStackedWidget.addWidget(self.recordsSearchPage)
        self.recordsDetailsPage = QWidget()
        self.recordsDetailsPage.setObjectName(u"recordsDetailsPage")
        self.verticalLayout_281 = QVBoxLayout(self.recordsDetailsPage)
        self.verticalLayout_281.setObjectName(u"verticalLayout_281")
        self.recDetailsContent = QWidget(self.recordsDetailsPage)
        self.recDetailsContent.setObjectName(u"recDetailsContent")
        sizePolicy1.setHeightForWidth(self.recDetailsContent.sizePolicy().hasHeightForWidth())
        self.recDetailsContent.setSizePolicy(sizePolicy1)
        self.horizontalLayout_66 = QHBoxLayout(self.recDetailsContent)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.recExitBtn2Frame = QFrame(self.recDetailsContent)
        self.recExitBtn2Frame.setObjectName(u"recExitBtn2Frame")
        self.recExitBtn2Frame.setFrameShape(QFrame.StyledPanel)
        self.recExitBtn2Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.recExitBtn2Frame)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(15, 20, 15, 0)
        self.recExitBtn2 = QPushButton(self.recExitBtn2Frame)
        self.recExitBtn2.setObjectName(u"recExitBtn2")
        self.recExitBtn2.setIcon(icon5)
        self.recExitBtn2.setIconSize(QSize(24, 24))

        self.horizontalLayout_73.addWidget(self.recExitBtn2, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_66.addWidget(self.recExitBtn2Frame)

        self.recDetailsCards = QFrame(self.recDetailsContent)
        self.recDetailsCards.setObjectName(u"recDetailsCards")
        sizePolicy2.setHeightForWidth(self.recDetailsCards.sizePolicy().hasHeightForWidth())
        self.recDetailsCards.setSizePolicy(sizePolicy2)
        self.recDetailsCards.setStyleSheet(u"#recDetailsBlueCard {\n"
"	border-radius: 20px;\n"
"}\n"
"#recDetailsWhiteCard {\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.recDetailsCards.setFrameShape(QFrame.StyledPanel)
        self.recDetailsCards.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.recDetailsCards)
        self.verticalLayout_68.setSpacing(9)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(15, 20, 60, 20)
        self.recDetailsBlueCard = QFrame(self.recDetailsCards)
        self.recDetailsBlueCard.setObjectName(u"recDetailsBlueCard")
        self.recDetailsBlueCard.setStyleSheet(u"background-color: rgb(20, 113, 201);\n"
"background-color: rgb(88, 169, 235);\n"
"")
        self.recDetailsBlueCard.setFrameShape(QFrame.StyledPanel)
        self.recDetailsBlueCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.recDetailsBlueCard)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(10, 0, 0, 0)
        self.recDetailsWhiteCard = QFrame(self.recDetailsBlueCard)
        self.recDetailsWhiteCard.setObjectName(u"recDetailsWhiteCard")
        self.recDetailsWhiteCard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.recDetailsWhiteCard.setFrameShape(QFrame.StyledPanel)
        self.recDetailsWhiteCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.recDetailsWhiteCard)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.recDetailsContentContainer = QWidget(self.recDetailsWhiteCard)
        self.recDetailsContentContainer.setObjectName(u"recDetailsContentContainer")
        self.recDetailsContentContainer.setStyleSheet(u"#recPatientDetailsOutlinedContainer, #recEmergencyOutlinedContainer, #recSymptomsOutlinedContainer{border: 1px solid gray;}\n"
"#recPatientDetailsOutlinedContainer, #recEmergencyOutlinedContainer, #recSymptomsOutlinedContainer{border-radius: 10px;}")
        self.verticalLayout_71 = QVBoxLayout(self.recDetailsContentContainer)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(20, 10, 20, 10)
        self.recDetailsLbl1Container = QFrame(self.recDetailsContentContainer)
        self.recDetailsLbl1Container.setObjectName(u"recDetailsLbl1Container")
        self.recDetailsLbl1Container.setFrameShape(QFrame.StyledPanel)
        self.recDetailsLbl1Container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.recDetailsLbl1Container)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.recDetailsLbl1 = QLabel(self.recDetailsLbl1Container)
        self.recDetailsLbl1.setObjectName(u"recDetailsLbl1")
        font25 = QFont()
        font25.setFamily(u"Raleway SemiBold")
        font25.setPointSize(20)
        font25.setBold(True)
        font25.setWeight(75)
        self.recDetailsLbl1.setFont(font25)
        self.recDetailsLbl1.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_74.addWidget(self.recDetailsLbl1)


        self.verticalLayout_71.addWidget(self.recDetailsLbl1Container, 0, Qt.AlignBottom)

        self.recPatientDetailsContentContainer_1 = QFrame(self.recDetailsContentContainer)
        self.recPatientDetailsContentContainer_1.setObjectName(u"recPatientDetailsContentContainer_1")
        sizePolicy2.setHeightForWidth(self.recPatientDetailsContentContainer_1.sizePolicy().hasHeightForWidth())
        self.recPatientDetailsContentContainer_1.setSizePolicy(sizePolicy2)
        self.recPatientDetailsContentContainer_1.setFont(font12)
        self.recPatientDetailsContentContainer_1.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.recPatientDetailsContentContainer_1.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsContentContainer_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.recPatientDetailsContentContainer_1)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsOutlinedContainer = QFrame(self.recPatientDetailsContentContainer_1)
        self.recPatientDetailsOutlinedContainer.setObjectName(u"recPatientDetailsOutlinedContainer")
        self.recPatientDetailsOutlinedContainer.setStyleSheet(u"")
        self.recPatientDetailsOutlinedContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsOutlinedContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_143 = QVBoxLayout(self.recPatientDetailsOutlinedContainer)
        self.verticalLayout_143.setSpacing(0)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.verticalLayout_143.setContentsMargins(20, 10, 20, 0)
        self.recPatientDetailsTopContainer = QFrame(self.recPatientDetailsOutlinedContainer)
        self.recPatientDetailsTopContainer.setObjectName(u"recPatientDetailsTopContainer")
        self.recPatientDetailsTopContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsTopContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_144 = QVBoxLayout(self.recPatientDetailsTopContainer)
        self.verticalLayout_144.setSpacing(0)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.verticalLayout_144.setContentsMargins(0, 0, 0, 15)
        self.recPatientDetailsNameHeadingContainer = QFrame(self.recPatientDetailsTopContainer)
        self.recPatientDetailsNameHeadingContainer.setObjectName(u"recPatientDetailsNameHeadingContainer")
        self.recPatientDetailsNameHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsNameHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_145 = QVBoxLayout(self.recPatientDetailsNameHeadingContainer)
        self.verticalLayout_145.setSpacing(0)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.verticalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsNameHeading = QLabel(self.recPatientDetailsNameHeadingContainer)
        self.recPatientDetailsNameHeading.setObjectName(u"recPatientDetailsNameHeading")
        self.recPatientDetailsNameHeading.setFont(font17)

        self.verticalLayout_145.addWidget(self.recPatientDetailsNameHeading, 0, Qt.AlignBottom)


        self.verticalLayout_144.addWidget(self.recPatientDetailsNameHeadingContainer)

        self.recPatientDetailsNameLabelContainer = QFrame(self.recPatientDetailsTopContainer)
        self.recPatientDetailsNameLabelContainer.setObjectName(u"recPatientDetailsNameLabelContainer")
        self.recPatientDetailsNameLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsNameLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_146 = QVBoxLayout(self.recPatientDetailsNameLabelContainer)
        self.verticalLayout_146.setSpacing(0)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.verticalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsNameLabel = QLabel(self.recPatientDetailsNameLabelContainer)
        self.recPatientDetailsNameLabel.setObjectName(u"recPatientDetailsNameLabel")
        self.recPatientDetailsNameLabel.setFont(font12)

        self.verticalLayout_146.addWidget(self.recPatientDetailsNameLabel, 0, Qt.AlignTop)


        self.verticalLayout_144.addWidget(self.recPatientDetailsNameLabelContainer)


        self.verticalLayout_143.addWidget(self.recPatientDetailsTopContainer)

        self.recPatientDetailsMidContainer = QFrame(self.recPatientDetailsOutlinedContainer)
        self.recPatientDetailsMidContainer.setObjectName(u"recPatientDetailsMidContainer")
        self.recPatientDetailsMidContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsMidContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.recPatientDetailsMidContainer)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 15)
        self.recPatientDetailsBirthdateContainer = QFrame(self.recPatientDetailsMidContainer)
        self.recPatientDetailsBirthdateContainer.setObjectName(u"recPatientDetailsBirthdateContainer")
        self.recPatientDetailsBirthdateContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsBirthdateContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_147 = QVBoxLayout(self.recPatientDetailsBirthdateContainer)
        self.verticalLayout_147.setSpacing(0)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.verticalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsBirthdateHeadingContainer = QFrame(self.recPatientDetailsBirthdateContainer)
        self.recPatientDetailsBirthdateHeadingContainer.setObjectName(u"recPatientDetailsBirthdateHeadingContainer")
        self.recPatientDetailsBirthdateHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsBirthdateHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_148 = QVBoxLayout(self.recPatientDetailsBirthdateHeadingContainer)
        self.verticalLayout_148.setSpacing(0)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.verticalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsBirthdateHeading = QLabel(self.recPatientDetailsBirthdateHeadingContainer)
        self.recPatientDetailsBirthdateHeading.setObjectName(u"recPatientDetailsBirthdateHeading")
        self.recPatientDetailsBirthdateHeading.setFont(font17)

        self.verticalLayout_148.addWidget(self.recPatientDetailsBirthdateHeading)


        self.verticalLayout_147.addWidget(self.recPatientDetailsBirthdateHeadingContainer)

        self.recPatientDetailsBirthdateLabelContainer = QFrame(self.recPatientDetailsBirthdateContainer)
        self.recPatientDetailsBirthdateLabelContainer.setObjectName(u"recPatientDetailsBirthdateLabelContainer")
        self.recPatientDetailsBirthdateLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsBirthdateLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_149 = QVBoxLayout(self.recPatientDetailsBirthdateLabelContainer)
        self.verticalLayout_149.setSpacing(0)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.verticalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsBirthdateLabel = QLabel(self.recPatientDetailsBirthdateLabelContainer)
        self.recPatientDetailsBirthdateLabel.setObjectName(u"recPatientDetailsBirthdateLabel")
        self.recPatientDetailsBirthdateLabel.setFont(font12)

        self.verticalLayout_149.addWidget(self.recPatientDetailsBirthdateLabel)


        self.verticalLayout_147.addWidget(self.recPatientDetailsBirthdateLabelContainer)


        self.horizontalLayout_75.addWidget(self.recPatientDetailsBirthdateContainer, 0, Qt.AlignLeft)

        self.recPatientDetailsAgeContainer = QFrame(self.recPatientDetailsMidContainer)
        self.recPatientDetailsAgeContainer.setObjectName(u"recPatientDetailsAgeContainer")
        self.recPatientDetailsAgeContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsAgeContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_150 = QVBoxLayout(self.recPatientDetailsAgeContainer)
        self.verticalLayout_150.setSpacing(0)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.verticalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsAgeHeadingContainer = QFrame(self.recPatientDetailsAgeContainer)
        self.recPatientDetailsAgeHeadingContainer.setObjectName(u"recPatientDetailsAgeHeadingContainer")
        self.recPatientDetailsAgeHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsAgeHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_151 = QVBoxLayout(self.recPatientDetailsAgeHeadingContainer)
        self.verticalLayout_151.setSpacing(0)
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")
        self.verticalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsAgeHeading = QLabel(self.recPatientDetailsAgeHeadingContainer)
        self.recPatientDetailsAgeHeading.setObjectName(u"recPatientDetailsAgeHeading")
        self.recPatientDetailsAgeHeading.setFont(font17)

        self.verticalLayout_151.addWidget(self.recPatientDetailsAgeHeading)


        self.verticalLayout_150.addWidget(self.recPatientDetailsAgeHeadingContainer)

        self.recPatientDetailsAgeLabelContainer = QFrame(self.recPatientDetailsAgeContainer)
        self.recPatientDetailsAgeLabelContainer.setObjectName(u"recPatientDetailsAgeLabelContainer")
        self.recPatientDetailsAgeLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsAgeLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_152 = QVBoxLayout(self.recPatientDetailsAgeLabelContainer)
        self.verticalLayout_152.setSpacing(0)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.verticalLayout_152.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsAgeLabel = QLabel(self.recPatientDetailsAgeLabelContainer)
        self.recPatientDetailsAgeLabel.setObjectName(u"recPatientDetailsAgeLabel")
        self.recPatientDetailsAgeLabel.setFont(font12)

        self.verticalLayout_152.addWidget(self.recPatientDetailsAgeLabel)


        self.verticalLayout_150.addWidget(self.recPatientDetailsAgeLabelContainer)


        self.horizontalLayout_75.addWidget(self.recPatientDetailsAgeContainer, 0, Qt.AlignHCenter)

        self.recPatientDetailsSexContainer = QFrame(self.recPatientDetailsMidContainer)
        self.recPatientDetailsSexContainer.setObjectName(u"recPatientDetailsSexContainer")
        self.recPatientDetailsSexContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsSexContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_153 = QVBoxLayout(self.recPatientDetailsSexContainer)
        self.verticalLayout_153.setSpacing(0)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.verticalLayout_153.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsSexHeadingContainer = QFrame(self.recPatientDetailsSexContainer)
        self.recPatientDetailsSexHeadingContainer.setObjectName(u"recPatientDetailsSexHeadingContainer")
        self.recPatientDetailsSexHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsSexHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_154 = QVBoxLayout(self.recPatientDetailsSexHeadingContainer)
        self.verticalLayout_154.setSpacing(0)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.verticalLayout_154.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsSexHeading = QLabel(self.recPatientDetailsSexHeadingContainer)
        self.recPatientDetailsSexHeading.setObjectName(u"recPatientDetailsSexHeading")
        self.recPatientDetailsSexHeading.setFont(font17)

        self.verticalLayout_154.addWidget(self.recPatientDetailsSexHeading)


        self.verticalLayout_153.addWidget(self.recPatientDetailsSexHeadingContainer)

        self.recPatientDetailsSexLabelContainer = QFrame(self.recPatientDetailsSexContainer)
        self.recPatientDetailsSexLabelContainer.setObjectName(u"recPatientDetailsSexLabelContainer")
        self.recPatientDetailsSexLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsSexLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.recPatientDetailsSexLabelContainer)
        self.verticalLayout_155.setSpacing(0)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.verticalLayout_155.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsSexLabel = QLabel(self.recPatientDetailsSexLabelContainer)
        self.recPatientDetailsSexLabel.setObjectName(u"recPatientDetailsSexLabel")
        self.recPatientDetailsSexLabel.setFont(font12)

        self.verticalLayout_155.addWidget(self.recPatientDetailsSexLabel)


        self.verticalLayout_153.addWidget(self.recPatientDetailsSexLabelContainer)


        self.horizontalLayout_75.addWidget(self.recPatientDetailsSexContainer, 0, Qt.AlignHCenter)

        self.recPatientDetailsCivilContainer = QFrame(self.recPatientDetailsMidContainer)
        self.recPatientDetailsCivilContainer.setObjectName(u"recPatientDetailsCivilContainer")
        self.recPatientDetailsCivilContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsCivilContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_217 = QVBoxLayout(self.recPatientDetailsCivilContainer)
        self.verticalLayout_217.setSpacing(0)
        self.verticalLayout_217.setObjectName(u"verticalLayout_217")
        self.verticalLayout_217.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsCivilHeadingContainer = QFrame(self.recPatientDetailsCivilContainer)
        self.recPatientDetailsCivilHeadingContainer.setObjectName(u"recPatientDetailsCivilHeadingContainer")
        self.recPatientDetailsCivilHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsCivilHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_218 = QVBoxLayout(self.recPatientDetailsCivilHeadingContainer)
        self.verticalLayout_218.setSpacing(0)
        self.verticalLayout_218.setObjectName(u"verticalLayout_218")
        self.verticalLayout_218.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsCivilHeading = QLabel(self.recPatientDetailsCivilHeadingContainer)
        self.recPatientDetailsCivilHeading.setObjectName(u"recPatientDetailsCivilHeading")
        self.recPatientDetailsCivilHeading.setFont(font17)

        self.verticalLayout_218.addWidget(self.recPatientDetailsCivilHeading)


        self.verticalLayout_217.addWidget(self.recPatientDetailsCivilHeadingContainer)

        self.recPatientDetailsCivilLabelContainer = QFrame(self.recPatientDetailsCivilContainer)
        self.recPatientDetailsCivilLabelContainer.setObjectName(u"recPatientDetailsCivilLabelContainer")
        self.recPatientDetailsCivilLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsCivilLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_219 = QVBoxLayout(self.recPatientDetailsCivilLabelContainer)
        self.verticalLayout_219.setSpacing(0)
        self.verticalLayout_219.setObjectName(u"verticalLayout_219")
        self.verticalLayout_219.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsCivilLabel = QLabel(self.recPatientDetailsCivilLabelContainer)
        self.recPatientDetailsCivilLabel.setObjectName(u"recPatientDetailsCivilLabel")
        self.recPatientDetailsCivilLabel.setFont(font12)

        self.verticalLayout_219.addWidget(self.recPatientDetailsCivilLabel)


        self.verticalLayout_217.addWidget(self.recPatientDetailsCivilLabelContainer)


        self.horizontalLayout_75.addWidget(self.recPatientDetailsCivilContainer, 0, Qt.AlignHCenter)

        self.recPatientDetailsContactContainer = QFrame(self.recPatientDetailsMidContainer)
        self.recPatientDetailsContactContainer.setObjectName(u"recPatientDetailsContactContainer")
        self.recPatientDetailsContactContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsContactContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_266 = QVBoxLayout(self.recPatientDetailsContactContainer)
        self.verticalLayout_266.setSpacing(0)
        self.verticalLayout_266.setObjectName(u"verticalLayout_266")
        self.verticalLayout_266.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsContactHeadingContainer = QFrame(self.recPatientDetailsContactContainer)
        self.recPatientDetailsContactHeadingContainer.setObjectName(u"recPatientDetailsContactHeadingContainer")
        self.recPatientDetailsContactHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsContactHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_267 = QVBoxLayout(self.recPatientDetailsContactHeadingContainer)
        self.verticalLayout_267.setSpacing(0)
        self.verticalLayout_267.setObjectName(u"verticalLayout_267")
        self.verticalLayout_267.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsContactHeading = QLabel(self.recPatientDetailsContactHeadingContainer)
        self.recPatientDetailsContactHeading.setObjectName(u"recPatientDetailsContactHeading")
        self.recPatientDetailsContactHeading.setFont(font17)

        self.verticalLayout_267.addWidget(self.recPatientDetailsContactHeading)


        self.verticalLayout_266.addWidget(self.recPatientDetailsContactHeadingContainer)

        self.recPatientDetailsContactLabelContainer = QFrame(self.recPatientDetailsContactContainer)
        self.recPatientDetailsContactLabelContainer.setObjectName(u"recPatientDetailsContactLabelContainer")
        self.recPatientDetailsContactLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsContactLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_268 = QVBoxLayout(self.recPatientDetailsContactLabelContainer)
        self.verticalLayout_268.setSpacing(0)
        self.verticalLayout_268.setObjectName(u"verticalLayout_268")
        self.verticalLayout_268.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsContactLabel = QLabel(self.recPatientDetailsContactLabelContainer)
        self.recPatientDetailsContactLabel.setObjectName(u"recPatientDetailsContactLabel")
        self.recPatientDetailsContactLabel.setFont(font12)

        self.verticalLayout_268.addWidget(self.recPatientDetailsContactLabel)


        self.verticalLayout_266.addWidget(self.recPatientDetailsContactLabelContainer)


        self.horizontalLayout_75.addWidget(self.recPatientDetailsContactContainer, 0, Qt.AlignRight)


        self.verticalLayout_143.addWidget(self.recPatientDetailsMidContainer)

        self.recPatientDetailsBottomContainer = QFrame(self.recPatientDetailsOutlinedContainer)
        self.recPatientDetailsBottomContainer.setObjectName(u"recPatientDetailsBottomContainer")
        self.recPatientDetailsBottomContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsBottomContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_269 = QVBoxLayout(self.recPatientDetailsBottomContainer)
        self.verticalLayout_269.setSpacing(0)
        self.verticalLayout_269.setObjectName(u"verticalLayout_269")
        self.verticalLayout_269.setContentsMargins(0, 0, 0, 15)
        self.recPatientDetailsAdressHeadingContainer = QFrame(self.recPatientDetailsBottomContainer)
        self.recPatientDetailsAdressHeadingContainer.setObjectName(u"recPatientDetailsAdressHeadingContainer")
        self.recPatientDetailsAdressHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsAdressHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_270 = QVBoxLayout(self.recPatientDetailsAdressHeadingContainer)
        self.verticalLayout_270.setSpacing(0)
        self.verticalLayout_270.setObjectName(u"verticalLayout_270")
        self.verticalLayout_270.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsAdressHeading = QLabel(self.recPatientDetailsAdressHeadingContainer)
        self.recPatientDetailsAdressHeading.setObjectName(u"recPatientDetailsAdressHeading")
        self.recPatientDetailsAdressHeading.setFont(font17)

        self.verticalLayout_270.addWidget(self.recPatientDetailsAdressHeading)


        self.verticalLayout_269.addWidget(self.recPatientDetailsAdressHeadingContainer, 0, Qt.AlignBottom)

        self.recPatientDetailsAdressLabelContainer = QFrame(self.recPatientDetailsBottomContainer)
        self.recPatientDetailsAdressLabelContainer.setObjectName(u"recPatientDetailsAdressLabelContainer")
        self.recPatientDetailsAdressLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.recPatientDetailsAdressLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_271 = QVBoxLayout(self.recPatientDetailsAdressLabelContainer)
        self.verticalLayout_271.setSpacing(9)
        self.verticalLayout_271.setObjectName(u"verticalLayout_271")
        self.verticalLayout_271.setContentsMargins(0, 0, 0, 0)
        self.recPatientDetailsAdressLabel = QLabel(self.recPatientDetailsAdressLabelContainer)
        self.recPatientDetailsAdressLabel.setObjectName(u"recPatientDetailsAdressLabel")

        self.verticalLayout_271.addWidget(self.recPatientDetailsAdressLabel, 0, Qt.AlignTop)


        self.verticalLayout_269.addWidget(self.recPatientDetailsAdressLabelContainer)


        self.verticalLayout_143.addWidget(self.recPatientDetailsBottomContainer)


        self.verticalLayout_72.addWidget(self.recPatientDetailsOutlinedContainer)


        self.verticalLayout_71.addWidget(self.recPatientDetailsContentContainer_1, 0, Qt.AlignTop)

        self.recDetailsLbl2Container = QFrame(self.recDetailsContentContainer)
        self.recDetailsLbl2Container.setObjectName(u"recDetailsLbl2Container")
        self.recDetailsLbl2Container.setFrameShape(QFrame.StyledPanel)
        self.recDetailsLbl2Container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.recDetailsLbl2Container)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.recDetailsLbl2 = QLabel(self.recDetailsLbl2Container)
        self.recDetailsLbl2.setObjectName(u"recDetailsLbl2")
        self.recDetailsLbl2.setFont(font25)
        self.recDetailsLbl2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_76.addWidget(self.recDetailsLbl2)


        self.verticalLayout_71.addWidget(self.recDetailsLbl2Container, 0, Qt.AlignTop)

        self.recEmergencyContentContainer = QFrame(self.recDetailsContentContainer)
        self.recEmergencyContentContainer.setObjectName(u"recEmergencyContentContainer")
        self.recEmergencyContentContainer.setFrameShape(QFrame.StyledPanel)
        self.recEmergencyContentContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.recEmergencyContentContainer)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.recEmergencyOutlinedContainer = QFrame(self.recEmergencyContentContainer)
        self.recEmergencyOutlinedContainer.setObjectName(u"recEmergencyOutlinedContainer")
        self.recEmergencyOutlinedContainer.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.recEmergencyOutlinedContainer.setFrameShape(QFrame.StyledPanel)
        self.recEmergencyOutlinedContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.recEmergencyOutlinedContainer)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(20, 10, 20, 10)
        self.recEmergencyNameContainer = QFrame(self.recEmergencyOutlinedContainer)
        self.recEmergencyNameContainer.setObjectName(u"recEmergencyNameContainer")
        self.recEmergencyNameContainer.setFrameShape(QFrame.StyledPanel)
        self.recEmergencyNameContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_272 = QVBoxLayout(self.recEmergencyNameContainer)
        self.verticalLayout_272.setSpacing(0)
        self.verticalLayout_272.setObjectName(u"verticalLayout_272")
        self.verticalLayout_272.setContentsMargins(0, 0, 0, 0)
        self.recEmergencyNameHeadingContainer = QFrame(self.recEmergencyNameContainer)
        self.recEmergencyNameHeadingContainer.setObjectName(u"recEmergencyNameHeadingContainer")
        self.recEmergencyNameHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.recEmergencyNameHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_273 = QVBoxLayout(self.recEmergencyNameHeadingContainer)
        self.verticalLayout_273.setSpacing(0)
        self.verticalLayout_273.setObjectName(u"verticalLayout_273")
        self.verticalLayout_273.setContentsMargins(0, 0, 0, 0)
        self.recEmergencyNameHeading = QLabel(self.recEmergencyNameHeadingContainer)
        self.recEmergencyNameHeading.setObjectName(u"recEmergencyNameHeading")
        self.recEmergencyNameHeading.setFont(font17)

        self.verticalLayout_273.addWidget(self.recEmergencyNameHeading, 0, Qt.AlignBottom)


        self.verticalLayout_272.addWidget(self.recEmergencyNameHeadingContainer, 0, Qt.AlignBottom)

        self.recEmergencyNameLabelContainer = QFrame(self.recEmergencyNameContainer)
        self.recEmergencyNameLabelContainer.setObjectName(u"recEmergencyNameLabelContainer")
        self.recEmergencyNameLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.recEmergencyNameLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_274 = QVBoxLayout(self.recEmergencyNameLabelContainer)
        self.verticalLayout_274.setSpacing(0)
        self.verticalLayout_274.setObjectName(u"verticalLayout_274")
        self.verticalLayout_274.setContentsMargins(0, 0, 0, 0)
        self.recEmergencyNameLabel = QLabel(self.recEmergencyNameLabelContainer)
        self.recEmergencyNameLabel.setObjectName(u"recEmergencyNameLabel")
        self.recEmergencyNameLabel.setFont(font12)

        self.verticalLayout_274.addWidget(self.recEmergencyNameLabel, 0, Qt.AlignTop)


        self.verticalLayout_272.addWidget(self.recEmergencyNameLabelContainer, 0, Qt.AlignTop)


        self.horizontalLayout_77.addWidget(self.recEmergencyNameContainer)

        self.recEmergencyRelationContainer = QFrame(self.recEmergencyOutlinedContainer)
        self.recEmergencyRelationContainer.setObjectName(u"recEmergencyRelationContainer")
        self.recEmergencyRelationContainer.setFrameShape(QFrame.StyledPanel)
        self.recEmergencyRelationContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_275 = QVBoxLayout(self.recEmergencyRelationContainer)
        self.verticalLayout_275.setSpacing(0)
        self.verticalLayout_275.setObjectName(u"verticalLayout_275")
        self.verticalLayout_275.setContentsMargins(0, 0, 0, 0)
        self.recEmergencyRelationHeadingContainer = QFrame(self.recEmergencyRelationContainer)
        self.recEmergencyRelationHeadingContainer.setObjectName(u"recEmergencyRelationHeadingContainer")
        self.recEmergencyRelationHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.recEmergencyRelationHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_276 = QVBoxLayout(self.recEmergencyRelationHeadingContainer)
        self.verticalLayout_276.setSpacing(0)
        self.verticalLayout_276.setObjectName(u"verticalLayout_276")
        self.verticalLayout_276.setContentsMargins(0, 0, 0, 0)
        self.recvEmergencyRelationHeading = QLabel(self.recEmergencyRelationHeadingContainer)
        self.recvEmergencyRelationHeading.setObjectName(u"recvEmergencyRelationHeading")
        self.recvEmergencyRelationHeading.setFont(font17)

        self.verticalLayout_276.addWidget(self.recvEmergencyRelationHeading, 0, Qt.AlignBottom)


        self.verticalLayout_275.addWidget(self.recEmergencyRelationHeadingContainer, 0, Qt.AlignBottom)

        self.recEmergencyRelationLabelContainer = QFrame(self.recEmergencyRelationContainer)
        self.recEmergencyRelationLabelContainer.setObjectName(u"recEmergencyRelationLabelContainer")
        self.recEmergencyRelationLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.recEmergencyRelationLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_277 = QVBoxLayout(self.recEmergencyRelationLabelContainer)
        self.verticalLayout_277.setSpacing(0)
        self.verticalLayout_277.setObjectName(u"verticalLayout_277")
        self.verticalLayout_277.setContentsMargins(0, 0, 0, 0)
        self.recEmergencyRelationLabel = QLabel(self.recEmergencyRelationLabelContainer)
        self.recEmergencyRelationLabel.setObjectName(u"recEmergencyRelationLabel")
        self.recEmergencyRelationLabel.setFont(font12)

        self.verticalLayout_277.addWidget(self.recEmergencyRelationLabel)


        self.verticalLayout_275.addWidget(self.recEmergencyRelationLabelContainer, 0, Qt.AlignTop)


        self.horizontalLayout_77.addWidget(self.recEmergencyRelationContainer)

        self.recEmergencyContactContainer = QFrame(self.recEmergencyOutlinedContainer)
        self.recEmergencyContactContainer.setObjectName(u"recEmergencyContactContainer")
        self.recEmergencyContactContainer.setFrameShape(QFrame.StyledPanel)
        self.recEmergencyContactContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_278 = QVBoxLayout(self.recEmergencyContactContainer)
        self.verticalLayout_278.setSpacing(0)
        self.verticalLayout_278.setObjectName(u"verticalLayout_278")
        self.verticalLayout_278.setContentsMargins(0, 0, 0, 0)
        self.recEmergencyContactHeadingContainer = QFrame(self.recEmergencyContactContainer)
        self.recEmergencyContactHeadingContainer.setObjectName(u"recEmergencyContactHeadingContainer")
        self.recEmergencyContactHeadingContainer.setFrameShape(QFrame.StyledPanel)
        self.recEmergencyContactHeadingContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_279 = QVBoxLayout(self.recEmergencyContactHeadingContainer)
        self.verticalLayout_279.setSpacing(0)
        self.verticalLayout_279.setObjectName(u"verticalLayout_279")
        self.verticalLayout_279.setContentsMargins(0, 0, 0, 0)
        self.recEmergencyContactHeading = QLabel(self.recEmergencyContactHeadingContainer)
        self.recEmergencyContactHeading.setObjectName(u"recEmergencyContactHeading")
        self.recEmergencyContactHeading.setFont(font17)

        self.verticalLayout_279.addWidget(self.recEmergencyContactHeading)


        self.verticalLayout_278.addWidget(self.recEmergencyContactHeadingContainer, 0, Qt.AlignBottom)

        self.recEmergencyContactLabelContainer = QFrame(self.recEmergencyContactContainer)
        self.recEmergencyContactLabelContainer.setObjectName(u"recEmergencyContactLabelContainer")
        self.recEmergencyContactLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.recEmergencyContactLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_280 = QVBoxLayout(self.recEmergencyContactLabelContainer)
        self.verticalLayout_280.setSpacing(0)
        self.verticalLayout_280.setObjectName(u"verticalLayout_280")
        self.verticalLayout_280.setContentsMargins(0, 0, 0, 0)
        self.recEmergencyContactLabel = QLabel(self.recEmergencyContactLabelContainer)
        self.recEmergencyContactLabel.setObjectName(u"recEmergencyContactLabel")
        self.recEmergencyContactLabel.setFont(font12)

        self.verticalLayout_280.addWidget(self.recEmergencyContactLabel)


        self.verticalLayout_278.addWidget(self.recEmergencyContactLabelContainer, 0, Qt.AlignTop)


        self.horizontalLayout_77.addWidget(self.recEmergencyContactContainer)


        self.verticalLayout_73.addWidget(self.recEmergencyOutlinedContainer)


        self.verticalLayout_71.addWidget(self.recEmergencyContentContainer)

        self.recDetailsLbl3Container = QFrame(self.recDetailsContentContainer)
        self.recDetailsLbl3Container.setObjectName(u"recDetailsLbl3Container")
        self.recDetailsLbl3Container.setFrameShape(QFrame.StyledPanel)
        self.recDetailsLbl3Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.recDetailsLbl3Container)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.recDetailsLbl3 = QLabel(self.recDetailsLbl3Container)
        self.recDetailsLbl3.setObjectName(u"recDetailsLbl3")
        self.recDetailsLbl3.setFont(font25)
        self.recDetailsLbl3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_74.addWidget(self.recDetailsLbl3)


        self.verticalLayout_71.addWidget(self.recDetailsLbl3Container)

        self.recTableWidgetContainer = QFrame(self.recDetailsContentContainer)
        self.recTableWidgetContainer.setObjectName(u"recTableWidgetContainer")
        self.recTableWidgetContainer.setFrameShape(QFrame.StyledPanel)
        self.recTableWidgetContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.recTableWidgetContainer)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.recTableWidget = QTableWidget(self.recTableWidgetContainer)
        if (self.recTableWidget.columnCount() < 4):
            self.recTableWidget.setColumnCount(4)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.recTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.recTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.recTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.recTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        if (self.recTableWidget.rowCount() < 37):
            self.recTableWidget.setRowCount(37)
        font26 = QFont()
        font26.setFamily(u"Segoe UI")
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font26);
        self.recTableWidget.setVerticalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(6, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(7, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(8, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(9, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(10, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(11, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(12, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(13, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(14, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(15, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(16, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(17, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(18, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(19, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(20, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(21, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(22, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(23, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(24, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(25, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(26, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(27, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(28, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(29, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(30, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(31, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(32, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(33, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(34, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(35, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.recTableWidget.setVerticalHeaderItem(36, __qtablewidgetitem53)
        font27 = QFont()
        font27.setBold(False)
        font27.setWeight(50)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setFont(font27);
        self.recTableWidget.setItem(0, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.recTableWidget.setItem(0, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.recTableWidget.setItem(0, 2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.recTableWidget.setItem(0, 3, __qtablewidgetitem57)
        self.recTableWidget.setObjectName(u"recTableWidget")
        sizePolicy2.setHeightForWidth(self.recTableWidget.sizePolicy().hasHeightForWidth())
        self.recTableWidget.setSizePolicy(sizePolicy2)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush5 = QBrush(QColor(255, 255, 255, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush6 = QBrush(QColor(255, 255, 255, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.recTableWidget.setPalette(palette1)
        self.recTableWidget.setStyleSheet(u"\n"
"QTableWidget {	\n"
"	padding: 0px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(20, 113, 201);\n"
"	border: 1px solid rgb(20, 113, 201);\n"
"}\n"
"QTableWidget::item{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QHeaderView::section{\n"
"	Background-color: rgb(20, 113, 201);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(20, 113, 201);\n"
"	background-color: rgb(20, 113, 201);\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.recTableWidget.setFrameShape(QFrame.NoFrame)
        self.recTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.recTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.recTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.recTableWidget.setAlternatingRowColors(False)
        self.recTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.recTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.recTableWidget.setShowGrid(True)
        self.recTableWidget.setGridStyle(Qt.SolidLine)
        self.recTableWidget.setSortingEnabled(False)
        self.recTableWidget.horizontalHeader().setVisible(False)
        self.recTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.recTableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.recTableWidget.horizontalHeader().setHighlightSections(True)
        self.recTableWidget.horizontalHeader().setStretchLastSection(True)
        self.recTableWidget.verticalHeader().setVisible(False)
        self.recTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.recTableWidget.verticalHeader().setHighlightSections(False)
        self.recTableWidget.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_75.addWidget(self.recTableWidget)


        self.verticalLayout_71.addWidget(self.recTableWidgetContainer)


        self.verticalLayout_70.addWidget(self.recDetailsContentContainer)


        self.verticalLayout_69.addWidget(self.recDetailsWhiteCard)


        self.verticalLayout_68.addWidget(self.recDetailsBlueCard)


        self.horizontalLayout_66.addWidget(self.recDetailsCards)


        self.verticalLayout_281.addWidget(self.recDetailsContent)

        self.recordsStackedWidget.addWidget(self.recordsDetailsPage)

        self.verticalLayout_8.addWidget(self.recordsStackedWidget)

        self.mainPages.addWidget(self.recordsPages)
        self.summaryPages = QWidget()
        self.summaryPages.setObjectName(u"summaryPages")
        self.verticalLayout_9 = QVBoxLayout(self.summaryPages)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.summaryStackedWidget = QStackedWidget(self.summaryPages)
        self.summaryStackedWidget.setObjectName(u"summaryStackedWidget")
        self.summaryAuthPage = QWidget()
        self.summaryAuthPage.setObjectName(u"summaryAuthPage")
        self.verticalLayout_287 = QVBoxLayout(self.summaryAuthPage)
        self.verticalLayout_287.setObjectName(u"verticalLayout_287")
        self.verticalLayout_287.setContentsMargins(50, 40, 50, 40)
        self.sumCardsFrame = QWidget(self.summaryAuthPage)
        self.sumCardsFrame.setObjectName(u"sumCardsFrame")
        self.horizontalLayout_11 = QHBoxLayout(self.sumCardsFrame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.sumAuthBlueCard = QFrame(self.sumCardsFrame)
        self.sumAuthBlueCard.setObjectName(u"sumAuthBlueCard")
        self.sumAuthBlueCard.setStyleSheet(u"background-color: rgb(189, 223, 255);")
        self.sumAuthBlueCard.setFrameShape(QFrame.StyledPanel)
        self.sumAuthBlueCard.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.sumAuthBlueCard)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.sumImageContainer = QWidget(self.sumAuthBlueCard)
        self.sumImageContainer.setObjectName(u"sumImageContainer")
        self.sumImageContainer.setStyleSheet(u"")
        self.verticalLayout_282 = QVBoxLayout(self.sumImageContainer)
        self.verticalLayout_282.setSpacing(0)
        self.verticalLayout_282.setObjectName(u"verticalLayout_282")
        self.verticalLayout_282.setContentsMargins(0, 0, 0, 0)
        self.sumImage = QLabel(self.sumImageContainer)
        self.sumImage.setObjectName(u"sumImage")
        self.sumImage.setStyleSheet(u"")
        self.sumImage.setPixmap(QPixmap(u":/images/images/recordsPicture.png"))
        self.sumImage.setScaledContents(True)
        self.sumImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_282.addWidget(self.sumImage)


        self.horizontalLayout_12.addWidget(self.sumImageContainer)

        self.sumAuthWhiteCard = QFrame(self.sumAuthBlueCard)
        self.sumAuthWhiteCard.setObjectName(u"sumAuthWhiteCard")
        self.sumAuthWhiteCard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sumAuthWhiteCard.setFrameShape(QFrame.StyledPanel)
        self.sumAuthWhiteCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_283 = QVBoxLayout(self.sumAuthWhiteCard)
        self.verticalLayout_283.setSpacing(5)
        self.verticalLayout_283.setObjectName(u"verticalLayout_283")
        self.verticalLayout_283.setContentsMargins(40, 40, 40, 40)
        self.sumAuthContent = QWidget(self.sumAuthWhiteCard)
        self.sumAuthContent.setObjectName(u"sumAuthContent")
        self.sumAuthContent.setStyleSheet(u" QLineEdit {\n"
"	border: 1px solid #D9D9D9;\n"
"	border-radius: 5px\n"
" }")
        self.verticalLayout_284 = QVBoxLayout(self.sumAuthContent)
        self.verticalLayout_284.setObjectName(u"verticalLayout_284")
        self.sumAuthframe1 = QFrame(self.sumAuthContent)
        self.sumAuthframe1.setObjectName(u"sumAuthframe1")
        self.sumAuthframe1.setFrameShape(QFrame.StyledPanel)
        self.sumAuthframe1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_285 = QVBoxLayout(self.sumAuthframe1)
        self.verticalLayout_285.setObjectName(u"verticalLayout_285")
        self.verticalLayout_285.setContentsMargins(38, -1, 31, -1)
        self.label_5 = QLabel(self.sumAuthframe1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font19)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_5.setWordWrap(True)

        self.verticalLayout_285.addWidget(self.label_5)


        self.verticalLayout_284.addWidget(self.sumAuthframe1)

        self.sumAuthframe2 = QFrame(self.sumAuthContent)
        self.sumAuthframe2.setObjectName(u"sumAuthframe2")
        self.sumAuthframe2.setFrameShape(QFrame.StyledPanel)
        self.sumAuthframe2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.sumAuthframe2)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(9, 15, 25, -1)
        self.label_6 = QLabel(self.sumAuthframe2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font20)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_6.setWordWrap(True)

        self.horizontalLayout_78.addWidget(self.label_6)


        self.verticalLayout_284.addWidget(self.sumAuthframe2)

        self.sumAuthframe3 = QFrame(self.sumAuthContent)
        self.sumAuthframe3.setObjectName(u"sumAuthframe3")
        self.sumAuthframe3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.sumAuthframe3.setFrameShape(QFrame.StyledPanel)
        self.sumAuthframe3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.sumAuthframe3)
        self.horizontalLayout_79.setSpacing(0)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(9, -1, -1, 0)
        self.sumAuthCheckBox = QCheckBox(self.sumAuthframe3)
        self.sumAuthCheckBox.setObjectName(u"sumAuthCheckBox")
        self.sumAuthCheckBox.setFont(font21)

        self.horizontalLayout_79.addWidget(self.sumAuthCheckBox)


        self.verticalLayout_284.addWidget(self.sumAuthframe3, 0, Qt.AlignHCenter)

        self.sumAuthframe4 = QFrame(self.sumAuthContent)
        self.sumAuthframe4.setObjectName(u"sumAuthframe4")
        self.sumAuthframe4.setFont(font4)
        self.sumAuthframe4.setFrameShape(QFrame.StyledPanel)
        self.sumAuthframe4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_286 = QVBoxLayout(self.sumAuthframe4)
        self.verticalLayout_286.setSpacing(0)
        self.verticalLayout_286.setObjectName(u"verticalLayout_286")
        self.verticalLayout_286.setContentsMargins(20, 0, 20, 0)
        self.sumAuthPasswordLbl = QLabel(self.sumAuthframe4)
        self.sumAuthPasswordLbl.setObjectName(u"sumAuthPasswordLbl")
        self.sumAuthPasswordLbl.setFont(font22)
        self.sumAuthPasswordLbl.setLayoutDirection(Qt.LeftToRight)
        self.sumAuthPasswordLbl.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.sumAuthPasswordLbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.sumAuthPasswordLbl.setWordWrap(False)

        self.verticalLayout_286.addWidget(self.sumAuthPasswordLbl)

        self.sumAuthPasswordLineEdit = QLineEdit(self.sumAuthframe4)
        self.sumAuthPasswordLineEdit.setObjectName(u"sumAuthPasswordLineEdit")
        self.sumAuthPasswordLineEdit.setFont(font4)

        self.verticalLayout_286.addWidget(self.sumAuthPasswordLineEdit, 0, Qt.AlignTop)


        self.verticalLayout_284.addWidget(self.sumAuthframe4, 0, Qt.AlignVCenter)

        self.sumAuthframe5 = QFrame(self.sumAuthContent)
        self.sumAuthframe5.setObjectName(u"sumAuthframe5")
        self.sumAuthframe5.setFrameShape(QFrame.StyledPanel)
        self.sumAuthframe5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.sumAuthframe5)
        self.horizontalLayout_80.setSpacing(0)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.sumAuthSubmitBtn = QPushButton(self.sumAuthframe5)
        self.sumAuthSubmitBtn.setObjectName(u"sumAuthSubmitBtn")
        self.sumAuthSubmitBtn.setFont(font13)
        self.sumAuthSubmitBtn.setStyleSheet(u"background-color:rgb(56, 166, 255);\n"
"padding: 3px 23px 3px 23px;\n"
"border-radius: 15px;\n"
"color: #fff;")

        self.horizontalLayout_80.addWidget(self.sumAuthSubmitBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_284.addWidget(self.sumAuthframe5)


        self.verticalLayout_283.addWidget(self.sumAuthContent)


        self.horizontalLayout_12.addWidget(self.sumAuthWhiteCard)


        self.horizontalLayout_11.addWidget(self.sumAuthBlueCard)


        self.verticalLayout_287.addWidget(self.sumCardsFrame)

        self.summaryStackedWidget.addWidget(self.summaryAuthPage)
        self.summaryMainPage = QWidget()
        self.summaryMainPage.setObjectName(u"summaryMainPage")
        self.verticalLayout_298 = QVBoxLayout(self.summaryMainPage)
        self.verticalLayout_298.setObjectName(u"verticalLayout_298")
        self.sumMainContent = QWidget(self.summaryMainPage)
        self.sumMainContent.setObjectName(u"sumMainContent")
        sizePolicy1.setHeightForWidth(self.sumMainContent.sizePolicy().hasHeightForWidth())
        self.sumMainContent.setSizePolicy(sizePolicy1)
        self.horizontalLayout_81 = QHBoxLayout(self.sumMainContent)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.sumMainExitBtnFrame = QFrame(self.sumMainContent)
        self.sumMainExitBtnFrame.setObjectName(u"sumMainExitBtnFrame")
        self.sumMainExitBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.sumMainExitBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.sumMainExitBtnFrame)
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(15, 20, 15, 0)
        self.sumMainExitBtn = QPushButton(self.sumMainExitBtnFrame)
        self.sumMainExitBtn.setObjectName(u"sumMainExitBtn")
        self.sumMainExitBtn.setIcon(icon5)
        self.sumMainExitBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_82.addWidget(self.sumMainExitBtn, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_81.addWidget(self.sumMainExitBtnFrame)

        self.sumMainCards = QFrame(self.sumMainContent)
        self.sumMainCards.setObjectName(u"sumMainCards")
        sizePolicy2.setHeightForWidth(self.sumMainCards.sizePolicy().hasHeightForWidth())
        self.sumMainCards.setSizePolicy(sizePolicy2)
        self.sumMainCards.setStyleSheet(u"#sumMainBlueCard {\n"
"	border-radius: 20px;\n"
"}\n"
"#sumMainWhiteCard {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.sumMainCards.setFrameShape(QFrame.StyledPanel)
        self.sumMainCards.setFrameShadow(QFrame.Raised)
        self.verticalLayout_288 = QVBoxLayout(self.sumMainCards)
        self.verticalLayout_288.setSpacing(9)
        self.verticalLayout_288.setObjectName(u"verticalLayout_288")
        self.verticalLayout_288.setContentsMargins(15, 20, 60, 20)
        self.sumMainBlueCard = QFrame(self.sumMainCards)
        self.sumMainBlueCard.setObjectName(u"sumMainBlueCard")
        self.sumMainBlueCard.setStyleSheet(u"background-color: rgb(20, 113, 201);\n"
"background-color: rgb(88, 169, 235);\n"
"")
        self.sumMainBlueCard.setFrameShape(QFrame.StyledPanel)
        self.sumMainBlueCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_289 = QVBoxLayout(self.sumMainBlueCard)
        self.verticalLayout_289.setObjectName(u"verticalLayout_289")
        self.verticalLayout_289.setContentsMargins(10, 0, 0, 0)
        self.sumMainWhiteCard = QFrame(self.sumMainBlueCard)
        self.sumMainWhiteCard.setObjectName(u"sumMainWhiteCard")
        self.sumMainWhiteCard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sumMainWhiteCard.setFrameShape(QFrame.StyledPanel)
        self.sumMainWhiteCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_290 = QVBoxLayout(self.sumMainWhiteCard)
        self.verticalLayout_290.setObjectName(u"verticalLayout_290")
        self.sumMainContainer = QWidget(self.sumMainWhiteCard)
        self.sumMainContainer.setObjectName(u"sumMainContainer")
        self.sumMainContainer.setStyleSheet(u"#sumMainTotalDiagnosisContainer, #sumMainTotalPatientsContainer {border: 1px solid gray;}\n"
"#sumMainTotalDiagnosisContainer, #sumMainTotalPatientsContainer{border-radius: 10px;}")
        self.verticalLayout_291 = QVBoxLayout(self.sumMainContainer)
        self.verticalLayout_291.setObjectName(u"verticalLayout_291")
        self.sumMainTopContainer = QFrame(self.sumMainContainer)
        self.sumMainTopContainer.setObjectName(u"sumMainTopContainer")
        self.sumMainTopContainer.setFrameShape(QFrame.StyledPanel)
        self.sumMainTopContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.sumMainTopContainer)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.sumMainLabelContainer = QFrame(self.sumMainTopContainer)
        self.sumMainLabelContainer.setObjectName(u"sumMainLabelContainer")
        self.sumMainLabelContainer.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.sumMainLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.sumMainLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_292 = QVBoxLayout(self.sumMainLabelContainer)
        self.verticalLayout_292.setObjectName(u"verticalLayout_292")
        self.sumMainLabel1 = QLabel(self.sumMainLabelContainer)
        self.sumMainLabel1.setObjectName(u"sumMainLabel1")
        font28 = QFont()
        font28.setFamily(u"Raleway SemiBold")
        font28.setPointSize(30)
        self.sumMainLabel1.setFont(font28)

        self.verticalLayout_292.addWidget(self.sumMainLabel1)

        self.sumMainLabel2 = QLabel(self.sumMainLabelContainer)
        self.sumMainLabel2.setObjectName(u"sumMainLabel2")
        font29 = QFont()
        font29.setFamily(u"Raleway SemiBold")
        font29.setPointSize(20)
        self.sumMainLabel2.setFont(font29)

        self.verticalLayout_292.addWidget(self.sumMainLabel2)


        self.horizontalLayout_83.addWidget(self.sumMainLabelContainer, 0, Qt.AlignTop)

        self.sumMainGraph1Container = QFrame(self.sumMainTopContainer)
        self.sumMainGraph1Container.setObjectName(u"sumMainGraph1Container")
        self.sumMainGraph1Container.setFrameShape(QFrame.StyledPanel)
        self.sumMainGraph1Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_293 = QVBoxLayout(self.sumMainGraph1Container)
        self.verticalLayout_293.setObjectName(u"verticalLayout_293")
        self.sumMainGraph1 = QLabel(self.sumMainGraph1Container)
        self.sumMainGraph1.setObjectName(u"sumMainGraph1")
        self.sumMainGraph1.setPixmap(QPixmap(u":/progressBarImages/images/graph1.png"))

        self.verticalLayout_293.addWidget(self.sumMainGraph1, 0, Qt.AlignHCenter)


        self.horizontalLayout_83.addWidget(self.sumMainGraph1Container, 0, Qt.AlignHCenter)

        self.sumMainGraph3Container = QFrame(self.sumMainTopContainer)
        self.sumMainGraph3Container.setObjectName(u"sumMainGraph3Container")
        self.sumMainGraph3Container.setFrameShape(QFrame.StyledPanel)
        self.sumMainGraph3Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_294 = QVBoxLayout(self.sumMainGraph3Container)
        self.verticalLayout_294.setObjectName(u"verticalLayout_294")
        self.sumMainGraph3 = QLabel(self.sumMainGraph3Container)
        self.sumMainGraph3.setObjectName(u"sumMainGraph3")
        self.sumMainGraph3.setPixmap(QPixmap(u":/progressBarImages/images/graph2.png"))

        self.verticalLayout_294.addWidget(self.sumMainGraph3, 0, Qt.AlignHCenter)


        self.horizontalLayout_83.addWidget(self.sumMainGraph3Container, 0, Qt.AlignHCenter)

        self.sumMainGraph2Container = QFrame(self.sumMainTopContainer)
        self.sumMainGraph2Container.setObjectName(u"sumMainGraph2Container")
        self.sumMainGraph2Container.setFrameShape(QFrame.StyledPanel)
        self.sumMainGraph2Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_295 = QVBoxLayout(self.sumMainGraph2Container)
        self.verticalLayout_295.setObjectName(u"verticalLayout_295")
        self.sumMainGraph2 = QLabel(self.sumMainGraph2Container)
        self.sumMainGraph2.setObjectName(u"sumMainGraph2")
        self.sumMainGraph2.setPixmap(QPixmap(u":/progressBarImages/images/graph3.png"))

        self.verticalLayout_295.addWidget(self.sumMainGraph2, 0, Qt.AlignHCenter)


        self.horizontalLayout_83.addWidget(self.sumMainGraph2Container, 0, Qt.AlignHCenter)


        self.verticalLayout_291.addWidget(self.sumMainTopContainer)

        self.sumMainTotalContainer = QFrame(self.sumMainContainer)
        self.sumMainTotalContainer.setObjectName(u"sumMainTotalContainer")
        self.sumMainTotalContainer.setFrameShape(QFrame.StyledPanel)
        self.sumMainTotalContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.sumMainTotalContainer)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.sumMainTotalDiagnosisContainer = QFrame(self.sumMainTotalContainer)
        self.sumMainTotalDiagnosisContainer.setObjectName(u"sumMainTotalDiagnosisContainer")
        self.sumMainTotalDiagnosisContainer.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.sumMainTotalDiagnosisContainer.setFrameShape(QFrame.StyledPanel)
        self.sumMainTotalDiagnosisContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.sumMainTotalDiagnosisContainer)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.sumMainTotalDiagnosis1 = QLabel(self.sumMainTotalDiagnosisContainer)
        self.sumMainTotalDiagnosis1.setObjectName(u"sumMainTotalDiagnosis1")
        font30 = QFont()
        font30.setFamily(u"Open Sans")
        font30.setPointSize(38)
        self.sumMainTotalDiagnosis1.setFont(font30)

        self.horizontalLayout_85.addWidget(self.sumMainTotalDiagnosis1, 0, Qt.AlignHCenter)

        self.sumMainTotalDiagnosis2 = QLabel(self.sumMainTotalDiagnosisContainer)
        self.sumMainTotalDiagnosis2.setObjectName(u"sumMainTotalDiagnosis2")
        self.sumMainTotalDiagnosis2.setFont(font20)

        self.horizontalLayout_85.addWidget(self.sumMainTotalDiagnosis2, 0, Qt.AlignHCenter)


        self.horizontalLayout_84.addWidget(self.sumMainTotalDiagnosisContainer, 0, Qt.AlignTop)

        self.sumMainTotalPatientsContainer = QFrame(self.sumMainTotalContainer)
        self.sumMainTotalPatientsContainer.setObjectName(u"sumMainTotalPatientsContainer")
        self.sumMainTotalPatientsContainer.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.sumMainTotalPatientsContainer.setFrameShape(QFrame.StyledPanel)
        self.sumMainTotalPatientsContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.sumMainTotalPatientsContainer)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.sumMainTotalPatients1 = QLabel(self.sumMainTotalPatientsContainer)
        self.sumMainTotalPatients1.setObjectName(u"sumMainTotalPatients1")
        self.sumMainTotalPatients1.setFont(font30)

        self.horizontalLayout_86.addWidget(self.sumMainTotalPatients1, 0, Qt.AlignHCenter)

        self.sumMainTotalPatients2 = QLabel(self.sumMainTotalPatientsContainer)
        self.sumMainTotalPatients2.setObjectName(u"sumMainTotalPatients2")
        self.sumMainTotalPatients2.setFont(font20)

        self.horizontalLayout_86.addWidget(self.sumMainTotalPatients2, 0, Qt.AlignHCenter)


        self.horizontalLayout_84.addWidget(self.sumMainTotalPatientsContainer, 0, Qt.AlignTop)


        self.verticalLayout_291.addWidget(self.sumMainTotalContainer)

        self.sumMainBottomContainer = QFrame(self.sumMainContainer)
        self.sumMainBottomContainer.setObjectName(u"sumMainBottomContainer")
        self.sumMainBottomContainer.setFrameShape(QFrame.StyledPanel)
        self.sumMainBottomContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.sumMainBottomContainer)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.sumMainTableWidgetContainer = QFrame(self.sumMainBottomContainer)
        self.sumMainTableWidgetContainer.setObjectName(u"sumMainTableWidgetContainer")
        self.sumMainTableWidgetContainer.setFrameShape(QFrame.StyledPanel)
        self.sumMainTableWidgetContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_296 = QVBoxLayout(self.sumMainTableWidgetContainer)
        self.verticalLayout_296.setObjectName(u"verticalLayout_296")
        self.verticalLayout_296.setContentsMargins(-1, 30, -1, 30)
        self.sumMainTableWidget = QTableWidget(self.sumMainTableWidgetContainer)
        if (self.sumMainTableWidget.columnCount() < 2):
            self.sumMainTableWidget.setColumnCount(2)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.sumMainTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.sumMainTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem59)
        if (self.sumMainTableWidget.rowCount() < 9):
            self.sumMainTableWidget.setRowCount(9)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setFont(font26);
        self.sumMainTableWidget.setVerticalHeaderItem(0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.sumMainTableWidget.setVerticalHeaderItem(1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.sumMainTableWidget.setVerticalHeaderItem(2, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.sumMainTableWidget.setVerticalHeaderItem(3, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.sumMainTableWidget.setVerticalHeaderItem(4, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.sumMainTableWidget.setVerticalHeaderItem(5, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.sumMainTableWidget.setVerticalHeaderItem(6, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.sumMainTableWidget.setVerticalHeaderItem(7, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.sumMainTableWidget.setVerticalHeaderItem(8, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.sumMainTableWidget.setItem(0, 0, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.sumMainTableWidget.setItem(0, 1, __qtablewidgetitem70)
        self.sumMainTableWidget.setObjectName(u"sumMainTableWidget")
        sizePolicy2.setHeightForWidth(self.sumMainTableWidget.sizePolicy().hasHeightForWidth())
        self.sumMainTableWidget.setSizePolicy(sizePolicy2)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        brush7 = QBrush(QColor(255, 255, 255, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush8 = QBrush(QColor(255, 255, 255, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.sumMainTableWidget.setPalette(palette2)
        self.sumMainTableWidget.setStyleSheet(u"\n"
"QTableWidget {	\n"
"	padding: 0px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(20, 113, 201);\n"
"	border: 1px solid rgb(20, 113, 201);\n"
"}\n"
"QTableWidget::item{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QHeaderView::section{\n"
"	Background-color: rgb(20, 113, 201);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(20, 113, 201);\n"
"	background-color: rgb(20, 113, 201);\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.sumMainTableWidget.setFrameShape(QFrame.NoFrame)
        self.sumMainTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.sumMainTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.sumMainTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sumMainTableWidget.setAlternatingRowColors(False)
        self.sumMainTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.sumMainTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.sumMainTableWidget.setShowGrid(True)
        self.sumMainTableWidget.setGridStyle(Qt.SolidLine)
        self.sumMainTableWidget.setSortingEnabled(False)
        self.sumMainTableWidget.horizontalHeader().setVisible(False)
        self.sumMainTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.sumMainTableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.sumMainTableWidget.horizontalHeader().setHighlightSections(True)
        self.sumMainTableWidget.horizontalHeader().setStretchLastSection(True)
        self.sumMainTableWidget.verticalHeader().setVisible(False)
        self.sumMainTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.sumMainTableWidget.verticalHeader().setHighlightSections(False)
        self.sumMainTableWidget.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_296.addWidget(self.sumMainTableWidget)


        self.horizontalLayout_87.addWidget(self.sumMainTableWidgetContainer)

        self.sumMainGraph4Container = QFrame(self.sumMainBottomContainer)
        self.sumMainGraph4Container.setObjectName(u"sumMainGraph4Container")
        self.sumMainGraph4Container.setFrameShape(QFrame.StyledPanel)
        self.sumMainGraph4Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_297 = QVBoxLayout(self.sumMainGraph4Container)
        self.verticalLayout_297.setObjectName(u"verticalLayout_297")
        self.verticalLayout_297.setContentsMargins(50, -1, 50, -1)

        self.horizontalLayout_87.addWidget(self.sumMainGraph4Container, 0, Qt.AlignHCenter)


        self.verticalLayout_291.addWidget(self.sumMainBottomContainer)


        self.verticalLayout_290.addWidget(self.sumMainContainer)


        self.verticalLayout_289.addWidget(self.sumMainWhiteCard)


        self.verticalLayout_288.addWidget(self.sumMainBlueCard)


        self.horizontalLayout_81.addWidget(self.sumMainCards)


        self.verticalLayout_298.addWidget(self.sumMainContent)

        self.summaryStackedWidget.addWidget(self.summaryMainPage)

        self.verticalLayout_9.addWidget(self.summaryStackedWidget)

        self.mainPages.addWidget(self.summaryPages)

        self.horizontalLayout_2.addWidget(self.mainPages)


        self.verticalLayout_5.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.mainMenuContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.labelAchi.setText(QCoreApplication.translate("MainWindow", u"ACHi  ", None))
#if QT_CONFIG(tooltip)
        self.leftMenuBtnContainer.setToolTip(QCoreApplication.translate("MainWindow", u"go to Diagnosis", None))
#endif // QT_CONFIG(tooltip)
        self.leftMenuDiagnosisBtn.setText(QCoreApplication.translate("MainWindow", u"Diagnosis    ", None))
#if QT_CONFIG(tooltip)
        self.leftMenuRecordsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"go to Records", None))
#endif // QT_CONFIG(tooltip)
        self.leftMenuRecordsBtn.setText(QCoreApplication.translate("MainWindow", u"Records        ", None))
#if QT_CONFIG(tooltip)
        self.leftMenuSummaryBtn.setToolTip(QCoreApplication.translate("MainWindow", u"go to Summary", None))
#endif // QT_CONFIG(tooltip)
        self.leftMenuSummaryBtn.setText(QCoreApplication.translate("MainWindow", u" Summary   ", None))
#if QT_CONFIG(tooltip)
        self.leftMenuLogoutBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Exit", None))
#endif // QT_CONFIG(tooltip)
        self.leftMenuLogoutBtn.setText(QCoreApplication.translate("MainWindow", u"  Exit", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"We care about your well-being", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Answer a short questionnaire about your symptoms to find out what might be causing them ", None))
        self.dTakeBtn.setText(QCoreApplication.translate("MainWindow", u"Take the test", None))
        self.dImage_2.setText("")
        self.pPExitBtn.setText("")
        self.pPProgress.setText("")
        self.pPExitBtn2.setText("")
        self.pTopLabel.setText(QCoreApplication.translate("MainWindow", u"User Details", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Fields marked by an asterisk (*) are required", None))
        self.pUserDetailsLnameLabel.setText(QCoreApplication.translate("MainWindow", u"Last Name*", None))
        self.pUserDetailsFnameLabel.setText(QCoreApplication.translate("MainWindow", u"First Name*", None))
        self.pUserDetailsMnameLabel.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.lnameErrorLabel.setText("")
        self.fnameErrorLabel.setText("")
        self.mnameErrorLabel.setText("")
        self.pUserDetailsBirthdateLabel.setText(QCoreApplication.translate("MainWindow", u"Birthdate*", None))
        self.pUserDetailsBirthdateFormatLabel.setText(QCoreApplication.translate("MainWindow", u"MM/DD/YYYY", None))
        self.pUserDetailsBirthdateDateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MM/dd/yyyy", None))
        self.pUserDetailsAgeLabel.setText(QCoreApplication.translate("MainWindow", u"Age*", None))
        self.pUserDetailsSexLabel.setText(QCoreApplication.translate("MainWindow", u"Sex*", None))
        self.pUserDetailsSexCb.setItemText(0, QCoreApplication.translate("MainWindow", u"Select", None))
        self.pUserDetailsSexCb.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.pUserDetailsSexCb.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.pUserDetailsCivilLabel.setText(QCoreApplication.translate("MainWindow", u"Civil Status*", None))
        self.pUserDetailsCivilCb.setItemText(0, QCoreApplication.translate("MainWindow", u"Select", None))
        self.pUserDetailsCivilCb.setItemText(1, QCoreApplication.translate("MainWindow", u"Single", None))
        self.pUserDetailsCivilCb.setItemText(2, QCoreApplication.translate("MainWindow", u"Married", None))
        self.pUserDetailsCivilCb.setItemText(3, QCoreApplication.translate("MainWindow", u"Widowed", None))
        self.pUserDetailsCivilCb.setItemText(4, QCoreApplication.translate("MainWindow", u"Separated", None))

        self.pUserDetailsContactLabel.setText(QCoreApplication.translate("MainWindow", u"Contact Number", None))
        self.birthdateErrorLabel.setText("")
        self.ageErrorLabel.setText("")
        self.sexErrorLabel.setText("")
        self.civilErrorLabel.setText("")
        self.contactErrorLabel.setText("")
        self.pUserDetailsAddressLabel.setText(QCoreApplication.translate("MainWindow", u"Complete Address", None))
        self.addressErrorLabel.setText("")
        self.pMidLabel.setText(QCoreApplication.translate("MainWindow", u"Emergency Contact", None))
        self.emergencyNameLabel.setText(QCoreApplication.translate("MainWindow", u"Complete Name", None))
        self.emergencyRelationLabel.setText(QCoreApplication.translate("MainWindow", u"Relation to Patient", None))
        self.emergencyContactLabel.setText(QCoreApplication.translate("MainWindow", u"Contact Number", None))
        self.emergencyNameErrorLabel.setText("")
        self.emergencyRelationErrorLabel.setText("")
        self.emergencyContactErrorLabel.setText("")
        self.pBottomNextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.symPExitBtn.setText("")
        self.symPProgress.setText("")
        self.symPExitBtn2.setText("")
        self.symTopLabel.setText(QCoreApplication.translate("MainWindow", u"Select Symptoms", None))
        self.symSearchIcon.setText(QCoreApplication.translate("MainWindow", u"SearchIcon", None))
        self.symSearchLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search e.g. Headache, Nausea, etc.", None))
        self.symCb1.setText(QCoreApplication.translate("MainWindow", u"Symptom", None))
        self.symDesc1.setText(QCoreApplication.translate("MainWindow", u"insert description of symptom here", None))
        self.symCb2.setText(QCoreApplication.translate("MainWindow", u"Symptom", None))
        self.symDesc2.setText(QCoreApplication.translate("MainWindow", u"insert description of symptom here", None))
        self.symCb3.setText(QCoreApplication.translate("MainWindow", u"Symptom", None))
        self.symDesc3.setText(QCoreApplication.translate("MainWindow", u"insert description of symptom here", None))
        self.symBodyComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select a body part", None))
        self.symBodyComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Head", None))
        self.symBodyComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Neck", None))
        self.symBodyComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Arms", None))
        self.symBodyComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Legs", None))
        self.symBodyComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Back", None))

        self.symImage.setText(QCoreApplication.translate("MainWindow", u"Insert Picture", None))
        self.symBottomNextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.iPExitBtn.setText("")
        self.iPProgress.setText("")
        self.iPExitBtn2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Do you have any of the following symptoms?", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select all answers that apply", None))
        self.isymCb.setText(QCoreApplication.translate("MainWindow", u"Symptom", None))
        self.iDesc1.setText(QCoreApplication.translate("MainWindow", u"insert description of symptom here", None))
        self.isymCb_3.setText(QCoreApplication.translate("MainWindow", u"Symptom", None))
        self.iDesc1_3.setText(QCoreApplication.translate("MainWindow", u"insert description of symptom here", None))
        self.isymCb_8.setText(QCoreApplication.translate("MainWindow", u"Symptom", None))
        self.iDesc1_8.setText(QCoreApplication.translate("MainWindow", u"insert description of symptom here", None))
        self.isymCb_9.setText(QCoreApplication.translate("MainWindow", u"Symptom", None))
        self.iDesc1_9.setText(QCoreApplication.translate("MainWindow", u"insert description of symptom here", None))
        self.isymCb_7.setText(QCoreApplication.translate("MainWindow", u"Symptom", None))
        self.iDesc1_7.setText(QCoreApplication.translate("MainWindow", u"insert description of symptom here", None))
        self.isymCb_6.setText(QCoreApplication.translate("MainWindow", u"Symptom", None))
        self.iDesc1_6.setText(QCoreApplication.translate("MainWindow", u"insert description of symptom here", None))
        self.isymCb_5.setText(QCoreApplication.translate("MainWindow", u"Symptom", None))
        self.iDesc1_5.setText(QCoreApplication.translate("MainWindow", u"insert description of symptom here", None))
        self.isymCb_4.setText(QCoreApplication.translate("MainWindow", u"Symptom", None))
        self.iDesc1_4.setText(QCoreApplication.translate("MainWindow", u"insert description of symptom here", None))
        self.isymCb_2.setText(QCoreApplication.translate("MainWindow", u"Symptom", None))
        self.iDesc1_2.setText(QCoreApplication.translate("MainWindow", u"insert description of symptom here", None))
        self.iBottomNextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.vPExitBtn.setText("")
        self.vPProgess.setText("")
        self.vPExitBtn2.setText("")
        self.vTopLabel.setText(QCoreApplication.translate("MainWindow", u"Patient Details", None))
        self.vTopEditBtn.setText(QCoreApplication.translate("MainWindow", u"Edit Details", None))
        self.vPatientDetailsNameHeading.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.vPatientDetailsNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sample Patient Full Name", None))
        self.vPatientDetailsBirthdateHeading.setText(QCoreApplication.translate("MainWindow", u"Birthdate", None))
        self.vPatientDetailsBirthdateLabel.setText(QCoreApplication.translate("MainWindow", u"01/30/2001", None))
        self.vPatientDetailsAgeHeading.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.vPatientDetailsAgeLabel.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.vPatientDetailsSexHeading.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.vPatientDetailsSexLabel.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.vPatientDetailsCivilHeading.setText(QCoreApplication.translate("MainWindow", u"Civil Status", None))
        self.vPatientDetailsCivilLabel.setText(QCoreApplication.translate("MainWindow", u"Married", None))
        self.vPatientDetailsContactHeading.setText(QCoreApplication.translate("MainWindow", u"Contact Number", None))
        self.vPatientDetailsContactLabel.setText(QCoreApplication.translate("MainWindow", u"09123546879", None))
        self.vPatientDetailsAddressHeading.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.vPatientDetailsAddressLabel.setText(QCoreApplication.translate("MainWindow", u"143 Some Random Street Another Random Avenue Blank City, Insert Province Country", None))
        self.vMidLabel.setText(QCoreApplication.translate("MainWindow", u"Emergency Contact", None))
        self.vEmergencyNameHeading.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.vEmergencyNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sample Emergency Contact Name", None))
        self.vEmergencyRelationHeading.setText(QCoreApplication.translate("MainWindow", u"Relation to Patient", None))
        self.vEmergencyRelationLabel.setText(QCoreApplication.translate("MainWindow", u"Parent", None))
        self.vEmergencyContactHeading.setText(QCoreApplication.translate("MainWindow", u"Contact Number", None))
        self.vEmergencyContactLabel.setText(QCoreApplication.translate("MainWindow", u"09787536475", None))
        self.vMidLabel2.setText(QCoreApplication.translate("MainWindow", u"Symptoms", None))
        self.vMidEditBtn.setText(QCoreApplication.translate("MainWindow", u"Edit Symptoms", None))

        __sortingEnabled = self.vSymptomsSymptomsListWidget.isSortingEnabled()
        self.vSymptomsSymptomsListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.vSymptomsSymptomsListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u25cf Cold", None));
        ___qlistwidgetitem1 = self.vSymptomsSymptomsListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u25cf Headache", None));
        ___qlistwidgetitem2 = self.vSymptomsSymptomsListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u25cf Backpain", None));
        ___qlistwidgetitem3 = self.vSymptomsSymptomsListWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u25cf Migrane", None));
        ___qlistwidgetitem4 = self.vSymptomsSymptomsListWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u25cf Vertigo", None));
        ___qlistwidgetitem5 = self.vSymptomsSymptomsListWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u25cf Blurred Vision", None));
        self.vSymptomsSymptomsListWidget.setSortingEnabled(__sortingEnabled)

        self.vBottomNextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.resPExitBtn.setText("")
        self.resPProgress.setText("")
        self.resPExitBtn2.setText("")
        self.resTopLabel.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.resTopPrintBtn.setText(QCoreApplication.translate("MainWindow", u"Download Simplified", None))
        self.resTopDownloadBtn.setText(QCoreApplication.translate("MainWindow", u"Print Simplified", None))
        self.resUserDetailsNameHeading.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.resUserDetailsNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sample Patient Full Name", None))
        self.resUserDetailsBirthdateHeading.setText(QCoreApplication.translate("MainWindow", u"Birthdate", None))
        self.resUserDetailsBirthdateLabel.setText(QCoreApplication.translate("MainWindow", u"01/30/2001", None))
        self.resUserDetailsAgeHeading.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.resUserDetailsAgeLabel.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.resUserDetailsSexHeadingContainer_2.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.resUserDetailsSexLabel.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.resUserDetailsCivilHeading.setText(QCoreApplication.translate("MainWindow", u"Civil Status", None))
        self.resUserDetailsCivilLabel.setText(QCoreApplication.translate("MainWindow", u"Married", None))
        self.resUserDetailsContactHeading.setText(QCoreApplication.translate("MainWindow", u"Contact Number", None))
        self.resUserDetailsContactLabel.setText(QCoreApplication.translate("MainWindow", u"09123546879", None))
        self.resUserDetailsAddressHeading.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.resUserDetailsAddressLabel.setText(QCoreApplication.translate("MainWindow", u"143 Some Random Street Another Random Avenue Blank City, Insert Province Country", None))
        self.resResultPredictionHeading.setText(QCoreApplication.translate("MainWindow", u"Prediction", None))
        self.resResultPredictionLabel.setText(QCoreApplication.translate("MainWindow", u"Insert Disease", None))
        self.resResultConfidenceHeading.setText(QCoreApplication.translate("MainWindow", u"Confidence Rating", None))
        self.resResultConfidenceLabel.setText(QCoreApplication.translate("MainWindow", u"Very Likely", None))
        self.resResultCauseLabel.setText(QCoreApplication.translate("MainWindow", u"Potential Causes:", None))

        __sortingEnabled1 = self.resResultCauseListWidget.isSortingEnabled()
        self.resResultCauseListWidget.setSortingEnabled(False)
        ___qlistwidgetitem6 = self.resResultCauseListWidget.item(0)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem7 = self.resResultCauseListWidget.item(1)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem8 = self.resResultCauseListWidget.item(2)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem9 = self.resResultCauseListWidget.item(3)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem10 = self.resResultCauseListWidget.item(4)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.resResultCauseListWidget.setSortingEnabled(__sortingEnabled1)

        self.resResultActionLabel.setText(QCoreApplication.translate("MainWindow", u"Recommended Actions", None))

        __sortingEnabled2 = self.resResultActionListWidget.isSortingEnabled()
        self.resResultActionListWidget.setSortingEnabled(False)
        ___qlistwidgetitem11 = self.resResultActionListWidget.item(0)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem12 = self.resResultActionListWidget.item(1)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem13 = self.resResultActionListWidget.item(2)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem14 = self.resResultActionListWidget.item(3)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem15 = self.resResultActionListWidget.item(4)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.resResultActionListWidget.setSortingEnabled(__sortingEnabled2)

        self.resBottomCloseBtn.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.resBottomSaveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.recImage.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Authentication Required", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"You are about to access potentially sensitive medical information. Legal action against any and all form of unauthorized access and distribution will be pursued.", None))
        self.recAuthCheckBox.setText(QCoreApplication.translate("MainWindow", u"I understand the provision above", None))
        self.recAuthPasswordLbl.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.recAuthSubmitBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.recExitBtn1.setText("")
        self.recSearchMainLabel.setText(QCoreApplication.translate("MainWindow", u"Patient Records", None))
        self.recSearchPushButton.setText("")
        ___qtablewidgetitem = self.recSearchTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem1 = self.recSearchTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem2 = self.recSearchTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None));
        ___qtablewidgetitem3 = self.recSearchTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Birthdate", None));
        ___qtablewidgetitem4 = self.recSearchTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Last Consultation", None));
        ___qtablewidgetitem5 = self.recSearchTable.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.recSearchTable.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.recSearchTable.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.recSearchTable.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.recSearchTable.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.recSearchTable.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.recSearchTable.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.recSearchTable.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.recExitBtn2.setText("")
        self.recDetailsLbl1.setText(QCoreApplication.translate("MainWindow", u"Latest Patient Details", None))
        self.recPatientDetailsNameHeading.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.recPatientDetailsNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sample Patient Full Name", None))
        self.recPatientDetailsBirthdateHeading.setText(QCoreApplication.translate("MainWindow", u"Birthdate", None))
        self.recPatientDetailsBirthdateLabel.setText(QCoreApplication.translate("MainWindow", u"01/30/2001", None))
        self.recPatientDetailsAgeHeading.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.recPatientDetailsAgeLabel.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.recPatientDetailsSexHeading.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.recPatientDetailsSexLabel.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.recPatientDetailsCivilHeading.setText(QCoreApplication.translate("MainWindow", u"Civil Status", None))
        self.recPatientDetailsCivilLabel.setText(QCoreApplication.translate("MainWindow", u"Married", None))
        self.recPatientDetailsContactHeading.setText(QCoreApplication.translate("MainWindow", u"Contact Number", None))
        self.recPatientDetailsContactLabel.setText(QCoreApplication.translate("MainWindow", u"09123546879", None))
        self.recPatientDetailsAdressHeading.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.recPatientDetailsAdressLabel.setText(QCoreApplication.translate("MainWindow", u"143 Some Random Street Another Random Avenue Blank City, Insert Province Country", None))
        self.recDetailsLbl2.setText(QCoreApplication.translate("MainWindow", u"Emergency Contact", None))
        self.recEmergencyNameHeading.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.recEmergencyNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sample Emergency Contact Name", None))
        self.recvEmergencyRelationHeading.setText(QCoreApplication.translate("MainWindow", u"Relation to Patient", None))
        self.recEmergencyRelationLabel.setText(QCoreApplication.translate("MainWindow", u"Parent", None))
        self.recEmergencyContactHeading.setText(QCoreApplication.translate("MainWindow", u"Contact Number", None))
        self.recEmergencyContactLabel.setText(QCoreApplication.translate("MainWindow", u"09787536475", None))
        self.recDetailsLbl3.setText(QCoreApplication.translate("MainWindow", u"Consultation History", None))
        ___qtablewidgetitem13 = self.recTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"All", None));
        ___qtablewidgetitem14 = self.recTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem15 = self.recTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Prediction", None));
        ___qtablewidgetitem16 = self.recTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Recommendation", None));
        ___qtablewidgetitem17 = self.recTableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.recTableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.recTableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.recTableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.recTableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem22 = self.recTableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem23 = self.recTableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem24 = self.recTableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem25 = self.recTableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem26 = self.recTableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem27 = self.recTableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem28 = self.recTableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem29 = self.recTableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem30 = self.recTableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.recTableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem32 = self.recTableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem33 = self.recTableWidget.verticalHeaderItem(16)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem34 = self.recTableWidget.verticalHeaderItem(17)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem35 = self.recTableWidget.verticalHeaderItem(18)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem36 = self.recTableWidget.verticalHeaderItem(19)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem37 = self.recTableWidget.verticalHeaderItem(20)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem38 = self.recTableWidget.verticalHeaderItem(21)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem39 = self.recTableWidget.verticalHeaderItem(22)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem40 = self.recTableWidget.verticalHeaderItem(23)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem41 = self.recTableWidget.verticalHeaderItem(24)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem42 = self.recTableWidget.verticalHeaderItem(25)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem43 = self.recTableWidget.verticalHeaderItem(26)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem44 = self.recTableWidget.verticalHeaderItem(27)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem45 = self.recTableWidget.verticalHeaderItem(28)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem46 = self.recTableWidget.verticalHeaderItem(29)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem47 = self.recTableWidget.verticalHeaderItem(30)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem48 = self.recTableWidget.verticalHeaderItem(31)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem49 = self.recTableWidget.verticalHeaderItem(32)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem50 = self.recTableWidget.verticalHeaderItem(33)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem51 = self.recTableWidget.verticalHeaderItem(34)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem52 = self.recTableWidget.verticalHeaderItem(35)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem53 = self.recTableWidget.verticalHeaderItem(36)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled3 = self.recTableWidget.isSortingEnabled()
        self.recTableWidget.setSortingEnabled(False)
        ___qtablewidgetitem54 = self.recTableWidget.item(0, 1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"June 25, 2022", None));
        ___qtablewidgetitem55 = self.recTableWidget.item(0, 2)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Malaria", None));
        ___qtablewidgetitem56 = self.recTableWidget.item(0, 3)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Paracetamol, Clonazepam, Ribofla...", None));
        self.recTableWidget.setSortingEnabled(__sortingEnabled3)

        self.sumImage.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Authentication Required", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"You are about to access potentially sensitive medical information. Legal action against any and all form of unauthorized access and distribution will be pursued.", None))
        self.sumAuthCheckBox.setText(QCoreApplication.translate("MainWindow", u"I understand the provision above", None))
        self.sumAuthPasswordLbl.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.sumAuthSubmitBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.sumMainExitBtn.setText("")
        self.sumMainLabel1.setText(QCoreApplication.translate("MainWindow", u"Summary", None))
        self.sumMainLabel2.setText(QCoreApplication.translate("MainWindow", u"Sitio Junel Purok 7", None))
        self.sumMainGraph1.setText("")
        self.sumMainGraph3.setText("")
        self.sumMainGraph2.setText("")
        self.sumMainTotalDiagnosis1.setText(QCoreApplication.translate("MainWindow", u"102", None))
        self.sumMainTotalDiagnosis2.setText(QCoreApplication.translate("MainWindow", u"Total Number of Diagnosis", None))
        self.sumMainTotalPatients1.setText(QCoreApplication.translate("MainWindow", u"85", None))
        self.sumMainTotalPatients2.setText(QCoreApplication.translate("MainWindow", u"Total Number of Patients", None))
        ___qtablewidgetitem57 = self.sumMainTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Disease", None));
        ___qtablewidgetitem58 = self.sumMainTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Total Number of Cases", None));
        ___qtablewidgetitem59 = self.sumMainTableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem60 = self.sumMainTableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem61 = self.sumMainTableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem62 = self.sumMainTableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem63 = self.sumMainTableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem64 = self.sumMainTableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem65 = self.sumMainTableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem66 = self.sumMainTableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem67 = self.sumMainTableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled4 = self.sumMainTableWidget.isSortingEnabled()
        self.sumMainTableWidget.setSortingEnabled(False)
        ___qtablewidgetitem68 = self.sumMainTableWidget.item(0, 0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Malaria", None));
        ___qtablewidgetitem69 = self.sumMainTableWidget.item(0, 1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.sumMainTableWidget.setSortingEnabled(__sortingEnabled4)

    # retranslateUi

