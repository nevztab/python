from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class Uygulamam (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Uygulamam 2')
        self.setGeometry(100,100,500,500)
        self.arayuz()

    def arayuz(self):
        self.label_isim= QtWidgets.QLabel(self)
        self.label_isim.setText('isim')
        self.label_isim.move(100,100)

def ac ():
    apk =  QApplication(sys.argv)
    pencere = Uygulamam()
    pencere.show()
    sys.exit(apk.exec_())

ac()