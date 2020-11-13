import sys

from PyQt5 import QtCore, QtWidgets, QtMultimedia

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    filename = 'TravisScott-Goosebumps.mp3'
    fullpath = QtCore.QDir.current().absoluteFilePath(filename)
    media = QtCore.QUrl.fromLocalFile(fullpath)
    content = QtMultimedia.QMediaContent(media)
    player = QtMultimedia.QMediaPlayer()
    player.setMedia(content)
    player.play()
    sys.exit(app.exec_())
