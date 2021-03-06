# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\darsh\darshapp\updated.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import qtmodern.styles
import qtmodern.windows

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 130)
        font = QtGui.QFont()
        font.setPointSize(15)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 10, 150, 50))
        self.label.setObjectName("label")
        self.ok = QtWidgets.QPushButton(Dialog)
        self.ok.setCheckable(True)
        self.ok.setGeometry(QtCore.QRect(100,80,100,40))
        self.ok.setObjectName("ok")        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.ok.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NOTE"))
        self.label.setText(_translate("Dialog", "UPDATED!!"))
        self.ok.setText (_translate("Dialog","OK"))


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
