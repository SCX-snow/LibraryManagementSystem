# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'User.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

from qfluentwidgets import (ComboBox, LineEdit, PushButton, TableView,
    TextEdit)

class Ui_User(object):
    def setupUi(self, User):
        if not User.objectName():
            User.setObjectName(u"User")
        User.resize(640, 480)
        self.verticalLayout = QVBoxLayout(User)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 60, 20, 20)
        self.TableView = TableView(User)
        self.TableView.setObjectName(u"TableView")

        self.verticalLayout.addWidget(self.TableView)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(User)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u5f97\u610f\u9ed1"])
        font.setPointSize(15)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.idEdit = TextEdit(User)
        self.idEdit.setObjectName(u"idEdit")
        self.idEdit.setMinimumSize(QSize(0, 33))

        self.horizontalLayout.addWidget(self.idEdit)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 9)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(User)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.nameEdit = TextEdit(User)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setMinimumSize(QSize(0, 33))

        self.horizontalLayout_2.addWidget(self.nameEdit)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 9)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(User)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.passwordEdit = LineEdit(User)
        self.passwordEdit.setObjectName(u"passwordEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordEdit.sizePolicy().hasHeightForWidth())
        self.passwordEdit.setSizePolicy(sizePolicy)
        self.passwordEdit.setMaximumSize(QSize(16777215, 16777215))
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.passwordEdit)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 9)

        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(User)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.truenameEdit = TextEdit(User)
        self.truenameEdit.setObjectName(u"truenameEdit")
        self.truenameEdit.setMinimumSize(QSize(0, 33))

        self.horizontalLayout_4.addWidget(self.truenameEdit)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 9)

        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(User)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.phoneEdit = TextEdit(User)
        self.phoneEdit.setObjectName(u"phoneEdit")
        self.phoneEdit.setMinimumSize(QSize(0, 33))

        self.horizontalLayout_5.addWidget(self.phoneEdit)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 9)

        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(User)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.modComboBox = ComboBox(User)
        self.modComboBox.setObjectName(u"modComboBox")

        self.horizontalLayout_6.addWidget(self.modComboBox)

        self.runButton = PushButton(User)
        self.runButton.setObjectName(u"runButton")

        self.horizontalLayout_6.addWidget(self.runButton)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 8)
        self.horizontalLayout_6.setStretch(2, 1)

        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(User)

        QMetaObject.connectSlotsByName(User)
    # setupUi

    def retranslateUi(self, User):
        User.setWindowTitle(QCoreApplication.translate("User", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("User", u"\u7528\u6237ID:", None))
        self.label_2.setText(QCoreApplication.translate("User", u"\u7528\u6237\u540d:", None))
        self.label_3.setText(QCoreApplication.translate("User", u"\u5bc6\u7801:", None))
        self.label_4.setText(QCoreApplication.translate("User", u"\u59d3\u540d:", None))
        self.label_5.setText(QCoreApplication.translate("User", u"\u8054\u7cfb\u7535\u8bdd:", None))
        self.label_6.setText(QCoreApplication.translate("User", u"\u6a21\u5f0f:", None))
        self.runButton.setText(QCoreApplication.translate("User", u"\u6267\u884c", None))
    # retranslateUi

