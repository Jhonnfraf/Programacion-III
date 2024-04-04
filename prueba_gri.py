from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,  QPushButton, QLayout, QWidget
from PySide6.QtGui import QMovie
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("GIF Viewer")
        self.setGeometry(100,100,400,400)
        #--------------gif 1
        self.label = QLabel(self)
        self.label.setGeometry(100,100,100,120)
        self.movie = QMovie("C:/Users/Udenar/Downloads/calcu/Gif/Gif_prueba.gif")
        self.label.setScaledContents(True) #para escalar el contenido
        #-------------gif 2
        self.movie2 = QMovie("C:/Users/Udenar/Downloads/calcu/Gif/cambio.gif")

        self.label.setMovie(self.movie2)
        self.movie2.start()

        self.label.setMovie(self.movie)
        self.movie.start()
         
        #----------boto1
        self.button = QPushButton("Pause/Play", self)
        self.button.setGeometry(10, 10, 100, 30)
        self.button.clicked.connect(self.toggle_playback)
        self.setCentralWidget(self.label)

        #-------boton2
        self.boton = QPushButton("Change GIF", self)
        self.boton.setGeometry(10, 50, 100, 30)
        self.boton.clicked.connect(self.change_image)
 
        self.pause_label = QLabel("Pausa", self)
        self.pause_label.setGeometry(650, 10, 300, 100)
        self.pause_label.setFont("Bauhaus 93")
        font =  self.pause_label.font()
        font.setPointSize(30)
        self.pause_label.setFont(font)

        self.pause_label.setVisible(False)  # Inicialmente oculta

    def change_image(self):
        if  self.label.movie() == self.movie:
            self.label.setMovie(self.movie2)
        else:
            self.label.setMovie(self.movie)

    def toggle_playback(self): # pausar o reproducir  la animación
        if self.movie.state() == QMovie.Running:
            self.movie.setPaused(True)
            self.pause_label.setVisible(True)
        else:
            self.movie.start()
            self.pause_label.setVisible(False)  # Ocultar etiqueta "Pausa"


        if self.movie2.state() == QMovie.Running:
            self.movie2.setPaused(True)
            self.pause_label.setVisible(True)
        else:
            self.movie2.start()
            self.pause_label.setVisible(False) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())