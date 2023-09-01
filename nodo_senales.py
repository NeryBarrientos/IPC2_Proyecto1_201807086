class NodoSenales(object):
    def __init__(self,t,a,nombre,frecuencias):
        self.t = t
        self.a = a
        self.nombre = nombre
        self.frecuencias = frecuencias
        self.binaria = None
        self.reducida = None
        self.siguiente = None