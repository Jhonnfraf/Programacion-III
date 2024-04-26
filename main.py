from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,400,500)
        #self.MainPage()
        self.Game()

    def MainPage (self):
        V_layout=QVBoxLayout()

        # Configuracion Imagen

        dir_pat=os.path.dirname(__file__)
        image_file="tic_tac_toe.png"
        image_path= os.path.join(dir_pat,image_file)
        image=QLabel(self)
        image_pixmap = QPixmap(image_path)

        desired_width = 200
        desired_height = 100

        scaled_pixmap = image_pixmap.scaled(desired_width, desired_height, Qt.KeepAspectRatio)
        image.setStyleSheet("margin-bottom: 40px; margin-top: 10px")
        image.setPixmap(scaled_pixmap)
        image.setAlignment(Qt.AlignCenter)

        #Configurar el form

        form=QFormLayout()

        self.titulo=QLabel("TRES EN LINEA")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet("margin:0;padding:0;margin-bottom:50px")
        form.addRow(self.titulo)
        self.name=QLineEdit()
        form.addRow("Player 1:",self.name)
        self.name2=QLineEdit()
        self.name2.setStyleSheet("margin:0;padding:0;margin-bottom:200px")
        form.addRow("Player 2:",self.name2)

        #Boton

        button=QPushButton("Start")
        #button.clicked.connect(self.start)
        
        # Obtener dimensiones de la pantalla
        

        #Añadir widgets
        V_layout.addWidget(image)
        V_layout.addLayout(form)
        V_layout.addWidget(button)
        self.setLayout(V_layout)

        self.setWindowTitle("Tic Tac Toe")
        
        geometry = self.geometry()
        print(f"Posición de la ventana: ({geometry.x()}, {geometry.y()})")
        print(f"Tamaño de la ventana: {geometry.width()}x{geometry.height()} pixels")

    def Game(self):
        layout=QVBoxLayout()

        #formulario de juego
        form=QFormLayout()

        #Titulo
        self.titulo=QLabel("TRES EN LINEA")
        self.titulo.setAlignment(Qt.AlignCenter)
       # self.titulo.setStyleSheet("margin:0;padding:0;margin-bottom:10px; margin-top: 10px")
        form.addRow(self.titulo)

        #Ganadoe
        self.texto="Partida en curso..."
        self.ganador=QLabel(self.texto)
        self.ganador.setAlignment(Qt.AlignCenter)
        form.addRow(self.ganador)
        

        #JUEGO YEI
        self.game=QGridLayout()
        #Botones
        self.boton11_text=""
        self.boton11=QPushButton(self.boton11_text)
        self.boton11.setFixedSize(100,100)
        self.boton11.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.boton11.setMinimumSize(100,100)
        #self.boton11.setStyleSheet("background-color:white;border:1px solid black;")
        self.game.addWidget(self.boton11,0,0)

        self.boton12_text=""
        self.boton12=QPushButton(self.boton12_text)
        self.boton12.setFixedSize(100,100)
        self.boton12.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.boton12.setMinimumSize(100,100)
        #self.boton12.setStyleSheet("background-color:white;border:1px solid black;")
        self.game.addWidget(self.boton12,0,1)

        self.boton13_text=""
        self.boton13=QPushButton(self.boton13_text)
        self.boton13.setFixedSize(100,100)
        self.boton13.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.boton13.setMinimumSize(100,100)
        #self.boton13.setStyleSheet("background-color:white;border:1px solid black;")
        self.game.addWidget(self.boton13,0,2)

        self.boton21_text=""
        self.boton21=QPushButton(self.boton21_text)
        self.boton21.setFixedSize(100,100)
        self.boton21.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.boton21.setMinimumSize(100,100)
        #self.boton21.setStyleSheet("background-color:white;border:1px solid black;")
        self.game.addWidget(self.boton21,1,0)

        self.boton22_text=""
        self.boton22=QPushButton(self.boton22_text)
        self.boton22.setFixedSize(100,100)
        self.boton22.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.boton22.setMinimumSize(100,100)
        #self.boton22.setStyleSheet("background-color:white;border:1px solid black;")
        self.game.addWidget(self.boton22,1,1)

        self.boton23_text=""
        self.boton23=QPushButton(self.boton23_text)
        self.boton23.setFixedSize(100,100)
        self.boton23.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.boton23.setMinimumSize(100,100)
        #self.boton23.setStyleSheet("background-color:white;border:1px solid black;")
        self.game.addWidget(self.boton23,1,2)

        self.boton31_text=""
        self.boton31=QPushButton(self.boton31_text)
        self.boton31.setFixedSize(100,100)
        self.boton31.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.boton31.setMinimumSize(100,100)
        #self.boton31.setStyleSheet("background-color:white;border:1px solid black;")
        self.game.addWidget(self.boton31,2,0)

        self.boton32_text=""
        self.boton32=QPushButton(self.boton32_text)
        self.boton32.setFixedSize(100,100)
        self.boton32.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.boton32.setMinimumSize(100,100)
        #self.boton32.setStyleSheet("background-color:white;border:1px solid black;")
        self.game.addWidget(self.boton32,2,1)

        self.boton33_text=""
        self.boton33=QPushButton(self.boton33_text)
        self.boton33.setFixedSize(100,100)
        self.boton33.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.boton33.setMinimumSize(100,100)
        #self.boton33.setStyleSheet("background-color:white;border:1px solid black;")
        self.game.addWidget(self.boton33,2,2)

        
        
        layout.addLayout(form)
        layout.addLayout(self.game)

        
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
# Get the screen resolution
