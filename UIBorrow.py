# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Borrow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

from qfluentwidgets import (LineEdit, PrimaryPushButton, PushButton, TextEdit)

class Ui_Borrow(object):
    def setupUi(self, Borrow):
        if not Borrow.objectName():
            Borrow.setObjectName(u"Borrow")
        Borrow.resize(640, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Borrow.sizePolicy().hasHeightForWidth())
        Borrow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"\u5f97\u610f\u9ed1"])
        Borrow.setFont(font)
        self.horizontalLayout_13 = QHBoxLayout(Borrow)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, 60, 20, 20)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(Borrow)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"\u5f97\u610f\u9ed1"])
        font1.setPointSize(15)
        self.label.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label)

        self.bookidEdit = TextEdit(Borrow)
        self.bookidEdit.setObjectName(u"bookidEdit")
        self.bookidEdit.setMinimumSize(QSize(0, 33))
        self.bookidEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.horizontalLayout_11.addWidget(self.bookidEdit)

        self.booksearchButton = PushButton(Borrow)
        self.booksearchButton.setObjectName(u"booksearchButton")

        self.horizontalLayout_11.addWidget(self.booksearchButton)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 8)
        self.horizontalLayout_11.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.groupBox = QGroupBox(Borrow)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"\u5f97\u610f\u9ed1"])
        font2.setPointSize(13)
        self.groupBox.setFont(font2)
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"\n"
"border-width:2px;\n"
"\n"
"border-style:solid;\n"
"\n"
"border-radius: 10px;\n"
"\n"
"border-color:gray;\n"
"\n"
"margin-top:0.5ex;\n"
"\n"
"}")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFont(font1)

        self.horizontalLayout.addWidget(self.label_3)

        self.booknamelabel = QLabel(self.groupBox)
        self.booknamelabel.setObjectName(u"booknamelabel")
        font3 = QFont()
        font3.setPointSize(13)
        self.booknamelabel.setFont(font3)

        self.horizontalLayout.addWidget(self.booknamelabel)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.bookauthorlabel = QLabel(self.groupBox)
        self.bookauthorlabel.setObjectName(u"bookauthorlabel")
        self.bookauthorlabel.setFont(font3)

        self.horizontalLayout_2.addWidget(self.bookauthorlabel)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.bookpresslabel = QLabel(self.groupBox)
        self.bookpresslabel.setObjectName(u"bookpresslabel")
        self.bookpresslabel.setFont(font3)

        self.horizontalLayout_3.addWidget(self.bookpresslabel)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.bookisbnlabel = QLabel(self.groupBox)
        self.bookisbnlabel.setObjectName(u"bookisbnlabel")
        self.bookisbnlabel.setFont(font3)

        self.horizontalLayout_4.addWidget(self.bookisbnlabel)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.bookinventorylabel = QLabel(self.groupBox)
        self.bookinventorylabel.setObjectName(u"bookinventorylabel")
        self.bookinventorylabel.setFont(font3)

        self.horizontalLayout_5.addWidget(self.bookinventorylabel)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.booktotallabel = QLabel(self.groupBox)
        self.booktotallabel.setObjectName(u"booktotallabel")
        self.booktotallabel.setFont(font3)

        self.horizontalLayout_6.addWidget(self.booktotallabel)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 9)

        self.horizontalLayout_13.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_2 = QLabel(Borrow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_2)

        self.useridEdit = TextEdit(Borrow)
        self.useridEdit.setObjectName(u"useridEdit")
        self.useridEdit.setMinimumSize(QSize(0, 33))
        self.useridEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.horizontalLayout_12.addWidget(self.useridEdit)

        self.usersearchButton = PushButton(Borrow)
        self.usersearchButton.setObjectName(u"usersearchButton")

        self.horizontalLayout_12.addWidget(self.usersearchButton)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 8)
        self.horizontalLayout_12.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.groupBox_2 = QGroupBox(Borrow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setFont(font2)
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"\n"
"border-width:2px;\n"
"\n"
"border-style:solid;\n"
"\n"
"border-radius: 10px;\n"
"\n"
"border-color:gray;\n"
"\n"
"margin-top:0.5ex;\n"
"\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_11)

        self.usernamelabel = QLabel(self.groupBox_2)
        self.usernamelabel.setObjectName(u"usernamelabel")
        self.usernamelabel.setFont(font3)

        self.horizontalLayout_10.addWidget(self.usernamelabel)

        self.horizontalLayout_10.setStretch(0, 2)
        self.horizontalLayout_10.setStretch(1, 5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.usertruenamelabel = QLabel(self.groupBox_2)
        self.usertruenamelabel.setObjectName(u"usertruenamelabel")
        self.usertruenamelabel.setFont(font3)

        self.horizontalLayout_9.addWidget(self.usertruenamelabel)

        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_10)

        self.userphonelabel = QLabel(self.groupBox_2)
        self.userphonelabel.setObjectName(u"userphonelabel")
        self.userphonelabel.setFont(font3)

        self.horizontalLayout_8.addWidget(self.userphonelabel)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.passwordEdit = LineEdit(self.groupBox_2)
        self.passwordEdit.setObjectName(u"passwordEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.passwordEdit.sizePolicy().hasHeightForWidth())
        self.passwordEdit.setSizePolicy(sizePolicy3)
        self.passwordEdit.setMinimumSize(QSize(0, 33))
        self.passwordEdit.setMaximumSize(QSize(16777215, 16777215))
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.passwordEdit)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 9)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.borrowsearchButton = PrimaryPushButton(self.groupBox_2)
        self.borrowsearchButton.setObjectName(u"borrowsearchButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.borrowsearchButton.sizePolicy().hasHeightForWidth())
        self.borrowsearchButton.setSizePolicy(sizePolicy4)

        self.verticalLayout_2.addWidget(self.borrowsearchButton)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)

        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 9)

        self.horizontalLayout_13.addLayout(self.verticalLayout_3)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)

        self.retranslateUi(Borrow)

        QMetaObject.connectSlotsByName(Borrow)
    # setupUi

    def retranslateUi(self, Borrow):
        Borrow.setWindowTitle(QCoreApplication.translate("Borrow", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Borrow", u"\u56fe\u4e66ID:", None))
        self.booksearchButton.setText(QCoreApplication.translate("Borrow", u"\u641c\u7d22", None))
        self.groupBox.setTitle(QCoreApplication.translate("Borrow", u"\u56fe\u4e66\u4fe1\u606f", None))
        self.label_3.setText(QCoreApplication.translate("Borrow", u"\u540d\u79f0:", None))
        self.booknamelabel.setText("")
        self.label_4.setText(QCoreApplication.translate("Borrow", u"\u4f5c\u8005:", None))
        self.bookauthorlabel.setText("")
        self.label_5.setText(QCoreApplication.translate("Borrow", u"\u51fa\u7248\u793e:", None))
        self.bookpresslabel.setText("")
        self.label_6.setText(QCoreApplication.translate("Borrow", u"ISBN:", None))
        self.bookisbnlabel.setText("")
        self.label_7.setText(QCoreApplication.translate("Borrow", u"\u5e93\u5b58\u6570\u91cf:", None))
        self.bookinventorylabel.setText("")
        self.label_8.setText(QCoreApplication.translate("Borrow", u"\u603b\u6570\u91cf:", None))
        self.booktotallabel.setText("")
        self.label_2.setText(QCoreApplication.translate("Borrow", u"\u7528\u6237ID:", None))
        self.usersearchButton.setText(QCoreApplication.translate("Borrow", u"\u67e5\u8be2", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Borrow", u"\u7528\u6237\u4fe1\u606f", None))
        self.label_11.setText(QCoreApplication.translate("Borrow", u"\u7528\u6237\u540d:", None))
        self.usernamelabel.setText("")
        self.label_9.setText(QCoreApplication.translate("Borrow", u"\u59d3\u540d:", None))
        self.usertruenamelabel.setText("")
        self.label_10.setText(QCoreApplication.translate("Borrow", u"\u8054\u7cfb\u7535\u8bdd:", None))
        self.userphonelabel.setText("")
        self.label_13.setText(QCoreApplication.translate("Borrow", u"\u5bc6\u7801:", None))
        self.borrowsearchButton.setText(QCoreApplication.translate("Borrow", u"\u501f\u9605", None))
    # retranslateUi

