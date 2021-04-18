
class Cuerpo:
    def __init__(self):
        self.brazos = ""
        self.piernas = ""
        self.cabeza = ""
        self.torso = ""
        self.imgcuerpo = ""

       
class DecoradorCuerpo (Cuerpo):
    def __init__(self):
        self.brazos = ""
        self.piernas = ""
        self.cabeza = ""
        self.torso = ""
        self.imgcuerpo = ""


class CuerpoHumano(Cuerpo):
    def __init__(self):
        self.brazos = "Fuertes"
        self.piernas = "Largas"
        self.cabeza = "Pequeña"
        self.torso = "Grande"
        self.descripcion = "Cuerpo Humano"
        self.imgcuerpo = "static/imagenes/humanos/Cuerpo.jpg"

class CuerpoOrco(Cuerpo):
    def __init__(self):
        self.brazos = "feos"
        self.piernas = "Feos"
        self.cabeza = "Feos"
        self.torso = "Feos"
        self.descripcion = "Cuerpo Orco"
        self.imgcuerpo = "static/imagenes/orcos/Cuerpo.jpg"

