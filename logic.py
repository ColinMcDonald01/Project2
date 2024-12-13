from PyQt6.QtWidgets import *
from Project2 import *
class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda : self.submit)
        def submit(self):
            try:
                grade1 = int(self.lineEdit_2.text())
                grade2 = int(self.lineEdit_3.text())
                grade3 = int(self.lineEdit_4.text())
                grade4 = int(self.lineEdit_5.text())
                x =[]
                x.add(grade1, grade2, grade3, grade4)
                y=100
                if(grade1>0 and grade2>0 and grade3>0 and grade4>0 and grade1 <=100 and grade2 <=100 and grade3 <=100 and grade4 <=100):
                    if(radioButton.isChecked()):
                        for i in x:
                            if i<y:
                                y =i
                        average = (grade1 + grade2 + grade3 + grade4 -y)/4
                        self.label_2.setText(f'Average: {average}')
                    else:
                        average = (grade1 + grade2 + grade3 + grade4)/4
                        self.label_2.setText(f'Average: {average}')
                else:
                    self.label_2.setText('Values must be greater than 0 and less than 100')
            except:
                self.label_2.setText('Invalid input')
