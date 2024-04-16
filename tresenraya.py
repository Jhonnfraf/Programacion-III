from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import *


class MainWindow(QWidget):
    def __init__(self, ):
        super().__init__()

        self.pagina1()


    def pagina1(self):
        primerly=QVBoxLayout()

        
        jugadores=QFormLayout()
        self.name=QLineEdit()
        jugadores.addRow("Jogador 1:",self.name)
        self.email=QLineEdit()
        jugadores.addRow("Jogador 2:",self.email)

        primerly.addLayout(jugadores)

        self.setLayout(primerly)



        
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()