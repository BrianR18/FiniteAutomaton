import sys

from PyQt5 import QtWidgets

from src.GUI.GuiController import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.changesThings()
    sys.exit(app.exec_())
