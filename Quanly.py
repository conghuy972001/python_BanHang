import mysql.connector
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow , QTableWidget, QMessageBox
import numpy
import random


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1234, 628)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(193, 221, 255, 255), stop:0.522685 rgba(255, 255, 255, 255), stop:1 rgba(255, 206, 213, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(160, -30, 1081, 661))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setGeometry(QtCore.QRect(410, 40, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(890, 100, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: none")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setGeometry(QtCore.QRect(360, 99, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: none")
        self.label_4.setObjectName("label_4")
        self.label_1 = QtWidgets.QLabel(self.tab_1)
        self.label_1.setGeometry(QtCore.QRect(40, 100, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("background-color: none")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(660, 100, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: none")
        self.label_2.setObjectName("label_2")
        self.label_14 = QtWidgets.QLabel(self.tab_1)
        self.label_14.setGeometry(QtCore.QRect(410, 180, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: none")
        self.label_14.setObjectName("label_14")
        self.label_12 = QtWidgets.QLabel(self.tab_1)
        self.label_12.setGeometry(QtCore.QRect(50, 450, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: none")
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.tab_1)
        self.label_11.setGeometry(QtCore.QRect(400, 360, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: none")
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(self.tab_1)
        self.label_9.setGeometry(QtCore.QRect(20, 400, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: none")
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 350, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.label_6.setGeometry(QtCore.QRect(210, 300, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setLineWidth(2)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_1)
        self.label_7.setGeometry(QtCore.QRect(210, 400, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setLineWidth(2)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.tab_1)
        self.label_13.setGeometry(QtCore.QRect(210, 450, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_13.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_13.setLineWidth(2)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_10 = QtWidgets.QLabel(self.tab_1)
        self.label_10.setGeometry(QtCore.QRect(20, 350, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: none")
        self.label_10.setObjectName("label_10")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_1)
        self.textEdit_2.setGeometry(QtCore.QRect(440, 90, 171, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_1)
        self.textEdit_3.setGeometry(QtCore.QRect(730, 90, 151, 31))
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 140, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_17 = QtWidgets.QLabel(self.tab_1)
        self.label_17.setGeometry(QtCore.QRect(90, 250, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: none")
        self.label_17.setObjectName("label_17")
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(210, 250, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: none")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_1)
        self.textEdit_4.setGeometry(QtCore.QRect(210, 350, 181, 31))
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.tab_1)
        self.pushButton.setGeometry(QtCore.QRect(440, 450, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab_1)
        self.textEdit_5.setGeometry(QtCore.QRect(160, 90, 181, 31))
        self.textEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_7 = QtWidgets.QTextEdit(self.tab_1)
        self.textEdit_7.setGeometry(QtCore.QRect(610, 270, 371, 211))
        self.textEdit_7.setStyleSheet("background-color: none")
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_20 = QtWidgets.QLabel(self.tab_1)
        self.label_20.setGeometry(QtCore.QRect(620, 200, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: none")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab_1)
        self.label_21.setGeometry(QtCore.QRect(620, 230, 361, 31))
        self.label_21.setStyleSheet("background-color: none")
        self.label_21.setObjectName("label_21")
        self.label_18 = QtWidgets.QLabel(self.tab_1)
        self.label_18.setGeometry(QtCore.QRect(70, 300, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: none")
        self.label_18.setObjectName("label_18")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_3.setGeometry(QtCore.QRect(760, 520, 141, 41))
        self.pushButton_3.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: none")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_21.setGeometry(QtCore.QRect(200, 130, 93, 28))
        self.pushButton_21.setObjectName("pushButton_21")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(350, 20, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(80, 120, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color:none;")
        self.label_16.setObjectName("label_16")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:none;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit_10 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_10.setGeometry(QtCore.QRect(250, 120, 171, 31))
        self.textEdit_10.setStyleSheet("background-color:none;")
        self.textEdit_10.setObjectName("textEdit_10")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 180, 601, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setStyleSheet("background-color:none;")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget)

        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget.clicked.connect(self.on_click_HH)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 540, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(20)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(500, 540, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(20)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(570, 540, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(20)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(84, 410, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:none;")
        self.label_8.setObjectName("label_8")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_14.setGeometry(QtCore.QRect(430, 470, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x1:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 170, 0, 255));\n"
"")
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(40, 450, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color:none;")
        self.label_19.setObjectName("label_19")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(40, 500, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color:none;")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(70, 550, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color:none;")
        self.label_23.setObjectName("label_23")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(130, 400, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color:none;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_6.setGeometry(QtCore.QRect(130, 500, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setStyleSheet("background-color:none;")
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_8 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_8.setGeometry(QtCore.QRect(130, 450, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_8.setFont(font)
        self.textEdit_8.setStyleSheet("background-color:none;")
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_9.setGeometry(QtCore.QRect(130, 550, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_9.setFont(font)
        self.textEdit_9.setStyleSheet("background-color:none;")
        self.textEdit_9.setObjectName("textEdit_9")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(660, 180, 231, 211))
        self.label_24.setStyleSheet("background-color: none\n"
"")
        self.label_24.setFrameShape(QtWidgets.QFrame.Box)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(50, 160, 661, 451))
        self.tableWidget_3.setStyleSheet("background-color: none")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        self.pushButton_22 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_22.setGeometry(QtCore.QRect(580, 90, 121, 41))
        self.pushButton_22.setStyleSheet("background-color: none")
        self.pushButton_22.setObjectName("pushButton_22")
        self.textEdit_18 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_18.setGeometry(QtCore.QRect(280, 90, 261, 41))
        self.textEdit_18.setStyleSheet("background-color: none")
        self.textEdit_18.setObjectName("textEdit_18")
        self.label_33 = QtWidgets.QLabel(self.tab_3)
        self.label_33.setGeometry(QtCore.QRect(110, 100, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("background-color: none")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.tab_3)
        self.label_34.setGeometry(QtCore.QRect(370, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab)
        self.pushButton_17.setGeometry(QtCore.QRect(480, 90, 93, 28))
        self.pushButton_17.setStyleSheet("background-color: none")
        self.pushButton_17.setObjectName("pushButton_17")
        self.textEdit_12 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_12.setGeometry(QtCore.QRect(230, 90, 231, 31))
        self.textEdit_12.setStyleSheet("background-color: none\n"
"")
        self.textEdit_12.setObjectName("textEdit_12")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(80, 100, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background-color: none")
        self.label_25.setObjectName("label_25")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 150, 611, 441))
        self.tableWidget_2.setStyleSheet("background-color: none\n"
"")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)

        self.tableWidget_2.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget_2.clicked.connect(self.on_click)
        self.textEdit_13 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_13.setGeometry(QtCore.QRect(770, 160, 271, 41))
        self.textEdit_13.setStyleSheet("background-color: none")
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit_14 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_14.setGeometry(QtCore.QRect(770, 230, 271, 41))
        self.textEdit_14.setStyleSheet("background-color: none")
        self.textEdit_14.setObjectName("textEdit_14")
        self.textEdit_15 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_15.setGeometry(QtCore.QRect(770, 300, 271, 41))
        self.textEdit_15.setStyleSheet("background-color: none")
        self.textEdit_15.setObjectName("textEdit_15")
        self.textEdit_16 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_16.setGeometry(QtCore.QRect(770, 360, 271, 41))
        self.textEdit_16.setStyleSheet("background-color: none")
        self.textEdit_16.setObjectName("textEdit_16")
        self.textEdit_17 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_17.setGeometry(QtCore.QRect(770, 440, 271, 41))
        self.textEdit_17.setStyleSheet("background-color: none")
        self.textEdit_17.setObjectName("textEdit_17")
        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setGeometry(QtCore.QRect(730, 170, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background-color: none")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setGeometry(QtCore.QRect(690, 245, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("background-color: none")
        self.label_27.setObjectName("label_27")
        self.label_29 = QtWidgets.QLabel(self.tab)
        self.label_29.setGeometry(QtCore.QRect(690, 310, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("background-color: none")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.tab)
        self.label_30.setGeometry(QtCore.QRect(670, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("background-color: none")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(670, 440, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background-color: none")
        self.label_31.setObjectName("label_31")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab)
        self.pushButton_18.setGeometry(QtCore.QRect(722, 527, 91, 31))
        self.pushButton_18.setStyleSheet("background-color: none;\n"
"")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab)
        self.pushButton_19.setGeometry(QtCore.QRect(840, 527, 91, 31))
        self.pushButton_19.setStyleSheet("background-color: none")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab)
        self.pushButton_20.setGeometry(QtCore.QRect(960, 527, 91, 31))
        self.pushButton_20.setStyleSheet("background-color: none")
        self.pushButton_20.setObjectName("pushButton_20")
        self.label_32 = QtWidgets.QLabel(self.tab)
        self.label_32.setGeometry(QtCore.QRect(400, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.label_28 = QtWidgets.QLabel(self.tab)
        self.label_28.setGeometry(QtCore.QRect(800, 495, 211, 21))
        self.label_28.setStyleSheet("background-color: none;\n"
"color: rgb(255, 0, 0);")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.tabWidget.addTab(self.tab, "")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 20, 141, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-radius:10px;\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 140, 141, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(0, 85, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 260, 141, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(0, 255, 0);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 380, 141, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 85, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 500, 141, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius:10px;")
        self.pushButton_13.setObjectName("pushButton_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.action_BanHang = QtWidgets.QAction(MainWindow)
        self.action_BanHang.setObjectName("action_BanHang")
        self.action_Kho = QtWidgets.QAction(MainWindow)
        self.action_Kho.setObjectName("action_Kho")
        self.actionTG = QtWidgets.QAction(MainWindow)
        self.actionTG.setObjectName("actionTG")
        self.actionTh_ng_tin_n_h_ng = QtWidgets.QAction(MainWindow)
        self.actionTh_ng_tin_n_h_ng.setObjectName("actionTh_ng_tin_n_h_ng")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.action_ng_nh_p = QtWidgets.QAction(MainWindow)
        self.action_ng_nh_p.setObjectName("action_ng_nh_p")
        self.actionTh_m_H_ng_H_a = QtWidgets.QAction(MainWindow)
        self.actionTh_m_H_ng_H_a.setObjectName("actionTh_m_H_ng_H_a")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "     Bán Hàng "))
        self.label_3.setText(_translate("MainWindow", "vnđ"))
        self.label_4.setText(_translate("MainWindow", "Số lượng:"))
        self.label_1.setText(_translate("MainWindow", "Mã sản phẩm:"))
        self.label_2.setText(_translate("MainWindow", "Giá bán:"))
        self.label_14.setText(_translate("MainWindow", "......................................"))
        self.label_12.setText(_translate("MainWindow", "Tiền trả lại:"))
        self.label_11.setText(_translate("MainWindow", "vnđ"))
        self.label_9.setText(_translate("MainWindow", "Tiền khách đưa:"))
        self.pushButton_2.setText(_translate("MainWindow", "Tiền thừa"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "Tiền khách đưa:"))
        self.pushButton_5.setText(_translate("MainWindow", "Tính tiền"))
        self.label_17.setText(_translate("MainWindow", "Mã SP:"))
        self.pushButton.setText(_translate("MainWindow", "Xóa"))
        self.label_20.setText(_translate("MainWindow", "Bill"))
        self.label_21.setText(_translate("MainWindow", "TenSP             Số Lượng            Giá                Tiền"))
        self.label_18.setText(_translate("MainWindow", "Tổng Bill:"))
        self.pushButton_3.setText(_translate("MainWindow", "In bill"))
        self.pushButton_21.setText(_translate("MainWindow", "Kiểm tra"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Bán Hàng"))
        self.label_15.setText(_translate("MainWindow", "    Thông Tin Hàng Hóa"))
        self.label_16.setText(_translate("MainWindow", "Từ khóa liên quan:"))
        self.pushButton_4.setText(_translate("MainWindow", "Tìm"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên SP"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Giá"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Nơi sản xuất"))
        self.pushButton_6.setText(_translate("MainWindow", ""))
        self.pushButton_7.setText(_translate("MainWindow", ""))
        self.pushButton_8.setText(_translate("MainWindow", ""))
        self.label_8.setText(_translate("MainWindow", "ID:"))
        self.pushButton_14.setText(_translate("MainWindow", "Thêm"))
        self.label_19.setText(_translate("MainWindow", "Tên SP:"))
        self.label_22.setText(_translate("MainWindow", "Giá bán:"))
        self.label_23.setText(_translate("MainWindow", "NSX:"))
        self.label_24.setText(_translate("MainWindow", "Ảnh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Thông tin SP"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã Bill"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ngày"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mã Hàng hóa"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Số Lượng"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Giá"))
        self.pushButton_22.setText(_translate("MainWindow", "Tìm"))
        self.label_33.setText(_translate("MainWindow", "Từ khóa liên quan:"))
        self.label_34.setText(_translate("MainWindow", "Thông tin Bill"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Thông tin Bill"))
        self.pushButton_17.setText(_translate("MainWindow", "tìm"))
        self.label_25.setText(_translate("MainWindow", "Từ khóa liên quan:"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên Nhân viên"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Số ĐT"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Giới tính"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Năm sinh"))
        self.label_26.setText(_translate("MainWindow", "ID:"))
        self.label_27.setText(_translate("MainWindow", "Tên NV:"))
        self.label_29.setText(_translate("MainWindow", "Số ĐT:"))
        self.label_30.setText(_translate("MainWindow", "Giới tính:"))
        self.label_31.setText(_translate("MainWindow", "Năm sinh:"))
        self.pushButton_18.setText(_translate("MainWindow", "Thêm"))
        self.pushButton_19.setText(_translate("MainWindow", "Cập nhật"))
        self.pushButton_20.setText(_translate("MainWindow", "Xóa"))
        self.label_32.setText(_translate("MainWindow", "Nhân viên"))
        self.label_28.setText(_translate("MainWindow", "----"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Thông tin nhân viên"))
        self.pushButton_9.setText(_translate("MainWindow", "Bán Hàng"))
        self.pushButton_10.setText(_translate("MainWindow", "Thông tin SP"))
        self.pushButton_11.setText(_translate("MainWindow", "Thông tin Bill"))
        self.pushButton_12.setText(_translate("MainWindow", "Thông tin NV"))
        self.pushButton_13.setText(_translate("MainWindow", "Exit"))
        self.action_BanHang.setText(_translate("MainWindow", "Bán Hàng"))
        self.action_Kho.setText(_translate("MainWindow", "Kho"))
        self.actionTG.setText(_translate("MainWindow", "Tác Giả"))
        self.actionTh_ng_tin_n_h_ng.setText(_translate("MainWindow", "Thông tin đơn hàng"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.action_ng_nh_p.setText(_translate("MainWindow", "Đặng nhập"))
        self.actionTh_m_H_ng_H_a.setText(_translate("MainWindow", "Thêm Hàng Hóa"))





        # tab bán hàng
        self.pushButton_9.clicked.connect(self.showBanHang)
        self.pushButton_5.clicked.connect(self.tinhtiennhan)
        self.pushButton_2.clicked.connect(self.tinhtientru)
        self.pushButton_21.clicked.connect(self.showgiatien)
        self.pushButton.clicked.connect(self.xoa)

        # tab thông tín sản phẩm
        self.pushButton_10.clicked.connect(self.showTTsanpham)
        self.pushButton_4.clicked.connect(self.loaddataHH)
        self.pushButton_14.clicked.connect(self.insertdataHH)
        self.pushButton_7.clicked.connect(self.updatedataHH)
        self.pushButton_8.clicked.connect(self.deletedataHH)


        # tab thông tin bill
        self.pushButton_11.clicked.connect(self.showTTbill)
        self.pushButton_22.clicked.connect(self.showbill)


        # tab thông tin nhân viên
        self.pushButton_12.clicked.connect(self.showTTnhanvien)
        self.pushButton_17.clicked.connect(self.loadTT)
        self.pushButton_18.clicked.connect(self.addTT)
        self.pushButton_19.clicked.connect(self.updateTT)
        self.pushButton_20.clicked.connect(self.deleteTT)


    def on_click(self):
        index = (self.tableWidget_2.selectionModel().currentIndex())
        sid = index.siblingAtColumn(0).data()
        sten = index.siblingAtColumn(1).data()
        ssdt = index.siblingAtColumn(2).data()
        sgt = index.siblingAtColumn(3).data()
        sdc = index.siblingAtColumn(4).data()

        self.textEdit_13.setText(sid)
        self.textEdit_14.setText(sten)
        self.textEdit_15.setText(ssdt)
        self.textEdit_16.setText(sgt)
        self.textEdit_17.setText(sdc)

    def on_click_HH(self):
        index = (self.tableWidget.selectionModel().currentIndex())
        sma = index.siblingAtColumn(0).data()
        sten = index.siblingAtColumn(1).data()
        sgia = index.siblingAtColumn(2).data()
        snsx = index.siblingAtColumn(3).data()

        self.textEdit.setText(sma)
        self.textEdit_8.setText(sten)
        self.textEdit_6.setText(sgia)
        self.textEdit_9.setText(snsx)





    def showTTnhanvien(self):
        self.tabWidget.setCurrentWidget(self.tab)

    def showBanHang(self):
        self.tabWidget.setCurrentWidget(self.tab_1)

    def showTTsanpham(self):
        self.tabWidget.setCurrentWidget(self.tab_2)

    def showTTbill(self):
        self.tabWidget.setCurrentWidget(self.tab_3)

    # .....................................bán hàng...................................................................................
    def xoa(self):
        self.textEdit_5.setText('')
        self.textEdit_2.setText('')
        self.textEdit_3.setText('')
        self.textEdit_4.setText('')
        self.label_5.setText('')
        self.label_6.setText('')
        self.label_7.setText('')
        self.label_13.setText('')

    def showgiatien(self):
        mahh = self.textEdit_5.toPlainText()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Conghuy090701",
            database="quanly123")
        query = "SELECT * FROM hanghoa "
        cur = mydb.cursor()
        cur.execute(query)
        result = cur.fetchall()
        c = ''
        for row in result:
            if row[0] == mahh:
                c = row
        try:
            self.textEdit_3.setText(str(c[2]))
        except:
            self.textEdit_3.setText("không tìm thấy giá")

    def tinhtiennhan(self):
        a = random.randint(100000, 999999)
        copy = self.textEdit_5.toPlainText()
        b = str(copy)
        c = str(self.textEdit_2.toPlainText())
        # show lại màn hình khi đã copy
        self.label_5.setText(copy)

        tien = self.textEdit_2.toPlainText() + "*" + self.textEdit_3.toPlainText()
        try:
            result = eval(tien)
            d = str(result)
            self.label_6.setText(str(result))
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Conghuy090701",
                database="quanly123")

            mycursor = mydb.cursor()

            mycursor.execute("INSERT INTO  thongtin_bill (ma_bill,Ngay,Ma_HH,SoLuong,TongTien) VALUES ( '"+str(a)+"' ,now(), '"+b+"', '"+c+"', '"+d+"')")
            mydb.commit()

        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Lỗi rồi!!!")
            msg.setInformativeText('kiểm tra lại số đi má')
            msg.setWindowTitle("Lỗi")
            msg.exec_()
            return

    def tinhtientru(self):
        copy = self.textEdit_4.toPlainText()
        # show lại màn hình khi đã copy
        self.label_7.setText(copy)
        tien = self.textEdit_4.toPlainText() + "-" + self.textEdit_2.toPlainText() + "*" + self.textEdit_3.toPlainText()
        try:
            result = eval(tien)
            self.label_13.setText(str(result))

        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Lỗi rồi!!!")
            msg.setInformativeText('kiểm tra lại số đi má')
            msg.setWindowTitle("Lỗi")
            msg.exec_()
            return

#.....................................thông tin sản phẩm...............................................................
    def loaddataHH(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Conghuy090701",
            database="quanly123")

        text = self.textEdit_10.toPlainText()
        if text == '':
            query = "SELECT * FROM hanghoa "
            cur = mydb.cursor()
            cur.execute(query)
            result = cur.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            cur.close()
        else:
            query = "SELECT DISTINCT * FROM hanghoa WHERE Ma_HH LIKE '%" + text + "%' OR Ten_HH LIKE '%"+text+"%' OR NSX LIKE '%"+text+"%'"
            cur = mydb.cursor()
            cur.execute(query)
            result = cur.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            cur.close()

    def insertdataHH(self):
        mahh = self.textEdit.toPlainText()
        tenhh = self.textEdit_8.toPlainText()
        gia = self.textEdit_6.toPlainText()
        nsx = self.textEdit_9.toPlainText()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Conghuy090701",
            database="quanly123")

        mycursor = mydb.cursor()
        sql = "SELECT * FROM hanghoa WHERE Ma_HH = '%s'" % (mahh)
        mycursor.execute(sql)
        if mycursor.fetchone():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Trùng mã rồi")
            msg.setInformativeText('kiểm tra lại Mã Háng hóa đi má')
            msg.setWindowTitle("Lỗi")
            msg.exec_()
            return
        elif mahh == '' and tenhh == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Thiếu thông tin rồi")
            msg.setInformativeText('Thêm thông tin đi má')
            msg.setWindowTitle("Lỗi")
            msg.exec_()
            return
        else:
            mycursor.execute("INSERT INTO hanghoa (Ma_HH, Ten_HH, Gia, NSX) VALUES (%s, %s, %s, %s)",
                             (mahh, tenhh, gia, nsx))
            mydb.commit()

    def updatedataHH(self):
        mahh = self.textEdit.toPlainText()
        ten = self.textEdit_8.toPlainText()
        gia = self.textEdit_6.toPlainText()
        nsx = self.textEdit_9.toPlainText()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Conghuy090701",
            database="quanly123")
        mycursor = mydb.cursor()
        sql = "UPDATE hanghoa SET Ten_HH = '"+ten+"', Gia = '"+gia+"',NSX= '"+nsx+"' WHERE Ma_HH = '"+mahh+"'"
        mycursor.execute(sql)
        mydb.commit()

    def deletedataHH(self):
        ten = self.textEdit.toPlainText()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Conghuy090701",
            database="quanly123")
        mycursor = mydb.cursor()
        sql = "DELETE FROM hanghoa WHERE Ma_HH = %s"
        adr = (ten,)
        mycursor.execute(sql, adr)
        mydb.commit()




#............................................thông tin bill.............................................................
    def showbill(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Conghuy090701",
            database="quanly123")

        text = self.textEdit_18.toPlainText()
        if text == '':
            query = "SELECT * FROM thongtin_bill "
            cur = mydb.cursor()
            cur.execute(query)
            result = cur.fetchall()
            self.tableWidget_3.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget_3.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_3.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            cur.close()
        else:
            query = "SELECT DISTINCT * FROM thongtin_bill WHERE ma_bill LIKE '%" + text + "%' OR DATE(Ngay) LIKE '%"+text+"%'"
            cur = mydb.cursor()
            cur.execute(query)
            result = cur.fetchall()
            self.tableWidget_3.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget_3.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_3.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            cur.close()



    # .....................................thông tin nhân viên.........................................................................

    def loadTT(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Conghuy090701",
            database="quanly123")

        text = self.textEdit_12.toPlainText()
        if text == '':
            query = "SELECT * FROM nhan_vien "
            cur = mydb.cursor()
            cur.execute(query)
            result = cur.fetchall()
            self.tableWidget_2.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget_2.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            cur.close()
        else:
            query = "SELECT DISTINCT * FROM nhan_vien WHERE ID LIKE '%" + text + "%' OR TenNV LIKE '%" + text + "%'"
            cur = mydb.cursor()
            cur.execute(query)
            result = cur.fetchall()
            self.tableWidget_2.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget_2.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            cur.close()

    def addTT(self):
        id = self.textEdit_13.toPlainText()
        ten = self.textEdit_14.toPlainText()
        sdt = self.textEdit_15.toPlainText()
        gt = self.textEdit_16.toPlainText()
        nam = self.textEdit_17.toPlainText()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Conghuy090701",
            database="quanly123")

        mycursor = mydb.cursor()
        sql = "SELECT * FROM nhan_vien WHERE ID = '%s'" % (id)
        mycursor.execute(sql)
        if mycursor.fetchone():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Trùng ID rồi")
            msg.setInformativeText('Kiểm tra lại ID đi má')
            msg.setWindowTitle("Lỗi")
            msg.exec_()
            return
        elif id == '' and ten == '' and sdt == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Thiếu thông tin rồi")
            msg.setInformativeText('Thêm thông tin đi má')
            msg.setWindowTitle("Lỗi")
            msg.exec_()
            return
        else:
            mycursor.execute("INSERT INTO nhan_vien (ID, TenNV, SDT, GT, DiaChi) VALUES (%s, %s, %s, %s, %s)",
                             (id, ten, sdt, gt, nam))
            mydb.commit()
            self.label_28.setText("đã thêm thành công")

    def updateTT(self):
        id = self.textEdit_13.toPlainText()
        ten = self.textEdit_14.toPlainText()
        sdt = self.textEdit_15.toPlainText()
        gt = self.textEdit_16.toPlainText()
        nam = self.textEdit_17.toPlainText()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Conghuy090701",
            database="quanly123")
        mycursor = mydb.cursor()
        sql = "UPDATE nhan_vien SET TenNV = '"+ten+"', SDT = '"+sdt+"',GT= '"+gt+"', DiaChi = '"+nam+"' WHERE ID = '"+id+"'"
        mycursor.execute(sql)
        mydb.commit()
        self.label_28.setText("đã cập nhật")



    def deleteTT(self):
        ten = self.textEdit_14.toPlainText()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Conghuy090701",
            database="quanly123")
        mycursor = mydb.cursor()
        sql = "DELETE FROM nhan_vien WHERE TenNV = %s"
        adr = (ten,)
        mycursor.execute(sql, adr)
        mydb.commit()
        self.label_28.setText("đã xóa")







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
