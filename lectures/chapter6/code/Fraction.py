from gcd import gcd

class Fraction:
    def __init__(self, numerator = 1, denominator = 1):
        if denominator == 0:
            self._top = 0
            self._bottom = 0
        
        else:
            factor = gcd(abs(numerator), abs(denominator))
            
            if denominator < 0:
                factor = -factor
                
            self._top = numerator // factor
            self._bottom = denominator // factor
            
    def __str__(self): 
        
        return str(self._top) + "/" + str(self._bottom)
    
    def __float__(self):
        
        return self._top/self._bottom

    def __add__(self, other):
    
        return Fraction(self._top * other._bottom + 
                    self._bottom * other._top, self._bottom * other._bottom)
        
    def __sub__(self, other):
        
        return Fraction(self._top * other._bottom - 
                    self._bottom * other._top, self._bottom * other._bottom)
                    
    def __mul__(self, other):
        
        return Fraction(self._top * other._top, self._bottom * other._bottom)
        
    def __truediv__(self, other):
        
        return Fraction(self._top * other._bottom, self._bottom * other._top)
        
    def __eq__(self, other):
        
        return self._top == other._top and self._bottom == other._bottom
        
    def __lt__(self, other):
        
        return float(self) < float(other)
        
    def __neg__(self):
        
        return Fraction(-self._top, self._bttom)
        
    def __abs__(self):
        
        return Fraction(abs(self._top), self._bottom)
