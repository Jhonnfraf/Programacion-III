#ESTUDIANTES
#JUAN FRANCISCO ACOSTA FAJARDO
#YOVANI QUIROZ

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario")
        self.setFixedSize(500, 500)
        self.formulario()

    def formulario(self):
        self.lay_v=QVBoxLayout()
        self.form=QFormLayout()
        regex= QRegularExpression ("[a-zñáéíóúA-ZÑÁÉÍÓÚ ]*")
        validator=QRegularExpressionValidator(regex)

        self.nombre_line=QLineEdit()
        self.nombre_line.setValidator(validator)
        self.nombre_line.setPlaceholderText("Nombres completos")
        self.form.addRow("Nombre.", self.nombre_line)

        self.apellido_line=QLineEdit()
        self.apellido_line.setValidator(validator)
        self.apellido_line.setPlaceholderText("Apellidos completos")
        self.form.addRow("Apellido:", self.apellido_line)

        self.fecha_nacimiento = QDateEdit()  # Instancia de QDateEdit
        self.fecha_nacimiento.setCalendarPopup(True)  # Habilitar el calendario emergente
        self.form.addRow("Fecha de Nacimiento:", self.fecha_nacimiento)


        self.email_line=QLineEdit()
        self.email_line.setPlaceholderText("E-mail")
        self.form.addRow("Email.", self.email_line)

        self.subtitle=QLabel("REQUISITOS:")
        self.subtitle.setStyleSheet("font-size:15px;font-weight:bold;")
        
        self.subtitle.setStyleSheet("margin-top:20px;padding:0px")
        self.form.addRow(self.subtitle)

        self.salario_line=QLineEdit()
        self.salario_line.setPlaceholderText("Min. 1.200.000, max 6.000.000")
        self.form.addRow("Salario",self.salario_line)


        experiencia_lay=QHBoxLayout()

        self.exp_laboral=QCheckBox()
        self.exp_laboral.setText("Experiencia Laboral")
        self.exp_laboral_line=QLineEdit()
        self.exp_laboral_line.setPlaceholderText("Años de experiencia")
        #self.exp_laboral_line.setReadOnly(True)
        self.exp_laboral.toggled.connect(self.exp_laboral_line.setEnabled)

        self.idiomas_lay=QHBoxLayout()

        self.sub_idiomas = QLabel()
        self.sub_idiomas.setText("¿Conoce algún idioma?")

        self.idiomas_si = QRadioButton("Sí")
        self.idiomas_no = QRadioButton("No")

        self.idiomas_si.toggled.connect(self.on_radio_button_toggled)

        self.idioma_ingles = QCheckBox("Inglés")
        self.idioma_espanol = QCheckBox("Chino")
        self.idioma_frances = QCheckBox("Francés")
        self.idioma_italiano = QCheckBox("italiano")

        self.idioma_ingles.setEnabled(False)
        self.idioma_espanol.setEnabled(False)
        self.idioma_frances.setEnabled(False)
        self.idioma_italiano.setEnabled(False)

        self.lenguajes_lay=QHBoxLayout()
        self.progam_label=QLabel("Que lenguajes de programacion conoce?")

        self.lenguajes_lay1=QVBoxLayout()
        self.python=QCheckBox()
        self.python.setText("Python")
        self.java=QCheckBox()
        self.java.setText("Java")
        self.javascript=QCheckBox()
        self.javascript.setText("Java_Script")
        self.sql=QCheckBox()
        self.sql.setText("SQL")
        self.rust=QCheckBox("rust")
        self.c=QCheckBox("C++")

        self.lay_preguntas=QHBoxLayout()

        self.lay_preguntas1=QVBoxLayout()
        self.sub_preguntas = QLabel()
        self.sub_preguntas.setText("¿Esta casado?")

        self.casado_si = QRadioButton("Sí")
        self.casado_no = QRadioButton("No")

        self.lay_preguntas2=QVBoxLayout()
        self.sub_preguntas1 = QLabel()
        self.sub_preguntas1.setText("¿Tiene hijos?")

        self.hijos_si = QRadioButton("Sí")
        self.hijos_no = QRadioButton("No")

        self.lay_preguntas3=QVBoxLayout()
        self.sub_preguntas2 = QLabel()
        self.sub_preguntas2.setText("¿Tiene seguro de vida?")

        self.seguro_si = QRadioButton("Sí")
        self.seguro_no = QRadioButton("No")
        
        #ORDEN LAYOUT PREGUNTAS
        self.lay_preguntas.addLayout(self.lay_preguntas1)
        self.lay_preguntas.addLayout(self.lay_preguntas2)
        self.lay_preguntas.addLayout(self.lay_preguntas3)

        self.lay_preguntas1.addWidget(self.sub_preguntas)
        self.lay_preguntas1.addWidget(self.casado_si)
        self.lay_preguntas1.addWidget(self.casado_no)
        self.lay_preguntas2.addWidget(self.sub_preguntas1)
        self.lay_preguntas2.addWidget(self.hijos_si)
        self.lay_preguntas2.addWidget(self.hijos_no)
        self.lay_preguntas3.addWidget(self.sub_preguntas2)
        self.lay_preguntas3.addWidget(self.seguro_si)
        self.lay_preguntas3.addWidget(self.seguro_no)
        
        #ORDEN LAYOUT DE LENGUAJES
        self.lenguajes_lay.addWidget(self.progam_label)
        self.lenguajes_lay.addLayout(self.lenguajes_lay1)
        self.lenguajes_lay1.addWidget(self.python)
        self.lenguajes_lay1.addWidget(self.java)
        self.lenguajes_lay1.addWidget(self.javascript)
        self.lenguajes_lay1.addWidget(self.sql)
        self.lenguajes_lay1.addWidget(self.rust)
        self.lenguajes_lay1.addWidget(self.c)
        

        #ORDEN LAYOUT DE EXPERIENCIA
        experiencia_lay.addWidget(self.exp_laboral)
        experiencia_lay.addWidget(self.exp_laboral_line)

        #ORDEN LAYOUT DE IDIOMAS
        self.idiomas_lay.addWidget(self.sub_idiomas)
        self.idiomas_lay.addWidget(self.idiomas_si)
        self.idiomas_lay.addWidget(self.idiomas_no)
        self.idiomas_lay.addWidget(self.idioma_ingles)
        self.idiomas_lay.addWidget(self.idioma_espanol)
        self.idiomas_lay.addWidget(self.idioma_frances)
        self.idiomas_lay.addWidget(self.idioma_italiano)

        #ORDEN DE EL LAYOUT PRINCIPAL
        self.lay_v.addLayout(self.form)
        self.lay_v.addLayout(experiencia_lay)
        self.lay_v.addLayout(self.idiomas_lay)
        self.lay_v.addLayout(self.lenguajes_lay)
        self.lay_v.addLayout(self.lay_preguntas)

        self.button=QPushButton("Enviar")
        self.button.clicked.connect(self.on_button_clicked)
        self.lay_v.addWidget(self.button)


        self.setLayout(self.lay_v)

    def guardar_reporte(self):
        pass
        
    def on_radio_button_toggled(self):
        if self.idiomas_si.isChecked():
            # Si el usuario selecciona "Sí", habilita los checkboxes
            self.idioma_ingles.setEnabled(True)
            self.idioma_espanol.setEnabled(True)
            self.idioma_frances.setEnabled(True)
            self.idioma_italiano.setEnabled(True)
        else:
            # Si el usuario selecciona "No", deshabilita y desmarca los checkboxes
            self.idioma_ingles.setEnabled(False)
            self.idioma_espanol.setEnabled(False)
            self.idioma_frances.setEnabled(False)
            self.idioma_italiano.setEnabled(False)
    
    def on_button_clicked(self):
        pass

        
if __name__ == "__main__":
    app = QApplication([])
    window  = MainWindow()
    window.show()
    app.exec()