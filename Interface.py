import hashlib

import pymysql
import datetime
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIntValidator
from PySide6.QtWidgets import QApplication, QWidget, QHeaderView
from qfluentwidgets import MessageDialog, SplitFluentWindow
from qframelesswindow import FramelessDialog

from UIBook import Ui_Book
from UIBorrow import Ui_Borrow
from UIUser import Ui_User
from UIReturn import Ui_Return


class BookWindow(QWidget, Ui_Book):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.TableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.password = str()
        self.userId = str()
        self.serverAddress = str()
        self.tableModel = QStandardItemModel()
        self.modComboBox.addItem('查询')
        self.modComboBox.addItem('入库')
        self.modComboBox.addItem('数量修改')
        self.modComboBox.setCurrentText('查询')
        self.inventorySpinBox.setEnabled(False)
        self.totalSpinBox.setEnabled(False)
        self.modComboBox.currentIndexChanged.connect(self.mod_changed)
        self.runButton.clicked.connect(self.run_button)
        self.idEdit.textChanged.connect(self.num_restrict)
        self.isbnEdit.textChanged.connect(self.num_restrict)

    def num_restrict(self):
        if self.sender().toPlainText().isnumeric() is False and self.sender().toPlainText() != '':
            self.sender().setText("".join([c for c in self.sender().toPlainText() if c.isdigit()]))

    def num_edit(self):
        if self.idEdit.toPlainText() == '':
            f = MessageDialog('错误', '请填写id', self)
            f.exec()
            return
        else:
            try:
                db = pymysql.connect(host=self.serverAddress,
                                     user=self.userId,
                                     password=self.password,
                                     database='Book',
                                     charset='utf8')
                cursor = db.cursor()
                sql = "UPDATE books SET stock_quantity = %d, total_quantity = %d WHERE book_id = %s" % (
                    self.inventorySpinBox.value(), self.totalSpinBox.value(), self.idEdit.toPlainText())
                cursor.execute(sql)
                db.commit()
                db.close()
            except pymysql.Error:
                f = MessageDialog('错误', '修改失败 请检查', self)
                f.exec()
                return
            self.nameEdit.setText('')
            self.authorEdit.setText('')
            self.pressEdit.setText('')
            self.isbnEdit.setText('')
            self.search()
            self.TableView.setCurrentIndex(self.tableModel.index(0, 0))
            self.table_changed()

    def book_in(self):
        if self.nameEdit.toPlainText() == '' or self.authorEdit.toPlainText() == '' or self.pressEdit.toPlainText() == '' or self.isbnEdit.toPlainText() == '':
            f = MessageDialog('错误', '请填写完整书籍数据', self)
            f.exec()
            return
        else:
            try:
                db = pymysql.connect(host=self.serverAddress,
                                     user=self.userId,
                                     password=self.password,
                                     database='Book',
                                     charset='utf8')
                cursor = db.cursor()
                sql = ("INSERT INTO books (title, author, publisher, isbn, stock_quantity, total_quantity) VALUES "
                       "('%s', '%s', '%s', '%s', %d, %d)") % (self.nameEdit.toPlainText(),
                                                              self.authorEdit.toPlainText(),
                                                              self.pressEdit.toPlainText(),
                                                              self.isbnEdit.toPlainText(),
                                                              self.inventorySpinBox.value(),
                                                              self.totalSpinBox.value())
                cursor.execute(sql)
                db.commit()
                db.close()
            except pymysql.Error:
                f = MessageDialog('错误', '入库失败 请检查', self)
                f.exec()
                return
            self.search()

    def search(self):
        self.table_view()
        if (
                self.idEdit.toPlainText() == '' and self.nameEdit.toPlainText() == '' and self.authorEdit.toPlainText() == '' and self.pressEdit.toPlainText() == '' and self.isbnEdit.toPlainText() == '') is False:
            if self.idEdit.toPlainText() != '':
                i = 0
                while True:
                    if i == self.tableModel.rowCount():
                        break
                    if self.idEdit.toPlainText() not in self.tableModel.index(i, 0).data():
                        self.tableModel.removeRow(i)
                        continue
                    i = i + 1
            if self.nameEdit.toPlainText() != '':
                i = 0
                while True:
                    if i == self.tableModel.rowCount():
                        break
                    if self.nameEdit.toPlainText() not in self.tableModel.index(i, 1).data():
                        self.tableModel.removeRow(i)
                        continue
                    i = i + 1
            if self.authorEdit.toPlainText() != '':
                i = 0
                while True:
                    if i == self.tableModel.rowCount():
                        break
                    if self.authorEdit.toPlainText() not in self.tableModel.index(i, 2).data():
                        self.tableModel.removeRow(i)
                        continue
                    i = i + 1
            if self.pressEdit.toPlainText() != '':
                i = 0
                while True:
                    if i == self.tableModel.rowCount():
                        break
                    if self.pressEdit.toPlainText() not in self.tableModel.index(i, 3).data():
                        self.tableModel.removeRow(i)
                        continue
                    i = i + 1
            if self.isbnEdit.toPlainText() != '':
                i = 0
                while True:
                    if i == self.tableModel.rowCount():
                        break
                    if self.isbnEdit.toPlainText() not in self.tableModel.index(i, 4).data():
                        self.tableModel.removeRow(i)
                        continue
                    i = i + 1
            self.TableView.setCurrentIndex(self.tableModel.index(0, 0))

    def run_button(self):
        if self.modComboBox.text() == '查询':
            self.TableView.selectionModel().currentChanged.disconnect()
            self.search()
            self.TableView.selectionModel().currentChanged.connect(self.table_changed)
        elif self.modComboBox.text() == '入库':
            self.book_in()
        elif self.modComboBox.text() == '数量修改':
            self.TableView.selectionModel().currentChanged.disconnect()
            self.num_edit()
            self.TableView.selectionModel().currentChanged.connect(self.table_changed)

    def table_changed(self):
        self.idEdit.setText(self.tableModel.index(self.TableView.currentIndex().row(), 0).data())
        self.nameEdit.setText(self.tableModel.index(self.TableView.currentIndex().row(), 1).data())
        self.authorEdit.setText(self.tableModel.index(self.TableView.currentIndex().row(), 2).data())
        self.pressEdit.setText(self.tableModel.index(self.TableView.currentIndex().row(), 3).data())
        self.isbnEdit.setText(self.tableModel.index(self.TableView.currentIndex().row(), 4).data())
        self.inventorySpinBox.setValue(int(self.tableModel.index(self.TableView.currentIndex().row(), 5).data()))
        self.totalSpinBox.setValue(int(self.tableModel.index(self.TableView.currentIndex().row(), 6).data()))

    def variable(self, server, user, password):
        self.serverAddress = server
        self.userId = user
        self.password = password

    def table_view(self):
        self.tableModel.clear()
        try:
            db = pymysql.connect(host=self.serverAddress,
                                 user=self.userId,
                                 password=self.password,
                                 database='Book',
                                 charset='utf8')
            cursor = db.cursor()
            sql = 'SELECT * FROM books'
            cursor.execute(sql)
            data = cursor.fetchall()
            db.close()
        except pymysql.Error:
            f = MessageDialog('错误', '致命错误,程序退出', self)
            f.exec()
            return
        self.tableModel.setHorizontalHeaderLabels(['ID', '书名', '作者', '出版社', 'ISBN', '库存', '总数'])
        for i in range(len(data)):
            for j in range(7):
                k = QStandardItem(str(data[i][j]))
                self.tableModel.setItem(i, j, k)
        self.TableView.setModel(self.tableModel)

    def mod_changed(self):
        if self.modComboBox.currentText() == '查询':
            self.inventorySpinBox.setEnabled(False)
            self.totalSpinBox.setEnabled(False)
            self.idEdit.setEnabled(True)
            self.nameEdit.setEnabled(True)
            self.authorEdit.setEnabled(True)
            self.pressEdit.setEnabled(True)
            self.isbnEdit.setEnabled(True)
            self.TableView.selectionModel().currentChanged.connect(self.table_changed)
        if self.modComboBox.currentText() == '入库':
            self.inventorySpinBox.setEnabled(True)
            self.totalSpinBox.setEnabled(True)
            self.idEdit.setEnabled(False)
            self.nameEdit.setEnabled(True)
            self.authorEdit.setEnabled(True)
            self.pressEdit.setEnabled(True)
            self.isbnEdit.setEnabled(True)
            self.idEdit.setText('')
            self.nameEdit.setText('')
            self.authorEdit.setText('')
            self.pressEdit.setText('')
            self.isbnEdit.setText('')
            self.inventorySpinBox.setValue(0)
            self.totalSpinBox.setValue(0)
            self.TableView.selectionModel().currentChanged.disconnect()
        if self.modComboBox.currentText() == '数量修改':
            self.inventorySpinBox.setEnabled(True)
            self.totalSpinBox.setEnabled(True)
            self.idEdit.setEnabled(True)
            self.nameEdit.setEnabled(False)
            self.authorEdit.setEnabled(False)
            self.pressEdit.setEnabled(False)
            self.isbnEdit.setEnabled(False)
            self.TableView.selectionModel().currentChanged.connect(self.table_changed)


