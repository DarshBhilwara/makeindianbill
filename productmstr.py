# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\darsh\darshapp\productmstr.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from mysql import connector

class Ui_productmaster(object):
    def setupUi(self, productmaster):
        self.mydb = connector.connect(
            host="localhost",
            user="root",
            password="root",
            database= "filedb"
            )
        self.cur= self.mydb.cursor()
        productmaster.setObjectName("productmaster")
        productmaster.resize(880, 630)
        font = QtGui.QFont()
        font.setPointSize(10)
        productmaster.setFont(font)
        self.tabWidget = QtWidgets.QTabWidget(productmaster)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 880, 570))
        self.tabWidget.setObjectName("tabWidget")
        self.product = QtWidgets.QWidget()
        self.product.setObjectName("product")
        self.prdct = QtWidgets.QLabel(self.product)
        self.prdct.setGeometry(QtCore.QRect(20, 30, 120, 25))
        self.prdct.setObjectName("prdct")
        self.prdctw = QtWidgets.QComboBox(self.product)
        self.prdctw.setGeometry(QtCore.QRect(170, 30, 450, 25))
        self.prdctw.setObjectName("prdctw")
        self.cur.execute("Select * from product")
        myresult= self.cur.fetchall()
        self.prdctw.addItem("")
        for i in myresult:
            self.prdctw.addItem(i[1])
        self.pnm = QtWidgets.QLabel(self.product)
        self.pnm.setGeometry(QtCore.QRect(160, 100, 110, 25))
        self.pnm.setObjectName("pnm")
        self.hsn = QtWidgets.QLabel(self.product)
        self.hsn.setGeometry(QtCore.QRect(160, 160, 75, 25))
        self.hsn.setObjectName("hsn")
        self.unit = QtWidgets.QLabel(self.product)
        self.unit.setGeometry(QtCore.QRect(340, 160, 50, 25))
        self.unit.setObjectName("unit")
        self.slr = QtWidgets.QLabel(self.product)
        self.slr.setGeometry(QtCore.QRect(530, 160, 100, 25))
        self.slr.setObjectName("slr")
        self.sgst = QtWidgets.QLabel(self.product)
        self.sgst.setGeometry(QtCore.QRect(160, 260, 60, 25))
        self.sgst.setObjectName("sgst")
        self.igst = QtWidgets.QLabel(self.product)
        self.igst.setGeometry(QtCore.QRect(340, 260, 60, 25))
        self.igst.setObjectName("igst")
        self.cgst = QtWidgets.QLabel(self.product)
        self.cgst.setGeometry(QtCore.QRect(530, 260, 60, 25))
        self.cgst.setObjectName("cgst")
        self.pnmw = QtWidgets.QLineEdit(self.product)
        self.pnmw.setGeometry(QtCore.QRect(300, 100, 411, 25))
        self.pnmw.setObjectName("pnmw")
        self.hsnw = QtWidgets.QLineEdit(self.product)
        self.hsnw.setGeometry(QtCore.QRect(160, 210, 100, 25))
        self.hsnw.setObjectName("hsnw")
        self.unitw = QtWidgets.QLineEdit(self.product)
        self.unitw.setGeometry(QtCore.QRect(340, 210, 100, 25))
        self.unitw.setObjectName("unitw")
        self.slrw = QtWidgets.QLineEdit(self.product)
        self.slrw.setGeometry(QtCore.QRect(530, 210, 100, 25))
        self.slrw.setObjectName("slrw")
        self.sgstw = QtWidgets.QLineEdit(self.product)
        self.sgstw.setGeometry(QtCore.QRect(160, 320, 100, 25))
        self.sgstw.setObjectName("sgstw")
        self.igstw = QtWidgets.QLineEdit(self.product)
        self.igstw.setGeometry(QtCore.QRect(340, 320, 100, 25))
        self.igstw.setObjectName("igstw")
        self.cgstw = QtWidgets.QLineEdit(self.product)
        self.cgstw.setGeometry(QtCore.QRect(530, 320, 100, 25))
        self.cgstw.setObjectName("cgstw")
        self.tabWidget.addTab(self.product, "")
        self.shall = QtWidgets.QWidget()
        self.shall.setObjectName("shall")
        self.tabWidget.addTab(self.shall, "")
        self.add = QtWidgets.QPushButton(productmaster)
        self.add.setGeometry(QtCore.QRect(10, 590, 90, 30))
        self.add.setObjectName("add")
        self.update = QtWidgets.QPushButton(productmaster)
        self.update.setGeometry(QtCore.QRect(120, 590, 90, 30))
        self.update.setObjectName("update")
        self.dlt = QtWidgets.QPushButton(productmaster)
        self.dlt.setGeometry(QtCore.QRect(230, 590, 90, 30))
        self.dlt.setObjectName("dlt")
        self.save = QtWidgets.QPushButton(productmaster)
        self.save.setGeometry(QtCore.QRect(540, 590, 90, 30))
        self.save.setObjectName("save")
        self.save.setEnabled(False)
        self.refresh = QtWidgets.QPushButton(productmaster)
        self.refresh.setGeometry(QtCore.QRect(650, 590, 90, 30))
        self.refresh.setObjectName("refresh")
        self.close = QtWidgets.QPushButton(productmaster)
        self.close.setGeometry(QtCore.QRect(760, 590, 90, 30))
        self.close.setObjectName("close")
        self.update.setEnabled(False)
        self.dlt.setEnabled(False)
       # self.prdctw.activated.connect(self.btEnable)
        self.retranslateUi(productmaster)
        self.tabWidget.setCurrentIndex(0)
        self.close.clicked.connect(productmaster.close)
        self.refresh.clicked.connect(self.whenRefreshed)
        self.add.clicked.connect(self.whenadd)
        self.save.clicked.connect(self.whenSaved)
        self.dlt.clicked.connect(self.whenDelete)
        QtCore.QMetaObject.connectSlotsByName(productmaster)

    def retranslateUi(self, productmaster):
        _translate = QtCore.QCoreApplication.translate
        productmaster.setWindowTitle(_translate("productmaster", "PRODUCT MASTER"))
        self.prdct.setText(_translate("productmaster", "Product"))
        self.pnm.setText(_translate("productmaster", "Product Name"))
        self.hsn.setText(_translate("productmaster", "HSN Code"))
        self.unit.setText(_translate("productmaster", "Unit"))
        self.slr.setText(_translate("productmaster", "Sell Rate"))
        self.sgst.setText(_translate("productmaster", "SGST%"))
        self.igst.setText(_translate("productmaster", "IGST%"))
        self.cgst.setText(_translate("productmaster", "CGST%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.product), _translate("productmaster", "Products"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shall), _translate("productmaster", "Show All"))
        self.add.setText(_translate("productmaster", "Add"))
        self.update.setText(_translate("productmaster", "Update"))
        self.dlt.setText(_translate("productmaster", "Delete"))
        self.save.setText(_translate("productmaster", "Save"))
        self.refresh.setText(_translate("productmaster", "Refresh"))
        self.close.setText(_translate("productmaster", "Close"))


    def whenDelete(self):
        pdw = self.pnmw
        slw = self.slrw
        self.cur.execute("DELETE * FROM product WHERE Nm = %s and SellRate = %s",(pdw,slw))

        
    def whenRefreshed(self):
        self.hsnw.setText("")
        #self.prdctw.setText("")
        self.pnmw.setText("")
        self.unitw.setText("")
        self.slrw.setText("")
        self.sgstw.setText("")
        self.igstw.setText("")
        self.cgstw.setText("")
        self.prdct.show()
        self.prdctw.show()
        self.prdctw.setEnabled(True)
        self.pnmw.setEnabled(True)
        self.unitw.setEnabled(True)
        self.slrw.setEnabled(True)
        self.hsnw.setEnabled(True)
        self.sgstw.setEnabled(True)
        self.cgstw.setEnabled(True)
        self.igstw.setEnabled(True)

    def whenSaved(self):
        self.prdct.hide()
        self.prdctw.hide()
        self.update.setEnabled(True)
        self.dlt.setEnabled(True)
        self.cgstw.setText("")
        #self.prdctw.setEnabled(False)
        self.pnmw.setEnabled(False)
        self.unitw.setEnabled(False)
        self.slrw.setEnabled(False)
        self.hsnw.setEnabled(False)
        self.sgstw.setEnabled(False)
        self.cgstw.setEnabled(False)
        self.igstw.setEnabled(False)
        self.hsnw.setText("")
        #self.prdctw.setText("")
        self.pnmw.setText("")
        self.unitw.setText("")
        self.slrw.setText("")
        self.sgstw.setText("")
        self.igstw.setText("")
        self.cgstw.setText("")
        
        
    def whenadd(self):
        self.prdctw.hide()
        self.prdct.hide()
        self.save.setEnabled(True)
        self.update.setEnabled(False)
        self.dlt.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    productmaster = QtWidgets.QDialog()
    ui = Ui_productmaster()
    ui.setupUi(productmaster)
    productmaster.show()
    sys.exit(app.exec_())
