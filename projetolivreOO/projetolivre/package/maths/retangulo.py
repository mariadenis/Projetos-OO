from package.maths.point import Point
import math

class Retangulo(Point):
    def __init__(self, x, y, base, height):
        super().__init__(x, y)
        self._base = base
        self._height = height

    def perimetro(self):
        perimetro = self._base * 2 + self._height * 2
        return perimetro
    
    def area(self):
        area = self._base * self._height
        return area
    
    def distancia_origem(self):
        distancia = math.sqrt(self._x**2 +  self._y**2)
        return distancia
    
    def modelo_retangulo(self):
        print(f'O centro do retângulo se localiza na coordenada: ({self._x},{self._y})')
