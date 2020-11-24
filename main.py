import sys, os, codecs
from PyQt5 import QtCore, QtGui, QtWidgets
from Style_PlayerNE import Ui_MainWindow
import pygame
from pygame import mixer

mixer.init()



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

dict_music = '/Users/nicholaseisemann/Desktop/Python_Project/Player_beta/Music'
music_sort = os.listdir(dict_music)



def btnClickedstart():
    if pygame.mixer.music.get_busy() == False:
            selitem = ui.listWidget.currentRow()
            put = music_sort[selitem]
            pygame.mixer.music.load(dict_music + '/' + put)
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play(0)
    else:
        pygame.mixer.music.unpause()

def btnClickedstop():
    pygame.mixer.music.stop()

def btnClickedpause():
    pygame.mixer.music.pause()

def set_volume_low():
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)


def set_volume_up():
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)

ui.play.clicked.connect(btnClickedstart)
ui.stop.clicked.connect(btnClickedstop)
ui.pause.clicked.connect(btnClickedpause)
ui.listWidget.addItems(music_sort)
ui.volume_low.clicked.connect(set_volume_low)
ui.volume_up.clicked.connect(set_volume_up)


sys.exit(app.exec_())