class BorrowWindow(QWidget, Ui_Borrow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.password = str()
        self.userId = str()
        self.serverAddress = str()
        self.borrowsearchButton.setEnabled(False)
        self.booksearchButton.clicked.connect(self.book_search)
        self.usersearchButton.clicked.connect(self.user_search)
        self.borrowsearchButton.clicked.connect(self.borrow)
        self.bookidEdit.textChanged.connect(self.num_restrict)
        self.useridEdit.textChanged.connect(self.num_restrict)

    def borrow(self):
        if int(self.bookinventorylabel.text()) > 0:
            try:
                db = pymysql.connect(host=self.serverAddress,
                                     user=self.userId,
                                     password=self.password,
                                     database='Book',
                                     charset='utf8')
                cursor = db.cursor()
                sql = "SELECT password FROM users WHERE user_id = %s" % self.useridEdit.toPlainText()
                cursor.execute(sql)
                data = cursor.fetchone()
                hs = hashlib.sha3_512()
                hs.update(bytes(self.passwordEdit.text(), 'utf-8'))
                if hs.hexdigest() != data[0]:
                    db.close()
                    f = MessageDialog('错误', '密码错误', self)
                    f.exec()
                    return
                today = datetime.date.today()
                return_day = (datetime.datetime(today.year, today.month, today.day) + datetime.timedelta(days=14))
                sql = ("INSERT INTO  borrow_records (book_id, user_id, borrow_date, due_date) VALUES (%s, %s, '%s', "
                       "'%s')") % (self.bookidEdit.toPlainText(), self.useridEdit.toPlainText(), today.strftime(
                    "%Y-%m-%d"), return_day.strftime("%Y-%m-%d"))
                cursor.execute(sql)
                db.commit()
                db.close()
                sql = "UPDATE books SET stock_quantity = stock_quantity - 1 WHERE book_id = %s" % self.bookidEdit.toPlainText()
                cursor.execute(sql)
                db.commit()
                db.close()
                f = MessageDialog('成功', '借阅成功', self)
                f.exec()
                return
            except pymysql.Error:
                f = MessageDialog('错误', '借阅失败 请检查', self)
                f.exec()
                return
        else:
            f = MessageDialog('错误', '库存数量不足', self)
            f.exec()

    def borrow_ready_check(self):
        if self.booknamelabel.text() != '' and self.usernamelabel.text() != '':
            self.borrowsearchButton.setEnabled(True)
        else:
            self.borrowsearchButton.setEnabled(False)

    def num_restrict(self):
        if self.sender().toPlainText().isnumeric() is False and self.sender().toPlainText() != '':
            self.sender().setText("".join([c for c in self.sender().toPlainText() if c.isdigit()]))

    def user_search(self):
        self.usernamelabel.setText('')
        self.usertruenamelabel.setText('')
        self.userphonelabel.setText('')
        self.borrow_ready_check()
        if self.useridEdit.toPlainText() == '':
            f = MessageDialog('错误', '请输入用户ID', self)
            f.exec()
            return
        else:
            try:
                db = pymysql.connect(host=self.serverAddress,
                                     user=self.userId,
                                     password=self.password,
                                     database='Book',
                                     charset='utf8')
                cursor = db.cursor()
                sql = "SELECT * FROM users WHERE user_id = %s" % self.useridEdit.toPlainText()
                cursor.execute(sql)
                data = cursor.fetchone()
                db.close()
                if data is None:
                    f = MessageDialog('错误', '未查寻到对应用户', self)
                    f.exec()
                    return
                else:
                    self.usernamelabel.setText(data[1])
                    self.usertruenamelabel.setText(data[3])
                    self.userphonelabel.setText(data[4])
            except pymysql.Error:
                f = MessageDialog('错误', '致命错误,程序退出', self)
                f.exec()
                return
        self.borrow_ready_check()

    def variable(self, server, user, password):
        self.serverAddress = server
        self.userId = user
        self.password = password

    def book_search(self):
        self.booknamelabel.setText('')
        self.bookauthorlabel.setText('')
        self.bookpresslabel.setText('')
        self.bookisbnlabel.setText('')
        self.bookinventorylabel.setText('')
        self.booktotallabel.setText('')
        self.borrow_ready_check()
        if self.bookidEdit.toPlainText() == '':
            f = MessageDialog('错误', '请输入图书ID', self)
            f.exec()
            return
        else:
            try:
                db = pymysql.connect(host=self.serverAddress,
                                     user=self.userId,
                                     password=self.password,
                                     database='Book',
                                     charset='utf8')
                cursor = db.cursor()
                sql = "SELECT * FROM books WHERE book_id = %s" % self.bookidEdit.toPlainText()
                cursor.execute(sql)
                data = cursor.fetchone()
                db.close()
                if data is None:
                    f = MessageDialog('错误', '未查寻到对应图书', self)
                    f.exec()
                    return
                else:
                    self.booknamelabel.setText(data[1])
                    self.bookauthorlabel.setText(data[2])
                    self.bookpresslabel.setText(data[3])
                    self.bookisbnlabel.setText(data[4])
                    self.bookinventorylabel.setText(str(data[5]))
                    self.booktotallabel.setText(str(data[6]))
            except pymysql.Error:
                f = MessageDialog('错误', '致命错误,程序退出', self)
                f.exec()
                return
        self.borrow_ready_check()


class ReturnWindow(QWidget, Ui_Return):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.TableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableModel = QStandardItemModel()
        self.password = str()
        self.userId = str()
        self.serverAddress = str()
        self.modComboBox.addItem('搜索')
        self.modComboBox.addItem('还书')
        self.bookidEdit.textChanged.connect(self.num_restrict)
        self.useridEdit.textChanged.connect(self.num_restrict)
        self.runButton.clicked.connect(self.run_button)
        self.modComboBox.currentTextChanged.connect(self.mod_change)

    def mod_change(self):
        if self.modComboBox.text() == '搜索':
            self.bookidEdit.setEnabled(True)
            self.useridEdit.setEnabled(True)
        elif self.modComboBox.text() == '还书':
            self.bookidEdit.setEnabled(False)
            self.useridEdit.setEnabled(False)

    def return_book(self):
        if self.borrowidEdit.toPlainText() == '':
            f = MessageDialog('错误', '未选择还书目标', self)
            f.exec()
            return
        else:
            try:
                db = pymysql.connect(host=self.serverAddress,
                                     user=self.userId,
                                     password=self.password,
                                     database='Book',
                                     charset='utf8')
                cursor = db.cursor()
                sql = "UPDATE borrow_records SET return_date = '%s'" % datetime.date.today().strftime('%Y-%m-%d')
                cursor.execute(sql)
                db.commit()
                db.close()
                self.table_view()
                f = MessageDialog('成功', '归还成功', self)
                f.exec()
                self.bookidEdit.setText('')
                self.namelabel.setText('')
                self.contactlabel.setText('')
                self.useridEdit.setText('')
                self.borrowdatelabel.setText('')
                self.duedatelabel.setText('')
                self.borrowidEdit.setText('')
                self.booknamelabel.setText('')
            except pymysql.Error:
                f = MessageDialog('错误', '致命错误,程序退出', self)
                f.exec()
                return

    def search(self):
        self.table_view()
        if self.bookidEdit.toPlainText() != '':
            i = 0
            while True:
                if i == self.tableModel.rowCount():
                    break
                if self.bookidEdit.toPlainText() not in self.tableModel.index(i, 1).data():
                    self.tableModel.removeRow(i)
                    continue
                i = i + 1
        if self.useridEdit.toPlainText() != '':
            i = 0
            while True:
                if i == self.tableModel.rowCount():
                    break
                if self.useridEdit.toPlainText() not in self.tableModel.index(i, 2).data():
                    self.tableModel.removeRow(i)
                    continue
                i = i + 1
        if self.borrowidEdit.toPlainText() != '':
            i = 0
            while True:
                if i == self.tableModel.rowCount():
                    break
                if self.borrowidEdit.toPlainText() not in self.tableModel.index(i, 0).data():
                    self.tableModel.removeRow(i)
                    continue
                i = i + 1

    def run_button(self):
        if self.modComboBox.text() == '搜索':
            self.TableView.selectionModel().currentChanged.disconnect()
            self.search()
            self.TableView.selectionModel().currentChanged.connect(self.table_changed)
        elif self.modComboBox.text() == '还书':
            self.TableView.selectionModel().currentChanged.disconnect()
            self.return_book()
            self.TableView.selectionModel().currentChanged.connect(self.table_changed)

    def table_changed(self):
        self.borrowidEdit.setText(self.tableModel.index(self.TableView.currentIndex().row(), 0).data())
        self.bookidEdit.setText(self.tableModel.index(self.TableView.currentIndex().row(), 1).data())
        self.useridEdit.setText(self.tableModel.index(self.TableView.currentIndex().row(), 2).data())
        self.borrowdatelabel.setText(self.tableModel.index(self.TableView.currentIndex().row(), 3).data())
        self.duedatelabel.setText(self.tableModel.index(self.TableView.currentIndex().row(), 4).data())
        try:
            db = pymysql.connect(host=self.serverAddress,
                                 user=self.userId,
                                 password=self.password,
                                 database='Book',
                                 charset='utf8')
            cursor = db.cursor()
            sql = "SELECT name, contact, username FROM users WHERE user_id = %s" % self.useridEdit.toPlainText()
            cursor.execute(sql)
            data = cursor.fetchone()
            self.namelabel.setText(data[0])
            self.contactlabel.setText(data[1])
            sql = "SELECT title FROM books WHERE book_id = %s" % self.bookidEdit.toPlainText()
            cursor.execute(sql)
            data = cursor.fetchone()
            self.booknamelabel.setText(data[0])
            db.close()
        except pymysql.Error:
            f = MessageDialog('错误', '致命错误,程序退出', self)
            f.exec()
            return

    def num_restrict(self):
        if self.sender().toPlainText().isnumeric() is False and self.sender().toPlainText() != '':
            self.sender().setText("".join([c for c in self.sender().toPlainText() if c.isdigit()]))

    def variable(self, server, user, password):
        self.serverAddress = server
        self.userId = user
        self.password = password

    def table_view(self):
        self.tableModel.clear()
        try:
            db = pymysql.connect(host=self.serverAddress,
                                 user=self.userId,
                                 password=self.password,
                                 database='Book',
                                 charset='utf8')
            cursor = db.cursor()
            sql = 'SELECT * FROM borrow_records WHERE return_date is null'
            cursor.execute(sql)
            data = cursor.fetchall()
            db.close()
        except pymysql.Error:
            f = MessageDialog('错误', '致命错误,程序退出', self)
            f.exec()
            return
        self.tableModel.setHorizontalHeaderLabels(['ID', '图书ID', '用户ID', '借阅日期', '应归还日期'])
        for i in range(len(data)):
            for j in range(5):
                k = QStandardItem(str(data[i][j]))
                self.tableModel.setItem(i, j, k)
        self.TableView.setModel(self.tableModel)


class UserWindow(QWidget, Ui_User):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.tableModel = QStandardItemModel()
        self.password = str()
        self.userId = str()
        self.serverAddress = str()
        self.modComboBox.addItem('查询')
        self.modComboBox.addItem('修改')
        self.modComboBox.addItem('添加')
        self.nameEdit.setEnabled(False)
        self.passwordEdit.setEnabled(False)
        self.truenameEdit.setEnabled(False)
        self.phoneEdit.setEnabled(False)
        self.idEdit.textChanged.connect(self.num_restrict)
        self.phoneEdit.textChanged.connect(self.num_restrict)
        self.modComboBox.currentTextChanged.connect(self.mod_changed)
        self.runButton.clicked.connect(self.run_button)

    def user_add(self):
        if self.nameEdit.toPlainText() == '' or self.passwordEdit.text() == '' or self.truenameEdit.toPlainText() == '' or self.phoneEdit.toPlainText() == '':
            f = MessageDialog('错误', '请填写完整数据', self)
            f.exec()
            return
        elif len(self.phoneEdit.toPlainText()) != 11:
            f = MessageDialog('错误', '请填写正确手机号', self)
            f.exec()
            return
        else:
            try:
                db = pymysql.connect(host=self.serverAddress,
                                     user=self.userId,
                                     password=self.password,
                                     database='Book',
                                     charset='utf8')
                cursor = db.cursor()
                hs = hashlib.sha3_512()
                hs.update(bytes(self.passwordEdit.text(), 'utf-8'))
                sql = "INSERT INTO users (username, password, name, contact) VALUES ('%s', '%s', '%s', '%s')" % (
                    self.nameEdit.toPlainText(), hs.hexdigest(), self.truenameEdit.toPlainText(),
                    self.phoneEdit.toPlainText())
                cursor.execute(sql)
                db.commit()
                db.close()
            except pymysql.Error:
                f = MessageDialog('错误', '添加失败 请检查', self)
                f.exec()
                return
            self.search()
            self.TableView.setCurrentIndex(self.tableModel.index(0, 0))
            self.table_changed()

    def user_edit(self):
        if self.idEdit.toPlainText() == '':
            f = MessageDialog('错误', '请填写id', self)
            f.exec()
            return
        else:
            try:
                db = pymysql.connect(host=self.serverAddress,
                                     user=self.userId,
                                     password=self.password,
                                     database='Book',
                                     charset='utf8')
                cursor = db.cursor()
                if self.passwordEdit.text() == '':
                    sql = "UPDATE users SET username = '%s', name = '%s', contact = '%s' WHERE user_id = %s" % (
                        self.nameEdit.toPlainText(), self.truenameEdit.toPlainText(), self.phoneEdit.toPlainText(),
                        self.idEdit.toPlainText())
                else:
                    hs = hashlib.sha3_512()
                    hs.update(bytes(self.passwordEdit.text(), 'utf-8'))
                    sql = ("UPDATE users SET username = '%s', name = '%s', password = '%s', contact = '%s' WHERE "
                           "user_id = %s") % (
                              self.nameEdit.toPlainText(), self.truenameEdit.toPlainText(), hs.hexdigest(),
                              self.phoneEdit.toPlainText(), self.idEdit.toPlainText())
                cursor.execute(sql)
                db.commit()
                db.close()
            except pymysql.Error:
                f = MessageDialog('错误', '修改失败 请检查', self)
                f.exec()
                return
            self.search()
            self.TableView.setCurrentIndex(self.tableModel.index(0, 0))
            self.table_changed()

    def search(self):
        self.table_view()
        if self.idEdit.toPlainText() != '':
            i = 0
            while True:
                if i == self.tableModel.rowCount():
                    break
                if self.idEdit.toPlainText() not in self.tableModel.index(i, 0).data():
                    self.tableModel.removeRow(i)
                    continue
                i = i + 1

    def run_button(self):
        if self.modComboBox.text() == '查询':
            self.TableView.selectionModel().currentChanged.disconnect()
            self.search()
            self.TableView.selectionModel().currentChanged.connect(self.table_changed)
        elif self.modComboBox.text() == '修改':
            self.TableView.selectionModel().currentChanged.disconnect()
            self.user_edit()
            self.TableView.selectionModel().currentChanged.connect(self.table_changed)
        elif self.modComboBox.text() == '添加':
            self.TableView.selectionModel().currentChanged.disconnect()
            self.user_add()
            self.TableView.selectionModel().currentChanged.connect(self.table_changed)

    def mod_changed(self):
        if self.modComboBox.text() == '查询':
            self.TableView.selectionModel().currentChanged.connect(self.table_changed)
            self.nameEdit.setEnabled(False)
            self.passwordEdit.setEnabled(False)
            self.truenameEdit.setEnabled(False)
            self.phoneEdit.setEnabled(False)
        elif self.modComboBox.text() == '修改':
            self.TableView.selectionModel().currentChanged.connect(self.table_changed)
            self.nameEdit.setEnabled(True)
            self.passwordEdit.setEnabled(True)
            self.truenameEdit.setEnabled(True)
            self.phoneEdit.setEnabled(True)
        elif self.modComboBox.text() == '添加':
            self.TableView.selectionModel().currentChanged.disconnect()
            self.idEdit.setEnabled(False)
            self.nameEdit.setEnabled(True)
            self.passwordEdit.setEnabled(True)
            self.truenameEdit.setEnabled(True)
            self.phoneEdit.setEnabled(True)
            self.idEdit.setText('')
            self.nameEdit.setText('')
            self.passwordEdit.setText('')
            self.truenameEdit.setText('')
            self.phoneEdit.setText('')

    def table_changed(self):
        self.idEdit.setText(self.tableModel.index(self.TableView.currentIndex().row(), 0).data())
        self.nameEdit.setText(self.tableModel.index(self.TableView.currentIndex().row(), 1).data())
        self.truenameEdit.setText(self.tableModel.index(self.TableView.currentIndex().row(), 2).data())
        self.phoneEdit.setText(self.tableModel.index(self.TableView.currentIndex().row(), 3).data())

    def table_view(self):
        self.tableModel.clear()
        try:
            db = pymysql.connect(host=self.serverAddress,
                                 user=self.userId,
                                 password=self.password,
                                 database='Book',
                                 charset='utf8')
            cursor = db.cursor()
            sql = 'SELECT user_id, username, name, contact FROM users'
            cursor.execute(sql)
            data = cursor.fetchall()
            db.close()
        except pymysql.Error:
            f = MessageDialog('错误', '致命错误,程序退出', self)
            f.exec()
            return
        self.tableModel.setHorizontalHeaderLabels(['用户ID', '用户名', '姓名', '联系电话', '借阅中数量', '总借阅数量'])
        for i in range(len(data)):
            for j in range(4):
                k = QStandardItem(str(data[i][j]))
                self.tableModel.setItem(i, j, k)
            try:
                db = pymysql.connect(host=self.serverAddress,
                                     user=self.userId,
                                     password=self.password,
                                     database='Book',
                                     charset='utf8')
                cursor = db.cursor()
                sql = 'SELECT user_id FROM borrow_records WHERE user_id = %s and return_date is null' % data[i][0]
                k = QStandardItem(str(cursor.execute(sql)))
                self.tableModel.setItem(i, 4, k)
                sql = 'SELECT user_id FROM borrow_records WHERE user_id = %s' % data[i][0]
                k = QStandardItem(str(cursor.execute(sql)))
                self.tableModel.setItem(i, 5, k)
                db.close()
            except pymysql.Error:
                f = MessageDialog('错误', '致命错误,程序退出', self)
                f.exec()
                return
        self.TableView.setModel(self.tableModel)

    def num_restrict(self):
        if self.sender().toPlainText().isnumeric() is False and self.sender().toPlainText() != '':
            self.sender().setText("".join([c for c in self.sender().toPlainText() if c.isdigit()]))

    def variable(self, server, user, password):
        self.serverAddress = server
        self.userId = user
        self.password = password
