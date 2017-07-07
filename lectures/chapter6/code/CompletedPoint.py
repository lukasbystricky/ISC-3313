import numpy as np

class Point:
    """ 
    A class that represents a point (x,y) in a 2D plane. 
    """
    
    def __init__(self, x=0, y=0):
        """ 
        Constructor
        
        Parameters
        ----------
        x [float]
        y [float]
        """
        
        self._x = x
        self._y = y
        
    def getX(self):
        """
        Get x
        """
        return self._x
    
    def getY(self):
        """
        Get y
        """
        return self._y
    
    def setX(self,value):
        """
        Set x
        
        Parameters
        ----------
        x [float]
        """
        self._x = value
        
    def setY(self, value):
        """
        Set y
        
        Parameters
        ----------
        y [float]
        """
        self._y = value
        
    def scale(self, factor):
        """ Scales both coordinate values by a factor
        
        Parameters
        ----------
        factor [float]
        """
        self._x *= factor
        self._y *= factor
    
    def distance(self, other):
        """
        Computes the distance between this point and another point
        
        Parameters
        ----------
        other [Point] 
        
        Returns
        -------
        d [float] : distance between this point and other point
        """
        
        dx = self._x - other._x
        dy = self._y - other._y

        return np.sqrt(dx**2 + dy**2)

    def normalize(self):
        """
        Scales the point to have unit length from origin
        """
        
        mag = self.distance(Point()) # compute the distance from point to the origin
        if mag > 0:
            # if the magnitude is not 0, scale by 1 over magnitude
            self.scale(1/mag)
            
    def __add__(self, other):
        
        return Point(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        
        return Point(self.x - other.x, self.y - other.y)
        
    def __neg__(self):
        
        return Point(-self.x, -self.y)
        
    def __abs__(self):
        
        return self.distance(Point())
        
    def __eq__(self, other):
        
        return self.x == other.x and self.y == other.y
        
    def __str__(self):
        
        return "(" + str(self.x) + "," + str(self.y) + ")"
        
