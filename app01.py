from PySide6.QtWidgets import QApplication, QWidget, QPushButton,QLabel
from PySide6.QtCore import Qt


class MainWindow (QWidget):

    def __init__(self):
        super().__init__ ()

        self.setWindowTitle("My App")

        label= QLabel("Holaa",self)
        font =label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter|
                           Qt.AlignmentFlag.AlignVCenter)
        aligncenter=Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignHCenter
        
        


if __name__=="__main__":
    app=QApplication([])
    window=MainWindow()
    window.show()
    app.exec()