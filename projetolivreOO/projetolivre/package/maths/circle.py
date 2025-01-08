from package.maths.point import Point
import math

class Circle(Point):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self._r = r

    def perimetro(self):
        perimetro = 2 * 3.14 * self._r
        return perimetro
    
    def area(self):
        area = 3.14 * (self._r**2)
        return area
    
    def distancia_origem(self):
        distancia = math.sqrt(self._x**2 +  self._y**2)
        return distancia
    
    def modelo_circulo(self):
        print(f'O centro do círculo se localiza na coordenada: ({self._x},{self._y})')
        print(f'Seu raio mede: {self._r}cm.')
