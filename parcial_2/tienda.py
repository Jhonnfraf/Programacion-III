from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap,QFont,QMovie
import os

# Franklin Steven Villota Benavides 
# Sofia ibarra Egas

class MainWindow(QWidget):
    def __init__(self):
        self.productos = []
        super().__init__()
        self.setWindowTitle("Tienda ACME")
        
        ###  Imagen de supermercado
        self.label_carrito = QLabel(self)
        self.image_carrito = os.path.join(os.path.dirname(__file__), 'imagenes', 'supermarket.png') # Concatenar ruta completa
        self.pixmap = QPixmap(self.image_carrito) # Cargar imagen
        #scaled_pixmap = pixmap.scaled(300, 200) # ajuste de tamaño
        self.label_carrito.setPixmap(self.pixmap)
        self.label_carrito.setScaledContents(True)
        self.label_carrito.setGeometry(130,20,200,100)  # ajuste de tamaño
        
        ### gif super merkado
        self.label_gif = QLabel(self)
        self.gif = os.path.join(os.path.dirname(__file__), 'imagenes', 'shooping.gif') # Carga el GIF desde el archivo
        self.movie_gif = QMovie(self.gif)
        self.label_gif.setMovie(self.movie_gif)  # Establece el GIF en la etiqueta
        self.movie_gif.start()  # Inicia la animación
        self.label_gif.setGeometry(510,20,150,100)
        self.label_gif.setScaledContents(True)
        
        ###  Imagen de supermercado
        self.label_carrito = QLabel(self)
        self.image_carrito = os.path.join(os.path.dirname(__file__), 'imagenes', 'supermarket.png') # Concatenar ruta completa
        self.pixmap = QPixmap(self.image_carrito) # Cargar imagen
        #scaled_pixmap = pixmap.scaled(300, 200) # ajuste de tamaño
        self.label_carrito.setPixmap(self.pixmap)
        self.label_carrito.setScaledContents(True)
        self.label_carrito.setGeometry(730,20,200,100)  # ajuste de tamaño
        
        
        
        ### entrada, titulo y boton producto 1
        self.titul_product_1 = QLabel("Producto 1: ", self)
        self.entrada_producto = QLineEdit(self)
        self.titul_product_1.setGeometry(50, 120, 100, 20)
        self.entrada_producto.setGeometry(120, 120, 200, 20)
        self.entrada_producto.setPlaceholderText("Nombre del producto 1")
        self.boton_actualizar_1 = QPushButton("Actualizar",self)
        self.boton_actualizar_1.setGeometry(330,120,200,28)
        self.boton_actualizar_1.clicked.connect(self.guardar_info_producto_1)
        self.boton_actualizar_1.setEnabled(False)
        self.entrada_producto.setReadOnly(True)
        
        ### Titulos y entradas producto 1
        self.titul_product_1_tipo = QLabel("Tipo: ", self)
        self.entrada_producto_1_tipo = QLineEdit(self)
        self.titul_product_1_tipo.setGeometry(230, 185, 100, 20)
        self.entrada_producto_1_tipo.setGeometry(370, 180, 165, 28)
        self.entrada_producto_1_tipo.setPlaceholderText("Tipo producto 1")
        self.entrada_producto_1_tipo.setReadOnly(True)
        
        self.titul_product_1_cbodega = QLabel("Cantidad en bodega: ", self)
        self.entrada_producto_1_cbodega = QLineEdit(self)
        self.titul_product_1_cbodega.setGeometry(230, 225, 150, 20)
        self.entrada_producto_1_cbodega.setGeometry(370, 220, 165, 28)
        self.entrada_producto_1_cbodega.setPlaceholderText("Cantidad producto 1")
        self.entrada_producto_1_cbodega.setReadOnly(True)
        
        self.titul_product_1_vu = QLabel("Valor unitario: ", self)
        self.entrada_producto_1_vu = QLineEdit(self)
        self.titul_product_1_vu.setGeometry(230, 265, 150, 20)
        self.entrada_producto_1_vu.setGeometry(370, 260, 165, 28)
        self.entrada_producto_1_vu.setPlaceholderText("Valor producto 1")
        self.entrada_producto_1_vu.setReadOnly(True)
        
        self.titul_product_1_cminima = QLabel("Cantidad minima: ", self)
        self.entrada_producto_1_cminima = QLineEdit(self)
        self.titul_product_1_cminima.setGeometry(230, 305, 150, 20)
        self.entrada_producto_1_cminima.setGeometry(370, 300, 165, 28)
        self.entrada_producto_1_cminima.setPlaceholderText("Minima producto 1")
        self.entrada_producto_1_cminima.setReadOnly(True)
        
        self.titul_product_1_img = QLabel("Imagen producto: ", self)
        self.entrada_producto_1_img = QLineEdit(self)
        self.titul_product_1_img.setGeometry(230, 345, 150, 20)
        self.entrada_producto_1_img.setGeometry(370, 340, 165, 28)
        self.entrada_producto_1_img.setPlaceholderText("Imagen producto 1")
        self.entrada_producto_1_img.setReadOnly(True)
        
        self.boton_vender_1 = QPushButton("Vender",self)
        self.boton_vender_1.setGeometry(60,380,90,28)
        self.entrada_vender_1 = QLineEdit(self)
        self.entrada_vender_1.setGeometry(160,380,50,28)
        
        self.boton_abastecer_1 = QPushButton("Abastecer",self)
        self.boton_abastecer_1.setGeometry(240,380,90,28)
        self.entrada_abastecer_1 = QLineEdit(self)
        self.entrada_abastecer_1.setGeometry(340,380,80,28)
        self.boton_abastecer_1.clicked.connect(self.abastecer_1)
        
        self.boton_modificar_1 = QPushButton("Modificar",self)
        self.boton_modificar_1.setGeometry(440,380,95,28)
        self.boton_modificar_1.clicked.connect(self.modificar_1)
        
        ###  Imagen de producto 1
        self.label_caja_1 = QLabel(self)
        self.image_caja_1 = os.path.join(os.path.dirname(__file__), 'imagenes', 'image.png') # Concatenar ruta completa
        self.pixmap_caja_1 = QPixmap(self.image_caja_1) # Cargar imagen
        #scaled_pixmap = pixmap.scaled(300, 200) # ajuste de tamaño
        self.label_caja_1.setPixmap(self.pixmap_caja_1)
        self.label_caja_1.setScaledContents(True)
        self.label_caja_1.setGeometry(50,190,150,110)  # ajuste de tamaño
        
        
        
        ### entrada, titulo y boton producto 2
        self.titul_product_2 = QLabel("Producto 1: ", self)
        self.entrada_producto_2 = QLineEdit(self)
        self.titul_product_2.setGeometry(590, 120, 100, 20)
        self.entrada_producto_2.setGeometry(660, 120, 200, 20)
        self.entrada_producto_2.setPlaceholderText("Nombre del producto 1")
        self.boton_actualizar_2 = QPushButton("Actualizar",self)
        self.boton_actualizar_2.setGeometry(870,120,200,28)
        self.boton_actualizar_2.clicked.connect(self.guardar_info_producto_2)
        self.boton_actualizar_2.setEnabled(True)
        self.entrada_producto_2.setReadOnly(True)
        
        ### Titulos y entradas producto 2
        self.titul_product_2_tipo = QLabel("Tipo: ", self)
        self.entrada_producto_2_tipo = QLineEdit(self)
        self.titul_product_2_tipo.setGeometry(780, 185, 100, 20)
        self.entrada_producto_2_tipo.setGeometry(920, 180, 165, 28)
        self.entrada_producto_2_tipo.setPlaceholderText("Tipo producto 2")
        self.entrada_producto_2_tipo.setReadOnly(True)
        
        self.titul_product_2_cbodega = QLabel("Cantidad en bodega: ", self)
        self.entrada_producto_2_cbodega = QLineEdit(self)
        self.titul_product_2_cbodega.setGeometry(780, 225, 150, 20)
        self.entrada_producto_2_cbodega.setGeometry(920, 220, 165, 28)
        self.entrada_producto_2_cbodega.setPlaceholderText("Cantidad producto 1")
        self.entrada_producto_2_cbodega.setReadOnly(True)
        
        self.titul_product_2_vu = QLabel("Valor unitario: ", self)
        self.entrada_producto_2_vu = QLineEdit(self)
        self.titul_product_2_vu.setGeometry(780, 265, 150, 20)
        self.entrada_producto_2_vu.setGeometry(920, 260, 165, 28)
        self.entrada_producto_2_vu.setPlaceholderText("Valor producto 1")
        self.entrada_producto_2_vu.setReadOnly(True)
        
        self.titul_product_2_cminima = QLabel("Cantidad minima: ", self)
        self.entrada_producto_2_cminima = QLineEdit(self)
        self.titul_product_2_cminima.setGeometry(780, 305, 150, 20)
        self.entrada_producto_2_cminima.setGeometry(920, 300, 165, 28)
        self.entrada_producto_2_cminima.setPlaceholderText("Minima producto 1")
        self.entrada_producto_2_cminima.setReadOnly(True)
        
        self.titul_product_2_img = QLabel("Imagen producto: ", self)
        self.entrada_producto_2_img = QLineEdit(self)
        self.titul_product_2_img.setGeometry(780, 345, 150, 20)
        self.entrada_producto_2_img.setGeometry(920, 340, 165, 28)
        self.entrada_producto_2_img.setPlaceholderText("Imagen producto 1")
        self.entrada_producto_2_img.setReadOnly(True)
        
        self.boton_vender_2 = QPushButton("Vender",self)
        self.boton_vender_2.setGeometry(620,380,90,28)
        self.entrada_vender_2 = QLineEdit(self)
        self.entrada_vender_2.setGeometry(725,380,50,28)
        
        self.boton_abastecer_2 = QPushButton("Abastecer",self)
        self.boton_abastecer_2.setGeometry(800,380,90,28)
        self.entrada_abastecer_2 = QLineEdit(self)
        self.entrada_abastecer_2.setGeometry(900,380,80,28)
        
        self.boton_modificar_2 = QPushButton("Modificar",self)
        self.boton_modificar_2.setGeometry(990,380,95,28)
        self.boton_modificar_2.clicked.connect(self.modificar_2)
        
        ###  Imagen de producto 2
        self.label_caja_2 = QLabel(self)
        self.image_caja_2 = os.path.join(os.path.dirname(__file__), 'imagenes', 'image.png') # Concatenar ruta completa
        self.pixmap_caja_2 = QPixmap(self.image_caja_2) # Cargar imagen
        #scaled_pixmap = pixmap.scaled(300, 200) # ajuste de tamaño
        self.label_caja_2.setPixmap(self.pixmap_caja_2)
        self.label_caja_2.setScaledContents(True)
        self.label_caja_2.setGeometry(590,190,150,110)  # ajuste de tamaño
            
        
    
        
        ### entrada, titulo y boton producto 3
        self.titul_product_3 = QLabel("Producto 3: ", self)
        self.entrada_producto_3 = QLineEdit(self)
        self.titul_product_3.setGeometry(50, 440, 100, 20)
        self.entrada_producto_3.setGeometry(120, 440, 200, 20)
        self.entrada_producto_3.setPlaceholderText("Nombre del producto 1")
        self.boton_actualizar_3 = QPushButton("Actualizar",self)
        self.boton_actualizar_3.setGeometry(330,440,200,28)
        self.entrada_producto_3.setReadOnly(True)
        self.boton_actualizar_3.setEnabled(False)
        self.boton_actualizar_3.clicked.connect(self.guardar_info_producto_3)
        
        ### Titulos y entradas producto 3
        self.titul_product_3_tipo = QLabel("Tipo: ", self)
        self.entrada_producto_3_tipo = QLineEdit(self)
        self.titul_product_3_tipo.setGeometry(230, 505, 100, 20)
        self.entrada_producto_3_tipo.setGeometry(370, 500, 165, 28)
        self.entrada_producto_3_tipo.setPlaceholderText("Tipo producto 1")
        self.entrada_producto_3_tipo.setReadOnly(True)
        
        self.titul_product_3_cbodega = QLabel("Cantidad en bodega: ", self)
        self.entrada_producto_3_cbodega = QLineEdit(self)
        self.titul_product_3_cbodega.setGeometry(230, 545, 150, 20)
        self.entrada_producto_3_cbodega.setGeometry(370, 540, 165, 28)
        self.entrada_producto_3_cbodega.setPlaceholderText("Cantidad producto 1")
        self.entrada_producto_3_cbodega.setReadOnly(True)
        
        self.titul_product_3_vu = QLabel("Valor unitario: ", self)
        self.entrada_producto_3_vu = QLineEdit(self)
        self.titul_product_3_vu.setGeometry(230, 585, 150, 20)
        self.entrada_producto_3_vu.setGeometry(370, 580, 165, 28)
        self.entrada_producto_3_vu.setPlaceholderText("Valor producto 1")
        self.entrada_producto_3_vu.setReadOnly(True)
        
        self.titul_product_3_cminima = QLabel("Cantidad minima: ", self)
        self.entrada_producto_3_cminima = QLineEdit(self)
        self.titul_product_3_cminima.setGeometry(230, 625, 150, 20)
        self.entrada_producto_3_cminima.setGeometry(370, 620, 165, 28)
        self.entrada_producto_3_cminima.setPlaceholderText("Minima producto 1")
        self.entrada_producto_3_cminima.setReadOnly(True)
        
        self.titul_product_3_img = QLabel("Imagen producto: ", self)
        self.entrada_producto_3_img = QLineEdit(self)
        self.titul_product_3_img.setGeometry(230, 665, 150, 20)
        self.entrada_producto_3_img.setGeometry(370, 660, 165, 28)
        self.entrada_producto_3_img.setPlaceholderText("Imagen producto 1")
        
        self.boton_vender_3 = QPushButton("Vender",self)
        self.boton_vender_3.setGeometry(60,700,90,28)
        self.entrada_vender_3 = QLineEdit(self)
        self.entrada_vender_3.setGeometry(160,700,50,28)
        
        self.boton_abastecer_3 = QPushButton("Abastecer",self)
        self.boton_abastecer_3.setGeometry(240,700,90,28)
        self.entrada_abastecer_3 = QLineEdit(self)
        self.entrada_abastecer_3.setGeometry(340,700,80,28)
        
        self.boton_modificar_3 = QPushButton("Modificar",self)
        self.boton_modificar_3.setGeometry(440,700,95,28)
        self.boton_modificar_3.clicked.connect(self.modificar_3)
        
        ###  Imagen de producto 2
        self.label_caja_3 = QLabel(self)
        self.image_caja_3 = os.path.join(os.path.dirname(__file__), 'imagenes', 'image.png') # Concatenar ruta completa
        self.pixmap_caja_3 = QPixmap(self.image_caja_3) # Cargar imagen
        #scaled_pixmap = pixmap.scaled(300, 200) # ajuste de tamaño
        self.label_caja_3.setPixmap(self.pixmap_caja_3)
        self.label_caja_3.setScaledContents(True)
        self.label_caja_3.setGeometry(50,510,150,110)  # ajuste de tamaño
        
        
        
        ### entrada, titulo y boton producto 4
        self.titul_product_4 = QLabel("Producto 4: ", self)
        self.entrada_producto_4 = QLineEdit(self)
        self.titul_product_4.setGeometry(590, 440, 100, 20)
        self.entrada_producto_4.setGeometry(660, 440, 200, 20)
        self.entrada_producto_4.setPlaceholderText("Nombre del producto 1")
        self.boton_actualizar_4 = QPushButton("Actualizar",self)
        self.boton_actualizar_4.setGeometry(870,440,200,28)
        self.entrada_producto_4.setReadOnly(True)
        self.boton_actualizar_4.setEnabled(False)
        self.boton_actualizar_4.clicked.connect(self.guardar_info_producto_4)
        
        ### Titulos y entradas producto 4
        self.titul_product_4_tipo = QLabel("Tipo: ", self)
        self.entrada_producto_4_tipo = QLineEdit(self)
        self.titul_product_4_tipo.setGeometry(780, 505, 100, 20)
        self.entrada_producto_4_tipo.setGeometry(920, 500, 165, 28)
        self.entrada_producto_4_tipo.setPlaceholderText("Tipo producto 2")
        self.entrada_producto_4_tipo.setReadOnly(True)
        
        self.titul_product_4_cbodega = QLabel("Cantidad en bodega: ", self)
        self.entrada_producto_4_cbodega = QLineEdit(self)
        self.titul_product_4_cbodega.setGeometry(780, 545, 150, 20)
        self.entrada_producto_4_cbodega.setGeometry(920, 540, 165, 28)
        self.entrada_producto_4_cbodega.setPlaceholderText("Cantidad producto 1")
        self.entrada_producto_4_cbodega.setReadOnly(True)
        
        self.titul_product_4_vu = QLabel("Valor unitario: ", self)
        self.entrada_producto_4_vu = QLineEdit(self)
        self.titul_product_4_vu.setGeometry(780, 585, 150, 20)
        self.entrada_producto_4_vu.setGeometry(920, 580, 165, 28)
        self.entrada_producto_4_vu.setPlaceholderText("Valor producto 1")
        self.entrada_producto_4_vu.setReadOnly(True)
        
        self.titul_product_4_cminima = QLabel("Cantidad minima: ", self)
        self.entrada_producto_4_cminima = QLineEdit(self)
        self.titul_product_4_cminima.setGeometry(780, 625, 150, 20)
        self.entrada_producto_4_cminima.setGeometry(920, 620, 165, 28)
        self.entrada_producto_4_cminima.setPlaceholderText("Minima producto 1")
        self.entrada_producto_4_cminima.setReadOnly(True)
        
        self.titul_product_4_img = QLabel("Imagen producto: ", self)
        self.entrada_producto_4_img = QLineEdit(self)
        self.titul_product_4_img.setGeometry(780, 665, 150, 20)
        self.entrada_producto_4_img.setGeometry(920, 660, 165, 28)
        self.entrada_producto_4_img.setPlaceholderText("Imagen producto 1")
        self.entrada_producto_4_img.setReadOnly(True)
        
        self.boton_vender_4 = QPushButton("Vender",self)
        self.boton_vender_4.setGeometry(620,700,90,28)
        self.entrada_vender_4 = QLineEdit(self)
        self.entrada_vender_4.setGeometry(725,700,50,28)
        
        self.boton_abastecer_4 = QPushButton("Abastecer",self)
        self.boton_abastecer_4.setGeometry(800,700,90,28)
        self.entrada_abastecer_4 = QLineEdit(self)
        self.entrada_abastecer_4.setGeometry(900,700,80,28)
        
        self.boton_modificar_4 = QPushButton("Modificar",self)
        self.boton_modificar_4.setGeometry(1000,700,95,28)
        self.boton_modificar_4.clicked.connect(self.modificar_4)
        
        ###  Imagen de producto 4
        self.label_caja_4 = QLabel(self)
        self.image_caja_4 = os.path.join(os.path.dirname(__file__), 'imagenes', 'image.png') # Concatenar ruta completa
        self.pixmap_caja_4 = QPixmap(self.image_caja_4) # Cargar imagen
        #scaled_pixmap = pixmap.scaled(300, 200) # ajuste de tamaño
        self.label_caja_4.setPixmap(self.pixmap_caja_4)
        self.label_caja_4.setScaledContents(True)
        self.label_caja_4.setGeometry(590,510,150,110)  # ajuste de tamaño
        
        
        ### Estadisticas
        self.titulo_estadisticas = QLabel("Estadísticas",self)
        self.titulo_estadisticas.setGeometry(500,750,400,40)
        self.titulo_estadisticas.setFont(QFont("Georgia",20))
        
        #### titulos y entradas estadisticas
        self.producto_mas_vend = QPushButton("Producto(s) más vendido(s)",self)
        self.producto_mas_vend.setGeometry(50,790,175,28)
        self.producto_mas_vend_salida = QLineEdit(self)
        self.producto_mas_vend_salida.setGeometry(250,790,300,28)
        
        self.producto_menos_vend = QPushButton("Producto(s) menos vendido(s)",self)
        self.producto_menos_vend.setGeometry(620,790,180,28)
        self.producto_menos_vend_salida = QLineEdit(self)
        self.producto_menos_vend_salida.setGeometry(820,790,280,28)
        
        self.dinero_caja = QLabel("Dinero en caja: ",self)
        self.dinero_caja.setGeometry(50,840,170,28)
        self.dinero_caja_salida = QLineEdit(self)
        self.dinero_caja_salida.setGeometry(250,840,300,28)
        
        self.promedio_ventas = QLabel("Promedio ventas: ",self)
        self.promedio_ventas.setGeometry(620,840,170,28)
        self.promedio_ventas_salida = QLineEdit(self)
        self.promedio_ventas_salida.setGeometry(820,840,280,28)
        
        ##### informacon de productos
        
        
        ### imagenes
        #1
        self.mostrar_imagen_lapiz = QLabel(self)
        self.mostrar_imagen_lapiz.setGeometry(10, 140, 200, 200)
        self.imagen_lapiz = os.path.join(os.path.dirname(__file__), 'imagenes', 'lapiz.png')
        self.pixmap_lapiz = QPixmap(self.imagen_lapiz) 
        self.scaled_pixmap_lapiz = self.pixmap_lapiz.scaled(100, 100)
        self.mostrar_imagen_lapiz.setGeometry(50,190,150,110) 
        #2
        self.mostrar_imagen_cuaderno = QLabel(self)
        self.mostrar_imagen_cuaderno.setGeometry(10, 140, 200, 200)
        self.imagen_cuaderno = os.path.join(os.path.dirname(__file__), 'imagenes', 'cuaderno.png')
        self.pixmap_cuaderno = QPixmap(self.imagen_cuaderno) 
        self.scaled_pixmap_cuaderno = self.pixmap_cuaderno.scaled(100, 100)
        self.mostrar_imagen_cuaderno.setGeometry(50,190,150,110) 
        #3
        self.mostrar_imagen_galleta = QLabel(self)
        self.mostrar_imagen_galleta.setGeometry(10, 140, 200, 200)
        self.imagen_galleta = os.path.join(os.path.dirname(__file__), 'imagenes', 'galleta.png')
        self.pixmap_galleta = QPixmap(self.imagen_galleta) 
        self.scaled_pixmap_galleta = self.pixmap_galleta.scaled(100, 100)
        self.mostrar_imagen_galleta.setGeometry(50,190,150,110) 
        #4
        self.mostrar_imagen_pan = QLabel(self)
        self.mostrar_imagen_pan.setGeometry(10, 140, 200, 200)
        self.imagen_pan = os.path.join(os.path.dirname(__file__), 'imagenes', 'pan.png')
        self.pixmap_pan = QPixmap(self.imagen_pan) 
        self.scaled_pixmap_pan = self.pixmap_pan.scaled(100, 100)
        self.mostrar_imagen_pan.setGeometry(50,190,150,110) 
        #5
        self.mostrar_imagen_jarabe = QLabel(self)
        self.mostrar_imagen_jarabe.setGeometry(10, 140, 200, 200)
        self.imagen_jarabe = os.path.join(os.path.dirname(__file__), 'imagenes', 'jarabe.png')
        self.pixmap_jarabe = QPixmap(self.imagen_jarabe) 
        self.scaled_pixmap_jarabe = self.pixmap_jarabe.scaled(100, 100)
        self.mostrar_imagen_jarabe.setGeometry(50,190,150,110)
        #6
        self.mostrar_imagen_pildoras = QLabel(self)
        self.mostrar_imagen_pildoras.setGeometry(10, 140, 200, 200)
        self.imagen_pildoras = os.path.join(os.path.dirname(__file__), 'imagenes', 'pildoras.png')
        self.pixmap_pildoras = QPixmap(self.imagen_pildoras) 
        self.scaled_pixmap_pildoras = self.pixmap_pildoras.scaled(100, 100)
        self.mostrar_imagen_pildoras.setGeometry(50,190,150,110)  
        
        
        
        
    def guardar_info_producto_1(self):
        lista_produc = []
        producto_1 = self.entrada_producto.text()
        tipo = self.entrada_producto_1_tipo.text()
        cantidad_bodega = self.entrada_producto_1_cbodega.text()
        valor_unitario = self.entrada_producto_1_vu.text()
        cantidad_minima = self.entrada_producto_1_cminima.text()
        imagen_productos = self.entrada_producto_1_img.text()
        
        if not self.es_numero(cantidad_bodega):
           return
           
        elif not self.es_numero(cantidad_minima):
           return
        
        elif not self.es_numero(valor_unitario):
            return     
        else:
           c_bodega = int(cantidad_bodega)
           c_minima = int(cantidad_minima)
           val_unitario = float(valor_unitario)
           
           if producto_1.lower() in self.productos:
               return
           else:
               if tipo.lower() == "droguería":
                    dinero_iva = val_unitario * 0.12
                    val_unitario += dinero_iva
               elif tipo.lower() == "papelería":
                    dinero_iva = val_unitario*0.16
                    val_unitario += dinero_iva
               elif tipo.lower() == "supermercado":
                    dinero_iva = val_unitario*0.04
                    val_unitario+= dinero_iva
                
               lista_produc.append(producto_1)
               lista_produc.append(tipo)
               lista_produc.append(c_minima)
               lista_produc.append(c_bodega)
               lista_produc.append(val_unitario)
        self.productos.append(lista_produc)
        self.boton_actualizar_1.setEnabled(False)
        self.entrada_producto_1_img.setReadOnly(True)
        self.entrada_producto_1_cminima.setReadOnly(True)
        self.entrada_producto_1_cbodega.setReadOnly(True)
        self.entrada_producto_1_tipo.setReadOnly(True)
        self.entrada_producto_1_vu.setReadOnly(True)
        self.entrada_producto.setReadOnly(True)
        
        if imagen_productos == "lapiz":
            self.label_caja_1.clear()
            self.mostrar_imagen_lapiz.setPixmap(self.scaled_pixmap_lapiz)
            self.mostrar_imagen_lapiz.setGeometry(50,190,150,110) 
        elif imagen_productos == "jarabe":
            self.label_caja_1.clear()
            self.mostrar_imagen_jarabe.setPixmap(self.scaled_pixmap_jarabe)
            self.mostrar_imagen_jarabe.setGeometry(50,190,150,110) 
        elif imagen_productos == "galleta":
            self.label_caja_1.clear()
            self.mostrar_imagen_galleta.setPixmap(self.scaled_pixmap_galleta)
            self.mostrar_imagen_galleta.setGeometry(50,190,150,110) 
        elif imagen_productos == "pan":
            self.label_caja_1.clear()
            self.mostrar_imagen_pan.setPixmap(self.scaled_pixmap_pan)
            self.mostrar_imagen_pan.setGeometry(50,190,150,110) 
        elif imagen_productos == "pildoras":
            self.label_caja_1.clear()
            self.mostrar_imagen_pildoras.setPixmap(self.scaled_pixmap_pildoras)
            self.mostrar_imagen_pildoras.setGeometry(50,190,150,110) 
        elif imagen_productos == "cuaderno":
            self.label_caja_1.clear()
            self.mostrar_imagen_cuaderno.setPixmap(self.scaled_pixmap_cuaderno)
            self.mostrar_imagen_cuaderno.setGeometry(50,190,150,110) 
            
        print(lista_produc)
            
    def modificar_1(self):
        self.boton_actualizar_1.setEnabled(True)
        self.entrada_producto_1_img.setReadOnly(False)
        self.entrada_producto_1_cminima.setReadOnly(False)
        self.entrada_producto_1_cbodega.setReadOnly(False)
        self.entrada_producto_1_tipo.setReadOnly(False)
        self.entrada_producto_1_vu.setReadOnly(False)
        self.entrada_producto.setReadOnly(False)
        
    def guardar_info_producto_2(self):
        lista_produc = []
        producto_2 = self.entrada_producto_2.text()
        tipo = self.entrada_producto_2_tipo.text()
        cantidad_bodega = self.entrada_producto_2_cbodega.text()
        valor_unitario = self.entrada_producto_2_vu.text()
        cantidad_minima = self.entrada_producto_2_cminima.text()
        imagen_productos = self.entrada_producto_2_img.text()
        
        if not self.es_numero(cantidad_bodega):
           return
           
        elif not self.es_numero(cantidad_minima):
           return
        
        elif not self.es_numero(valor_unitario):
            return     
        else:
           c_bodega = int(cantidad_bodega)
           c_minima = int(cantidad_minima)
           val_unitario = float(valor_unitario)
           
           if producto_2.lower() in self.productos:
               return
           else:
               if tipo.lower() == "droguería":
                    dinero_iva = val_unitario * 0.12
                    val_unitario += dinero_iva
               elif tipo.lower() == "papelería":
                    dinero_iva = val_unitario*0.16
                    val_unitario += dinero_iva
               elif tipo.lower() == "supermercado":
                    dinero_iva = val_unitario*0.04
                    val_unitario+= dinero_iva
                
               lista_produc.append(producto_2)
               lista_produc.append(tipo)
               lista_produc.append(c_minima)
               lista_produc.append(c_bodega)
               lista_produc.append(val_unitario)
        self.productos.append(lista_produc)
        self.boton_actualizar_2.setEnabled(False)
        self.entrada_producto_2_img.setReadOnly(True)
        self.entrada_producto_2_cminima.setReadOnly(True)
        self.entrada_producto_2_cbodega.setReadOnly(True)
        self.entrada_producto_2_tipo.setReadOnly(True)
        self.entrada_producto_2_vu.setReadOnly(True)
        self.entrada_producto_2.setReadOnly(True)
        
        if imagen_productos == "lapiz":
            self.label_caja_2.clear()
            self.mostrar_imagen_lapiz.setPixmap(self.scaled_pixmap_lapiz)
            self.mostrar_imagen_lapiz.setGeometry(590,190,150,110)
        elif imagen_productos == "jarabe":
            self.label_caja_2.clear()
            self.mostrar_imagen_jarabe.setPixmap(self.scaled_pixmap_jarabe)
            self.mostrar_imagen_jarabe.setGeometry(590,190,150,110)
        elif imagen_productos == "galleta":
            self.label_caja_2.clear()
            self.mostrar_imagen_jarabe.setPixmap(self.scaled_pixmap_galleta)
            self.mostrar_imagen_jarabe.setGeometry(590,190,150,110)
        elif imagen_productos == "pan":
            self.label_caja_2.clear()
            self.mostrar_imagen_pan.setPixmap(self.scaled_pixmap_pan)
            self.mostrar_imagen_pan.setGeometry(590,190,150,110)
        elif imagen_productos == "pildoras":
            self.label_caja_2.clear()
            self.mostrar_imagen_pildoras.setPixmap(self.scaled_pixmap_pildoras)
            self.mostrar_imagen_pildoras.setGeometry(590,190,150,110)
        elif imagen_productos == "cuaderno":
            self.label_caja_2.clear()
            self.mostrar_imagen_cuaderno.setPixmap(self.scaled_pixmap_cuaderno)
            self.mostrar_imagen_cuaderno.setGeometry(590,190,150,110)
            
    def modificar_2(self):
        self.boton_actualizar_2.setEnabled(True)
        self.entrada_producto_2_img.setReadOnly(False)
        self.entrada_producto_2_cminima.setReadOnly(False)
        self.entrada_producto_2_cbodega.setReadOnly(False)
        self.entrada_producto_2_tipo.setReadOnly(False)
        self.entrada_producto_2_vu.setReadOnly(False)
        self.entrada_producto_2.setReadOnly(False)
        
    def guardar_info_producto_3(self):
        lista_produc = []
        producto_3 = self.entrada_producto_3.text()
        tipo = self.entrada_producto_3_tipo.text()
        cantidad_bodega = self.entrada_producto_3_cbodega.text()
        valor_unitario = self.entrada_producto_3_vu.text()
        cantidad_minima = self.entrada_producto_3_cminima.text()
        imagen_productos = self.entrada_producto_3_img.text()
        
        if not self.es_numero(cantidad_bodega):
           return
           
        elif not self.es_numero(cantidad_minima):
           return
        
        elif not self.es_numero(valor_unitario):
            return     
        else:
           c_bodega = int(cantidad_bodega)
           c_minima = int(cantidad_minima)
           val_unitario = float(valor_unitario)
           
           if producto_3.lower() in self.productos:
               return
           else:
               if tipo.lower() == "droguería":
                    dinero_iva = val_unitario * 0.12
                    val_unitario += dinero_iva
               elif tipo.lower() == "papelería":
                    dinero_iva = val_unitario*0.16
                    val_unitario += dinero_iva
               elif tipo.lower() == "supermercado":
                    dinero_iva = val_unitario*0.04
                    val_unitario+= dinero_iva
                
               lista_produc.append(producto_3)
               lista_produc.append(tipo)
               lista_produc.append(c_minima)
               lista_produc.append(c_bodega)
               lista_produc.append(val_unitario)
        self.productos.append(lista_produc)
        self.boton_actualizar_3.setEnabled(False)
        self.entrada_producto_3_img.setReadOnly(True)
        self.entrada_producto_3_cminima.setReadOnly(True)
        self.entrada_producto_3_cbodega.setReadOnly(True)
        self.entrada_producto_3_tipo.setReadOnly(True)
        self.entrada_producto_3_vu.setReadOnly(True)
        self.entrada_producto_3.setReadOnly(True)
        
        if imagen_productos == "lapiz":
            self.label_caja_3.clear()
            self.mostrar_imagen_lapiz.setPixmap(self.scaled_pixmap_lapiz)
            self.mostrar_imagen_lapiz.setGeometry(50,510,150,110) 
        elif imagen_productos == "jarabe":
            self.label_caja_3.clear()
            self.mostrar_imagen_jarabe.setPixmap(self.scaled_pixmap_jarabe)
            self.mostrar_imagen_jarabe.setGeometry(50,510,150,110) 
        elif imagen_productos == "galleta":
            self.label_caja_3.clear()
            self.mostrar_imagen_jarabe.setPixmap(self.scaled_pixmap_galleta)
            self.mostrar_imagen_jarabe.setGeometry(50,510,150,110) 
        elif imagen_productos == "pan":
            self.label_caja_3.clear()
            self.mostrar_imagen_pan.setPixmap(self.scaled_pixmap_pan)
            self.mostrar_imagen_pan.setGeometry(50,510,150,110) 
        elif imagen_productos == "pildoras":
            self.label_caja_3.clear()
            self.mostrar_imagen_pildoras.setPixmap(self.scaled_pixmap_pildoras)
            self.mostrar_imagen_pildoras.setGeometry(50,510,150,110) 
        elif imagen_productos == "cuaderno":
            self.label_caja_3.clear()
            self.mostrar_imagen_cuaderno.setPixmap(self.scaled_pixmap_cuaderno)
            self.mostrar_imagen_cuaderno.setGeometry(50,510,150,110) 
            
    def modificar_3(self):
        self.boton_actualizar_3.setEnabled(True)
        self.entrada_producto_3_img.setReadOnly(False)
        self.entrada_producto_3_cminima.setReadOnly(False)
        self.entrada_producto_3_cbodega.setReadOnly(False)
        self.entrada_producto_3_tipo.setReadOnly(False)
        self.entrada_producto_3_vu.setReadOnly(False)
        self.entrada_producto_3.setReadOnly(False)
        
    def guardar_info_producto_4(self):
        lista_produc = []
        producto_4 = self.entrada_producto_4.text()
        tipo = self.entrada_producto_4_tipo.text()
        cantidad_bodega = self.entrada_producto_4_cbodega.text()
        valor_unitario = self.entrada_producto_4_vu.text()
        cantidad_minima = self.entrada_producto_4_cminima.text()
        imagen_productos = self.entrada_producto_4_img.text()
        
        if not self.es_numero(cantidad_bodega):
           return
           
        elif not self.es_numero(cantidad_minima):
           return
        
        elif not self.es_numero(valor_unitario):
            return     
        else:
           c_bodega = int(cantidad_bodega)
           c_minima = int(cantidad_minima)
           val_unitario = float(valor_unitario)
           
           if producto_4.lower() in self.productos:
               return
           else:
               if tipo.lower() == "droguería":
                    dinero_iva = val_unitario * 0.12
                    val_unitario += dinero_iva
               elif tipo.lower() == "papelería":
                    dinero_iva = val_unitario*0.16
                    val_unitario += dinero_iva
               elif tipo.lower() == "supermercado":
                    dinero_iva = val_unitario*0.04
                    val_unitario+= dinero_iva
                
               lista_produc.append(producto_4)
               lista_produc.append(tipo)
               lista_produc.append(c_minima)
               lista_produc.append(c_bodega)
               lista_produc.append(val_unitario)
        self.productos.append(lista_produc)
        self.boton_actualizar_4.setEnabled(False)
        self.entrada_producto_4_img.setReadOnly(True)
        self.entrada_producto_4_cminima.setReadOnly(True)
        self.entrada_producto_4_cbodega.setReadOnly(True)
        self.entrada_producto_4_tipo.setReadOnly(True)
        self.entrada_producto_4_vu.setReadOnly(True)
        self.entrada_producto_4.setReadOnly(True)
        
        if imagen_productos == "lapiz":
            self.label_caja_4.clear()
            self.mostrar_imagen_lapiz.setPixmap(self.scaled_pixmap_lapiz)
            self.mostrar_imagen_lapiz.setGeometry(590,510,150,110)
        elif imagen_productos == "jarabe":
            self.label_caja_4.clear()
            self.mostrar_imagen_jarabe.setPixmap(self.scaled_pixmap_jarabe)
            self.mostrar_imagen_jarabe.setGeometry(590,510,150,110)
        elif imagen_productos == "galleta":
            self.label_caja_4.clear()
            self.mostrar_imagen_jarabe.setPixmap(self.scaled_pixmap_galleta)
            self.mostrar_imagen_jarabe.setGeometry(590,510,150,110) 
        elif imagen_productos == "pan":
            self.label_caja_4.clear()
            self.mostrar_imagen_pan.setPixmap(self.scaled_pixmap_pan)
            self.mostrar_imagen_pan.setGeometry(590,510,150,110)
        elif imagen_productos == "pildoras":
            self.label_caja_4.clear()
            self.mostrar_imagen_pildoras.setPixmap(self.scaled_pixmap_pildoras)
            self.mostrar_imagen_pildoras.setGeometry(590,510,150,110) 
        elif imagen_productos == "cuaderno":
            self.label_caja_4.clear()
            self.mostrar_imagen_cuaderno.setPixmap(self.scaled_pixmap_cuaderno)
            self.mostrar_imagen_cuaderno.setGeometry(590,510,150,110) 
            
    def modificar_4(self):
        self.boton_actualizar_4.setEnabled(True)
        self.entrada_producto_4_img.setReadOnly(False)
        self.entrada_producto_4_cminima.setReadOnly(False)
        self.entrada_producto_4_cbodega.setReadOnly(False)
        self.entrada_producto_4_tipo.setReadOnly(False)
        self.entrada_producto_4_vu.setReadOnly(False)
        self.entrada_producto_4.setReadOnly(False) 
        
    def abastecer_1(self):
        abastecer = self.entrada_abastecer_1.text()
        numero_abastecer = int(abastecer)
        nombre,tipo,cminima,cbodega,vu = self.productos[0]
        cbodega_num = int(cbodega)
        if cminima <= cbodega:
            cbodega_num+= numero_abastecer
            self.entrada_producto_1_cbodega.setText(cbodega_num)
        else:
            return
            
       
    def es_numero(self, texto):
        try:
            float(texto)
            return True
        except ValueError:
            return False 
                
           
    
        
        
        
        
    
        
        
        
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

        
        