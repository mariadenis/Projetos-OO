from package.maths.point import Point
import math

class Triangulo(Point):
    def __init__(self, x, y, base, height, a, b, c):
        super().__init__(x,y)
        self._base = base
        self._height = height
        self._a = a
        self._b = b
        self._c = c

    def triangulo(self):
         if (self._a + self._b > self._c) or (self._a + self._c > self._b) or (self._b + self._c > self._a):
            return True 
         else:
             return False
         
    def tipo(self):
        if self._a == self._b == self._c:
            return f"Equilatero"
        elif self._a == self._b or self._a == self._c or self._b == self._c:
            return f"Isosceles"
        else:
            return f"Escaleno"
        
    def area(self):
        area = (self._base * self._height) / 2
        return area
    
    def perimetro(self):
        perimetro = self._a + self._b + self._c
        return perimetro
    
    def distancia_origem(self):
        distancia = math.sqrt(self._x**2 +  self._y**2)
        return distancia

    def modelo_triangulo(self):
        print(f'O centro do triângulo se localiza na coordenada: ({self._x},{self._y})')
        print(f'Os lados do triângulo são: {self._a}, {self._b}, {self._c}.')
