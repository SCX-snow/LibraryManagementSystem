import sys
import pymysql
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import MessageDialog, SplitFluentWindow, FluentIcon
from qframelesswindow import FramelessDialog, TitleBar

from UILogin import Ui_Login
from Interface import BookWindow, BorrowWindow, UserWindow, ReturnWindow


class LoginWindow(FramelessDialog, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.login)

    def login(self):
        try:
            db = pymysql.connect(host=self.serverEdit.text(),
                                 user=self.idEdit.text(),
                                 password=self.passwordEdit.text(),
                                 database='Book',
                                 charset='utf8')
            cursor = db.cursor()
            sql = 'SELECT VERSION()'
            cursor.execute(sql)
            db.close()
        except pymysql.Error:
            f = MessageDialog('登录失败', '登录失败,请检查', self)
            f.exec()
            return
        self.close()
        Main.show()
        Main.init_sub_interface(self.serverEdit.text(), self.idEdit.text(), self.passwordEdit.text())
        Main.activateWindow()


class MainWindow(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('图书管理系统')
        self.resize(700, 480)

        self.bookInterface = BookWindow(self)
        self.borrowInterface = BorrowWindow(self)
        self.returnInterface = ReturnWindow(self)
        self.userInterface = UserWindow(self)

        self.addSubInterface(self.bookInterface, FluentIcon.LIBRARY, '图书管理')
        self.addSubInterface(self.borrowInterface, FluentIcon.EDUCATION, '借阅管理')
        self.addSubInterface(self.returnInterface, FluentIcon.DICTIONARY, '归还管理')
        self.addSubInterface(self.userInterface, FluentIcon.PEOPLE, '用户管理')

    def init_sub_interface(self, server, userid, password):
        self.bookInterface.variable(server, userid, password)
        self.borrowInterface.variable(server, userid, password)
        self.returnInterface.variable(server, userid, password)
        self.userInterface.variable(server, userid, password)
        self.bookInterface.table_view()
        self.returnInterface.table_view()
        self.userInterface.table_view()
        self.bookInterface.TableView.selectionModel().currentChanged.connect(self.bookInterface.table_changed)
        self.returnInterface.TableView.selectionModel().currentChanged.connect(self.returnInterface.table_changed)
        self.userInterface.TableView.selectionModel().currentChanged.connect(self.userInterface.table_changed)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = LoginWindow()
    Main = MainWindow()
    # Main.show()
    Login.show()
    app.exec()
