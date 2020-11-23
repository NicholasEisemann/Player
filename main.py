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
# dict_music_sort = dict(zip(music_sort, music_sort)).values()


def btnClickedstart():
    if pygame.mixer.music.get_busy() == False:
            selitem = ui.listWidget.currentRow()
            put = music_sort[selitem]
            pygame.mixer.music.load(dict_music + '/' + put)
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
ui.listWidget.addItems(music_sort)


sys.exit(app.exec_())
