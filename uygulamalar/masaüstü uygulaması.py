from cgitb import text
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


def uygulamam():

    uygulama= QApplication(sys.argv)
    pencere=QMainWindow()
    

    pencere.setGeometry(100,400,600,500)
    pencere.setWindowTitle("Hello")
    pencere.setToolTip("Ben geldim")
    pencere.setWindowIcon(QIcon('collie.png'))
        
    etiketIsim= QtWidgets.QLabel(pencere)
    etiketIsim.setText('Adınız: ')
    etiketIsim.move(50,50)
     
    text_isim = QtWidgets.QLineEdit(pencere)
    text_isim.move(100,50)
    

    sonuc_label= QtWidgets.QLabel(pencere)
    sonuc_label.move(100,150)
    sonuc_label.setText('sonuc')

    def kayıt():
        sonuc_label.setText(f"kaydedildi   :  {text_isim.text()}")

    button_kayıt= QtWidgets.QPushButton(pencere)
    button_kayıt.move(100,100)
    button_kayıt.setText('kayıt')
    button_kayıt.clicked.connect(kayıt)

    



    pencere.show()

    sys.exit(uygulama.exec_())

uygulamam()
