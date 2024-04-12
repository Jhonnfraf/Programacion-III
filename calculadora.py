from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QGridLayout,QSizePolicy,QSizeGrip
from PySide6.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")

        self.layout = QGridLayout()

        
        self.result = QLineEdit(self)
        self.result.setAlignment(Qt.AlignRight)
        self.result.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) # Set the size policy to expanding
        self.result.setMinimumSize(50, 50)
        self.result.setReadOnly(True)

        self.layout.addWidget(self.result, 0, 0, 1, 5)

        self.buttons1 = {}
        operations1 = ["C", "(", ")", "mod", "pi"]
        for i, operation in enumerate(operations1):
            button = QPushButton(operation)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) 
            button.setMinimumSize(50, 50)
            self.buttons1[operation] = button
            self.layout.addWidget(button, 1, i)
            button.clicked.connect(self.on_button_clicked(operation))
        
        self.buttons2={}
        operations2= ["7","8","9","+","/"]
        for i, operation in enumerate (operations2):
            button = QPushButton(operation)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) 
            button.setMinimumSize(50, 50)
            self.buttons2[operation] = button
            self.layout.addWidget(button,2,i)
            button.clicked.connect(self.on_button_clicked(operation))
        
        self.buttons3={}
        operations3= ["4","5","6","*","**"]
        for i, operation in enumerate (operations3):
            button = QPushButton(operation)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) 
            button.setMinimumSize(50, 50)
            self.buttons3[operation] = button
            self.layout.addWidget(button,3,i)
            button.clicked.connect(self.on_button_clicked(operation))
        
        self.buttons4={}
        operations2= ["1","2","3","-"]
        for i, operation in enumerate (operations2):
            button = QPushButton(operation)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) 
            button.setMinimumSize(50, 50)
            self.buttons4[operation] = button
            self.layout.addWidget(button,4,i)
            button.clicked.connect(self.on_button_clicked(operation))
        
        self.buttons5={}
        operations2= ["0",",","%","+"]
        for i, operation in enumerate (operations2):
            button = QPushButton(operation)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.setMinimumSize(50, 50)
            self.buttons5[operation] = button
            self.layout.addWidget(button,5,i)
            button.clicked.connect(self.on_button_clicked)

        self.boton_igual=QPushButton("=")
        self.boton_igual.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) 
        self.boton_igual.setMinimumSize(50, 50)
        self.layout.addWidget(self.boton_igual,4,4,2,1)
        self.boton_igual.clicked.connect(self.on_button_clicked)

        self.setLayout(self.layout)

    def on_button_clicked (self,text):
            self.result.clear()
            self.result.setText(self.result.text() + text)

    

        
        
if __name__ == "__main__":
    app = QApplication([])
    window = Calculator()
    window.show()
    app.exec()