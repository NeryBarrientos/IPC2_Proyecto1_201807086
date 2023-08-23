class NodoSenales(object):
    def __init__(self,t,a,nombre,frecuencias):
        self.t = t
        self.a = a
        self.nombre = nombre
        self.frecuencias = frecuencias
        self.siguiente = None