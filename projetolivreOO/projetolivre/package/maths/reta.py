from package.maths.point import Point
import math

class Reta(Point):
    def __init__(self,x,y,x1,y1):
       super().__init__(x,y)
       self._x1 = x1
       self._y1 = y1

    def tamanho(self):
        tamanho = math.sqrt((self._x1 - self._x)**2 +  (self._y1 - self._y)**2)
        return tamanho
    
    def distancia_origem(self):
        A = self._y1 - self._y
        B = self._x1 - self._x
        C = self._x1*self._y - self._x*self._y1
        
        numerador = abs(C)
        denominador = math.sqrt(A**2 + B**2)
        return numerador / denominador