from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


def uygulamam():

    uygulama= QApplication(sys.argv)
    pencere=QMainWindow()
    

    pencere.setGeometry(200,350,600,500)
    pencere.setWindowTitle("Hello")
    pencere.setToolTip("Ben geldim")
    pencere.setWindowIcon(QIcon('collie.png'))
        
    etiketIsim= QtWidgets.QLabel(pencere)
    etiketIsim.setText('Adınız: ')
    etiketIsim.move(50,50)
     
    text_isim = QtWidgets.QLineEdit(pencere)
    text_isim.move(100,50)
    

    sonuc_label= QtWidgets.QLabel(pencere)
    sonuc_label.move(225,50)
    sonuc_label.setText('sonuc')

    def kayıt():
        sonuc_label.setText(f"kaydedildi   :  {text_isim.text()}")

    button_kayıt= QtWidgets.QPushButton(pencere)
    button_kayıt.move(100,100)
    button_kayıt.setText('kayıt')
    button_kayıt.clicked.connect(kayıt)

    def dosya():
        dosyam = open("dosyalar/kayıt.txt","w")
        print(text_isim.text(),file=dosyam)
        dosyam.close()

    button_dosya= QtWidgets.QPushButton(pencere)
    button_dosya.move(100,150)
    button_dosya.setText('belgele')
    button_dosya.clicked.connect(dosya)


    pencere.show()

    sys.exit(uygulama.exec_())

uygulamam()
