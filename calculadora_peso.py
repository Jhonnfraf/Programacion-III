from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PySide6.QtGui import QPixmap, QMovie

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ancho=137
        self.alto=25
        self.setFixedSize(250, 250)
        self.setWindowTitle("Calculadora IMC")
        # COMENTARIOS PARA INGRESAR DATOS
        label_genero=QLabel("Genero",self)
        label_genero.move(12,75)
        label_altura=QLabel("Altura",self)
        label_altura.move(12,125)
        label_peso=QLabel("Peso",self)
        label_peso.move(12,175)
        label_imc=QLabel("IMC => ",self)
        label_imc.move(12,25)
        
        # LINEAS PARA INGRESAR DATOS
        genero=QLineEdit("M/F",self)  
        genero.setGeometry(60,20,137,25)
        
        altura=QLineEdit("metros",self)
        altura.setGeometry(60,70,137,25)
        
        peso=QLineEdit("kilogramos",self)  
        peso.setGeometry(60,120,137,25)
        
        IMC=QLineEdit("No calculado",self)
        IMC.setGeometry(60,170,137,25)
        IMC.setReadOnly(True)
        
        boton=QPushButton("Calcular",self)
        boton.clicked.connect(lambda:self.calcular(altura,peso,genero))
        boton.setGeometry(12,220,225,25)
    
    def calcular(self,altura,peso,genero):
        altura_cal=float(altura.text())
        peso_cal=float(peso.text())
        genero_cal=str(genero.text())
        try:
            if genero_cal.strip().upper() in ["M"]:
                imc = round((peso_cal/(altura_cal**2)), 1)
            elif genero_cal.strip().upper() in ["F"]:
                imc = round((peso_cal/(altura_cal**2)),1)
            if imc is not None: #AQUI HAY QUE AGREGAR LA TABLA DE PESOS
                self.IMC.setText(str(imc))
            else:
                self.IMC.setText("Error en los datos ingresados")
        except Exception as e:
            print(f"Ha ocurrido un error al realizar el calculo de IMC: {e}")
    
        
        

if __name__=="__main__":
    app=QApplication()
    window=MainWindow()
    window.show()
    app.exec()