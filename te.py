# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'te.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(340, 30, 91, 31))
        self.connectButton.setObjectName("connectButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ipEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.ipEdit.setGeometry(QtCore.QRect(90, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ipEdit.setFont(font)
        self.ipEdit.setObjectName("ipEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 321, 31))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 170, 411, 21))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(102)
        self.A_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.A_radioButton.setGeometry(QtCore.QRect(60, 200, 83, 16))
        self.A_radioButton.setText("")
        self.A_radioButton.setObjectName("A_radioButton")
        self.D65_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.D65_radioButton.setGeometry(QtCore.QRect(160, 200, 83, 16))
        self.D65_radioButton.setText("")
        self.D65_radioButton.setObjectName("D65_radioButton")
        self.TL84_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.TL84_radioButton.setGeometry(QtCore.QRect(250, 200, 83, 16))
        self.TL84_radioButton.setText("")
        self.TL84_radioButton.setObjectName("TL84_radioButton")
        self.CWF_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.CWF_radioButton.setGeometry(QtCore.QRect(360, 200, 83, 16))
        self.CWF_radioButton.setText("")
        self.CWF_radioButton.setObjectName("CWF_radioButton")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(440, 110, 671, 151))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(31)
        self.Record_Day_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Record_Day_Button.setGeometry(QtCore.QRect(340, 220, 81, 31))
        self.Record_Day_Button.setObjectName("Record_Day_Button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 70, 321, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 270, 431, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, 300, 391, 31))
        self.label_5.setObjectName("label_5")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(440, 340, 655, 370))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(10, item)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(31)
        self.Record_Night_Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Record_Night_Button_2.setGeometry(QtCore.QRect(340, 380, 81, 31))
        self.Record_Night_Button_2.setObjectName("Record_Night_Button_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 600, 411, 141))
        self.groupBox.setObjectName("groupBox")
        self.label_message = QtWidgets.QLabel(self.groupBox)
        self.label_message.setGeometry(QtCore.QRect(10, 60, 391, 31))
        self.label_message.setTextFormat(QtCore.Qt.AutoText)
        self.label_message.setObjectName("label_message")
        self.IRP_label = QtWidgets.QLabel(self.centralwidget)
        self.IRP_label.setGeometry(QtCore.QRect(240, 380, 71, 51))
        self.IRP_label.setObjectName("IRP_label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 350, 431, 31))
        self.label_7.setObjectName("label_7")
        self.Record_Night_Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Record_Night_Button_0.setGeometry(QtCore.QRect(340, 300, 81, 31))
        self.Record_Night_Button_0.setObjectName("Record_Night_Button_0")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 390, 141, 31))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 420, 391, 81))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 450, 391, 81))
        self.label_9.setObjectName("label_9")
        self.Record_Night_Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Record_Night_Button_4.setGeometry(QtCore.QRect(340, 470, 81, 31))
        self.Record_Night_Button_4.setObjectName("Record_Night_Button_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 500, 391, 81))
        self.label_10.setObjectName("label_10")
        self.Record_Night_Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Record_Night_Button_5.setGeometry(QtCore.QRect(340, 560, 81, 31))
        self.Record_Night_Button_5.setObjectName("Record_Night_Button_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(980, 730, 141, 21))
        self.label_11.setObjectName("label_11")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 10, 81, 81))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_ssh = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_ssh.setGeometry(QtCore.QRect(10, 20, 83, 16))
        self.radioButton_ssh.setObjectName("radioButton_ssh")
        self.radioButton_telnet = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_telnet.setGeometry(QtCore.QRect(10, 50, 83, 16))
        self.radioButton_telnet.setIconSize(QtCore.QSize(16, 16))
        self.radioButton_telnet.setObjectName("radioButton_telnet")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 40, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.ipEdit_username = QtWidgets.QTextEdit(self.centralwidget)
        self.ipEdit_username.setGeometry(QtCore.QRect(90, 40, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ipEdit_username.setFont(font)
        self.ipEdit_username.setObjectName("ipEdit_username")
        self.ipEdit_password = QtWidgets.QTextEdit(self.centralwidget)
        self.ipEdit_password.setGeometry(QtCore.QRect(90, 70, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ipEdit_password.setFont(font)
        self.ipEdit_password.setObjectName("ipEdit_password")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(690, 0, 421, 81))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "IP "))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:13pt;\">1.記錄各色光於day mode的數值</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "D65"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TL84"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CWF"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "A_DAY"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "D65_DAY"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "TL84_DAY"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "CWF_DAY"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Aperture"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ExpTime"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Gain"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ymean_all"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Rgain"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Bgain"))
        self.Record_Day_Button.setText(_translate("MainWindow", "1. Record"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Day mode data</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:13pt;\">2.記錄各色光於night mode下不開IR LED的數值(0% IR)</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Night mode data(A , D65 ,TL84, CWF)</span></p></body></html>"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "IRLV0"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "IRLV1"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "IRLV2"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "IRLV3"))
        item = self.tableWidget_3.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "IRLV4"))
        item = self.tableWidget_3.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "IRLV5"))
        item = self.tableWidget_3.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "IRLV6"))
        item = self.tableWidget_3.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "IRLV7"))
        item = self.tableWidget_3.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "IRLV8"))
        item = self.tableWidget_3.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "IRLV9"))
        item = self.tableWidget_3.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "IRMAX"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Aperture"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ExpTime"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Gain"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ymean_all"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Rgain"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Bgain"))
        self.Record_Night_Button_2.setText(_translate("MainWindow", "3. Record"))
        self.groupBox.setTitle(_translate("MainWindow", "Message"))
        self.label_message.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Welcome</span></p></body></html>"))
        self.IRP_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">IR_P</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:13pt;\">3.記錄各色光於night mode下開IR LED的數值(10-90% IR)</span></p></body></html>"))
        self.Record_Night_Button_0.setText(_translate("MainWindow", "2. Record"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:15pt; font-weight:600;\">IR Probability : </span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:13pt;\">4.清除已記錄完該色光的資料，並換下一個色光，</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:13pt;\">重複步驟二</span></p></body></html>"))
        self.Record_Night_Button_4.setText(_translate("MainWindow", "4. Clear"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:13pt;\">5.最後維持IR燈並關掉燈箱螢幕紀錄IR_MAX的點</span></p></body></html>"))
        self.Record_Night_Button_5.setText(_translate("MainWindow", "5. Record"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-style:italic; color:#0000ff;\">made with QT by IOD</span></p></body></html>"))
        self.radioButton_ssh.setText(_translate("MainWindow", "SSH"))
        self.radioButton_telnet.setText(_translate("MainWindow", "Telnet"))
        self.label_12.setText(_translate("MainWindow", "Username"))
        self.label_13.setText(_translate("MainWindow", "Password"))
        self.label_15.setText(_translate("MainWindow", "DNS TUNING HMI"))