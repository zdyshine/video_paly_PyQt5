# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5 import  QtGui,  QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_saftey_SR import Ui_MainWindow

from Read_video import VideoThread
from Read_SRvideo import SRVideoThread

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
        self.Video = VideoThread()
        self.SR_Video = SRVideoThread()
    
    def OpenVideo(self):
        if not self.Video.isRunning():
            self.Video.start()
            self.Bic_pushButton.setText('关闭视频')
        else:
            self.Video.Stop_Video()
            self.Bic_pushButton.setText('打开视频')
            #self.Camer_label.setPixmap(QPixmap.fromImage())  #设置图片还原
    
    def Fresh_Camera(self, show_pic):
        self.Bic_label.setScaledContents(True) #图片自适应大小
        self.Bic_label.setPixmap(QPixmap.fromImage(show_pic))
    
    def Un_Open(self):
        QtWidgets.QMessageBox.warning(self, '警告',  '打开视频失败')
        
        
    def Open_SRVideo(self):
        if not self.SR_Video.isRunning():
            self.SR_Video.start()
            self.SR_pushButton.setText('关闭视频')
        else:
            self.SR_Video.Stop_Video()
            self.SR_pushButton.setText('打开视频')
            #self.Camer_label.setPixmap(QPixmap.fromImage())  #设置图片还原
    
    def Fresh_SRCamera(self, show_pic):
        self.SR_label.setScaledContents(True) #图片自适应大小
        self.SR_label.setPixmap(QPixmap.fromImage(show_pic))
        
        
    @pyqtSlot()
    def on_Bic_pushButton_clicked(self):
        self.OpenVideo()
        self.Video.CameraFram.connect(self.Fresh_Camera)
        self.Video.OpenVideoFlage.connect(self.Un_Open)
        
        
    @pyqtSlot()
    def on_SR_pushButton_clicked(self):
        self.Open_SRVideo()
        self.SR_Video.CameraFram.connect(self.Fresh_SRCamera)
        self.SR_Video.OpenVideoFlage.connect(self.Un_Open)
    
    
    @pyqtSlot()
    def on_Play_pushButton_clicked(self):
        
        self.OpenVideo()
        self.Video.CameraFram.connect(self.Fresh_Camera)
#        self.Video.OpenVideoFlage.connect(self.Un_Open)
        
        self.Open_SRVideo()
        self.SR_Video.CameraFram.connect(self.Fresh_SRCamera)
        #self.SR_Video.OpenVideoFlage.connect(self.Un_Open)
    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    
