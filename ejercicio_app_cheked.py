from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicacion con QCheck_Box")
        self.setLayout(self.setup_ui())
    
    def setup_ui(self):
        lay_v=QVBoxLayout()
        self.chk_todos=QCheckBox("todos los colores")
        self.chk_todos.setTristate(False)

        self.chk_amarillo=QCheckBox("amarillo")
        self.chk_azul=QCheckBox("azul")
        self.chk_rojo=QCheckBox("rojo")
        
        lay_v.addWidget(self.chk_todos)
        lay_v.addWidget(self.chk_amarillo)
        lay_v.addWidget(self.chk_rojo)
        lay_v.addWidget(self.chk_azul)
        
        self.chk_amarillo.stateChanged.connect(self.check_all)
        self.chk_azul.stateChanged.connect(self.check_all)
        self.chk_rojo.stateChanged.connect(self.check_all)
        self.chk_todos.stateChanged.connect(self.toglle_other_chechkboxes)
        
        return lay_v
    
    def toglle_other_chechkboxes(self,state):
        if state==Qt.CheckState.Checked.value:
            self.chk_amarillo.setChecked(True)
            self.chk_azul.setChecked(True)
            self.chk_rojo.setChecked(True)
        elif state==Qt.CheckState.Unchecked.value:
            self.chk_amarillo.setChecked(False)
            self.chk_rojo.setChecked(False)
            self.chk_azul.setChecked(False)

    def check_all(self):
        if self.chk_amarillo.isChecked() and self.chk_azul.isChecked() and self.chk_rojo.isChecked():
            self.chk_todos.setCheckState(Qt.CheckState.Checked)
        elif self.chk_amarillo.isChecked() or self.chk_azul.isChecked() or self.chk_rojo.isChecked():
            self.chk_todos.setCheckState(Qt.CheckState.PartiallyChecked)
        else:
            self.chk_todos.setCheckState(Qt.CheckState.Unchecked)
    
    
if __name__ == "__main__":
    app = QApplication([])
    window  = MainWindow()
    window.show()
    app.exec()
    

if __name__ == "__main__":
    app = QApplication([])
    window  = MainWindow()
    window.show()
    app.exec()