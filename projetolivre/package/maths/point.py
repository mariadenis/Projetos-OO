import math

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def distancia_origem(self):
        distancia = math.sqrt(self._x**2 +  self._y**2)
        return distancia
    
    def modelo_ponto(self):
        print(f'O ponto se localiza na coordenada: ({self._x},{self._y})')

