import sys

from PyQt5.QtWidgets import QApplication

from send.send_init import QqSend





if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = QqSend()
    w.show()
    sys.exit(app.exec_())


