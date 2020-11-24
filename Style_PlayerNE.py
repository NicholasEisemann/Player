# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Style_PlayerNE.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 334)
        MainWindow.setMinimumSize(QtCore.QSize(474, 334))
        MainWindow.setMaximumSize(QtCore.QSize(474, 334))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0.453202 rgba(156, 255, 0, 255), stop:1 rgba(22, 255, 135, 255));")
        MainWindow.setIconSize(QtCore.QSize(95, 32))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setEnabled(True)
        self.play.setGeometry(QtCore.QRect(30, 220, 51, 41))
        self.play.setMouseTracking(False)
        self.play.setFocusPolicy(QtCore.Qt.TabFocus)
        self.play.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.play.setToolTip("")
        self.play.setToolTipDuration(0)
        self.play.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("play_or_stop.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.play.setIcon(icon)
        self.play.setIconSize(QtCore.QSize(45, 45))
        self.play.setAutoRepeatDelay(0)
        self.play.setAutoRepeatInterval(0)
        self.play.setAutoDefault(False)
        self.play.setDefault(False)
        self.play.setFlat(True)
        self.play.setObjectName("play")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("music_logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setEnabled(True)
        self.pause.setGeometry(QtCore.QRect(90, 220, 51, 41))
        self.pause.setMouseTracking(False)
        self.pause.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pause.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pause.setToolTip("")
        self.pause.setToolTipDuration(0)
        self.pause.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause.setIcon(icon1)
        self.pause.setIconSize(QtCore.QSize(45, 45))
        self.pause.setAutoRepeatDelay(0)
        self.pause.setAutoRepeatInterval(0)
        self.pause.setAutoDefault(False)
        self.pause.setDefault(False)
        self.pause.setFlat(True)
        self.pause.setObjectName("pause")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setEnabled(True)
        self.stop.setGeometry(QtCore.QRect(160, 220, 51, 41))
        self.stop.setMouseTracking(False)
        self.stop.setFocusPolicy(QtCore.Qt.TabFocus)
        self.stop.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.stop.setToolTip("")
        self.stop.setToolTipDuration(0)
        self.stop.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon2)
        self.stop.setIconSize(QtCore.QSize(45, 45))
        self.stop.setAutoRepeatDelay(0)
        self.stop.setAutoRepeatInterval(0)
        self.stop.setAutoDefault(False)
        self.stop.setDefault(False)
        self.stop.setFlat(True)
        self.stop.setObjectName("stop")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(230, 10, 231, 311))
        self.listWidget.setObjectName("listWidget")
        self.volume_up = QtWidgets.QPushButton(self.centralwidget)
        self.volume_up.setEnabled(True)
        self.volume_up.setGeometry(QtCore.QRect(60, 280, 51, 41))
        self.volume_up.setMouseTracking(False)
        self.volume_up.setFocusPolicy(QtCore.Qt.TabFocus)
        self.volume_up.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.volume_up.setToolTip("")
        self.volume_up.setToolTipDuration(0)
        self.volume_up.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("volume_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.volume_up.setIcon(icon3)
        self.volume_up.setIconSize(QtCore.QSize(30, 30))
        self.volume_up.setAutoRepeatDelay(0)
        self.volume_up.setAutoRepeatInterval(0)
        self.volume_up.setAutoDefault(False)
        self.volume_up.setDefault(False)
        self.volume_up.setFlat(True)
        self.volume_up.setObjectName("volume_up")
        self.volume_low = QtWidgets.QPushButton(self.centralwidget)
        self.volume_low.setEnabled(True)
        self.volume_low.setGeometry(QtCore.QRect(130, 280, 51, 41))
        self.volume_low.setMouseTracking(False)
        self.volume_low.setFocusPolicy(QtCore.Qt.TabFocus)
        self.volume_low.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.volume_low.setToolTip("")
        self.volume_low.setToolTipDuration(0)
        self.volume_low.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("volume_low.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.volume_low.setIcon(icon4)
        self.volume_low.setIconSize(QtCore.QSize(30, 30))
        self.volume_low.setAutoRepeatDelay(0)
        self.volume_low.setAutoRepeatInterval(0)
        self.volume_low.setAutoDefault(False)
        self.volume_low.setDefault(False)
        self.volume_low.setFlat(True)
        self.volume_low.setObjectName("volume_low")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
