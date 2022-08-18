import qrcode
import os

link_paraQR = input('Digite o link que deseja usar para criar o QRCode: ')
imgQR= qrcode.make(link_paraQR)
imgQR.save('QR_amazon.png')