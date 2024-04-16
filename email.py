from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setGeometry(0,0,200,100)

        #self.setup_form()
        self.setup_stacked()

    def setup_form(self):
        form=QFormLayout()
        self.name=QLineEdit()
        form.addRow("Name:",self.name)
        self.email=QLineEdit()
        form.addRow("Email:",self.email)
        self.age=QLineEdit()
        form.addRow("Age:",self.age)
        self.setLayout(form)

    def setup_stacked(self):
        
        stack1=QStackedLayout()
        
        page1=QWidget()
        layout1=QVBoxLayout()
        btn_1=QPushButton("Primero")
        btn_1.clicked.connect(lambda:stack1.setCurrentIndex(1))
        btn_2=QPushButton("Segundo")
        btn_2.clicked.connect(lambda:stack1.setCurrentIndex(2))
        btn_3=QPushButton("Tercero")
        btn_3.clicked.connect(lambda:stack1.setCurrentIndex(0))

        widget_1=QWidget()
        lay_v=QVBoxLayout()
        lay_v.addWidget(btn_1)
        lay_v.addWidget(btn_2)
        widget_1.setLayout(lay_v)

        stack1.addWidget(widget_1)
        stack1.addWidget(btn_3)
        page1.setLayout(layout1)

        
        

    

if __name__=="__main__":
    app=QApplication([])
    window=MainWindow()
    window.show()
    app.exec()