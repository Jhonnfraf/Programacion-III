from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QLineEdit 
from PySide6.QtGui import QPixmap, QMovie,QFont
from PySide6.QtCore import QTimer, Qt 

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resultado=0
        self.setWindowTitle("Calculadora simple")
        self.setGeometry(300,300,400,200)
        
        
        #NUMERO 1
        titulo1=QLabel("Número 1:",self)
        titulo1.move(0,0)
        input=QLineEdit(self)
        input.setPlaceholderText("Ingrese numero 1")
        input.resize (120,input.size().height())
        input.move(0,
                   20)
        
        #NUMERO 2
        titulo2=QLabel("Numero 2:",self)
        titulo2.move(0,55)
        input2=QLineEdit(self)
        input2.setPlaceholderText("Ingrese numero 2")
        input2.resize (120,input.size().height())
        input2.move(0,
                   70)
        
        
        #OPERADOR
        operator=QLineEdit(self)
        operator.resize(120,input.size().height())
        operator.move(0,
                     125)
        label=QLabel("Operacion:",self)
        label.move(0,110)
        
        #CALCULAR   
        button = QPushButton ("Calcular", self)
        button.resize(120,30)
        button.move(0,155)
        button.clicked.connect(lambda:self.calcular_operacion(input,input2,operator,advice))

        # RESULTADO 
        advice= QLabel(f'RESULTADO', self)
        advice.resize(250,50)
        advice.move(200,0)
        font=QFont("comic sans",16)
        font.setBold(True)
        advice.setFont(font)
        
        
    def calcular_operacion(self,input,input2,operator,advice):
        operator=operator.text()
        num1= float(input.text())
        num2=float(input2.text())
        if operator == "+" or  operator=="suma" or  operator=='+ ':
            self.resultado=num1+num2
        elif  operator=="-" or operator=="resta" or operator=="- " or operator=="resta ":
            self.resultado=num1-num2
        elif operator== "*" or operator=="multi" or operator=="* " or operator=="multi ":
            self.resultado=num1 * num2
        elif operator=="/" or operator=="div" or operator=="divicion" or operator=="/ " or operator== "divicion ":
            if num2==0:
                print("No se puede dividir entre cero")
            else:    
                self.resultado=num1/num2
        elif operator=="^" or operator=="potencia" or operator=="pot" or  operator=="**" or operator== "^ " or operator== "potencia " or operator=="pot ":
            self.resultado=num1**num2
        else:
            print ("Error en el Operador")
        
        advice.setText(f'RESULTADO:\n{self.resultado}')

            
        
        
        
    
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    
