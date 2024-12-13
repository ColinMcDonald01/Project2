from PyQt6.QtWidgets import QApplication
from logic import *
def main():
    applicatin = QApplication([])
    window = Logic()
    window.show()
    applicatin.exec()
if __name__ == '__main__':
    main()
