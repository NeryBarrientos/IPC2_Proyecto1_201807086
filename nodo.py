class Nodo(object):
    def __init__(self,x,y,combustible):
        self.x = x
        self.y = y
        self.combustible = combustible
        self.siguiente = None