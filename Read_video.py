from Ui_saftey_SR import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage
import cv2


class VideoThread(QThread, Ui_MainWindow):
    CameraFram = pyqtSignal(QImage)
    OpenVideoFlage = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__()
    def run(self):
        
        
        self.Run_Camera = 1
        self.vedio_path = 'D:\\0-比赛\\2019-优酷视频超分\\show\\Bicu.mp4'
        self.cap = cv2.VideoCapture(self.vedio_path)  # cv2读取视频
       # fps = self.cap.get(cv2.CAP_PROP_FPS) #cv2获取帧数
       # print(fps)
        #获取cap视频流的每帧大小  
        size = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),  
                int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  
        print(size)    
        h = size[1]
        w = size[0]        
        COUNT = 0
        totalFrameNumber = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)    
        
        if (self.cap.isOpened()):
            #while self.Run_Camera:
            while COUNT < totalFrameNumber:
                ret,  self.img_read = self.cap.read()
                #if self.img_read.all:
                #h, w = self.img_read.shape[:2]
                #print(h, w)
#                cv2.waitKey(1) #延时1s
                if ret !=None :
                    
                    input_img = cv2.cvtColor(self.img_read, cv2.COLOR_BGR2RGB)
                    show_pic = QImage(input_img.data,  w, h, QImage.Format_RGB888)
                    
                    
                    if self.Run_Camera:
                        self.CameraFram.emit(show_pic)
                    else:
                        break
                    #time.sleep(0.005)
                else:
                    print('视频已打开')
                COUNT = COUNT + 1
            self.cap.release()
            self.quit()
        else:
            self.OpenVideoFlage.emit(self.cap.isOpened())
    
    def Stop_Video(self):
        self.Run_Camera = 0
        
            
        
    
#    def identify(self):
#        
#        
#    def save_img(self):
            
