# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\darsh\darshapp\startup.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import changecom,chngpd,compmstr,dbbms,invoice,partymstr,productmstr,salesregister,error
from mysql import connector


class Ui_startup(object):
    def setupUi(self, startup):
        self.mydb = connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="filedb"
        )
        startup.setObjectName("startup")
        startup.resize(450, 250)
        self.unb = QtWidgets.QLabel(startup)
        self.unb.setGeometry(QtCore.QRect(50, 50, 110, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.unb.setFont(font)
        self.unb.setObjectName("unb")
        self.pw = QtWidgets.QLabel(startup)
        self.pw.setGeometry(QtCore.QRect(50, 135, 110, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pw.setFont(font)
        self.pw.setObjectName("pw")
        self.unbw = QtWidgets.QLineEdit(startup)
        self.unbw.setGeometry(QtCore.QRect(200, 50, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.unbw.setFont(font)
        self.unbw.setClearButtonEnabled(True)
        self.unbw.setObjectName("unbw")
        self.pww = QtWidgets.QLineEdit(startup)
        self.pww.setGeometry(QtCore.QRect(200, 140, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pww.setFont(font)
        self.pww.setClearButtonEnabled(True)
        self.pww.setObjectName("pww")
        self.pww.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.pww.setStyleSheet('lineedit-password-character: 65290')
        self.lgb = QtWidgets.QPushButton(startup)
        self.lgb.setGeometry(QtCore.QRect(250, 200, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lgb.setFont(font)
        self.lgb.setObjectName("lgb")
        self.rstb = QtWidgets.QPushButton(startup)
        self.rstb.setGeometry(QtCore.QRect(100, 200, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rstb.setFont(font)
        self.rstb.setObjectName("rstb")

        self.retranslateUi(startup)
        self.rstb.clicked.connect(self.unbw.clear)
        self.rstb.clicked.connect(self.pww.clear)
        self.lgb.clicked.connect(self.logindb)
        QtCore.QMetaObject.connectSlotsByName(startup)

    def logindb(self):
        cur = self.mydb.cursor()
        unbwr=self.unbw.text()
        pwwr = self.pww.text()
        cur.execute("SELECT * FROM users where UserName=%s and Password=%s", (unbwr,pwwr,))
        myresult = cur.fetchone()
        #print(myresult)
        if myresult is None:
            self.err = QtWidgets.QDialog()
            self.ui=error.Ui_Dialog()
            self.ui.setupUi(self.err)
            self.unbw.clear()
            self.pww.clear()
            self.err.show()
        else:
            self.bms = QtWidgets.QMainWindow()
            self.ui=dbbms.Ui_MainWindow()
            self.ui.setupUi(self.bms)
            startup.hide()
            self.bms.show()
        
            
    def retranslateUi(self, startup):
        _translate = QtCore.QCoreApplication.translate
        startup.setWindowTitle(_translate("startup", "Dialog"))
        self.rstb.setText(_translate("startup", "RESET"))
        self.lgb.setText(_translate("startup", "LOGIN"))
        self.unb.setText(_translate("startup", "USERNAME"))
        self.pw.setText(_translate("startup", "PASSWORD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)  
    startup = QtWidgets.QDialog()
    ui = Ui_startup()
    ui.setupUi(startup)
    startup.show()
    sys.exit(app.exec_())