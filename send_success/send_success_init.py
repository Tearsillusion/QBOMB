import sys

from PyQt5.QtWidgets import  QWidget

from send_success.send_success import Ui_qq_send_success


class QqSendSuccess(Ui_qq_send_success,QWidget):
    def __init__(self):
        super(QqSendSuccess, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)



