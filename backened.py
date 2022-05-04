from PySide2 import QtGui
from PySide2.QtWidgets import *


class backend:
    def __init__(self, ui):
        self.ui = ui
        self.file = ""

        self.load = self.ui.findChild(QAction, 'actionLoad_file')
        self.exit_button = self.ui.findChild(QAction, 'actionExit')
        self.help = self.ui.findChild(QAction, 'actionHelp')
        self.add = self.ui.findChild(QPushButton, "add")
        self.remove = self.ui.findChild(QPushButton, 'remove')
        self.found = self.ui.findChild(QPushButton, 'found')
        self.dict_size = self.ui.findChild(QLabel, 'dict_size')
        self.tree_size = self.ui.findChild(QLabel, 'tree_size')
        self.search_area = self.ui.findChild(QLineEdit, 'search_area')
        self.add_area = self.ui.findChild(QTextEdit, 'add_area')
        self.file_label = self.ui.findChild(QLabel, 'file')

        self.exit_button.triggered.connect(self.exit)
        self.load.triggered.connect(self.load_file)

    def exit(self):
        self.ui.close()

    def load_file(self):
        self.file = QFileDialog.getOpenFileName()[0]
        temp = self.file.rsplit('/', 1)[-1]
        self.file_label.setText(temp)
        with open(self.file) as fp:
            count = 0
            for line in fp:
                if line != "\n":
                    count = count + 1
        self.dict_size.setText(str(count)+" words")



