from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
import qrcode

def receber_link():
   lk = QR.g_link.text()
   imgQR= qrcode.make(lk)
   QMessageBox.about(QR, 'Seu QRCode', lk)
   iQR.show()
   imgQR.save('teste_1.png')
   iQR.aqui.setPixmap(QtGui.QPixmap('teste_1.png'))
   QR.g_link.setText('')


app=QtWidgets.QApplication([])
QR=uic.loadUi("painel.ui")
iQR=uic.loadUi("aparece.ui")
QR.Gerar_QRCode.clicked.connect(receber_link)

QR.show()
app.exec()