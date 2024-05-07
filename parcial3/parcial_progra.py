
#INTEGRANTES:
#Andres felipe taguada cuatin
#Cristian Samuel velasquez

from PySide6.QtWidgets import QCheckBox,QApplication,QWidget,QLabel,QLineEdit,QPushButton,QRadioButton,QStackedLayout,QVBoxLayout,QHBoxLayout,QGridLayout,QFormLayout,QGroupBox
from PySide6.QtGui import QPixmap,QFont
from PySide6.QtCore import Qt
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        ##########################################
        self.setWindowTitle("Aerolíneas-ACME")
        layout_prin = QVBoxLayout()
        layout_1 = QHBoxLayout()
        layout_1_1 = QVBoxLayout()
        #######################################



        clas_ejecutiva = QLabel("Clase ejecutiva")
        clas_ejecutiva.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        puesto_1 = QCheckBox("1")
        puesto_2 = QCheckBox("2")
        puesto_3 = QCheckBox("3")
        puesto_4 = QCheckBox("4")
        puesto_5 = QCheckBox("5")
        puesto_6 = QCheckBox("6")
        puesto_7 = QCheckBox("7")
        puesto_8 = QCheckBox("8")
        layout_1_1_a = QGridLayout()
        layout_1_1_a.addWidget(puesto_1,0,0)
        layout_1_1_a.addWidget(puesto_2,0,1)
        layout_1_1_a.addWidget(puesto_3,0,2)
        layout_1_1_a.addWidget(puesto_4,0,3)
        layout_1_1_a.addWidget(puesto_5,1,0)
        layout_1_1_a.addWidget(puesto_6,1,1)
        layout_1_1_a.addWidget(puesto_7,1,2)
        layout_1_1_a.addWidget(puesto_8,1,3)
        clas_economica = QLabel("Clase económica")
        clas_economica.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        puesto_9 = QCheckBox("9")
        puesto_10 = QCheckBox("10")
        puesto_11 = QCheckBox("11")
        puesto_12 = QCheckBox("12")
        puesto_13 = QCheckBox("13")
        puesto_14 = QCheckBox("14")
        puesto_15= QCheckBox("15")
        puesto_16 = QCheckBox("16")
        puesto_17 = QCheckBox("17")
        puesto_18 = QCheckBox("18")
        puesto_19 = QCheckBox("19")
        puesto_20 = QCheckBox("20")
        puesto_21 = QCheckBox("21")
        puesto_22 = QCheckBox("22")
        puesto_23 = QCheckBox("23")
        puesto_24 = QCheckBox("24")
        lista_checks = [puesto_1,puesto_2,puesto_3,puesto_4,puesto_5,puesto_6,puesto_7,puesto_8,
                        puesto_9,puesto_10,puesto_11,puesto_12,puesto_13,puesto_14,puesto_15,puesto_16,
                        puesto_17,puesto_18,puesto_19,puesto_20,puesto_21,puesto_22,puesto_23,puesto_24]
        layout_1_1_b = QGridLayout()
        layout_1_1_b.addWidget(puesto_9,0,0)
        layout_1_1_b.addWidget(puesto_10,0,1)
        layout_1_1_b.addWidget(puesto_11,0,2)
        layout_1_1_b.addWidget(puesto_12,0,3)
        layout_1_1_b.addWidget(puesto_13,1,0)
        layout_1_1_b.addWidget(puesto_14,1,1)
        layout_1_1_b.addWidget(puesto_15,1,2)
        layout_1_1_b.addWidget(puesto_16,1,3)
        layout_1_1_b.addWidget(puesto_17,2,0)
        layout_1_1_b.addWidget(puesto_18,2,1)
        layout_1_1_b.addWidget(puesto_19,2,2)
        layout_1_1_b.addWidget(puesto_20,2,3)
        layout_1_1_b.addWidget(puesto_21,3,0)
        layout_1_1_b.addWidget(puesto_22,3,1)
        layout_1_1_b.addWidget(puesto_23,3,2)
        layout_1_1_b.addWidget(puesto_24,3,3)
        layout_1_1.addWidget(clas_ejecutiva)
        layout_1_1.addLayout(layout_1_1_a)
        layout_1_1.addWidget(clas_economica)
        layout_1_1.addLayout(layout_1_1_b)
        
        layout_1_2 = QVBoxLayout()
        direccion = os.path.dirname(__file__)
        imagen = QLabel(self)
        imagen.setPixmap(QPixmap(os.path.join(direccion,"avión.png")))
        imagen.setScaledContents(True)
        imagen.setMaximumSize(200,200)
        layout_1_2.addSpacing(10)
        layout_1_2.addWidget(imagen)
        ##########################
        stakk = QStackedLayout()
        w_1 = QWidget()
        layout_1_3 = QVBoxLayout()
        registro_pasa = QLabel("Registro de Pasajeros")
        registro_pasa.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        fuente = registro_pasa.font()
        fuente.setBold(True)
        registro_pasa.setFont(fuente)
        layout_1_3_1 = QFormLayout()
        self.linea_doc = QLineEdit()
        layout_1_3_1.addRow("No. Documento:",self.linea_doc)
        caja_1 = QGroupBox()
        layout_1_3_2 = QHBoxLayout()
        tipo_doc = QLabel("Tipo Documento:")
        radio_pas = QRadioButton("Pasaporte")
        radio_ced = QRadioButton("Cédula")
        radio_t_i = QRadioButton("T.I.")
        layout_1_3_2.addWidget(tipo_doc)
        layout_1_3_2.addWidget(radio_pas)
        layout_1_3_2.addWidget(radio_ced)
        layout_1_3_2.addWidget(radio_t_i)
        caja_1.setLayout(layout_1_3_2)
        layout_1_3_3 = QFormLayout()
        self.linea_edad = QLineEdit()
        layout_1_3_3.addRow("Edad:",self.linea_edad)
        caja_2 = QGroupBox()
        layout_1_3_4 = QHBoxLayout()
        sexo = QLabel("Sexo:")
        radio_fem = QRadioButton("Femenino")
        radio_mas = QRadioButton("Masculino")
        layout_1_3_4.addWidget(sexo)
        layout_1_3_4.addWidget(radio_fem)
        layout_1_3_4.addWidget(radio_mas)
        caja_2.setLayout(layout_1_3_4)
        boton_reg_pas = QPushButton("Registrar Pasajero")
        infor_pas = QLabel("")
        layout_1_3.addWidget(registro_pasa)
        layout_1_3.addLayout(layout_1_3_1)
        layout_1_3.addWidget(caja_1)
        layout_1_3.addLayout(layout_1_3_3)
        layout_1_3.addWidget(caja_2)
        layout_1_3.addWidget(boton_reg_pas)
        layout_1_3.addWidget(infor_pas)
        w_1.setLayout(layout_1_3)
        stakk.addWidget(w_1)
        self.dict = []
        ##################
        w_2 = QWidget()
        layout_1_4 = QVBoxLayout()
        eliminacion = QLabel("Eliminación de Pasajeros")
        eliminacion.setFont(fuente)
        eliminacion.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout_1_4_1 = QFormLayout()
        self.linea_doc_2 = QLineEdit()
        layout_1_4_1.addRow("No.Documento:",self.linea_doc_2)
        caja_3 = QGroupBox()
        layout_1_4_2 = QHBoxLayout()
        tipo_doc_2 = QLabel("Tipo de Documento:")
        radio_pas_2 = QRadioButton("Pasaporte")
        radio_ced_2 = QRadioButton("Cédula")
        radio_t_i_2 = QRadioButton("T.I.")
        layout_1_4_2.addWidget(tipo_doc_2)
        layout_1_4_2.addWidget(radio_pas_2)
        layout_1_4_2.addWidget(radio_ced_2)
        layout_1_4_2.addWidget(radio_t_i_2)
        caja_3.setLayout(layout_1_4_2)
        boton_eliminado = QPushButton("Eliminar")
        infor_pas_2 = QLabel("")
        layout_1_4.addWidget(eliminacion)
        layout_1_4.addLayout(layout_1_4_1)
        layout_1_4.addWidget(caja_3)
        layout_1_4.addWidget(boton_eliminado)
        layout_1_4.addWidget(infor_pas_2)
        w_2.setLayout(layout_1_4)
        stakk.addWidget(w_2)
        
        ###################
        w_3 = QWidget()
        layout_5 = QVBoxLayout()
        estadisticas = QLabel("Estadísticas de vuelo")
        estadisticas.setFont(fuente)
        estadisticas.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout_5_1 = QFormLayout()
        self.linea_ocup = QLineEdit()
        self.linea_ocup.setReadOnly(True)
        self.linea_ejec = QLineEdit()
        self.linea_ejec.setReadOnly(True)
        self.linea_econ = QLineEdit()
        self.linea_econ.setReadOnly(True)
        self.linea_sex = QLineEdit()
        self.linea_sex.setReadOnly(True)
        layout_5_1.addRow("Porcentaje de ocupación:",self.linea_ocup)
        layout_5_1.addRow("Ocupación ejecutiva:",self.linea_ejec)
        layout_5_1.addRow("Ocupación economica:",self.linea_econ)
        layout_5_1.addRow("Ocupación por sexo:",self.linea_sex)
        layout_5_1_1 = QHBoxLayout()
        layout_5_1_1_1 = QHBoxLayout()
        espacio = QLabel("")
        radio_fem_2 = QRadioButton("Femenino")
        radio_mas_2 = QRadioButton("Masculino")
        layout_5_1_1_1.addWidget(radio_fem_2)
        layout_5_1_1_1.addWidget(radio_mas_2)
        layout_5_1_1.addWidget(espacio)
        layout_5_1_1.addLayout(layout_5_1_1_1)
        layout_5_2 = QFormLayout()
        self.linea_edad_2 = QLineEdit()
        self.linea_edad_2.setReadOnly(True)
        layout_5_2.addRow("Ocupación por Edad:", self.linea_edad_2)
        espacio_2 = QLabel("")
        layout_5_1_2 = QHBoxLayout()
        mayores = QCheckBox("Mayores de edad")
        layout_5_1_2.addWidget(espacio_2)
        layout_5_1_2.addWidget(mayores)
        layout_5.addWidget(estadisticas)
        layout_5.addLayout(layout_5_1)
        layout_5.addLayout(layout_5_1_1)
        layout_5.addLayout(layout_5_2)
        layout_5.addLayout(layout_5_1_2)
        w_3.setLayout(layout_5)
        stakk.addWidget(w_3)
        
        layout_2 = QHBoxLayout()
        boton_registro = QPushButton("Registro")
        boton_registro.clicked.connect(lambda:stakk.setCurrentIndex(0))
        boton_eliminar = QPushButton("Eliminar pasajero")
        boton_eliminar.clicked.connect(lambda: stakk.setCurrentIndex(1))
        boton_estadisticas = QPushButton("Estadisticas")
        boton_estadisticas.clicked.connect(lambda: stakk.setCurrentIndex(2))
        layout_2.addWidget(boton_registro,0,Qt.AlignmentFlag.AlignLeft)
        layout_2.addSpacing(100)
        layout_2.addWidget(boton_eliminar,0,Qt.AlignmentFlag.AlignHCenter)
        layout_2.addSpacing(100)
        layout_2.addWidget(boton_estadisticas,0,Qt.AlignmentFlag.AlignRight)
        
        layout_1.addLayout(layout_1_1)
        layout_1.addLayout(layout_1_2)
        layout_1.addLayout(stakk)
        layout_prin.addLayout(layout_1)
        layout_prin.addLayout(layout_2)
        self.setLayout(layout_prin)
        
        
        
        #señales
        boton_reg_pas.clicked.connect(lambda: self.registro_pasajero(self.linea_doc.text(),radio_pas,radio_ced,radio_t_i,self.linea_edad.text(),radio_fem,radio_mas,lista_checks,infor_pas))
        boton_eliminado.clicked.connect(lambda: self.eliminar_pasajero(self.linea_doc_2.text(),radio_pas_2,radio_ced_2,radio_t_i_2,infor_pas_2))
        boton_estadisticas.clicked.connect(lambda: self.estadisticas())
        radio_fem_2.toggled.connect(lambda: self.validar_radio_sexo(radio_fem_2.text()))
        radio_mas_2.toggled.connect(lambda: self.validar_radio_sexo(radio_mas_2.text()))
        mayores.toggled.connect(lambda: self.validar_mayor_edad(mayores))
        
    def isnum(self,tx):
        for i in tx:
            if i.isalpha()==True:
                return False
        return True
    def validar_edad(self,td,te):
        if self.isnum(te)==True and te!='':
            if td=='Cédula' and int(te)>=18:
                return True
            elif td=='T.I.' and int(te)<18:
                return True
            elif td=='Pasaporte':
                return True
            else:
                return False
        else:
            return False
    def check_Documento(self,b1,b2,b3):
        if b1.isChecked()==True or b2.isChecked()==True or b3.isChecked()==True:
            return True
        else:
            return False
    def check_sexo(self,b1,b2):
        if b1.isChecked()==True:
            return True
        elif b2.isChecked()==True:
            return True
        else:
            return False
    def validar_documento(self,tnd):
        if len(tnd)>=2:
            return True
        else:
            return False
    def validar_registro(self,l,tnd,label,td,te,genero):
        c=0
        for i in l:
            if i.isChecked()==True:
                c+=1
                check = i
        if c>1:
            label.setText('El pasajero no puede tener mas de un puesto asignado')
        elif c<1:
            label.setText('El pasajero no tiene un puesto elegido')
        else:
            l=[tnd,td,check,te,genero]
            self.dict.append(l)
            check.setDisabled(True)
            check.setChecked(False)
            label.setText(f'Pasajero {tnd} registrado en silla #{check.text()}')
    def registro_pasajero(self,tnd,rd1,rd2,rd3,te,bs1,bs2,lpuestos,label):
        if self.validar_documento(tnd)==True:
            if self.check_Documento(rd1,rd2,rd3)==True:
                l=[rd1,rd2,rd3]
                for i in l:
                    if i.isChecked()==True:
                        if self.validar_edad(i.text(),te)==True:
                            if self.check_sexo(bs1,bs2)==True:
                                if bs1.isChecked()==True:
                                    self.validar_registro(lpuestos,tnd,label,i.text(),te,bs1)
                                else:
                                    self.validar_registro(lpuestos,tnd,label,i.text(),te,bs2)
                            else:
                                label.setText('El pasajero no ha seleccionado un sexo')
                        else:
                            label.setText(f'Tipo documento: {i.text()}, y edad: {te} no concuerdan')
            else:
                label.setText('El pasajero no ha seleccionado un documento')
        else:
            label.setText('El documento del pasajero debe tener al menos 2 caracteres')
    def eliminar_pasajero(self,tnd2,t1,t2,t3,label2):
        l = [t1,t2,t3]
        for i in l:
            if i.isChecked()==True:
                c=i.text()
                break
            else:
                c=''
        b = 0
        for i in self.dict:
            if i[0]==tnd2 and i[1]==c:
                i[2].setDisabled(False)
                label2.setText(f'Pasajero {tnd2} eliminado. Silla #{i[2].text()} libre')
                self.dict.remove(i)
                b = 1
        if b == 0:
            label2.setText(f'Pasajero {tnd2} no pudo ser eliminado')
    def estadisticas(self):
        po = 0
        pej = 0
        pec = 0
        ped = 0
        l = ['1','2','3','4','5','6','7','8']
        l2 = ['9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
        for i in self.dict:
            po+=1
            if i[2].text() in l:
                pej+=1
            elif i[2].text() in l2:
                pec+=1
            if int(i[3])<18:
                ped+=1
        po = (po*100)/24
        pej = (pej*100)/8
        pec = (pec*100)/16
        ped = (ped*100)/len(self.dict)

        self.linea_ocup.setText(f'{str(po)}%')
        self.linea_ejec.setText(f'{str(pej)}%')
        self.linea_econ.setText(f'{str(pec)}%')
        self.linea_edad_2.setText(f'{str(ped)}%')
    
    def validar_radio_sexo(self,tr):
        psex = 0
        for i in self.dict:
            if tr==i[4].text():
                psex+=1
        psex = (psex*100)/len(self.dict)
        
        self.linea_sex.setText(f'{str(psex)}%')
    
    def validar_mayor_edad(self,btn):
        if btn.isChecked()==True:
            ped = 0
            for i in self.dict:
                if int(i[3])>=18:
                    ped+=1
            ped = (ped*100)/len(self.dict)
            self.linea_edad_2.setText(f'{str(ped)}%')
        else:
            ped = 0
            for i in self.dict:
                if int(i[3])<18:
                    ped+=1
            ped = (ped*100)/len(self.dict)
            self.linea_edad_2.setText(f'{str(ped)}%')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()