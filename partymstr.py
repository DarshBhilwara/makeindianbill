# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\darsh\darshapp\partymstr.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from mysql import connector
import updated,error


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.mydb = connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="filedb"
            )
        self.cur= self.mydb.cursor()
        Dialog.setObjectName("Dialog")
        Dialog.resize(1100, 650)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.add = QtWidgets.QPushButton(Dialog)
        self.add.setGeometry(QtCore.QRect(20, 600, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.update = QtWidgets.QPushButton(Dialog)
        self.update.setGeometry(QtCore.QRect(130, 600, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.update.setFont(font)
        self.update.setObjectName("update")
        self.update.setEnabled(False)
        self.del2 = QtWidgets.QPushButton(Dialog)
        self.del2.setGeometry(QtCore.QRect(240, 600, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.del2.setFont(font)
        self.del2.setObjectName("del")
        self.del2.setEnabled(False)
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setGeometry(QtCore.QRect(760, 600, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.close = QtWidgets.QPushButton(Dialog)
        self.close.setGeometry(QtCore.QRect(980, 600, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.close.setFont(font)
        self.close.setObjectName("close")
        self.refresh = QtWidgets.QPushButton(Dialog)
        self.refresh.setGeometry(QtCore.QRect(870, 600, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.refresh.setFont(font)
        self.refresh.setObjectName("refresh")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1100, 580))
        self.tabWidget.setObjectName("tabWidget")
        self.party = QtWidgets.QWidget()
        self.party.setObjectName("party")
        self.parties = QtWidgets.QComboBox(self.party)
        self.parties.setGeometry(QtCore.QRect(30, 20, 750, 30))
        self.parties.setObjectName("parties")
        self.parties.setEnabled(True)
        self.cur.execute("Select * from party")
        myres = self.cur.fetchall()
        self.parties.addItem("")
        for j in myres:
            self.parties.addItem(j[1])
        self.pnm = QtWidgets.QLabel(self.party)
        self.pnm.setGeometry(QtCore.QRect(30, 70, 100, 25))
        self.pnm.setObjectName("pnm")
        self.pnmw = QtWidgets.QLineEdit(self.party)
        self.pnmw.setGeometry(QtCore.QRect(30, 110, 400, 25))
        self.pnmw.setObjectName("pnmw")
        self.pnmw.setEnabled(False)
        self.station = QtWidgets.QLabel(self.party)
        self.station.setGeometry(QtCore.QRect(30, 150, 100, 25))
        self.station.setObjectName("station")
        self.stationw = QtWidgets.QLineEdit(self.party)
        self.stationw.setGeometry(QtCore.QRect(30, 190, 400, 25))
        self.stationw.setObjectName("stationw")
        self.stationw.setEnabled(False)
        self.adrs = QtWidgets.QLabel(self.party)
        self.adrs.setGeometry(QtCore.QRect(30, 230, 100, 25))
        self.adrs.setObjectName("adrs")
        self.adrsw = QtWidgets.QTextEdit(self.party)
        self.adrsw.setGeometry(QtCore.QRect(30, 260, 400, 100))
        self.adrsw.setObjectName("adrsw")
        self.adrsw.setEnabled(False)
        self.state = QtWidgets.QLabel(self.party)
        self.state.setGeometry(QtCore.QRect(30, 380, 320, 25))
        self.state.setObjectName("state")
        self.code = QtWidgets.QLabel(self.party)
        self.code.setGeometry(QtCore.QRect(360, 380, 70, 25))
        self.code.setObjectName("code")
        self.statew = QtWidgets.QComboBox(self.party)
        self.statew.setGeometry(QtCore.QRect(30, 420, 320, 25))
        self.statew.setObjectName("statew")
        self.statew.activated.connect(self.chngcod)
        self.statew.addItem("")
        self.cur.execute("Select * from statename")
        myresult= self.cur.fetchall()
        for i in myresult:
            self.statew.addItem(i[1])
        self.statew.setEnabled(False)
        self.codew = QtWidgets.QLineEdit(self.party)
        self.codew.setGeometry(QtCore.QRect(360, 420, 70, 25))
        self.codew.setObjectName("codew")
        self.codew.setEnabled(False)
        self.codew.setReadOnly(True)
        self.gst = QtWidgets.QLabel(self.party)
        self.gst.setGeometry(QtCore.QRect(30, 470, 100, 25))
        self.gst.setObjectName("gst")
        self.gstw = QtWidgets.QLineEdit(self.party)
        self.gstw.setGeometry(QtCore.QRect(30, 510, 400, 25))
        self.gstw.setObjectName("gstw")
        self.gstw.setEnabled(False)
        self.post = QtWidgets.QLabel(self.party)
        self.post.setGeometry(QtCore.QRect(450, 70, 150, 25))
        self.post.setObjectName("post")
        self.postw = QtWidgets.QTextEdit(self.party)
        self.postw.setGeometry(QtCore.QRect(450, 110, 300, 150))
        self.postw.setObjectName("postw")
        self.postw.setEnabled(False)
        self.agent = QtWidgets.QLabel(self.party)
        self.agent.setGeometry(QtCore.QRect(770, 80, 100, 25))
        self.agent.setObjectName("agent")
        self.agentw = QtWidgets.QLineEdit(self.party)
        self.agentw.setGeometry(QtCore.QRect(770, 110, 300, 25))
        self.agentw.setObjectName("agentw")
        self.agentw.setEnabled(False)
        self.cpn = QtWidgets.QLabel(self.party)
        self.cpn.setGeometry(QtCore.QRect(770, 140, 300, 25))
        self.cpn.setObjectName("cpn")
        self.cpnw = QtWidgets.QLineEdit(self.party)
        self.cpnw.setGeometry(QtCore.QRect(770, 170, 300, 25))
        self.cpnw.setObjectName("cpnw")
        self.cpnw.setEnabled(False)
        self.mno = QtWidgets.QLabel(self.party)
        self.mno.setGeometry(QtCore.QRect(770, 200, 300, 25))
        self.mno.setObjectName("mno")
        self.mnow = QtWidgets.QLineEdit(self.party)
        self.mnow.setGeometry(QtCore.QRect(770, 230, 300, 25))
        self.mnow.setObjectName("mnow")
        self.mnow.setEnabled(False)
        self.pno = QtWidgets.QLabel(self.party)
        self.pno.setGeometry(QtCore.QRect(770, 260, 300, 25))
        self.pno.setObjectName("pno")
        self.pnow = QtWidgets.QLineEdit(self.party)
        self.pnow.setGeometry(QtCore.QRect(770, 290, 300, 25))
        self.pnow.setObjectName("pnow")
        self.pnow.setEnabled(False)
        self.email = QtWidgets.QLabel(self.party)
        self.email.setGeometry(QtCore.QRect(770, 320, 300, 25))
        self.email.setObjectName("email")
        self.emailw = QtWidgets.QLineEdit(self.party)
        self.emailw.setGeometry(QtCore.QRect(770, 350, 300, 25))
        self.emailw.setObjectName("emailw")
        self.emailw.setEnabled(False)
        self.transport = QtWidgets.QLabel(self.party)
        self.transport.setGeometry(QtCore.QRect(770, 380, 300, 25))
        self.transport.setObjectName("transport")
        self.transportw = QtWidgets.QLineEdit(self.party)
        self.transportw.setGeometry(QtCore.QRect(770, 410, 300, 25))
        self.transportw.setObjectName("transportw")
        self.transportw.setEnabled(False)
        self.td = QtWidgets.QLabel(self.party)
        self.td.setGeometry(QtCore.QRect(770, 450, 55, 25))
        self.td.setObjectName("td")
        self.tdw = QtWidgets.QLineEdit(self.party)
        self.tdw.setGeometry(QtCore.QRect(770, 480, 55, 25))
        self.tdw.setObjectName("tdw")
        self.tdw.setEnabled(False)
        self.tabWidget.addTab(self.party, "")
        self.shall = QtWidgets.QWidget()
        self.shall.setObjectName("shall")
        self.tabWidget.addTab(self.shall, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.close.clicked.connect(Dialog.close)
        self.add.clicked.connect(self.whenAdded)
        self.refresh.clicked.connect(self.whenRefreshed)
        self.parties.activated.connect(self.btEnable)
        self.save.clicked.connect(self.whenSaved)
        self.update.clicked.connect(self.whenUpDated)
        self.del2.clicked.connect(self.whenDeleted)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PARTY MASTER"))
        self.add.setText(_translate("Dialog", "Add"))
        self.update.setText(_translate("Dialog", "Update"))
        self.del2.setText(_translate("Dialog", "Delete"))
        self.save.setText(_translate("Dialog", "Save"))
        self.close.setText(_translate("Dialog", "Close"))
        self.refresh.setText(_translate("Dialog", "Refresh"))
        self.pnm.setText(_translate("Dialog", "Party Name"))
        self.station.setText(_translate("Dialog", "City/Station"))
        self.adrs.setText(_translate("Dialog", "Address"))
        self.state.setText(_translate("Dialog", "State"))
        self.code.setText(_translate("Dialog", "Code"))
        self.gst.setText(_translate("Dialog", "GSTIN/UID"))
        self.post.setText(_translate("Dialog", "Postal Address"))
        self.agent.setText(_translate("Dialog", "Agent"))
        self.cpn.setText(_translate("Dialog", "Contact Person Name"))
        self.mno.setText(_translate("Dialog", "Mobile No."))
        self.pno.setText(_translate("Dialog", "Phone No."))
        self.email.setText(_translate("Dialog", "E - Mail"))
        self.transport.setText(_translate("Dialog", "Transport"))
        self.td.setText(_translate("Dialog", "T.D."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.party), _translate("Dialog", "Party"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shall), _translate("Dialog", "Show All"))


    def chngcod(self):
        self.cur.execute("Select * from statename")
        myresult= self.cur.fetchall()
        content=self.statew.currentText()
        for i in myresult:
            if content == i[1]:
                self.codew.setText(i[3])
                
    def btEnable(self):
        if len(self.parties.currentText())>0:
            x=self.parties.currentText()
            print(x)
            self.update.setEnabled(True)
            self.del2.setEnabled(True)
            self.cur.execute("Select * from party where Nm = %s",(x,))
            myresult= self.cur.fetchone()
            print(myresult)
            if myresult is not None:
                self.pnmw.setText(myresult[1])
                self.stationw.setText(myresult[2])
                self.adrsw.setText(myresult[3]) 
                self.statew.setCurrentText(myresult[4])
                self.codew.setText(myresult[5])
                self.gstw.setText(myresult[6])
                self.postw.setText(myresult[7])
                self.agentw.setText(myresult[8])
                self.mnow.setText(myresult[10])
                self.cpnw.setText(myresult[9])
                self.pnow.setText(myresult[11])
                self.emailw.setText(myresult[12])
                self.transportw.setText(myresult[13])
                
            
        else :
            self.update.setEnabled(False)
            self.del2.setEnabled(False)


    def whenDeleted(self):
        a = self.pnmw.text()
        self.cur.execute("""SELECT Nm FROM party""")
        b = self.cur.fetchall()
        c = 0
        for x in b:
            if a == b:
                c = c + 1
        if c == 0:
                self.er = QtWidgets.QDialog()
                self.ui=error.Ui_Dialog()
                self.ui.setupUi(self.er)
                self.er.show()
        else:
            self.cur.execute("""DELETE FROM party WHERE Nm = %s""",(a,))
            self.mydb.commit()
            self.ud = QtWidgets.QDialog()
            self.ui=updated.Ui_Dialog()
            self.ui.setupUi(self.ud)
            self.ud.show()

    def whenAdded(self):
        self.save.setEnabled(True)
        self.parties.hide()
        self.parties.setEnabled(False)
        self.pnmw.setEnabled(True)
        self.stationw.setEnabled(True)
        self.adrsw.setEnabled(True)
        self.statew.setEnabled(True)
        self.codew.setEnabled(True)
        self.gstw.setEnabled(True)
        self.postw.setEnabled(True)
        self.agentw.setEnabled(True)
        self.mnow.setEnabled(True)
        self.cpnw.setEnabled(True)
        self.pnow.setEnabled(True)
        self.emailw.setEnabled(True)
        self.transportw.setEnabled(True)
        self.tdw.setEnabled(True)
        self.pnmw.setText("")
        self.stationw.setText("")
        self.adrsw.setText("")
        self.codew.setText("")
        self.gstw.setText("")
        self.postw.setText("")
        self.agentw.setText("")
        self.mnow.setText("")
        self.cpnw.setText("")
        self.pnow.setText("")
        self.emailw.setText("")
        self.transportw.setText("")
        self.tdw.setText("")
        
        
    def whenRefreshed(self):
        self.update.setEnabled(False)
        self.del2.setEnabled(False)
        self.save.setEnabled(False)
        self.parties.setCurrentIndex(0)
        self.pnmw.setText("")
        self.stationw.setText("")
        self.adrsw.setText("") 
        self.codew.setText("")
        self.gstw.setText("")
        self.postw.setText("")
        self.agentw.setText("")
        self.mnow.setText("")
        self.cpnw.setText("")
        self.pnow.setText("")
        self.emailw.setText("")
        self.transportw.setText("")
        self.tdw.setText("")
        self.parties.show()
        self.parties.setEnabled(True)
        self.pnmw.setEnabled(False)
        self.stationw.setEnabled(False)
        self.adrsw.setEnabled(False)
        self.statew.setEnabled(False)
        self.codew.setEnabled(False)
        self.gstw.setEnabled(False)
        self.postw.setEnabled(False)
        self.agentw.setEnabled(False)
        self.mnow.setEnabled(False)
        self.cpnw.setEnabled(False)
        self.pnow.setEnabled(False)
        self.emailw.setEnabled(False)
        self.transportw.setEnabled(False)
        self.tdw.setEnabled(False)

        

    def whenSaved(self):
        self.save.setEnabled(False)
        self.add.setEnabled(False)
        self.update.setEnabled(False)
        self.del2.setEnabled(False)
        pnmw1 = self.pnmw.text()
        stationw1 = self.stationw.text()
        adrsw1 = self.adrsw.toPlainText()
        statew1 = self.statew.currentText()
        codew1 = self.codew.text()
        gstw1 = self.gstw.text()
        postw1 = self.postw.toPlainText()
        agentw1 = self.agentw.text()
        mnow1= self.mnow.text()
        cpnw1 = self.cpnw.text()
        pnow1 = self.pnow.text()
        emailw1 = self.emailw.text()
        transportw1= self.transportw.text()
        #tdw1 = float(int(self.tdw.text()))
        if self.glo == 0:
            if pnmw1 is None or stationw1 is None or adrsw1 is None or codew1 is None or gstw1 is None or postw1 is None or agentw1 is None or mnow1 is None or cpnw1 is None or pnow1 is None or emailw1 is None or transportw1 is None :
                self.er = QtWidgets.QDialog()
                self.ui=error.Ui_Dialog()
                self.ui.setupUi(self.er)
                self.er.show()
            elif pnmw1 is not None and stationw1 is not None and adrsw1 is not None and codew1 is not None and gstw1 is not None and postw1 is not None and agentw1 is not None and mnow1 is not None and cpnw1 is not None and pnow1 is not None and emailw1 is not None and transportw1 is not None:
                self.cur.execute("""Insert into party (Nm,City,Address,PState,StateCode,GSTNo,PostalAddress,Agent,ContactPerson,MoNo,PhNo,Email,Transport) Values(%s,%s,%s,%s, %s,%s,%s,%s, %s,%s,%s,%s, %s)""",(pnmw1,stationw1,adrsw1,statew1,codew1,gstw1,postw1,agentw1,cpnw1,mnow1,pnow1,emailw1,transportw1))
                self.mydb.commit()
                print(self.cur.rowcount, "was inserted.")
                if self.cur.rowcount>0:
                    self.ud = QtWidgets.QDialog()
                    self.ui=updated.Ui_Dialog()
                    self.ui.setupUi(self.ud)
                    self.ud.show()
        else:
            self.glo = 0
            if pnmw1 is None or stationw1 is None or adrsw1 is None or codew1 is None or gstw1 is None or postw1 is None or agentw1 is None or mnow1 is None or cpnw1 is None or pnow1 is None or emailw1 is None or transportw1 is None :
                self.er = QtWidgets.QDialog()
                self.ui=error.Ui_Dialog()
                self.ui.setupUi(self.er)
                self.er.show()
            elif pnmw1 is not None and stationw1 is not None and adrsw1 is not None and codew1 is not None and gstw1 is not None and postw1 is not None and agentw1 is not None and mnow1 is not None and cpnw1 is not None and pnow1 is not None and emailw1 is not None and transportw1 is not None:
                self.cur.execute("""UPDATE party set City =%s,Address=%s,PState=%s,StateCode=%s,GSTNo=%s,PostalAddress=%s,Agent=%s,ContactPerson=%s,MoNo=%s,PhNo=%s,Email=%s,Transport=%s WHERE Nm=%s""",(stationw1,adrsw1,statew1,codew1,gstw1,postw1,agentw1,cpnw1,mnow1,pnow1,emailw1,transportw1,pnmw1))
                self.mydb.commit()
                self.ud = QtWidgets.QDialog()
                self.ui=updated.Ui_Dialog()
                self.ui.setupUi(self.ud)
                self.ud.show()

                
        self.pnmw.setText("")
        self.stationw.setText("")
        self.adrsw.setText("")
        #self.statew.setText("")
        self.codew.setText("")
        self.gstw.setText("")
        self.postw.setText("")
        self.agentw.setText("")
        self.mnow.setText("")
        self.cpnw.setText("")
        self.pnow.setText("")
        self.emailw.setText("")
        self.transportw.setText("")
        self.tdw.setText("")
        self.statew.setCurrentText("")
        self.parties.setCurrentText("")


    def whenUpDated(self):
        self.glo = 1
        self.pnmw.setEnabled(True)
        self.stationw.setEnabled(True)
        self.adrsw.setEnabled(True)
        self.statew.setEnabled(True)
        self.codew.setEnabled(True)
        self.gstw.setEnabled(True)
        self.postw.setEnabled(True)
        self.agentw.setEnabled(True)
        self.mnow.setEnabled(True)
        self.cpnw.setEnabled(True)
        self.pnow.setEnabled(True)
        self.emailw.setEnabled(True)
        self.transportw.setEnabled(True)
        self.tdw.setEnabled(True)
        self.save.setEnabled(True)



        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
