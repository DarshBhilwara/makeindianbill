# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\darsh\darshapp\salesregister.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 700)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.close = QtWidgets.QPushButton(Dialog)
        self.close.setGeometry(QtCore.QRect(1050, 630, 120, 50))
        self.close.setObjectName("close")
        self.show = QtWidgets.QPushButton(Dialog)
        self.show.setGeometry(QtCore.QRect(30, 630, 120, 50))
        self.show.setObjectName("show")
        self.prit = QtWidgets.QPushButton(Dialog)
        self.prit.setGeometry(QtCore.QRect(550, 630, 120, 50))
        self.prit.setObjectName("prit")
        self.start = QtWidgets.QLabel(Dialog)
        self.start.setGeometry(QtCore.QRect(40, 30, 100, 25))
        self.start.setObjectName("start")
        self.startw = QtWidgets.QDateEdit(Dialog)
        self.startw.setGeometry(QtCore.QRect(150, 30, 110, 25))
        self.startw.setObjectName("startw")
        self.end = QtWidgets.QLabel(Dialog)
        self.end.setGeometry(QtCore.QRect(540, 30, 100, 25))
        self.end.setObjectName("end")
        self.endw = QtWidgets.QDateEdit(Dialog)
        self.endw.setGeometry(QtCore.QRect(650, 30, 110, 25))
        self.endw.setObjectName("endw")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 90, 1121, 531))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.retranslateUi(Dialog)
        self.close.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.close.setText(_translate("Dialog", "Close"))
        self.show.setText(_translate("Dialog", "Show"))
        self.start.setText(_translate("Dialog", "Start Date"))
        self.end.setText(_translate("Dialog", "End Date"))
        self.prit.setText(_translate("Dialog", "Print"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
