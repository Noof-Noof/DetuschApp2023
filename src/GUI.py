import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd

class Streaks(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.flag = QPixmap('../images/Flag_of_Germany.png')
        self.setPixmap(self.flag)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        
        self.test= QPushButton(self)
        
        self.streaks = Streaks(self)
        
        

        layout = QVBoxLayout()
        layout.addWidget(self.streaks)
        layout.addWidget(self.test)
        
        container = QWidget()
        container.setLayout(layout)
        
        
        self.setCentralWidget(container)
        #self.setupUi(self)