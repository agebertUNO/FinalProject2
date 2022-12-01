from PyQt5.QtWidgets import *
from view2 import *
import random

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.p_score = 0
        self.c_score = 0
        self.labelResults.setText('Please choose a game option above.')
        self.pushRock.clicked.connect(lambda: self.rock())
        self.pushScissors.clicked.connect(lambda: self.scissors())
        self.pushPaper.clicked.connect(lambda: self.paper())


    def computer(self):
        items = ['Rock', 'Paper', 'Scissors']
        choice = random.choice(items)
        return choice

    def computer_point3(self):
        self.labelResults.setText('Computer gets a point. Choose again!')
        self.c_score += 1
        if self.c_score == 3:
            self.labelResults.setText('Computer Wins!')
            self.reset()

    def player_point3(self):
        self.labelResults.setText('You get a point. Choose again!')
        self.c_score += 1
        if self.c_score == 3:
            self.labelResults.setText('You Win!')
            self.reset()

    def computer_point5(self):
        self.labelResults.setText('Computer gets a point. Choose again!')
        self.c_score += 1
        if self.c_score == 5:
            self.labelResults.setText('Computer Wins!')
            self.reset()

    def player_point5(self):
        self.labelResults.setText('You get a point. Choose again')
        self.p_score += 1
        if self.p_score == 5:
            self.labelResults.setText('You Win!')
            self.reset()

    def reset(self):
        self.p_score = 0
        self.c_score = 0

    def rock(self):
        try:
            checked = [self.buttonGroup.buttons()[x].isChecked() for x in range(len(self.buttonGroup.buttons()))].index(
                True)
            if checked == 0:
                c_choice = self.computer()
                self.labelCChoice.setText(c_choice)
                self.labelPChoice.setText('Rock')
                if c_choice == 'Rock':
                    self.labelResults.setText('Draw')
                elif c_choice == 'Scissors':
                    self.labelResults.setText('You Win!')
                elif c_choice == 'Paper':
                    self.labelResults.setText('Computer Wins!')
            elif checked == 1:
                c_choice = self.computer()
                self.labelCChoice.setText(c_choice)
                self.labelPChoice.setText('Rock')
                if c_choice == 'Rock':
                    self.labelResults.setText('Choose again')
                elif c_choice == 'Scissors':
                    self.player_point3()
                elif c_choice == 'Paper':
                    self.computer_point3()
            elif checked == 2:
                c_choice = self.computer()
                self.labelCChoice.setText(c_choice)
                self.labelPChoice.setText('Rock')
                if c_choice == 'Rock':
                    self.labelResults.setText('Choose again')
                elif c_choice == 'Scissors':
                    self.player_point5()
                elif c_choice == 'Paper':
                    self.computer_point5()
        except ValueError:
            self.labelResults.setText('Pick an game option to play!')

    def paper(self):
        try:
            checked = [self.buttonGroup.buttons()[x].isChecked() for x in range(len(self.buttonGroup.buttons()))].index(
                True)
            if checked == 0:
                c_choice = self.computer()
                self.labelCChoice.setText(c_choice)
                self.labelPChoice.setText('Paper')
                if c_choice == 'Rock':
                    self.labelResults.setText('You Win!')
                elif c_choice == 'Scissors':
                    self.labelResults.setText('Computer Wins!')
                elif c_choice == 'Paper':
                    self.labelResults.setText('Draw')
            elif checked == 1:
                c_choice = self.computer()
                self.labelCChoice.setText(c_choice)
                self.labelPChoice.setText('Paper')
                if c_choice == 'Rock':
                    self.player_point3()
                elif c_choice == 'Scissors':
                    self.computer_point3()
                elif c_choice == 'Paper':
                    self.labelResults.setText('Draw')
            elif checked == 2:
                c_choice = self.computer()
                self.labelCChoice.setText(c_choice)
                self.labelPChoice.setText('Paper')
                if c_choice == 'Rock':
                    self.player_point5()
                elif c_choice == 'Scissors':
                    self.computer_point5()
                elif c_choice == 'Paper':
                    self.labelResults.setText('Draw')
        except ValueError:
            self.labelResults.setText('Pick an game option to play!')

    def scissors(self):
        try:
            checked = [self.buttonGroup.buttons()[x].isChecked() for x in range(len(self.buttonGroup.buttons()))].index(
                True)
            if checked == 0:
                c_choice = self.computer()
                self.labelCChoice.setText(c_choice)
                self.labelPChoice.setText('Scissors')
                if c_choice == 'Rock':
                    self.labelResults.setText('Computer Wins!')
                elif c_choice == 'Scissors':
                    self.labelResults.setText('Draw')
                elif c_choice == 'Paper':
                    self.labelResults.setText('You Win')
            if checked == 1:
                c_choice = self.computer()
                self.labelCChoice.setText(c_choice)
                self.labelPChoice.setText('Scissors')
                if c_choice == 'Rock':
                    self.computer_point3()
                elif c_choice == 'Scissors':
                    self.labelResults.setText('Draw')
                elif c_choice == 'Paper':
                    self.player_point3()
            if checked == 2:
                c_choice = self.computer()
                self.labelCChoice.setText(c_choice)
                self.labelPChoice.setText('Scissors')
                if c_choice == 'Rock':
                    self.computer_point5()
                elif c_choice == 'Scissors':
                    self.labelResults.setText('Draw')
                elif c_choice == 'Paper':
                    self.player_point5()
        except ValueError:
            self.labelResults.setText('Pick an game option to play!')