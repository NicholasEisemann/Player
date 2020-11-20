from PyQt5 import QtWidgets
from new_style_player import Ui_MainWindow
import pygame
from pygame import mixer
import sys
mixer.init()

pygame.mixer.music.get_busy()


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.play.clicked.connect(lambda: self.btnClickedstart())
        self.ui.stop.clicked.connect(lambda: self.btnClickedstop())
        self.ui.pause.clicked.connect(lambda: self.btnClickedpause())


    def btnClickedstart(self):
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.load('TravisScott-Goosebumps.mp3')
            pygame.mixer.music.play(0)
        else:
            pygame.mixer.music.unpause()

    def btnClickedstop(self):
            pygame.mixer.music.stop()

    def btnClickedpause(self):
            pygame.mixer.music.pause()




app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
