from turtle import color
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
import qrcode, seletor_local

def receber_link():

   lk = QR.g_link.text() #pega o link que será utilizado.
   
   imgQR = qrcode.make(lk) #cria um QRCode
   dir_s = seletor_local.ret_local_sv() #diretorio em que irá salvar
   QR.g_link.setText('')
   if len(dir_s) < 3:
      aviso = QMessageBox
      aviso.about(QR, 'SEM LOCAL PARA SALVAR SEU QRCODE!', "Você não selecionou um local para o seu QRCode. Repita a operação")
   else:
      iQR.show()
      caminho=dir_s+'/Seu_QRCode.png'
      imgQR.save(caminho)
      iQR.space_QR.setPixmap(QtGui.QPixmap(caminho))
      QR.g_link.setText('')


app=QtWidgets.QApplication([])
QR=uic.loadUi("painel.ui")
iQR=uic.loadUi("apresenta_QR.ui")
QR.Gerar_QRCode.clicked.connect(receber_link)

QR.show()
app.exec()