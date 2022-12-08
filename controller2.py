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
        items = ['rock.png', 'Paper.png', 'scissors.png']
        choice = random.choice(items)
        return choice

    def computer_point3(self):
        self.labelResults.setText('Computer gets a point. Choose again!')
        self.c_score += 1
        self.labelCscore.setText(f'{self.c_score}')
        if self.c_score == 3:
            self.labelResults.setText('Computer Wins!')
            self.reset()

    def player_point3(self):
        self.labelResults.setText('You get a point. Choose again!')
        self.p_score += 1
        self.labelPscore.setText(f'{self.p_score}')
        if self.p_score == 3:
            self.labelResults.setText('You Win!')
            self.reset()

    def computer_point5(self):
        self.labelResults.setText('Computer gets a point. Choose again!')
        self.c_score += 1
        self.labelCscore.setText(f'{self.c_score}')
        if self.c_score == 5:
            self.labelResults.setText('Computer Wins!')
            self.reset()

    def player_point5(self):
        self.labelResults.setText('You get a point. Choose again')
        self.p_score += 1
        self.labelPscore.setText(f'{self.p_score}')
        if self.p_score == 5:
            self.labelResults.setText('You Win!')
            self.reset()

    def reset(self):
        self.p_score = 0
        self.c_score = 0
        self.labelCscore.setText(f'{self.c_score}')
        self.labelPscore.setText(f'{self.p_score}')

    def rock(self):
        try:
            checked = [self.buttonGroup.buttons()[x].isChecked() for x in range(len(self.buttonGroup.buttons()))].index(
                True)
            if checked == 0:
                c_choice = self.computer()
                self.labelCChoice.setPixmap(QtGui.QPixmap(c_choice))
                self.labelPChoice.setPixmap(QtGui.QPixmap('rock.png'))
                if c_choice == 'rock.png':
                    self.labelResults.setText('Draw')
                elif c_choice == 'scissors.png':
                    self.labelResults.setText('You Win!')
                    self.p_score += 1
                    self.labelPscore.setText(f'{self.p_score}')
                elif c_choice == 'Paper.png':
                    self.labelResults.setText('Computer Wins!')
                    self.c_score += 1
                    self.labelCscore.setText(f'{self.c_score}')
            elif checked == 1:
                c_choice = self.computer()
                self.labelCChoice.setPixmap(QtGui.QPixmap(c_choice))
                self.labelPChoice.setPixmap(QtGui.QPixmap('rock.png'))
                if c_choice == 'rock.png':
                    self.labelResults.setText('Choose again')
                elif c_choice == 'scissors.png':
                    self.player_point3()
                elif c_choice == 'Paper.png':
                    self.computer_point3()
            elif checked == 2:
                c_choice = self.computer()
                self.labelCChoice.setPixmap(QtGui.QPixmap(c_choice))
                self.labelPChoice.setPixmap(QtGui.QPixmap('rock.png'))
                if c_choice == 'rock.png':
                    self.labelResults.setText('Choose again')
                elif c_choice == 'scissors.png':
                    self.player_point5()
                elif c_choice == 'Paper.png':
                    self.computer_point5()
        except ValueError:
            self.labelResults.setText('Pick an game option to play!')

    def paper(self):
        try:
            checked = [self.buttonGroup.buttons()[x].isChecked() for x in range(len(self.buttonGroup.buttons()))].index(
                True)
            if checked == 0:
                c_choice = self.computer()
                self.labelCChoice.setPixmap(QtGui.QPixmap(c_choice))
                self.labelPChoice.setPixmap(QtGui.QPixmap('Paper.png'))
                if c_choice == 'rock.png':
                    self.labelResults.setText('You Win!')
                    self.p_score += 1
                    self.labelPscore.setText(f'{self.p_score}')
                elif c_choice == 'scissors.png':
                    self.labelResults.setText('Computer Wins!')
                    self.c_score += 1
                    self.labelCscore.setText(f'{self.c_score}')
                elif c_choice == 'Paper.png':
                    self.labelResults.setText('Draw')
            elif checked == 1:
                c_choice = self.computer()
                self.labelCChoice.setPixmap(QtGui.QPixmap(c_choice))
                self.labelPChoice.setPixmap(QtGui.QPixmap('Paper.png'))
                if c_choice == 'rock.png':
                    self.player_point3()
                elif c_choice == 'scissors.png':
                    self.computer_point3()
                elif c_choice == 'Paper.png':
                    self.labelResults.setText('Draw')
            elif checked == 2:
                c_choice = self.computer()
                self.labelCChoice.setPixmap(QtGui.QPixmap(c_choice))
                self.labelPChoice.setPixmap(QtGui.QPixmap('Paper.png'))
                if c_choice == 'rock.png':
                    self.player_point5()
                elif c_choice == 'scissors.png':
                    self.computer_point5()
                elif c_choice == 'Paper.png':
                    self.labelResults.setText('Draw')
        except ValueError:
            self.labelResults.setText('Pick an game option to play!')

    def scissors(self):
        try:
            checked = [self.buttonGroup.buttons()[x].isChecked() for x in range(len(self.buttonGroup.buttons()))].index(
                True)
            if checked == 0:
                c_choice = self.computer()
                self.labelCChoice.setPixmap(QtGui.QPixmap(c_choice))
                self.labelPChoice.setPixmap(QtGui.QPixmap('scissors.png'))
                if c_choice == 'rock.png':
                    self.labelResults.setText('Computer Wins!')
                    self.c_score += 1
                    self.labelCscore.setText(f'{self.c_score}')
                elif c_choice == 'scissors.png':
                    self.labelResults.setText('Draw')
                elif c_choice == 'Paper.png':
                    self.labelResults.setText('You Win')
                    self.p_score += 1
                    self.labelPscore.setText(f'{self.p_score}')
            if checked == 1:
                c_choice = self.computer()
                self.labelCChoice.setPixmap(QtGui.QPixmap(c_choice))
                self.labelPChoice.setPixmap(QtGui.QPixmap('scissors.png'))
                if c_choice == 'rock.png':
                    self.computer_point3()
                elif c_choice == 'scissors.png':
                    self.labelResults.setText('Draw')
                elif c_choice == 'Paper.png':
                    self.player_point3()
            if checked == 2:
                c_choice = self.computer()
                self.labelCChoice.setPixmap(QtGui.QPixmap(c_choice))
                self.labelPChoice.setPixmap(QtGui.QPixmap('scissors.png'))
                if c_choice == 'rock.png':
                    self.computer_point5()
                elif c_choice == 'scissors.png':
                    self.labelResults.setText('Draw')
                elif c_choice == 'Paper.png':
                    self.player_point5()
        except ValueError:
            self.labelResults.setText('Pick an game option to play!')