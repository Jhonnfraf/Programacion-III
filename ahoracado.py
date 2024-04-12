from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import *
import random

class HangmanGame(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Juego ahorcado")

        self.word_list = ["aristoteles","arquimedes","socrates","pitagoras","integrales","derivadas"]
        self.chosen_word = random.choice(self.word_list)
        self.guess_word = ["_" for _ in self.chosen_word]

        self.cont_errores = 0
        self.imagenes = ["image0.png", "image1.png", "image2.png", "image3.png", "image4.png", "image5.png", "image6.png"]
        self.image_label = QLabel(self)
        self.imagenes_ahorcado()

        self.word_label = QLabel(" ".join(self.guess_word), self)
        font = QFont("ArcadeClassic", 24, QFont.Bold)
        self.word_label.setFont(font)

        self.label_field=QLabel("Ingrese letra: ",self)
        self.input_field = QLineEdit(self)
        self.input_field.returnPressed.connect(self.guess_letter)
        self.input_field.setMaximumWidth(20)  # Reduce the width of the QLineEdit to fit only one letter

        self.new_button = QPushButton("Nueva palabra", self)
        self.new_button.clicked.connect(self.new_word)

        self.game_over = QLabel("", self)  
        self.game_over.setFont(QFont("ArcadeClassic", 24, QFont.Bold))  

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.word_label)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.label_field)
        self.h_layout.addWidget(self.input_field)
        self.h_layout.addItem(QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))  
        self.layout.addLayout(self.h_layout)

        self.layout.addWidget(self.new_button)
        
        
        self.gover_layout=QHBoxLayout()
        self.gover_layout.addWidget(self.game_over)
        self.gover_layout.addItem(QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum))
        self.layout.addLayout(self.gover_layout)



        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.main_layout.addLayout(self.layout)

        self.setLayout(self.main_layout)

    def new_word(self):
        self.chosen_word = random.choice(self.word_list)
        self.guess_word = ["_" for _ in self.chosen_word]
        self.word_label.setText(" ".join(self.guess_word))
        self.cont_errores = 0
        self.imagenes_ahorcado()
        self.game_over.setText("")  
        self.input_field.setReadOnly(False)

    def imagenes_ahorcado(self):
        self.image_label.setPixmap(QPixmap(self.imagenes[self.cont_errores]))

    def guess_letter(self):
        self.word_label.setText(" ".join(self.guess_word)) 
        letter = self.input_field.text()
        if letter in self.chosen_word:
            for i in range(len(self.chosen_word)):
                if self.chosen_word[i] == letter:
                    self.guess_word[i] = letter
            self.word_label.setText(" ".join(self.guess_word))
            if "_" not in self.guess_word:
                self.word_label.setText("CONGRATULATIONS")
                self.input_field.setReadOnly(True)
        else:
            self.cont_errores += 1
            if self.cont_errores == len(self.imagenes):
                self.game_over.setText("Game Over.")
                self.input_field.setReadOnly(True)

            else:
                self.imagenes_ahorcado()
        self.input_field.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = HangmanGame()
    window.show()
    app.exec()