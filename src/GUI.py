import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd

definitions = None

class Streaks(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.flag = QPixmap('../images/Flag_of_Germany.png')
        self.setPixmap(self.flag)

class WordLabel(QLabel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.resize(400, 200)



class Load(QPushButton):
    def __init__(self, parent):
        super().__init__("Load File", parent)
        self.clicked.connect(self.load_file)
        self.show()
        self.fileNames = None
    
    def load_file(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilter("csv(*.csv)")
        if dlg.exec_():
            self.fileNames = dlg.selectedFiles()
            df = pd.read_csv(self.fileNames[0], header=None, index_col=0)
            definitions = df.to_dict()[1]
            print(definitions)

    def get_file_name(self):
        if self.fileNames:
            return self.fileNames[0]
        return None
    


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        
        self.streaks = Streaks(self)
        self.load = Load(self)
        
        

        layout = QVBoxLayout()
        layout.addWidget(self.streaks)
        layout.addWidget(self.load)
        
        container = QWidget()
        container.setLayout(layout)
        
        
        self.setCentralWidget(container)
        #self.setupUi(self)

    def get_file_name(self):
        return self.load.get_file_name()