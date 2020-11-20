from PyQt5 import QtWidgets
from Style_List import Ui_MainWindow_Playlist
import controller
import sys


class MyWindowPlaylist(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindowPlaylist, self).__init__()
        self.ui = Ui_MainWindow_Playlist()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = MyWindowPlaylist()
application.show()

sys.exit(app.exec())
