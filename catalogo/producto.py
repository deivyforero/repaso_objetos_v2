from cuerpos import *

class Producto:
    def __init__(self, imagen, grupo, descripcion):
        self.imagen = imagen
        self.grupo = grupo
        self.descripcion = descripcion

class ArmaHumanos(Producto):
    def __init__(self, imagen, grupo, descripcion):
        self.imagen = imagen
        self.grupo = grupo
        self.descripcion = descripcion

class ArmaOrcos(Producto):
    def __init__(self, imagen, grupo, descripcion):
        self.imagen = imagen
        self.grupo = grupo
        self.descripcion = descripcion

class EscudoHumanos(Producto):
    def __init__(self, imagen, grupo, descripcion):
        self.imagen = imagen
        self.grupo = grupo
        self.descripcion = descripcion

class EscudoOrcos(Producto):
    def __init__(self, imagen, grupo, descripcion):
        self.imagen = imagen
        self.grupo = grupo
        self.descripcion = descripcion

class MonturaOrcos(DecoradorCuerpo):
    def __init__(self, imagen, grupo, descripcion):
        self.imagen = imagen
        self.grupo = grupo
        self.descripcion = descripcion

class MonturaHumanos(Producto):
    def __init__(self, imagen, grupo, descripcion):
        self.imagen = imagen
        self.grupo = grupo
        self.descripcion = descripcion

class DecorarProducto(Producto):
    def __init__(self, imagen, grupo, descripcion):
        self.imagen = imagen
        self.grupo = grupo
        self.descripcion = descripcion

class ConcreteDecorarProducto(DecorarProducto):
    def __init__(self, imagen, grupo, descripcion, cabeza,torso, brazos, piernas, ImagenArma, imagenEscudo, ImagenMontura  ):
     #   super(ConcreteDecorarProducto, self).__init__( "static/imagenes/orcos/escudo.png", "Humanos", "arma del humano")
        super(ConcreteDecorarProducto, self).__init__( imagen, grupo, descripcion)
      
        self.cabeza = cabeza
        self.torso = torso
        self.brazos = brazos
        self.piernas = piernas
        self.imagenArma= ImagenArma
        self.imagenEscudo= imagenEscudo
        self.imagenMontura= ImagenMontura

#################################################################


     

 

