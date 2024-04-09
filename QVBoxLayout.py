from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

def getWidgetColor(color, texto, color_l="withe"):
    widget= QWidget()
    label=QLabel(texto,widget)
    
    font= label.font()
    font.setPointSize(20)
    font.setBold(True)
    label.setFont(font)
    
    widget.setAutoFillBackground(True)
    palette= widget.palette()
    palette.setColor(QPalette.Window, color)
    palette.setColor(QPalette.WindowText, color_l)
    widget.setPalette(palette)
    widget.setMinimumSize(50,30)
    return widget
    
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setup_hbox()
        
        #self.setup_color()
    
    def setup_hbox(self):
        layout_h=QVBoxLayout()
        deic_color_num= {"0":"#a3d1ff","1":"#ebcff0","3":"#ffdbdb","4":"#ffdbdb","5":"#13659d","6":"#207bba","7":"#2397b6"}
        self.setLayout(layout_h) # Coloco el layout principal de la ventan
        for num, color in deic_color_num.items():
            layout_h.addWidget(getWidgetColor(num,color))
        #layout_v.addWidget(getWidgetColor("#a3d1ff","0"))
        #layout_v.addWidget(getWidgetColor("#ebcff0","2"))
        #layout_v.addWidget(getWidgetColor("#ffdbdb","3"))
        #layout_v.addWidget(getWidgetColor("#fbd3e3","4"))
        #layout_v.addWidget(getWidgetColor("#ffdbdb","5"))
        #layout_v.addWidget(getWidgetColor("#13659d","6"))
        #layout_v.addWidget(getWidgetColor("#207bba","7"))
        self.setLayout(layout_h)
    
    
    
        
        
if __name__=="__main__":
    app=QApplication()
    Window=MainWindow()
    Window.show()
    app.exec()