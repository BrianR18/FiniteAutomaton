from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction


class AlertWindow(object):
    def __init__(self, msg):
        self.Form = None
        self.mainW = None
        self.msg = msg

    def setupUi(self, form, main):
        self.mainW = main
        self.Form = form
        self.Form.setObjectName("Form")
        self.Form.resize(400, 150)
        self.Form.setMaximumSize(400, 150)
        self.Form.setMinimumSize(400, 150)
        self.messageLabel = QtWidgets.QLabel(self.Form)
        self.messageLabel.setGeometry(QtCore.QRect(120, 40, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        self.messageLabel.setFont(font)
        self.messageLabel.setObjectName("messageLabel")
        self.messageLabel.setText(self.msg)
        self.okButton = QtWidgets.QPushButton(self.Form)
        self.okButton.setGeometry(QtCore.QRect(140, 90, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")
        self.okButton.setText("Vale")
        self.okButton.clicked.connect(self.closeAlert)

    def closeAlert(self):
        self.mainW.setDisabled(False)
        self.Form.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = AlertWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
