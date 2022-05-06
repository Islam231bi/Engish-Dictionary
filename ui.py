from PySide2.QtCore import QFile, QProcess
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton
import sys

from backened import backend


class App:
    def __init__(self):
        self.ui = self.loadUiWidget('dictionary.ui')
        self.ui.show()

    def loadUiWidget(self, uifilename, parent=None):
        loader = QUiLoader()
        uifile = QFile(uifilename)
        uifile.open(QFile.ReadOnly)
        ui = loader.load(uifile, parent)
        uifile.close()
        return ui


app = QApplication(sys.argv)
a = App()
back = backend(a.ui)
app.exec_()
