import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
import GUI
import random
from numpy.core.defchararray import upper

class Assesser:
    def __init__(self, definitions):
        self.start_point = 20
        self.attempts = 0
        self.correct = 0
        self.history = []
        self.completed = []
        self.announced = False
        self.index = 0
        self.definitions = definitions
        self.keys = []

    def is_unique(self, test):
        if test not in self.completed:
            self.completed.append(test)
        if len(self.completed) == (len(self.definitions) - self.start_point):
            print("You have answered every word.")
            self.announced = True

    def get_index(self):
        return self.index

    def main(self):
        self.index = random.randint(self.start_point, len(self.definitions[1])-1)
        self.keys = list(self.definitions[1])
        print(f'{self.attempts + 1}. What does \"{self.keys[self.index].strip()}\" mean?')
    
    def answer(self, input):
        if input == '!' and self.attempts > 0:
            self.correct += 1
            self.history.pop()
            self.history.append('✔')
            return 1
        elif upper(input.strip()) == upper(self.definitions[2][self.index].strip()):
            self.attempts += 1
            self.correct += 1
            self.history.append('✔')
            self.is_unique(self.index)
            print("Sehr gut!")
            return 1
        else:
            self.attempts += 1
            self.history.append('❌')
            print(f"Dummkopf! It means \"{self.definitions[2][self.index].strip()}\".")
            return 0

    def set_definitions(self, definitions):
        self.definitions = definitions


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Nein out of Ten - In Loving Memory of Shane Karunaratne")
    app.setWindowIcon(QIcon('../images/Flag_of_Germany.png'))
    app.setApplicationDisplayName("Nein out of Ten- In Loving Memory of Shane Karunaratne")

    demo = GUI.MainWindow()

    timer = QTimer()
    timer.start(100)
    #timer.timeout.connect(terminally)
    
    demo.show()
    
    sys.exit(app.exec_())