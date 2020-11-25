import sys, os, codecs
from PyQt5 import QtCore, QtGui, QtWidgets
from Style_PlayerNE import Ui_MainWindow
import pygame
from pygame import mixer

mixer.init()

# подключение к шаблону окна

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# директория с музыкой
dict_music = '/Users/nicholaseisemann/Desktop/Python_Project/Player_beta/Music'
# получение списка файлов
music_sort = os.listdir(dict_music)


def btn_clicked_start():
    if pygame.mixer.music.get_busy() == False:
        item = ui.listWidget.currentRow()
        put = music_sort[item]
        pygame.mixer.music.load(dict_music + '/' + put) # вывод полного пути до файла для загрузки
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(0)
    else:
        pygame.mixer.music.unpause()


def btn_clicked_stop():
    pygame.mixer.music.stop()


def btn_clicked_pause():
    pygame.mixer.music.pause()


def set_volume_low():
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)


def set_volume_up():
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)


# подключение к кнопкам

ui.play.clicked.connect(btn_clicked_start)
ui.stop.clicked.connect(btn_clicked_stop)
ui.pause.clicked.connect(btn_clicked_pause)
ui.listWidget.addItems(music_sort)
ui.volume_low.clicked.connect(set_volume_low)
ui.volume_up.clicked.connect(set_volume_up)

sys.exit(app.exec_())
