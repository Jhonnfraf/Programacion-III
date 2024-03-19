from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtCore import QTimer

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicacion con etiquetas")

        label = QLabel(self)
        self.gif = QMovie("gif1.gif")
        label.setMovie(self.gif)

        start_button = QPushButton("Start", self)
        start_button.clicked.connect(self.start_gif)
        start_button.move(100,0)

        stop_button = QPushButton("Stop", self)
        stop_button.clicked.connect(self.stop_gif)

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: label.setPixmap(self.gif.currentPixmap()))

    def start_gif(self):
        self.gif.start()
        self.timer.start(100)

    def stop_gif(self):
        self.gif.stop()
        self.timer.stop()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()