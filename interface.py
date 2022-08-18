from curses import window
from PySide2.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton
from PySide2.QtCore import QSize
import sys

class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self). __init__()

        self.setWindowTitle('Distribuição Lucena - Criador de QRCode.')
        button = QPushButton('Clique aqui')
        self.setFixedSize(QSize(400,240))

        self.setCentralWidget(button)

        button.clicked.connect(self.clicked_button)
    
    def clicked_button(self):
        print('Você clicou no botão!')

app =  QApplication(sys.argv)

window= MyWidget()
window.show()

app.exec_()

