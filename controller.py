from PyQt5 import QtWidgets
from New_Style_Player import Ui_MainWindow_Player
import Playlist
import pygame
from pygame import mixer
import sys

mixer.init()


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow_Player()
        self.ui.setupUi(self)
        self.ui.play.clicked.connect(lambda: self.btnClickedstart())
        self.ui.stop.clicked.connect(lambda: self.btnClickedstop())
        self.ui.pause.clicked.connect(lambda: self.btnClickedpause())
        self.ui.playlist.clicked.connect(lambda: self.Playlist.Ui_MainWindow_Playlist)

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
