import sys
from PyQt5 import QtWidgets
from frontend import Ui_MainWindow
from backend import Calculator

def main():
    app = QtWidgets.QApplication(sys.argv)
    run = Calculator()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    