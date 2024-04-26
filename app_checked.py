from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicacion con QCheck_Box")
        self.setLayout(self.setup_ui())
    
    def setup_ui(self):
        lay_v=QVBoxLayout()
        chk_mujer=QCheckBox("Es una mujer?")
        chk_mujer.setTristate(True)
        #chk_hombre=QCheckBox("Es un hombre?")
        lay_v.addWidget(chk_mujer)
        #lay_v.addWidget(chk_hombre)
        #chk_mujer.toggled.connect(self.show_alternado)
        chk_mujer.stateChanged.connect(self.show_state)
        return lay_v
        

    def show_alternado(self,state):
        print("\n-----Show Alternado-----")
        if state == True:
            print ("Verificado, es mujer")
        else:
            print ("Verificado es hombre")
    
    def show_state(self, state):
        os.system("cls")
        print("\n-----Show State----")
        print(f"Estado vale {state}")
        if state== Qt.CheckState.Checked.value:
            print("Hola señorita")
        elif state== Qt.CheckState.Unchecked.value:
            print("Hola caballero")
        else:
            print("Hola divin@")
        

if __name__ == "__main__":
    app = QApplication([])
    window  = MainWindow()
    window.show()
    app.exec()