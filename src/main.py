import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
import GUI
import random

class Assesser:
    def __init__(self):
        filename = input("What is the file name? ")
        self.df = pd.read_csv(f"{filename}.csv", header=None, index_col=0)
        self.definitions = self.df.to_dict()[1]
        self.times = {}
        self.inv_definitions = {}
        print(f'Your chosen list is {len(self.definitions)} long.')
        self.start_point = int(input("Select a starting point (or enter 0 to practice the whole list): "))
        while self.start_point > (len(self.definitions) - 1):
            self.start_point = int(input(f'Your chosen list is {len(self.definitions)} long. Please choose a starting point smaller than the length. '))
        self.attempts = 0
        self.correct = 0
        self.history = []
        self.completed = []
        self.announced = False
        self.index = 0

    def is_unique(self, test):
        if test not in self.completed:
            self.completed.append(test)
        if len(self.completed) == (len(self.definitions) - self.start_point):
            print("You have answered every word.")
            self.announced = True

    def main(self):
        self.index = random.randint(self.start_point, len(self.definitions)-1)
        keys = list(self.definitions.keys())
        print(f'{self.attempts + 1}. What does \"{keys[self.index].strip()}\" mean?')
        answer = input()
        if answer == '!' and attempts > 0:
            self.correct += 1
            self.history.pop()
            self.history.append('✔')
        elif upper(answer.strip()) == upper(self.definitions[keys[self.index]].strip()):
            self.attempts += 1
            self.correct += 1
            self.history.append('✔')
            self.is_unique(index)
            print("Sehr gut!")
        else:
            self.attempts += 1
            self.history.append('❌')
            print(f"Dummkopf! It means \"{self.definitions[keys[index]].strip()}\".")

assesser = Assesser()

def terminally():
    try:
        assesser.main()
    except KeyboardInterrupt:
        top_streak = 0
        streak = 0
        print(f'Your score is {correct} out of {attempts}. That is {round(correct/attempts*100,2)}%.')
        for his in history:
            print(f'{his}', end='')
            if his == "✔":
                streak += 1
                if top_streak < streak:
                    top_streak = streak
            else:
                if top_streak < streak:
                    top_streak = streak
                streak = 0
            
        print('\n')
        print(f'Your longest streak was: {top_streak}')

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