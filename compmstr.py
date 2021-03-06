# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\darsh\darshapp\compmstr.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import nochng,updated
import qtmodern.styles
import qtmodern.windows


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.mydb = sqlite3.connect('filedb.sqlite')
        self.cur= self.mydb.cursor()
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 690)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.ifsccw = QtWidgets.QLineEdit(Dialog)
        self.ifsccw.setGeometry(QtCore.QRect(150, 490, 300, 25))
        self.ifsccw.setObjectName("ifsccw")
        self.branchw = QtWidgets.QLineEdit(Dialog)
        self.branchw.setGeometry(QtCore.QRect(150, 520, 300, 25))
        self.branchw.setObjectName("branchw")
        self.lm = QtWidgets.QLabel(Dialog)
        self.lm.setGeometry(QtCore.QRect(30, 550, 100, 25))
        self.lm.setObjectName("lm")
        self.mfg = QtWidgets.QLabel(Dialog)
        self.mfg.setGeometry(QtCore.QRect(30, 65, 420, 25))
        self.mfg.setObjectName("mfg")
        self.code = QtWidgets.QLabel(Dialog)
        self.code.setGeometry(QtCore.QRect(390, 250, 50, 25))
        self.code.setObjectName("code")
        self.address = QtWidgets.QLabel(Dialog)
        self.address.setGeometry(QtCore.QRect(30, 130, 420, 25))
        self.address.setObjectName("address")
        self.bacolor = QtWidgets.QPushButton(Dialog)
        self.bacolor.setGeometry(QtCore.QRect(150, 590, 100, 30))
        self.bacolor.setObjectName("bacolor")
        self.bacno = QtWidgets.QLabel(Dialog)
        self.bacno.setGeometry(QtCore.QRect(30, 460, 110, 25))
        self.bacno.setObjectName("bacno")
        self.ifscc = QtWidgets.QLabel(Dialog)
        self.ifscc.setGeometry(QtCore.QRect(30, 490, 110, 25))
        self.ifscc.setObjectName("ifscc")
        self.mnow = QtWidgets.QLineEdit(Dialog)
        self.mnow.setGeometry(QtCore.QRect(150, 400, 300, 25))
        self.mnow.setObjectName("mnow")
        self.comnmw = QtWidgets.QLineEdit(Dialog)
        self.comnmw.setGeometry(QtCore.QRect(30, 30, 420, 25))
        self.comnmw.setObjectName("comnmw")
        self.billpre = QtWidgets.QLabel(Dialog)
        self.billpre.setGeometry(QtCore.QRect(340, 320, 100, 25))
        self.billpre.setObjectName("billpre")
        self.mno = QtWidgets.QLabel(Dialog)
        self.mno.setGeometry(QtCore.QRect(30, 400, 110, 25))
        self.mno.setObjectName("mno")
        self.bacnow = QtWidgets.QLineEdit(Dialog)
        self.bacnow.setGeometry(QtCore.QRect(150, 460, 300, 25))
        self.bacnow.setObjectName("bacnow")
        self.gstuid = QtWidgets.QLabel(Dialog)
        self.gstuid.setGeometry(QtCore.QRect(30, 320, 300, 25))
        self.gstuid.setObjectName("gstuid")
        self.state = QtWidgets.QLabel(Dialog)
        self.state.setGeometry(QtCore.QRect(30, 250, 350, 25))
        self.state.setObjectName("state")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 630, 480, 60))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.save = QtWidgets.QPushButton(self.frame)
        self.save.setGeometry(QtCore.QRect(230, 10, 100, 30))
        self.save.setObjectName("save")
        self.close = QtWidgets.QPushButton(self.frame)
        self.close.setGeometry(QtCore.QRect(350, 10, 100, 30))
        self.close.setObjectName("close")
        self.comnm = QtWidgets.QLabel(Dialog)
        self.comnm.setGeometry(QtCore.QRect(30, 0, 420, 25))
        self.comnm.setObjectName("comnm")
        self.bnm = QtWidgets.QLabel(Dialog)
        self.bnm.setGeometry(QtCore.QRect(30, 430, 110, 25))
        self.bnm.setObjectName("bnm")
        self.bnmw = QtWidgets.QLineEdit(Dialog)
        self.bnmw.setGeometry(QtCore.QRect(150, 430, 300, 25))
        self.bnmw.setObjectName("bnmw")
        self.codew = QtWidgets.QLineEdit(Dialog)
        self.codew.setGeometry(QtCore.QRect(390, 280, 60, 25))
        self.codew.setReadOnly(True)
        self.codew.setObjectName("codew")
        self.addressw = QtWidgets.QTextEdit(Dialog)
        self.addressw.setGeometry(QtCore.QRect(30, 160, 420, 75))
        self.addressw.setObjectName("addressw")
        self.pacolor = QtWidgets.QPushButton(Dialog)
        self.pacolor.setGeometry(QtCore.QRect(270, 590, 100, 30))
        self.pacolor.setObjectName("pacolor")
        self.branch = QtWidgets.QLabel(Dialog)
        self.branch.setGeometry(QtCore.QRect(30, 520, 110, 25))
        self.branch.setObjectName("branch")
        self.mfgw = QtWidgets.QLineEdit(Dialog)
        self.mfgw.setGeometry(QtCore.QRect(30, 95, 420, 25))
        self.mfgw.setObjectName("mfgw")
        self.statew = QtWidgets.QComboBox(Dialog)
        self.statew.setGeometry(QtCore.QRect(30, 280, 350, 25))
        self.statew.activated.connect(self.chngcod)
        self.statew.setObjectName("statew")
        self.lmw = QtWidgets.QLineEdit(Dialog)
        self.lmw.setGeometry(QtCore.QRect(150, 550, 80, 25))
        self.lmw.setObjectName("lmw")
        self.billprew = QtWidgets.QLineEdit(Dialog)
        self.billprew.setGeometry(QtCore.QRect(340, 360, 110, 25))
        self.billprew.setObjectName("billprew")
        self.gstuidw = QtWidgets.QLineEdit(Dialog)
        self.gstuidw.setGeometry(QtCore.QRect(30, 360, 300, 25))
        self.gstuidw.setObjectName("gstuidw")
        self.cur.execute("Select * from statename")
        myresult= self.cur.fetchall()
        for i in myresult:
            self.statew.addItem(i[1])
        self.retranslateUi(Dialog)
        self.close.clicked.connect(Dialog.close)
        self.save.clicked.connect(self.saveDetails)
        QtCore.QMetaObject.connectSlotsByName(Dialog)                                                                                                                       
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "COMPANY MASTER"))
        self.lm.setText(_translate("Dialog", "Left Margin"))
        self.mfg.setText(_translate("Dialog", "Mfg/Supplier Of."))
        self.code.setText(_translate("Dialog", "Code"))
        self.address.setText(_translate("Dialog", "Address"))
        self.bacolor.setText(_translate("Dialog", "Back Color"))
        self.bacno.setText(_translate("Dialog", "Bank A/C No."))
        self.ifscc.setText(_translate("Dialog", "IFSC Code"))
        self.billpre.setText(_translate("Dialog", "Bill Prefix"))
        self.mno.setText(_translate("Dialog", "Mobile"))
        self.gstuid.setText(_translate("Dialog", "GST/UID"))
        self.state.setText(_translate("Dialog", "State"))
        self.save.setText(_translate("Dialog", "Save"))
        self.close.setText(_translate("Dialog", "Close"))
        self.comnm.setText(_translate("Dialog", "Company Name"))
        self.bnm.setText(_translate("Dialog", "Bank Name"))
        self.pacolor.setText(_translate("Dialog", "Panel Color"))
        self.branch.setText(_translate("Dialog", "Branch"))
        self.cur.execute("Select * from company")
        myresult= self.cur.fetchone()
        if myresult is not None:
            self.comnmw.setText(myresult[1])
            self.mfgw.setText(myresult[6])
            self.addressw.setText(myresult[2])
            self.codew.setText(myresult[4])
            self.gstuidw.setText(myresult[5])
            self.billprew.setText(myresult[9])
            self.mnow.setText(myresult[15])
            self.bnmw.setText(myresult[14])
            self.bacnow.setText(myresult[10])
            self.ifsccw.setText(myresult[11])
            self.branchw.setText((myresult[12]))
            self.lmw.setText(str(myresult[16]))

    def chngcod(self):
        self.cur.execute("Select * from statename")
        myresult= self.cur.fetchall()
        content=self.statew.currentText()
        print(content)
        for i in myresult:
            if content == i[1]:
                self.codew.setText(i[3])
            

    def saveDetails(self):
        f2=self.comnmw.text()
        f7=self.mfgw.text()
        f3=self.addressw.toPlainText()
        f4=self.statew.text()
        f5=self.codew.text()
        f6=self.gstuidw.text()
        f10=self.billprew.text()
        f15=self.mnow.text()
        f14=self.bnmw.text()
        f11=self.bacnow.text()
        f12=self.ifsccw.text()
        f13=self.branchw.text()
        f16=float(self.lmw.text())
        self.cur.execute("""UPDATE company set Nm = ?,
        Address = ?,
        StateNm=?,
        StateCode=?,
        GSTNo=?,
        SupOf=?,
        BillFormat= ?,
        BankDet1=?,
        BankDet2= ?,
        BankDet3=?,
        BankNm=?,
        Mo=?,
        LeftMargin = ?
        where CNo = 1 """ ,(f2,f3,f4,f5,f6,f7,f10,f11,f12,f13,f14,f15,f16))
        self.mydb.commit()
        if self.cur.rowcount>0:
            self.ud = QtWidgets.QDialog()
            self.ui=updated.Ui_Dialog()
            self.ui.setupUi(self.ud)
            self.ud.show()
            
        else:
            self.nc = QtWidgets.QDialog()
            self.ui=nochng.Ui_Dialog()
            self.ui.setupUi(self.nc)
            self.nc.show()
            
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    qtmodern.styles.dark(app)
    Dialog = qtmodern.windows.ModernWindow(Dialog)
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
