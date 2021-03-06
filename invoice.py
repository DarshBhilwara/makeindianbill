# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'invoice.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import qtmodern.styles
import qtmodern.windows


class Ui_inv(object):
    def setupUi(self, inv):
        self.mydb = sqlite3.connect('filedb.sqlite')
        inv.setObjectName("inv")
        inv.resize(1130, 750)
        font = QtGui.QFont()
        font.setPointSize(10)
        inv.setFont(font)
        inv.setStyleSheet("")
        self.weight = QtWidgets.QLabel(inv)
        self.weight.setGeometry(QtCore.QRect(725, 240, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.weight.setFont(font)
        self.weight.setObjectName("weight")
        self.ppage = QtWidgets.QPushButton(inv)
        self.ppage.setGeometry(QtCore.QRect(690, 700, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ppage.setFont(font)
        self.ppage.setObjectName("ppage")
        self.ordernow = QtWidgets.QLineEdit(inv)
        self.ordernow.setGeometry(QtCore.QRect(820, 60, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ordernow.setFont(font)
        self.ordernow.setObjectName("ordernow")
        self.codew = QtWidgets.QLineEdit(inv)
        self.codew.setEnabled(True)
        self.codew.setGeometry(QtCore.QRect(650, 175, 70, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.codew.setFont(font)
        self.codew.setObjectName("codew")
        self.pvm = QtWidgets.QLabel(inv)
        self.pvm.setGeometry(QtCore.QRect(925, 210, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pvm.setFont(font)
        self.pvm.setObjectName("pvm")
        self.transportw = QtWidgets.QLineEdit(inv)
        self.transportw.setGeometry(QtCore.QRect(820, 150, 300, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.transportw.setFont(font)
        self.transportw.setObjectName("transportw")
        self.ewb = QtWidgets.QLabel(inv)
        self.ewb.setGeometry(QtCore.QRect(240, 230, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ewb.setFont(font)
        self.ewb.setObjectName("ewb")
        self.code = QtWidgets.QLabel(inv)
        self.code.setEnabled(True)
        self.code.setGeometry(QtCore.QRect(600, 170, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.code.setFont(font)
        self.code.setObjectName("code")
        self.weightw = QtWidgets.QLineEdit(inv)
        self.weightw.setGeometry(QtCore.QRect(820, 240, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.weightw.setFont(font)
        self.weightw.setObjectName("weightw")
        self.npkt = QtWidgets.QLabel(inv)
        self.npkt.setGeometry(QtCore.QRect(925, 90, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.npkt.setFont(font)
        self.npkt.setObjectName("npkt")
        self.indate = QtWidgets.QLabel(inv)
        self.indate.setGeometry(QtCore.QRect(140, 60, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.indate.setFont(font)
        self.indate.setObjectName("indate")
        self.formLayoutWidget = QtWidgets.QWidget(inv)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 193, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.formLayoutWidget.setFont(font)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.inno = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.inno.setContentsMargins(0, 0, 0, 0)
        self.inno.setObjectName("inno")
        self.innow1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.innow1.setFont(font)
        self.innow1.setObjectName("innow1")
        self.inno.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.innow1)
        self.inno1 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inno1.setFont(font)
        self.inno1.setObjectName("inno1")
        self.inno.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.inno1)
        self.lrno = QtWidgets.QLabel(inv)
        self.lrno.setGeometry(QtCore.QRect(725, 120, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lrno.setFont(font)
        self.lrno.setObjectName("lrno")
        self.adrs = QtWidgets.QLabel(inv)
        self.adrs.setGeometry(QtCore.QRect(240, 90, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.adrs.setFont(font)
        self.adrs.setObjectName("adrs")
        self.pvmw = QtWidgets.QLineEdit(inv)
        self.pvmw.setGeometry(QtCore.QRect(1010, 210, 110, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pvmw.setFont(font)
        self.pvmw.setObjectName("pvmw")
        self.save = QtWidgets.QPushButton(inv)
        self.save.setGeometry(QtCore.QRect(800, 700, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.pnm = QtWidgets.QLabel(inv)
        self.pnm.setGeometry(QtCore.QRect(240, 60, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pnm.setFont(font)
        self.pnm.setObjectName("pnm")
        self.pdf = QtWidgets.QPushButton(inv)
        self.pdf.setGeometry(QtCore.QRect(580, 700, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pdf.setFont(font)
        self.pdf.setObjectName("pdf")
        self.add = QtWidgets.QPushButton(inv)
        self.add.setGeometry(QtCore.QRect(10, 700, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.gstno = QtWidgets.QLabel(inv)
        self.gstno.setGeometry(QtCore.QRect(240, 200, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gstno.setFont(font)
        self.gstno.setObjectName("gstno")
        self.gstnow = QtWidgets.QLineEdit(inv)
        self.gstnow.setGeometry(QtCore.QRect(350, 205, 215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gstnow.setFont(font)
        self.gstnow.setObjectName("gstnow")
        self.freight = QtWidgets.QLabel(inv)
        self.freight.setGeometry(QtCore.QRect(725, 210, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.freight.setFont(font)
        self.freight.setObjectName("freight")
        self.adrsw = QtWidgets.QTextEdit(inv)
        self.adrsw.setGeometry(QtCore.QRect(350, 95, 370, 75))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.adrsw.setFont(font)
        self.adrsw.setObjectName("adrsw")
        self.state = QtWidgets.QLabel(inv)
        self.state.setGeometry(QtCore.QRect(240, 170, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.state.setFont(font)
        self.state.setObjectName("state")
        self.lrnow = QtWidgets.QLineEdit(inv)
        self.lrnow.setGeometry(QtCore.QRect(820, 120, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lrnow.setFont(font)
        self.lrnow.setObjectName("lrnow")
        self.bkdbw = QtWidgets.QLineEdit(inv)
        self.bkdbw.setGeometry(QtCore.QRect(820, 90, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bkdbw.setFont(font)
        self.bkdbw.setObjectName("bkdbw")
        self.mno = QtWidgets.QLabel(inv)
        self.mno.setGeometry(QtCore.QRect(570, 200, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mno.setFont(font)
        self.mno.setObjectName("mno")
        self.refresh = QtWidgets.QPushButton(inv)
        self.refresh.setGeometry(QtCore.QRect(910, 700, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.refresh.setFont(font)
        self.refresh.setObjectName("refresh")
        self.ondatew = QtWidgets.QDateEdit(inv)
        self.ondatew.setGeometry(QtCore.QRect(1010, 60, 110, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ondatew.setFont(font)
        self.ondatew.setObjectName("ondatew")
        self.lrndatew = QtWidgets.QDateEdit(inv)
        self.lrndatew.setGeometry(QtCore.QRect(1010, 120, 110, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lrndatew.setFont(font)
        self.lrndatew.setObjectName("lrndatew")
        self.bkdb = QtWidgets.QLabel(inv)
        self.bkdb.setGeometry(QtCore.QRect(725, 90, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bkdb.setFont(font)
        self.bkdb.setObjectName("bkdb")
        self.npktw = QtWidgets.QLineEdit(inv)
        self.npktw.setGeometry(QtCore.QRect(1010, 90, 110, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.npktw.setFont(font)
        self.npktw.setObjectName("npktw")
        self.ewbw = QtWidgets.QLineEdit(inv)
        self.ewbw.setGeometry(QtCore.QRect(350, 235, 370, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ewbw.setFont(font)
        self.ewbw.setObjectName("ewbw")
        self.innow2 = QtWidgets.QLineEdit(inv)
        self.innow2.setGeometry(QtCore.QRect(20, 100, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.innow2.setFont(font)
        self.innow2.setObjectName("innow2")
        self.pos = QtWidgets.QLabel(inv)
        self.pos.setGeometry(QtCore.QRect(725, 180, 115, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pos.setFont(font)
        self.pos.setObjectName("pos")
        self.orderno = QtWidgets.QLabel(inv)
        self.orderno.setGeometry(QtCore.QRect(725, 60, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.orderno.setFont(font)
        self.orderno.setObjectName("orderno")
        self.delbt = QtWidgets.QPushButton(inv)
        self.delbt.setGeometry(QtCore.QRect(230, 700, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.delbt.setFont(font)
        self.delbt.setObjectName("delbt")
        self.indatew = QtWidgets.QDateEdit(inv)
        self.indatew.setGeometry(QtCore.QRect(120, 100, 110, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.indatew.setFont(font)
        self.indatew.setObjectName("indatew")
        self.mnow = QtWidgets.QLineEdit(inv)
        self.mnow.setGeometry(QtCore.QRect(615, 205, 105, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mnow.setFont(font)
        self.mnow.setObjectName("mnow")
        self.ondate = QtWidgets.QLabel(inv)
        self.ondate.setGeometry(QtCore.QRect(925, 60, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ondate.setFont(font)
        self.ondate.setObjectName("ondate")
        self.update = QtWidgets.QPushButton(inv)
        self.update.setGeometry(QtCore.QRect(120, 700, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.update.setFont(font)
        self.update.setObjectName("update")
        self.lrndate = QtWidgets.QLabel(inv)
        self.lrndate.setGeometry(QtCore.QRect(925, 120, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lrndate.setFont(font)
        self.lrndate.setObjectName("lrndate")
        self.transport = QtWidgets.QLabel(inv)
        self.transport.setGeometry(QtCore.QRect(725, 150, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.transport.setFont(font)
        self.transport.setObjectName("transport")
        self.pnmw = QtWidgets.QLineEdit(inv)
        self.pnmw.setGeometry(QtCore.QRect(350, 65, 370, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pnmw.setFont(font)
        self.pnmw.setObjectName("pnmw")
        self.posw = QtWidgets.QLineEdit(inv)
        self.posw.setGeometry(QtCore.QRect(840, 180, 280, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.posw.setFont(font)
        self.posw.setObjectName("posw")
        self.frieghtw = QtWidgets.QLineEdit(inv)
        self.frieghtw.setGeometry(QtCore.QRect(820, 210, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frieghtw.setFont(font)
        self.frieghtw.setObjectName("frieghtw")
        self.close = QtWidgets.QPushButton(inv)
        self.close.setGeometry(QtCore.QRect(1020, 700, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.close.setFont(font)
        self.close.setObjectName("close")
        self.statew = QtWidgets.QLineEdit(inv)
        self.statew.setGeometry(QtCore.QRect(350, 175, 215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statew.setFont(font)
        self.statew.setObjectName("statew")
        self.inno2 = QtWidgets.QLabel(inv)
        self.inno2.setGeometry(QtCore.QRect(20, 60, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inno2.setFont(font)
        self.inno2.setObjectName("inno2")
        self.descfr = QtWidgets.QFrame(inv)
        self.descfr.setGeometry(QtCore.QRect(10, 280, 1100, 330))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.descfr.setFont(font)
        self.descfr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.descfr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.descfr.setLineWidth(6)
        self.descfr.setObjectName("descfr")
        self.desc = QtWidgets.QLabel(self.descfr)
        self.desc.setGeometry(QtCore.QRect(10, 0, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc.setFont(font)
        self.desc.setObjectName("desc")
        self.size = QtWidgets.QLabel(self.descfr)
        self.size.setGeometry(QtCore.QRect(370, 0, 55, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.size.setFont(font)
        self.size.setObjectName("size")
        self.hsn = QtWidgets.QLabel(self.descfr)
        self.hsn.setGeometry(QtCore.QRect(470, 0, 55, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hsn.setFont(font)
        self.hsn.setObjectName("hsn")
        self.gst = QtWidgets.QLabel(self.descfr)
        self.gst.setGeometry(QtCore.QRect(550, 0, 55, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gst.setFont(font)
        self.gst.setObjectName("gst")
        self.qty = QtWidgets.QLabel(self.descfr)
        self.qty.setGeometry(QtCore.QRect(615, 0, 55, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qty.setFont(font)
        self.qty.setObjectName("qty")
        self.unit = QtWidgets.QLabel(self.descfr)
        self.unit.setGeometry(QtCore.QRect(700, 0, 55, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unit.setFont(font)
        self.unit.setObjectName("unit")
        self.rate = QtWidgets.QLabel(self.descfr)
        self.rate.setGeometry(QtCore.QRect(765, 0, 55, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rate.setFont(font)
        self.rate.setObjectName("rate")
        self.amount = QtWidgets.QLabel(self.descfr)
        self.amount.setGeometry(QtCore.QRect(855, 0, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.amount.setFont(font)
        self.amount.setObjectName("amount")
        self.disper = QtWidgets.QLabel(self.descfr)
        self.disper.setGeometry(QtCore.QRect(980, 0, 55, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.disper.setFont(font)
        self.disper.setObjectName("disper")
        self.addit = QtWidgets.QPushButton(self.descfr)
        self.addit.setGeometry(QtCore.QRect(1040, 25, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addit.setFont(font)
        self.addit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconadd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addit.setIcon(icon)
        self.addit.setIconSize(QtCore.QSize(40, 40))
        self.addit.setObjectName("addit")
        self.descw = QtWidgets.QLineEdit(self.descfr)
        self.descw.setGeometry(QtCore.QRect(10, 35, 350, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.descw.setFont(font)
        self.descw.setText("")
        self.descw.setObjectName("descw")
        self.unitw = QtWidgets.QLineEdit(self.descfr)
        self.unitw.setGeometry(QtCore.QRect(700, 35, 55, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unitw.setFont(font)
        self.unitw.setObjectName("unitw")
        self.sizew = QtWidgets.QLineEdit(self.descfr)
        self.sizew.setGeometry(QtCore.QRect(370, 35, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sizew.setFont(font)
        self.sizew.setObjectName("sizew")
        self.hsnw = QtWidgets.QLineEdit(self.descfr)
        self.hsnw.setGeometry(QtCore.QRect(470, 35, 70, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hsnw.setFont(font)
        self.hsnw.setObjectName("hsnw")
        self.gstw = QtWidgets.QLineEdit(self.descfr)
        self.gstw.setGeometry(QtCore.QRect(550, 35, 55, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gstw.setFont(font)
        self.gstw.setObjectName("gstw")
        self.qtyw = QtWidgets.QLineEdit(self.descfr)
        self.qtyw.setGeometry(QtCore.QRect(615, 35, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qtyw.setFont(font)
        self.qtyw.setObjectName("qtyw")
        self.ratew = QtWidgets.QLineEdit(self.descfr)
        self.ratew.setGeometry(QtCore.QRect(765, 35, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ratew.setFont(font)
        self.ratew.setObjectName("ratew")
        self.disperw = QtWidgets.QLineEdit(self.descfr)
        self.disperw.setGeometry(QtCore.QRect(980, 35, 55, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.disperw.setFont(font)
        self.disperw.setObjectName("disperw")
        self.amountw = QtWidgets.QLineEdit(self.descfr)
        self.amountw.setGeometry(QtCore.QRect(855, 35, 115, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.amountw.setFont(font)
        self.amountw.setObjectName("amountw")
        self.descriptiontable = QtWidgets.QTableWidget(self.descfr)
        self.descriptiontable.setGeometry(QtCore.QRect(10, 70, 350, 250))
        self.descriptiontable.setObjectName("descriptiontable")
        self.descriptiontable.setColumnCount(0)
        self.descriptiontable.setRowCount(0)
        self.sizetable = QtWidgets.QTableWidget(self.descfr)
        self.sizetable.setGeometry(QtCore.QRect(370, 70, 90, 250))
        self.sizetable.setObjectName("sizetable")
        self.sizetable.setColumnCount(0)
        self.sizetable.setRowCount(0)
        self.hsntable = QtWidgets.QTableWidget(self.descfr)
        self.hsntable.setGeometry(QtCore.QRect(470, 70, 70, 250))
        self.hsntable.setObjectName("hsntable")
        self.hsntable.setColumnCount(0)
        self.hsntable.setRowCount(0)
        self.gsttable = QtWidgets.QTableWidget(self.descfr)
        self.gsttable.setGeometry(QtCore.QRect(550, 70, 55, 250))
        self.gsttable.setObjectName("gsttable")
        self.gsttable.setColumnCount(0)
        self.gsttable.setRowCount(0)
        self.qtytable = QtWidgets.QTableWidget(self.descfr)
        self.qtytable.setGeometry(QtCore.QRect(615, 70, 75, 250))
        self.qtytable.setObjectName("qtytable")
        self.qtytable.setColumnCount(0)
        self.qtytable.setRowCount(0)
        self.unittable = QtWidgets.QTableWidget(self.descfr)
        self.unittable.setGeometry(QtCore.QRect(700, 70, 55, 250))
        self.unittable.setObjectName("unittable")
        self.unittable.setColumnCount(0)
        self.unittable.setRowCount(0)
        self.ratetable = QtWidgets.QTableWidget(self.descfr)
        self.ratetable.setGeometry(QtCore.QRect(765, 70, 80, 250))
        self.ratetable.setObjectName("ratetable")
        self.ratetable.setColumnCount(0)
        self.ratetable.setRowCount(0)
        self.amounttable = QtWidgets.QTableWidget(self.descfr)
        self.amounttable.setGeometry(QtCore.QRect(855, 70, 115, 250))
        self.amounttable.setObjectName("amounttable")
        self.amounttable.setColumnCount(0)
        self.amounttable.setRowCount(0)
        self.tdtable = QtWidgets.QTableWidget(self.descfr)
        self.tdtable.setGeometry(QtCore.QRect(980, 70, 55, 250))
        self.tdtable.setObjectName("tdtable")
        self.tdtable.setColumnCount(0)
        self.tdtable.setRowCount(0)
        self.total1 = QtWidgets.QLabel(inv)
        self.total1.setGeometry(QtCore.QRect(20, 630, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.total1.setFont(font)
        self.total1.setObjectName("total1")
        self.dis = QtWidgets.QLabel(inv)
        self.dis.setGeometry(QtCore.QRect(120, 630, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dis.setFont(font)
        self.dis.setObjectName("dis")
        self.taxval = QtWidgets.QLabel(inv)
        self.taxval.setGeometry(QtCore.QRect(220, 630, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.taxval.setFont(font)
        self.taxval.setObjectName("taxval")
        self.cgst = QtWidgets.QLabel(inv)
        self.cgst.setGeometry(QtCore.QRect(320, 630, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cgst.setFont(font)
        self.cgst.setObjectName("cgst")
        self.sgst = QtWidgets.QLabel(inv)
        self.sgst.setGeometry(QtCore.QRect(420, 630, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sgst.setFont(font)
        self.sgst.setObjectName("sgst")
        self.igst = QtWidgets.QLabel(inv)
        self.igst.setGeometry(QtCore.QRect(520, 630, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.igst.setFont(font)
        self.igst.setObjectName("igst")
        self.tgst = QtWidgets.QLabel(inv)
        self.tgst.setGeometry(QtCore.QRect(620, 630, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tgst.setFont(font)
        self.tgst.setObjectName("tgst")
        self.total2 = QtWidgets.QLabel(inv)
        self.total2.setGeometry(QtCore.QRect(720, 630, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.total2.setFont(font)
        self.total2.setObjectName("total2")
        self.lineEdit = QtWidgets.QLineEdit(inv)
        self.lineEdit.setGeometry(QtCore.QRect(820, 625, 90, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(inv)
        self.lineEdit_2.setGeometry(QtCore.QRect(920, 625, 90, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gtotal = QtWidgets.QLabel(inv)
        self.gtotal.setGeometry(QtCore.QRect(1020, 630, 90, 20))
        self.gtotal.setObjectName("gtotal")
        self.total1w = QtWidgets.QLineEdit(inv)
        self.total1w.setGeometry(QtCore.QRect(20, 660, 90, 25))
        self.total1w.setObjectName("total1w")
        self.disw = QtWidgets.QLineEdit(inv)
        self.disw.setGeometry(QtCore.QRect(120, 660, 90, 25))
        self.disw.setObjectName("disw")
        self.taxvalw = QtWidgets.QLineEdit(inv)
        self.taxvalw.setGeometry(QtCore.QRect(220, 660, 90, 25))
        self.taxvalw.setObjectName("taxvalw")
        self.cgstw = QtWidgets.QLineEdit(inv)
        self.cgstw.setGeometry(QtCore.QRect(320, 660, 90, 25))
        self.cgstw.setObjectName("cgstw")
        self.sgstw = QtWidgets.QLineEdit(inv)
        self.sgstw.setGeometry(QtCore.QRect(420, 660, 90, 25))
        self.sgstw.setObjectName("sgstw")
        self.igstw = QtWidgets.QLineEdit(inv)
        self.igstw.setGeometry(QtCore.QRect(520, 660, 90, 25))
        self.igstw.setObjectName("igstw")
        self.tgstw = QtWidgets.QLineEdit(inv)
        self.tgstw.setGeometry(QtCore.QRect(620, 660, 90, 25))
        self.tgstw.setObjectName("tgstw")
        self.total2w = QtWidgets.QLineEdit(inv)
        self.total2w.setGeometry(QtCore.QRect(720, 660, 90, 25))
        self.total2w.setObjectName("total2w")
        self.lineEdit_17 = QtWidgets.QLineEdit(inv)
        self.lineEdit_17.setGeometry(QtCore.QRect(820, 660, 90, 25))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(inv)
        self.lineEdit_18.setGeometry(QtCore.QRect(920, 660, 90, 25))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gtotalw = QtWidgets.QLineEdit(inv)
        self.gtotalw.setGeometry(QtCore.QRect(1020, 660, 90, 25))
        self.gtotalw.setObjectName("gtotalw")

        self.retranslateUi(inv)
        self.close.clicked.connect(inv.close)
        QtCore.QMetaObject.connectSlotsByName(inv)

    def retranslateUi(self, inv):
        _translate = QtCore.QCoreApplication.translate
        inv.setWindowTitle(_translate("inv", "Dialog"))
        self.weight.setText(_translate("inv", "Weight"))
        self.ppage.setText(_translate("inv", "Print"))
        self.pvm.setText(_translate("inv", "Pvt. Mark"))
        self.ewb.setText(_translate("inv", "E Way Bill"))
        self.code.setText(_translate("inv", "Code"))
        self.npkt.setText(_translate("inv", "No. of Pkt."))
        self.indate.setText(_translate("inv", "Date"))
        self.inno1.setText(_translate("inv", "Invoice No."))
        self.lrno.setText(_translate("inv", "L.R. NO."))
        self.adrs.setText(_translate("inv", "Address"))
        self.save.setText(_translate("inv", "Save"))
        self.pnm.setText(_translate("inv", "Party Name"))
        self.pdf.setText(_translate("inv", "PDF"))
        self.add.setText(_translate("inv", "Add"))
        self.gstno.setText(_translate("inv", "GST No."))
        self.freight.setText(_translate("inv", "Freight"))
        self.state.setText(_translate("inv", "State"))
        self.mno.setText(_translate("inv", "M No."))
        self.refresh.setText(_translate("inv", "Refresh"))
        self.bkdb.setText(_translate("inv", "Booked By"))
        self.pos.setText(_translate("inv", "Place of supply"))
        self.orderno.setText(_translate("inv", "Order No."))
        self.delbt.setText(_translate("inv", "Delete"))
        self.ondate.setText(_translate("inv", "Date"))
        self.update.setText(_translate("inv", "Update"))
        self.lrndate.setText(_translate("inv", "Date"))
        self.transport.setText(_translate("inv", "Transport"))
        self.close.setText(_translate("inv", "Close"))
        self.inno2.setText(_translate("inv", " Invoice No."))
        self.desc.setText(_translate("inv", "DESCRIPTION"))
        self.size.setText(_translate("inv", "SIZE"))
        self.hsn.setText(_translate("inv", "HSN"))
        self.gst.setText(_translate("inv", "GST%"))
        self.qty.setText(_translate("inv", "QTY."))
        self.unit.setText(_translate("inv", "UNIT"))
        self.rate.setText(_translate("inv", "RATE"))
        self.amount.setText(_translate("inv", "AMOUNT"))
        self.disper.setText(_translate("inv", "T.D.%"))
        self.total1.setText(_translate("inv", "Total"))
        self.dis.setText(_translate("inv", "Discount"))
        self.taxval.setText(_translate("inv", "Tax Value"))
        self.cgst.setText(_translate("inv", "CGST"))
        self.sgst.setText(_translate("inv", "SGST"))
        self.igst.setText(_translate("inv", "IGST"))
        self.tgst.setText(_translate("inv", "Total GST"))
        self.total2.setText(_translate("inv", "Total"))
        self.gtotal.setText(_translate("inv", "Grand Total"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inv = QtWidgets.QDialog()
    qtmodern.styles.dark(app)
    inv = qtmodern.windows.ModernWindow(inv)
    ui = Ui_inv()
    ui.setupUi(inv)
    inv.show()
    sys.exit(app.exec_())
