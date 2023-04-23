# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1052, 737)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font = QFont()
        font.setKerning(False)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setLineWidth(0)
        self.LobbyPage = QWidget()
        self.LobbyPage.setObjectName(u"LobbyPage")
        self.LobbyPage.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.145, y2:0.103, stop:0 rgba(117, 0, 153, 255), stop:1 rgba(85, 209, 255, 255));")
        self.verticalLayout_3 = QVBoxLayout(self.LobbyPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.Logo = QLabel(self.LobbyPage)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMinimumSize(QSize(0, 100))
        font1 = QFont()
        font1.setPointSize(35)
        self.Logo.setFont(font1)
        self.Logo.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.Logo.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Logo, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.LoginEdit = QLineEdit(self.LobbyPage)
        self.LoginEdit.setObjectName(u"LoginEdit")
        self.LoginEdit.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.LoginEdit)

        self.PasswordEdit = QLineEdit(self.LobbyPage)
        self.PasswordEdit.setObjectName(u"PasswordEdit")
        self.PasswordEdit.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.PasswordEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.ForgotPassword = QPushButton(self.LobbyPage)
        self.ForgotPassword.setObjectName(u"ForgotPassword")
        font2 = QFont()
        font2.setUnderline(True)
        self.ForgotPassword.setFont(font2)
        self.ForgotPassword.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout.addWidget(self.ForgotPassword)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.LoginButton = QPushButton(self.LobbyPage)
        self.LoginButton.setObjectName(u"LoginButton")

        self.verticalLayout.addWidget(self.LoginButton)

        self.SignUpButton = QPushButton(self.LobbyPage)
        self.SignUpButton.setObjectName(u"SignUpButton")

        self.verticalLayout.addWidget(self.SignUpButton)

        self.FreeButton = QPushButton(self.LobbyPage)
        self.FreeButton.setObjectName(u"FreeButton")

        self.verticalLayout.addWidget(self.FreeButton)


        self.gridLayout_2.addLayout(self.verticalLayout, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(200, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.stackedWidget.addWidget(self.LobbyPage)
        self.ManualPage = QWidget()
        self.ManualPage.setObjectName(u"ManualPage")
        self.verticalLayout_6 = QVBoxLayout(self.ManualPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.MenuLayout = QVBoxLayout()
        self.MenuLayout.setSpacing(0)
        self.MenuLayout.setObjectName(u"MenuLayout")
        self.MenuLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.MenuLayout.setContentsMargins(-1, -1, -1, 0)

        self.verticalLayout_6.addLayout(self.MenuLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listView = QListView(self.ManualPage)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout_2.addWidget(self.listView)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.MainGraph = QGraphicsView(self.ManualPage)
        self.MainGraph.setObjectName(u"MainGraph")

        self.verticalLayout_4.addWidget(self.MainGraph)

        self.SecondGraph = QGraphicsView(self.ManualPage)
        self.SecondGraph.setObjectName(u"SecondGraph")

        self.verticalLayout_4.addWidget(self.SecondGraph)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lineEdit = QLineEdit(self.ManualPage)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_5.addWidget(self.lineEdit)

        self.tableView = QTableView(self.ManualPage)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_5.addWidget(self.tableView)

        self.listView_2 = QListView(self.ManualPage)
        self.listView_2.setObjectName(u"listView_2")

        self.verticalLayout_5.addWidget(self.listView_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.horizontalLayout_2.setStretch(1, 80)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.ManualPage)
        self.DevelopmentPage = QWidget()
        self.DevelopmentPage.setObjectName(u"DevelopmentPage")
        self.DevelopmentPage.setMinimumSize(QSize(0, 0))
        self.DevelopmentPage.setSizeIncrement(QSize(1, 0))
        self.gridLayout = QGridLayout(self.DevelopmentPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.BackButton = QPushButton(self.DevelopmentPage)
        self.BackButton.setObjectName(u"BackButton")

        self.gridLayout.addWidget(self.BackButton, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.label_3 = QLabel(self.DevelopmentPage)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(40)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(0)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.DevelopmentPage)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.stackedWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.stackedWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.Logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Finam Screener</span></p></body></html>", None))
        self.LoginEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.PasswordEdit.setText("")
        self.PasswordEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.ForgotPassword.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0431\u044b\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c?", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.SignUpButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.FreeButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0437\u043d\u0430\u043a\u043e\u043c\u0438\u0442\u044c\u0441\u044f \u0441 \u0444\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b\u043e\u043c", None))
        self.BackButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0435", None))
    # retranslateUi

