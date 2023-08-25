import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        
        self.test= QPushButton(self)
        self.imageTest = QPixmap('../images/Flag_of_Germany.png')
        self.labelTest = QLabel(self)
        self.labelTest.setPixmap(self.imageTest)
        
        

        layout = QVBoxLayout()
        layout.addWidget(self.labelTest)
        layout.addWidget(self.test)
        
        container = QWidget()
        container.setLayout(layout)
        
        
        self.setCentralWidget(container)
        #self.setupUi(self)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Deutsch - In Loving Memory of Shane Karunaratne")
    app.setWindowIcon(QIcon('../images/Flag_of_Germany.png'))
    app.setApplicationDisplayName("Deutsch - In Loving Memory of Shane Karunaratne")

    demo = MainWindow()

    timer = QTimer()
    timer.start(100)
    
    demo.show()
    
    sys.exit(app.exec_())