'''
Hank Lee maintain in 2021/08/04
'''

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QTableWidgetItem
#from PyQt5 import  QtGui,QtCore
from te import *
import telnetlib
import threading
import math
import time
import numpy as np
import io
import pyperclip
import paramiko


# Command Line for SSH and Telnet
commend = '/usr/sbin/venc'              # Run venc
commend2 = '/etc/init.d/venc stop'      # Stop venc
commend3 = 'imgsys_test -l 10000000'    # Open DNS tuning log
commend4 = '/etc/init.d/rtsps restart'    # Open DNS tuning log

'''Open a thread for get string'''
# Telnet connection
def command(con, flag, str_=""):
    data = con.read_until(flag.encode())
    print(data.decode(errors='ignore'))
    con.write(str_.encode() + b"\n")
    return data

class StringGet_Telnet:
    def __init__(self):
        self.stopped = False
        self.ip = ""
        self.username = ""
        self.password = ""
        self.uiAperture = 0
        self.uiExpTime = 0
        self.uiGain = 0
        self.Ymean = 0
        self.R_Gain = 0.0
        self.B_Gain = 0.0
        self.Alldata = np.array([0, 0, 0, 0, 0, 0])
        self.waitFlag = 0
        self.close_flag = 0
        self.overEX_flag = 0

    def start(self):

        threading.Thread(target=self.get_data, args=()).start()
    def connect(self):
        # Build telnet object

        #Front view
        self.tn = telnetlib.Telnet(self.ip, port=23)
        command(self.tn, "", self.username)
        command(self.tn, "", self.password)

        #For other commend
        self.tn2 = telnetlib.Telnet(self.ip, port=23)
        command(self.tn2, "", self.username)
        command(self.tn2, "", self.password)


    def get_data(self):
        self.connect()
        print("Connect success!")

        #Commend Process
        command(self.tn, "", commend2)  #  ""  or   "~ # "
        print("Stop venc  " + commend2)
        time.sleep(6.0)
        command(self.tn, "", commend)
        print("Start venc  "+commend)
        time.sleep(10.0)
        command(self.tn2, "", commend3)
        print("Start log  " + commend3)
        time.sleep(1.0)
        command(self.tn2, "", commend4)
        print("Reflash streaming   " + commend4)


        self.Alldata=self.Alldata.astype(np.float32)
        while True:
            data = self.tn.read_until("\n".encode())
            print(data.decode('ascii'))
            # we can search the 1st variable to get the data we want

            for i in range(0,len(data.decode('ascii'))+1):
                #wating
                if (data.decode('ascii')[i:i + 6] == 'wating'):
                    self.waitFlag = 1
                    time.sleep(0.3)
                    continue
                else:
                    self.waitFlag = 0

                # Explosure info
                if (data.decode('ascii')[i:i + 10] == 'uiAperture'):
                    self.uiAperture = int(data.decode('ascii')[i + 12:i + 18])
                    self.Alldata[0] = self.uiAperture
                    self.Alldata[0] = int(self.Alldata[0])
                    #print("uiAperture = {:.0f} ".format(self.uiAperture))
                    #print("self.Alldata[0] = {:.0f} ".format(self.Alldata[0]))

                if (data.decode('ascii')[i:i + 9] == 'uiExpTime'):
                    self.uiExpTime = int(data.decode('ascii')[i + 11:i + 17])
                    self.Alldata[1] = self.uiExpTime
                    self.Alldata[1] = int(self.Alldata[1])


                if (data.decode('ascii')[i:i + 6] == 'uiGain'):
                    self.uiGain = int(data.decode('ascii')[i + 8:i + 12])
                    self.Alldata[2] = self.uiGain
                    self.Alldata[2] = int(self.Alldata[2])
                    i = len(data.decode('ascii'))

                if (data.decode('ascii')[i:i + 9] == 'YMean_del'):
                    self.Ymean = int(data.decode('ascii')[i + 11:i + 15])
                    self.Alldata[3] = self.Ymean
                    self.Alldata[3] = int(self.Alldata[3])
                    i = len(data.decode('ascii'))


                # data collection
                if(data.decode('ascii')[i:i+6] == 'R_Gain') :
                    self.R_Gain = float(data.decode('ascii')[i+8:i+15])
                    self.Alldata[4] =  self.R_Gain

                if (data.decode('ascii')[i:i + 6] == 'B_Gain'):
                    self.B_Gain = float(data.decode('ascii')[i + 8:i + 15])
                    self.Alldata[5] = self.B_Gain

                    i = len(data.decode('ascii'))

                #print(self.Alldata[:])

                #To notice over/under explosure
                if (data.decode('ascii')[i:i + 5] == 'There'):
                    self.overEX_flag = 1
                    time.sleep(0.3)
                    continue
                else:
                    self.overEX_flag = 0

                #dis connect the machine
                if(self.close_flag == 1 ):
                    command(self.tn2, "", commend2)
                    print("Stop venc  " + commend2)
                    self.stop()
                    break

        command(self.tn, "", " exit")
        self.tn.close()

    def stop(self):
        self.stopped = True

    def get_AccountInfo(self,string_username, string_password, string_ip):
        self.username = string_username
        self.password = string_password
        self.ip = string_ip
        print(self.username)
        print(self.password)
        print(self.ip)






