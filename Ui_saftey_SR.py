# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\0-比赛\2019公共安全大赛\video\saftey_SR.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 785)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.SR_label = QtWidgets.QLabel(self.centralWidget)
        self.SR_label.setGeometry(QtCore.QRect(130, 440, 480, 270))
        self.SR_label.setObjectName("SR_label")
        self.Bic_label = QtWidgets.QLabel(self.centralWidget)
        self.Bic_label.setGeometry(QtCore.QRect(130, 110, 480, 270))
        self.Bic_label.setObjectName("Bic_label")
        self.SR_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.SR_pushButton.setGeometry(QtCore.QRect(310, 30, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(12)
        self.SR_pushButton.setFont(font)
        self.SR_pushButton.setObjectName("SR_pushButton")
        self.Play_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.Play_pushButton.setGeometry(QtCore.QRect(470, 30, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(12)
        self.Play_pushButton.setFont(font)
        self.Play_pushButton.setObjectName("Play_pushButton")
        self.Bic_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.Bic_pushButton.setGeometry(QtCore.QRect(130, 30, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(12)
        self.Bic_pushButton.setFont(font)
        self.Bic_pushButton.setObjectName("Bic_pushButton")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SR_label.setText(_translate("MainWindow", "TextLabel"))
        self.Bic_label.setText(_translate("MainWindow", "TextLabel"))
        self.SR_pushButton.setText(_translate("MainWindow", "高分辨视频"))
        self.Play_pushButton.setText(_translate("MainWindow", "同时播放"))
        self.Bic_pushButton.setText(_translate("MainWindow", "低分辨视频"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

