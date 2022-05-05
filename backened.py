from PySide2 import QtGui
from PySide2.QtWidgets import *
from tree import RBTree


class backend:
    def __init__(self, ui):
        self.ui = ui
        self.file = ""
        self.tree = RBTree()

        self.load = self.ui.findChild(QAction, 'actionLoad_file')
        self.exit_button = self.ui.findChild(QAction, 'actionExit')
        self.help = self.ui.findChild(QAction, 'actionHelp')
        self.clear_button = self.ui.findChild(QAction, 'actionClear')

        self.add = self.ui.findChild(QPushButton, "add")
        self.remove = self.ui.findChild(QPushButton, 'remove')
        self.found = self.ui.findChild(QPushButton, 'found')

        self.dict_size = self.ui.findChild(QLabel, 'dict_size')
        self.tree_size = self.ui.findChild(QLabel, 'tree_size')
        self.file_label = self.ui.findChild(QLabel, 'file')
        self.isFound_label = self.ui.findChild(QLabel, 'isFound')

        self.search_area = self.ui.findChild(QLineEdit, 'search_area')
        self.add_area = self.ui.findChild(QLineEdit, 'add_area')

        self.exit_button.triggered.connect(self.exit)
        self.load.triggered.connect(self.load_file)
        self.clear_button.triggered.connect(self.clearSlot)
        self.found.clicked.connect(self.foundSlot)
        self.add.clicked.connect(self.addWord)
        self.remove.clicked.connect(self.removeWord)

    def load_file(self):
        self.file = QFileDialog.getOpenFileName()[0]
        temp = self.file.rsplit('/', 1)[-1]
        self.file_label.setText(temp)
        with open(self.file) as fp:
            count = 0
            for line in fp:
                if line != "\n":
                    line = line.strip('\n ')
                    self.tree.insertNode(line)
                    count = count + 1
        self.dict_size.setText(str(count))

    def foundSlot(self):
        search_word = self.search_area.text()
        found = self.tree.search(search_word)
        if found:
            self.isFound_label.setText("YES")
        else:
            self.isFound_label.setText("NO")

    def addWord(self):
        word = self.add_area.text()
        found = self.tree.search(word)
        if found:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Word already exists")
            msg.exec_()
        else:
            self.tree.insertNode(word)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Added successfully")
            msg.exec_()
            x = int(self.dict_size.text())
            x = x + 1
            self.dict_size.setText(str(x))
        self.add_area.clear()

    def removeWord(self):
        word = self.add_area.text()
        found = self.tree.search(word)
        if found:
            self.tree.delete_node(word)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Deleted successfully")
            msg.exec_()
            x = int(self.dict_size.text())
            x = x - 1
            self.dict_size.setText(str(x))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Word doesn't exist")
            msg.exec_()
        self.add_area.clear()

    def exit(self):
        self.ui.close()

    def clearSlot(self):
        self.file_label.clear()
        self.dict_size.clear()
        self.file = ""



