# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QSizePolicy, QWidget)

from qfluentwidgets import (LineEdit, PrimaryPushButton, PushButton)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(320, 240)
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 91, 31))
        font = QFont()
        font.setFamilies([u"\u5f97\u610f\u9ed1"])
        font.setPointSize(15)
        self.label.setFont(font)
        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 90, 61, 31))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 140, 41, 31))
        self.label_3.setFont(font)
        self.loginButton = PrimaryPushButton(Login)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(90, 190, 153, 32))
        self.serverEdit = LineEdit(Login)
        self.serverEdit.setObjectName(u"serverEdit")
        self.serverEdit.setGeometry(QRect(120, 40, 181, 33))
        self.idEdit = LineEdit(Login)
        self.idEdit.setObjectName(u"idEdit")
        self.idEdit.setGeometry(QRect(120, 90, 181, 33))
        self.passwordEdit = LineEdit(Login)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setGeometry(QRect(120, 140, 181, 33))
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Login", u"\u670d\u52a1\u5668\u5730\u5740:", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"\u7528\u6237\u540d:", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"\u5bc6\u7801:", None))
        self.loginButton.setText(QCoreApplication.translate("Login", u"\u767b\u5f55", None))
        self.serverEdit.setText(QCoreApplication.translate("Login", u"192.168.158.128", None))
    # retranslateUi

