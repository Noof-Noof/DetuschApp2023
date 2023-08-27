import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
import main

definitions = None
userinput = None

class Streaks(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.flag = QPixmap('../images/Flag_of_Germany.png')
        self.setPixmap(self.flag)
        self.show()

    def update_image(self, index):
        if type(definitions[3][index]) == 'float':
            self.flag = QPixmap(definitions[3][index])
        else:
            self.flag = QPixmap('../images/Flag_of_Germany.png')
        self.setPixmap(self.flag)

class WordLabel(QLabel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.resize(400, 200)
        self.show()

    def update_label(self, index):
        self.setText(definitions[1][index])

class User(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.resize(400,100)
        self.textChanged.connect(self.writting)

    def writting(self, msg):
        global userinput
        userinput = msg

class Enter(QPushButton):
    def __init__(self, parent):
        super().__init__("submit", parent=parent)
        self.clicked.connect(self.pushPress)
        self.dad = parent
        self.show()
    
    def pushPress(self):
        isRight = self.dad.assessor.answer(userinput)
        if isRight:
            self.dad.correct.correct(self.dad.assessor.get_index())
        else:
            self.dad.correct.incorrect(self.dad.assessor.get_index())
        self.dad.assessor.main()
        index = self.dad.assessor.get_index()
        self.dad.word.update_label(index)
        self.dad.streaks.update_image(index)

class Correct(QLabel):
    def __init__(self, parent):
        self.dad = parent
        super().__init__(parent=parent)
        self.resize(400, 100)

    def incorrect(self, index):
        self.setText(f"Dummkopf! It means \"{definitions[2][index].strip()}\".")
    
    def correct(self, index):
        self.setText("Sehr gut!")


class Load(QPushButton):
    def __init__(self, parent):
        super().__init__("Load File", parent)
        self.clicked.connect(self.load_file)
        self.show()
        self.fileNames = None
        self.dad = parent
    
    def load_file(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilter("csv(*.csv)")
        global definitions
        if dlg.exec_():
            self.fileNames = dlg.selectedFiles()
            df = pd.read_csv(self.fileNames[0], header=None, index_col=0)
            definitions = df.to_dict(orient='list')
            self.dad.assessor.set_definitions(definitions)
            self.dad.assessor.main()
            
            index = self.dad.assessor.get_index()
            self.dad.word.update_label(index)
            self.dad.streaks.update_image(index)

    def get_file_name(self):
        if self.fileNames:
            return self.fileNames[0]
        return None
    


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        
        self.assessor = main.Assesser(definitions)
        self.streaks = Streaks(self)
        self.word = WordLabel(self)
        self.user = User(self)
        self.enter = Enter(self)
        self.load = Load(self)
        self.correct = Correct(self)
        

        layout = QVBoxLayout()
        layout.addWidget(self.streaks)
        layout.addWidget(self.load)
        layout.addWidget(self.word)
        layout.addWidget(self.user)
        layout.addWidget(self.correct)
        layout.addWidget(self.enter)
        
        
        container = QWidget()
        container.setLayout(layout)
        
        
        self.setCentralWidget(container)
        #self.setupUi(self)

    def get_file_name(self):
        return self.load.get_file_name()