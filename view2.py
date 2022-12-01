# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushRock = QtWidgets.QPushButton(self.centralwidget)
        self.pushRock.setGeometry(QtCore.QRect(130, 310, 91, 91))
        self.pushRock.setIconSize(QtCore.QSize(100, 100))
        self.pushRock.setObjectName("pushRock")
        self.pushPaper = QtWidgets.QPushButton(self.centralwidget)
        self.pushPaper.setGeometry(QtCore.QRect(260, 310, 91, 91))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../OneDrive/Pictures/Paper.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushPaper.setIcon(icon)
        self.pushPaper.setIconSize(QtCore.QSize(150, 150))
        self.pushPaper.setObjectName("pushPaper")
        self.pushScissors = QtWidgets.QPushButton(self.centralwidget)
        self.pushScissors.setGeometry(QtCore.QRect(390, 310, 91, 91))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../OneDrive/Pictures/scissors.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushScissors.setIcon(icon1)
        self.pushScissors.setIconSize(QtCore.QSize(125, 100))
        self.pushScissors.setObjectName("pushScissors")
        self.radioSingle = QtWidgets.QRadioButton(self.centralwidget)
        self.radioSingle.setGeometry(QtCore.QRect(110, 70, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioSingle.setFont(font)
        self.radioSingle.setObjectName("radioSingle")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioSingle)
        self.radioThree = QtWidgets.QRadioButton(self.centralwidget)
        self.radioThree.setGeometry(QtCore.QRect(260, 70, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioThree.setFont(font)
        self.radioThree.setObjectName("radioThree")
        self.buttonGroup.addButton(self.radioThree)
        self.radioFive = QtWidgets.QRadioButton(self.centralwidget)
        self.radioFive.setGeometry(QtCore.QRect(380, 70, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioFive.setFont(font)
        self.radioFive.setObjectName("radioFive")
        self.buttonGroup.addButton(self.radioFive)
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(60, 10, 491, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelTitle.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.labelOption = QtWidgets.QLabel(self.centralwidget)
        self.labelOption.setGeometry(QtCore.QRect(150, 260, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelOption.setFont(font)
        self.labelOption.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOption.setObjectName("labelOption")
        self.labelPlayer = QtWidgets.QLabel(self.centralwidget)
        self.labelPlayer.setGeometry(QtCore.QRect(140, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.labelPlayer.setFont(font)
        self.labelPlayer.setObjectName("labelPlayer")
        self.labelResults = QtWidgets.QLabel(self.centralwidget)
        self.labelResults.setGeometry(QtCore.QRect(10, 210, 581, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelResults.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.labelResults.setFont(font)
        self.labelResults.setText("")
        self.labelResults.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResults.setObjectName("labelResults")
        self.labelComp = QtWidgets.QLabel(self.centralwidget)
        self.labelComp.setGeometry(QtCore.QRect(350, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.labelComp.setFont(font)
        self.labelComp.setObjectName("labelComp")
        self.labelPChoice = QtWidgets.QLabel(self.centralwidget)
        self.labelPChoice.setGeometry(QtCore.QRect(140, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelPChoice.setFont(font)
        self.labelPChoice.setText("")
        self.labelPChoice.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPChoice.setObjectName("labelPChoice")
        self.labelCChoice = QtWidgets.QLabel(self.centralwidget)
        self.labelCChoice.setGeometry(QtCore.QRect(360, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCChoice.setFont(font)
        self.labelCChoice.setText("")
        self.labelCChoice.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCChoice.setObjectName("labelCChoice")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushRock.setText(_translate("MainWindow", "Rock"))
        self.pushPaper.setText(_translate("MainWindow", "Paper"))
        self.pushScissors.setText(_translate("MainWindow", "Scissors"))
        self.radioSingle.setText(_translate("MainWindow", "Single Game"))
        self.radioThree.setText(_translate("MainWindow", "First to 3"))
        self.radioFive.setText(_translate("MainWindow", "First to 5"))
        self.labelTitle.setText(_translate("MainWindow", "Rock Paper Scissors"))
        self.labelOption.setText(_translate("MainWindow", "Play an option:"))
        self.labelPlayer.setText(_translate("MainWindow", "Player Choice"))
        self.labelComp.setText(_translate("MainWindow", "Computer Choice"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
