import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

from Quanly import Ui_MainWindow

import mysql.connector


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui",self)
        self.pushButton.clicked.connect(self.gotologin)
        self.pushButton_2.clicked.connect(self.gotocreate)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui",self)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton.clicked.connect(self.loginfunction)
        self.commandLinkButton.clicked.connect(self.signup)

    def loginfunction(self):
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if user == '' or password == '':
            self.label_6.setText("thiếu thông tin")
        else:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Conghuy090701",
                database="quanly123")
            mycursor = mydb.cursor()

            sql = "SELECT * FROM login WHERE user = '%s' AND password = '%s'" % (user, password)
            mycursor.execute(sql)
            if mycursor.fetchone():
                self.Second_Window = QtWidgets.QMainWindow()
                self.uic = Ui_MainWindow()
                self.uic.setupUi(self.Second_Window)
                self.Second_Window.show()

            else:
                self.label_6.setText("sai tài khoản mật khẩu")

    def signup(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("createacc.ui",self)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton.clicked.connect(self.signupfunction)
        self.commandLinkButton.clicked.connect(self.login)

    def signupfunction(self):
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confirmpassword = self.lineEdit_3.text()

        if user == '' or password == '' or confirmpassword == '':
            self.label_6.setText("Thiếu thông tin")

        elif password != confirmpassword:
            self.label_6.setText("Mật khẩu không trùng khớp")
        else:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Conghuy090701",
                database="quanly123")
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO login (user, password) VALUES (%s, %s)", (user, password))
            mydb.commit()
            self.label_6.setText("tạo tài khoản thành công")

    def login(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)




# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(550)
widget.setFixedWidth(600)
widget.show()
sys.exit(app.exec_())
