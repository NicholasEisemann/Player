from PyQt5 import QtCore, QtGui, QtWidgets
from Style_PlayerNE import Ui_MainWindow
import pygame
from pygame import mixer
import sys

mixer.init()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def btnClickedstart():
    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.load('TravisScott-Goosebumps.mp3')
        pygame.mixer.music.play(0)
    else:
        pygame.mixer.music.unpause()

def btnClickedstop():
    pygame.mixer.music.stop()

def btnClickedpause():
    pygame.mixer.music.pause()


ui.play.clicked.connect(btnClickedstart)
ui.stop.clicked.connect(btnClickedstop)
ui.pause.clicked.connect(btnClickedpause)




sys.exit(app.exec_())
