from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PySide6.QtGui import QPixmap, QMovie

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Aplicacion con entrada de datos")
        input=QLineEdit(self)
        input.setMaxLength(50)
        
        input.resize(100,input.size().height())

        input.setPlaceholderText("Ingrese su nombre")
        # input.setReadOnly(True)
        # input.setText("Texto de lectura")
        
        #input.returnPressed.connect(lambda:self.return_pressed(input))
        #input.selectionChanged.connect(lambda:self.selection_changed(input))
        
        # INICIO DE LABEL
        
        label = QLabel("Texto inicial",self)
        label.setGeometry(10,10,100,20)
        input.setGeometry(10,40,100,20)
        input.textChanged.connect(label.setText)
        #input.textEdited.connect(label.setText)
        
        #BOTON
        button= QPushButton("Poner texto",self)
        button.move(10,70)
        button.clicked.connect(lambda: input.setText("Sin editar"))
    
    def return_pressed(self,input):
        print("Return pressed! ")
        input.setText("BOOM!")
    def selection_changed(self,input):
        print("Selection changed! ")
        input.setText(f"Texto seleccionado: {input.selectedText()}")
        
if __name__=="__main__":
    app=QApplication()
    window=MainWindow()
    window.show()
    app.exec()