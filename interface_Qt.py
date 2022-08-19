from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QPushButton, QToolBar
import sys

class Janela1(QMainWindow):
    def __init__(self):
        super(Janela1, self).__init__()

        self.setWindowTitle('Distribuição Lucena - Criador de QRCode.')
        button = QPushButton('Clique aqui')
    
app = QApplication(sys.argv)
Mostrar_Janela=Janela1
Mostrar_Janela.show()