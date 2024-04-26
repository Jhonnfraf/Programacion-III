from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from functools import partial
import sys
import os
basedir = os.path.dirname(__file__)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App Juego Tres en Raya")
        self.resize(450, 500)
        
        self.setup_ui()
    
    def setup_ui(self):
        self.stl_main = QStackedLayout()
        # Capa 0: Login
        self.stl_main.addWidget(self.ui_login())
        
        # Capa 1: Juego
        self.stl_main.addWidget(self.ui_game())
        
        # Capa 2: About
        self.stl_main.addWidget(self.ui_about())
        
        self.setLayout(self.stl_main)
    
    # Capa 0: Login
    def ui_login(self):
        # Layout principal de la sección de login
        vbx_login = QVBoxLayout()
        
        # Logo
        lbl_logo = QLabel()
        pixmap = QPixmap(os.path.join(basedir, "img", "Tresenraya.png"))
        lbl_logo.setPixmap(pixmap)
        # Reducir tamaño del logo al 20%
        ancho_logo, alto_logo = lbl_logo.size().toTuple()
        lbl_logo.setPixmap(pixmap.scaled(ancho_logo * 0.2,
                                         alto_logo * 0.2,
                                         Qt.KeepAspectRatio))
        lbl_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbx_login.addWidget(lbl_logo)
        
        # Título
        lbl_titulo = QLabel("TRES EN RAYA", 
                            alignment=Qt.AlignmentFlag.AlignCenter)
        vbx_login.addWidget(lbl_titulo)
        
        # Entradas de los jugadores
        frm_players = QFormLayout()
        self.playerX = QLineEdit()
        self.playerO = QLineEdit()
        frm_players.addRow("Jugador X:", self.playerX)
        frm_players.addRow("Jugador O:", self.playerO)
        vbx_login.addLayout(frm_players)
        
        # Info estado
        self.lbl_estado = QLabel()
        vbx_login.addWidget(self.lbl_estado)
        
        # Botón de login
        btn_login = QPushButton("Jugar")
        btn_login.clicked.connect(self.validar_jugadores)
        vbx_login.addWidget(btn_login)
        
        widget = QWidget()
        widget.setLayout(vbx_login)
        return widget
    
    def validar_jugadores(self):
        msj = ""
        if self.playerX.text().strip() == "":
            msj = "El nombre del jugador X no es valido!\n"
            self.lbl_estado.setText(msj)
        if self.playerO.text().strip() == "":
            msj += "El nombre del jugador O no es valido!"
            self.lbl_estado.setText(msj)
            
        if msj == "":
            self.lbl_titulo.setText(f"TRES EN RAYA\nen turno {self.playerX.text()}")
            self.stl_main.setCurrentIndex(1)
            
    # Capa 1: Juego
    def ui_game(self):
        # Layout principal de la sección de Juego
        vbx_game = QVBoxLayout()
        self.marca_jugador = "X"
        self.matriz_juego = [[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]
        
        
        # Título
        self.lbl_titulo = QLabel("TRES EN RAYA",
                                 alignment=Qt.AlignmentFlag.AlignCenter)
        font = QFont('Arcade Normal', 20)
        self.lbl_titulo.setFont(font)
        vbx_game.addWidget(self.lbl_titulo, 20)
        
        # Interfáz del Juego
        self.frmGame = QFrame()
        grd_game = QGridLayout()
        for row in range(3):
            for column in range(3):
                btn_jugar = QPushButton()
                btn_jugar.clicked.connect(partial(self.clicked_jugar, btn_jugar, row, column))
                btn_jugar.setSizePolicy(QSizePolicy.Expanding,
                                        QSizePolicy.Expanding)
                grd_game.addWidget(btn_jugar, row, column)
        self.frmGame.setLayout(grd_game)
        vbx_game.addWidget(self.frmGame, 80)
        
        # Botón de About
        btn_about = QPushButton()
        btn_about.setIcon(QIcon(os.path.join(basedir, "img", "about.png")))
        btn_about.setIconSize(QSize(16, 16))
        btn_about.setFixedSize(20, 20)
        btn_about.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        btn_about.clicked.connect(self.pressed_about)
        
        vbx_game.addWidget(btn_about)
        
        widget = QWidget()
        widget.setLayout(vbx_game)
        return widget

    def clicked_jugar(self, btn_jugar, x, y):
          
        if btn_jugar.text() not in ["X", "O"]:
            btn_jugar.setText(self.marca_jugador)
            self.matriz_juego[x][y] = 1 if self.marca_jugador == "X" else 4
            print(self.matriz_juego)
            if not self.hay_ganador():
                bTodoJugado = True
                # Comprobar si hay alguna celda por jugar
                for row in self.matriz_juego:
                    if 0 in row:
                        bTodoJugado = False
                        break
                if not bTodoJugado:
                    if self.marca_jugador == "O":
                        self.marca_jugador = "X"
                        self.lbl_titulo.setText(f"TRES EN RAYA\nen turno {self.playerX.text()}")
                    else:
                        self.marca_jugador = "O"
                        self.lbl_titulo.setText(f"TRES EN RAYA\nen turno {self.playerO.text()}")
                else: #Todo YA ESTÁ JUGADO, no hay celdas disponibles
                    self.frmGame.setEnabled(False)
                    self.lbl_titulo.setText("TRES EN RAYA\nGame Over")
            else:
                # Cuando hay un ganador
                self.frmGame.setEnabled(False)
    
    def hay_ganador(self):
        # Sumatoria de todas las filas
        resRows = [sum(row) for row in self.matriz_juego]
        # Sumatoria de todas las columnas
        print('filas', resRows)
        resCols = [sum(col) for col in zip(*self.matriz_juego)]
        print('columnas', resCols)
        # Sumatoria de la diagonal principal
        sum_first_diagonal = sum(self.matriz_juego[i][i] for i in range(3))
        print('diagonal principal', sum_first_diagonal)
        # Sumatoria de la diagonal secundaria
        sum_second_diagonal = sum(self.matriz_juego[i][2-i] for i in range(3))
        print('diagonales secundaria', sum_second_diagonal)
        resDiags = [sum_first_diagonal, sum_second_diagonal]
        
        
        if self.marca_jugador == "X":
            if 3 in resRows or 3 in resCols or 3 in resDiags:
                self.lbl_titulo.setText(f"TRES EN RAYA\nGanador {self.playerX.text()}")
                return True
        else: # Marca del Jugador es "O"            
            if 12 in resRows or 12 in resCols or 12 in resDiags:
                self.lbl_titulo.setText(f"TRES EN RAYA\nGanador {self.playerO.text()}")
                return True
        return False
    
    def ui_about(self):
        
        vbx_about = QVBoxLayout()
        
        # Logo
        lbl_logo = QLabel()
        pixmap = QPixmap(os.path.join(basedir, "img", "Tresenraya.png"))
        # lbl_logo.setPixmap(pixmap)
        ancho_logo, alto_logo = lbl_logo.size().toTuple()
        lbl_logo.setPixmap(pixmap.scaled(ancho_logo * 0.2,
                                         alto_logo * 0.2,
                                         Qt.KeepAspectRatio))
        lbl_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbx_about.addWidget(lbl_logo)
        
        lbl_titulo = QLabel("Byron Orlando Coronel Zambrano", alignment=Qt.AlignmentFlag.AlignHCenter)
        vbx_about.addWidget(lbl_titulo)
        vbx_about.setSpacing(5)
        
        
        #btn
        btn_about = QPushButton()
        btn_about.setIcon(QIcon(os.path.join(basedir, "img", "Tresenraya.png")))
        btn_about.setIconSize(QSize(16, 16)) # Tamaño Icono
        btn_about.setFixedSize(20, 20) # Tamaño Boton
        btn_about.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        btn_about.clicked.connect(self.back_to_game)
        vbx_about.addWidget(btn_about)
        
        widget = QWidget()
        widget.setLayout(vbx_about)
        
        return widget
        
    def pressed_about(self):
        self.stl_main.setCurrentIndex(2)
        
    def back_to_game(self):
        self.stl_main.setCurrentIndex(1)
        
        
        
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window  = MainWindow()
    window.show()
    app.exec()