# SSH connection
class StringGet_SSH:
    def __init__(self):
        self.stopped = False
        self.ip = ""
        self.username = ""
        self.password = ""
        self.uiAperture = 0
        self.uiExpTime = 0
        self.uiGain = 0
        self.Ymean = 0
        self.R_Gain = 0.0
        self.B_Gain = 0.0
        self.Alldata = np.array([0, 0, 0, 0, 0, 0])
        self.waitFlag = 0
        self.close_flag = 0
        self.overEX_flag = 0

    def start(self):

        threading.Thread(target=self.get_data, args=()).start()
    def connect(self):
        # Build a ssh Object
        self.client = paramiko.SSHClient()
        # Allow to connect the host in 'know_hosts' list
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connecting
        self.client.connect(hostname=self.ip, port=22, username=self.username, password=self.password)



    def get_data(self):
        self.connect()

        #Commend Process
        stdin_stop, stdout_stop, stderr_stop = self.client.exec_command(commend2, get_pty=True)
        print("Stop venc  " + commend2)
        time.sleep(6.0)
        stdin, stdout, stderr = self.client.exec_command(commend, get_pty=True)
        print("Start venc  "+commend)
        time.sleep(10.0)
        stdin_log, stdout_log, stderr_log = self.client.exec_command(commend3, get_pty=True)
        print("Start log  " + commend3)
        time.sleep(1.0)
        stdin_rtsps, stdout_rtsps, stderr_rtsps = self.client.exec_command(commend4, get_pty=True)
        print("Reflash streaming  " + commend3)
        time.sleep(1.0)

        self.Alldata=self.Alldata.astype(np.float32)
        for line in iter(stdout.readline, ""):
            print(line, end="")
            data = line
            for i in range(0, len(data) + 1):
                # wating
                if (data[i:i + 6] == 'wating'):
                    self.waitFlag = 1
                    time.sleep(1)
                    continue
                else:
                    self.waitFlag = 0

                # Explosure info
                if (data[i:i + 10] == 'uiAperture'):
                    self.uiAperture = int(data[i + 12:i + 18])
                    self.Alldata[0] = self.uiAperture
                    self.Alldata[0] = int(self.Alldata[0])
                    # print("uiAperture = {:.0f} ".format(self.uiAperture))
                    # print("self.Alldata[0] = {:.0f} ".format(self.Alldata[0]))

                if (data[i:i + 9] == 'uiExpTime'):
                    self.uiExpTime = int(data[i + 11:i + 17])
                    self.Alldata[1] = self.uiExpTime
                    self.Alldata[1] = int(self.Alldata[1])

                if (data[i:i + 6] == 'uiGain'):
                    self.uiGain = int(data[i + 8:i + 12])
                    self.Alldata[2] = self.uiGain
                    self.Alldata[2] = int(self.Alldata[2])
                    i = len(data)

                if (data[i:i + 9] == 'YMean_del'):
                    self.Ymean = int(data[i + 11:i + 15])
                    self.Alldata[3] = self.Ymean
                    self.Alldata[3] = int(self.Alldata[3])
                    i = len(data)

                # data collection
                if (data[i:i + 6] == 'R_Gain'):
                    self.R_Gain = float(data[i + 8:i + 15])
                    self.Alldata[4] = self.R_Gain

                if (data[i:i + 6] == 'B_Gain'):
                    self.B_Gain = float(data[i + 8:i + 15])
                    self.Alldata[5] = self.B_Gain

                    i = len(data)

                # print(self.Alldata[:])

                # To notice over/under explosure
                if (data[i:i + 5] == 'There'):
                    self.overEX_flag = 1
                    time.sleep(0.3)
                    continue
                else:
                    self.overEX_flag = 0

                # dis connect the machine
                if (self.close_flag == 1):
                    stdin, stdout, stderr = self.client.exec_command(commend2, get_pty=True)
                    print("Stop venc  " + commend2)
                    self.stop()
                    break

    def stop(self):
        self.stopped = True

    def get_AccountInfo(self,string_username, string_password, string_ip):
        self.username = string_username
        self.password = string_password
        self.ip = string_ip
        print(self.username)
        print(self.password)
        print(self.ip)


