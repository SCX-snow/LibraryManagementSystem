# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Book.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDialog,
    QHBoxLayout, QHeaderView, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

from qfluentwidgets import (ComboBox, PushButton, SpinBox, TableView,
    TextEdit)

class Ui_Book(object):
    def setupUi(self, Book):
        if not Book.objectName():
            Book.setObjectName(u"Book")
        Book.resize(640, 480)
        self.verticalLayout = QVBoxLayout(Book)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 60, 20, 20)
        self.TableView = TableView(Book)
        self.TableView.setObjectName(u"TableView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TableView.sizePolicy().hasHeightForWidth())
        self.TableView.setSizePolicy(sizePolicy)
        self.TableView.setMinimumSize(QSize(0, 0))
        self.TableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.TableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TableView.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.TableView)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Book)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"\u5f97\u610f\u9ed1"])
        font.setPointSize(15)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.idEdit = TextEdit(Book)
        self.idEdit.setObjectName(u"idEdit")
        self.idEdit.setMinimumSize(QSize(0, 33))

        self.horizontalLayout.addWidget(self.idEdit)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 9)

        self.horizontalLayout_10.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Book)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.authorEdit = TextEdit(Book)
        self.authorEdit.setObjectName(u"authorEdit")
        self.authorEdit.setMinimumSize(QSize(0, 33))

        self.horizontalLayout_2.addWidget(self.authorEdit)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 9)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(Book)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.isbnEdit = TextEdit(Book)
        self.isbnEdit.setObjectName(u"isbnEdit")
        self.isbnEdit.setMinimumSize(QSize(0, 33))

        self.horizontalLayout_3.addWidget(self.isbnEdit)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 9)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(Book)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.nameEdit = TextEdit(Book)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setMinimumSize(QSize(0, 33))

        self.horizontalLayout_4.addWidget(self.nameEdit)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 9)

        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(Book)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.pressEdit = TextEdit(Book)
        self.pressEdit.setObjectName(u"pressEdit")
        self.pressEdit.setMinimumSize(QSize(0, 33))

        self.horizontalLayout_5.addWidget(self.pressEdit)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 9)

        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(Book)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.inventorySpinBox = SpinBox(Book)
        self.inventorySpinBox.setObjectName(u"inventorySpinBox")
        sizePolicy.setHeightForWidth(self.inventorySpinBox.sizePolicy().hasHeightForWidth())
        self.inventorySpinBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.inventorySpinBox)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 9)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(Book)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.totalSpinBox = SpinBox(Book)
        self.totalSpinBox.setObjectName(u"totalSpinBox")
        sizePolicy.setHeightForWidth(self.totalSpinBox.sizePolicy().hasHeightForWidth())
        self.totalSpinBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.totalSpinBox)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 9)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(Book)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.modComboBox = ComboBox(Book)
        self.modComboBox.setObjectName(u"modComboBox")
        sizePolicy.setHeightForWidth(self.modComboBox.sizePolicy().hasHeightForWidth())
        self.modComboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.modComboBox)

        self.runButton = PushButton(Book)
        self.runButton.setObjectName(u"runButton")
        sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.runButton)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 8)
        self.horizontalLayout_8.setStretch(2, 1)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.verticalLayout.setStretch(0, 7)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(Book)

        QMetaObject.connectSlotsByName(Book)
    # setupUi

    def retranslateUi(self, Book):
        Book.setWindowTitle(QCoreApplication.translate("Book", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Book", u"\u56fe\u4e66ID:", None))
        self.label_3.setText(QCoreApplication.translate("Book", u"\u4f5c\u8005:", None))
        self.label_5.setText(QCoreApplication.translate("Book", u"ISBN:", None))
        self.label_2.setText(QCoreApplication.translate("Book", u"\u540d\u79f0:", None))
        self.label_4.setText(QCoreApplication.translate("Book", u"\u51fa\u7248\u793e:", None))
        self.label_6.setText(QCoreApplication.translate("Book", u"\u5e93\u5b58\u6570\u91cf:", None))
        self.label_7.setText(QCoreApplication.translate("Book", u"\u603b\u6570\u91cf:", None))
        self.label_8.setText(QCoreApplication.translate("Book", u"\u6a21\u5f0f\u9009\u62e9:", None))
        self.runButton.setText(QCoreApplication.translate("Book", u"\u6267\u884c", None))
    # retranslateUi

