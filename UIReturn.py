# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Return.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (ComboBox, PushButton, TableView, TextEdit)

class Ui_Return(object):
    def setupUi(self, Return):
        if not Return.objectName():
            Return.setObjectName(u"Return")
        Return.resize(640, 480)
        self.verticalLayout = QVBoxLayout(Return)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 60, 20, 20)
        self.TableView = TableView(Return)
        self.TableView.setObjectName(u"TableView")

        self.verticalLayout.addWidget(self.TableView)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Return)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"\u5f97\u610f\u9ed1"])
        font.setPointSize(15)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.useridEdit = TextEdit(Return)
        self.useridEdit.setObjectName(u"useridEdit")
        self.useridEdit.setMinimumSize(QSize(0, 33))

        self.horizontalLayout.addWidget(self.useridEdit)

        self.horizontalLayout.setStretch(1, 9)

        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Return)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.namelabel = QLabel(Return)
        self.namelabel.setObjectName(u"namelabel")
        font1 = QFont()
        font1.setPointSize(15)
        self.namelabel.setFont(font1)

        self.horizontalLayout_2.addWidget(self.namelabel)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 9)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(Return)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.contactlabel = QLabel(Return)
        self.contactlabel.setObjectName(u"contactlabel")
        self.contactlabel.setFont(font1)

        self.horizontalLayout_3.addWidget(self.contactlabel)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 9)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(Return)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_5.addWidget(self.label)

        self.bookidEdit = TextEdit(Return)
        self.bookidEdit.setObjectName(u"bookidEdit")
        self.bookidEdit.setMinimumSize(QSize(0, 33))

        self.horizontalLayout_5.addWidget(self.bookidEdit)

        self.horizontalLayout_5.setStretch(0, 1)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(Return)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.borrowdatelabel = QLabel(Return)
        self.borrowdatelabel.setObjectName(u"borrowdatelabel")
        self.borrowdatelabel.setFont(font1)

        self.horizontalLayout_6.addWidget(self.borrowdatelabel)

        self.horizontalLayout_6.setStretch(1, 9)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(Return)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.duedatelabel = QLabel(Return)
        self.duedatelabel.setObjectName(u"duedatelabel")
        self.duedatelabel.setFont(font1)

        self.horizontalLayout_8.addWidget(self.duedatelabel)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 9)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(Return)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.borrowidEdit = TextEdit(Return)
        self.borrowidEdit.setObjectName(u"borrowidEdit")
        self.borrowidEdit.setMinimumSize(QSize(0, 33))

        self.horizontalLayout_7.addWidget(self.borrowidEdit)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(Return)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.booknamelabel = QLabel(Return)
        self.booknamelabel.setObjectName(u"booknamelabel")
        self.booknamelabel.setFont(font1)

        self.horizontalLayout_10.addWidget(self.booknamelabel)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 9)

        self.horizontalLayout_12.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(Return)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.modComboBox = ComboBox(Return)
        self.modComboBox.setObjectName(u"modComboBox")

        self.horizontalLayout_9.addWidget(self.modComboBox)

        self.runButton = PushButton(Return)
        self.runButton.setObjectName(u"runButton")

        self.horizontalLayout_9.addWidget(self.runButton)

        self.horizontalLayout_9.setStretch(1, 8)
        self.horizontalLayout_9.setStretch(2, 1)

        self.horizontalLayout_12.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 1)
        self.horizontalLayout_12.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.verticalLayout.setStretch(0, 7)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(Return)

        QMetaObject.connectSlotsByName(Return)
    # setupUi

    def retranslateUi(self, Return):
        Return.setWindowTitle(QCoreApplication.translate("Return", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Return", u"\u7528\u6237ID:", None))
        self.label_3.setText(QCoreApplication.translate("Return", u"\u59d3\u540d:", None))
        self.namelabel.setText("")
        self.label_4.setText(QCoreApplication.translate("Return", u"\u8054\u7cfb\u65b9\u5f0f:", None))
        self.contactlabel.setText("")
        self.label.setText(QCoreApplication.translate("Return", u"\u56fe\u4e66ID:", None))
        self.label_5.setText(QCoreApplication.translate("Return", u"\u501f\u9605\u65e5\u671f:", None))
        self.borrowdatelabel.setText("")
        self.label_6.setText(QCoreApplication.translate("Return", u"\u5e94\u8fd8\u65e5\u671f:", None))
        self.duedatelabel.setText("")
        self.label_8.setText(QCoreApplication.translate("Return", u"\u501f\u9605ID:", None))
        self.label_9.setText(QCoreApplication.translate("Return", u"\u4e66\u540d:", None))
        self.booknamelabel.setText("")
        self.label_7.setText(QCoreApplication.translate("Return", u"\u6a21\u5f0f:", None))
        self.runButton.setText(QCoreApplication.translate("Return", u"\u6267\u884c", None))
    # retranslateUi