# Main HMI
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.connectButton.clicked.connect(self.thread_getdata)
        self.Record_Day_Button.clicked.connect(self.record_day_data)
        self.Record_Night_Button_2.clicked.connect(self.record_night_data)
        self.Record_Night_Button_0.clicked.connect(self.record_night_data_0IR)
        self.Record_Night_Button_4.clicked.connect(self.clear_night_data)
        self.Record_Night_Button_5.clicked.connect(self.record_night_data_IRMAX)

        #Decide connect object
        self.getData_SSH = StringGet_SSH()
        self.getData_Telnet = StringGet_Telnet()
        self.getData = self.getData_Telnet      #Copy

        self.show_count = 0
        # install event filter
        self.tableWidget_2.installEventFilter(self)
        self.tableWidget_3.installEventFilter(self)

        self.text =""
        self.IR_P = 0
        self.IR_P_flag = 0
        self.ShowBlowser_flag = 0


        # IR IP
        self.Aperatue_0IR = 0.0
        self.ExpTime_0IR = 0.0
        self.Gain_0IR = 0.0
        self.Ymean_0IR = 0.0
        # Record now data
        self.Aperatue_IR_now = 0.0
        self.ExpTime_IR_now = 0.0
        self.Gain_IR_now = 0.0
        self.Ymean_IR_now = 0.0
        self.all_0IR = 0.0
        self.all_m = 0.0
        self.Aperatue_m = 0.0
        self.ExpTime_m = 0.0
        self.Gain_m = 0.0

    def closeEvent(self, event):   #Close window
        self.getData.close_flag = 1

        if( self.ShowBlowser_flag == 1):
           threading.Thread(target=self.show2browser, args=()).join()  # Wait for this thread close
           QApplication.closeAllWindows()


    def thread_getdata(self):
        self.ShowBlowser_flag = 1

        if self.radioButton_ssh.isChecked() == True:
            self.getData = self.getData_SSH
            print("SSH connecting")
        else:
            print("Telnet connecting")


        #Connection
        str_ip = self.ipEdit.toPlainText()
        str_username = self.ipEdit_username.toPlainText()
        str_password = self.ipEdit_password.toPlainText()
        self.getData.get_AccountInfo(str_username, str_password, str_ip)
        self.getData.start()

        #show
        threading.Thread(target=self.show2browser, args=()).start()



    def record_day_data(self):
        LightSouceIndex = 0
        if self.A_radioButton.isChecked() == True:
                LightSouceIndex = 0
        elif self.D65_radioButton.isChecked() == True:
                LightSouceIndex = 1
        elif self.TL84_radioButton.isChecked() == True:
                LightSouceIndex = 2
        elif self.CWF_radioButton.isChecked() == True:
                LightSouceIndex = 3
        else:
                pass

        for i in range(0, 6):
            self.tableWidget_2.setItem(LightSouceIndex, i, QTableWidgetItem(str(self.getData.Alldata[i])))

    def record_night_data_0IR(self):

        for i in range(0, 6):
            self.tableWidget_3.setItem(0, i, QTableWidgetItem(str(self.getData.Alldata[i])))

        # Open IR probability calculation
        self.IR_P_flag = 1

    def record_night_data_IRMAX(self):

        for i in range(0, 6):
            self.tableWidget_3.setItem(10, i, QTableWidgetItem(str(self.getData.Alldata[i])))

    def record_night_data(self):
        Tolerance = 3 # +-3%
        Recordlevel = 10
        for Recordlevel in range(10,100,10):
            if self.IR_P > (Recordlevel - Tolerance) and self.IR_P < (Recordlevel + Tolerance):
                for i in range(0, 6):
                    self.tableWidget_3.setItem((Recordlevel/10), i, QTableWidgetItem(str(self.getData.Alldata[i])))


    def clear_night_data(self):
        self.tableWidget_3.clearContents()
        print("clear all data in night mode \n")

        # Close IR probability calculation
        self.IR_P_flag = 0



    # add event filter
    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress and
                event.matches(QtGui.QKeySequence.Copy)):
            self.copySelection()
            return True
        return super(MyMainWindow, self).eventFilter(source, event)

    def copySelection(self):
        clipboardString = io.StringIO()
        clipboardString2 = io.StringIO()
        # day mode data
        selectedIndexes = self.tableWidget_2.selectedIndexes()
        selectedIndexes2 = self.tableWidget_3.selectedIndexes()

        if selectedIndexes :
            countList = len(selectedIndexes)
            for r in range(countList):
                #print(r)
                current = selectedIndexes[r]
                displayText = current.data(QtCore.Qt.DisplayRole)
                if r + 1 < countList:
                    next_ = selectedIndexes[r + 1]
                    if next_.row() != current.row():
                        displayText += ("\n")
                    else:
                        displayText += ("\t")
                    #print(displayText)
                clipboardString.write(displayText)
            pyperclip.copy(clipboardString.getvalue())
        else :
            print("Not day mode data\n")

        # night mode data  ----------  must have valus , or it well  fail to copy!!!!!!!!!
        if selectedIndexes2 :
            countList2 = len(selectedIndexes2) #choose num

            for rr in range(countList2):
                #print(rr)  #6
                current2 = selectedIndexes2[rr]
                displayText2 = current2.data(QtCore.Qt.DisplayRole)
                #print(displayText2)  #none

                if displayText2 == None :   #Dont know why it will fail but day_mode won't.....
                    continue

                if rr + 1 < countList2 :
                    next2_ = selectedIndexes2[rr + 1]
                    if next2_.row() != current2.row():
                        displayText2 += ("\n")
                    else:
                        displayText2 += ("\t")


                clipboardString2.write(displayText2)

            pyperclip.copy(clipboardString2.getvalue())

        else:
            print("Not night mode data\n")


    def IR_P_caculation(self):
        try:
            self.IR_P = 0      #Private code
            self.IRP_text = str(round(self.IR_P,2))
        except:
            print("AttributeError: 'NoneType' object has no attribute 'text ,because we clear up data in night mode")
            pass


    def show2browser(self):
        #initial
        self.IRP_text = " "
        self.label_message.setText(self.text)
        self.IRP_label.setText(self.IRP_text)
        self.IRP_label.setStyleSheet('color: red')
        self.IRP_label.setFont(QtGui.QFont("Times",13, QtGui.QFont.Bold))
        self.IRP_label.setAlignment(QtCore.Qt.AlignCenter)

        self.text = " "
        self.label_message.setText(self.text)
        self.label_message.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.label_message.setAlignment(QtCore.Qt.AlignCenter)


        while True:
            if self.getData.waitFlag :
                self.text = "Please wait for table stable !"
                self.label_message.setText(self.text)
                #self.label_message.setStyleSheet('color: red')
                time.sleep(2.0)
            elif self.getData.overEX_flag:
                self.text = "There're over/under exposure blocks!!"
                self.label_message.setText(self.text)
                # self.label_message.setStyleSheet('color: red')
                time.sleep(2.0)
            else :
                self.text = "You can record it !"
                self.label_message.setText(self.text)
                #self.label_message.setStyleSheet('color: gray')

                if self.IR_P_flag == 1:
                    self.IRP_text = "0"
                    self.IR_P_caculation()
                    self.IRP_label.setText(self.IRP_text+" % ")
                else:
                    self.IRP_text = "0"
                    self.IRP_label.setText(self.IRP_text + " % ")


if __name__ == "__main__":

    #HMI
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())