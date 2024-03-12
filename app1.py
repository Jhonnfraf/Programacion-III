from PySide6.QtWidgets import QApplication, QWidget, QPushButton
import sys
class MainWindow (QWidget):
    def __init__(self):
        super().__init__ ()
        self.setWindowTitle("My App")
        boton = QPushButton("MACHUCAME")
        boton.setParent(self)
if __name__=="__main__":
    app=QApplication([])
    window=MainWindow()
    window.show()
    app.exec()
    