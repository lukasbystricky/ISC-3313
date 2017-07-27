from CompletedPoint import Point

class CirclePoint(Point):
    """
    Represents a Point class that is constrained to lie only on the unit
    circle. 
    
    """
    def __init__(self, x, y):
        """
        Initializes a CirclePoint. x and y can be any points in the 
        Cartesian frame, they will be scaled to be on the unit circle.
        
        Parameters
        ----------
        x [float]: x coordinate of a point
        y [float]: y coordinate of a point
        
        """
        p = Point(x,y)
        self._x = x/abs(p)
        self._y = y/abs(p)
        
    def __add__(self, other):
        """
        Defines the addition operator. This method returns a CirclePoint.
        
        """
        
        return CirclePoint(self._x + other._x, self._y + other._y)
        
    def __sub__(self, other):
        """
        Defines the subtraction operator. This method returns a CirclePoint.
        
        """
        
        return CirclePoint(self._x - other._x, self._y - other._y)
        
    def __abs__(self):
        """
        Defines the absolute value function for CirclePoints. As with 
        regular Points the absolute value is the distance from the origin.
        For CirclePoints, this distance is always 1.
        
        """
        
        return 1
        
    def __mul__(self, other):
        """
        Defines the multiplication operator, in this case the dot product
        between two CirclePoints.
        
        Parameters
        ----------
        other [Point]
        
        Returns
        [float] - the dot product if of self and other 
               
        """

        return self._x * other._x + self._y * other._y
            
    def normalize(self):
        """
        Normalizes a Point. Since CirclePoints already are normalized,
        this method does not do anything.
        
        """
        
        pass
        
    def scale(self, factor):
        """
        Scales a Point by a factor. If the factor is not 1 the scaled point
        will not be a CirclePoint. Therefore this method should not be
        called and will raise an exception.
        
        """
        
        raise RuntimeError("scale function not supported for CirclePoint class")
        
    def setX(self):
        """
        Sets the x coordinate of a Point. The resulting Point will not 
        necessarily be a CirclePoint, so an error will be raised if
        this method is called.
        
        """
        
        raise RuntimeError("setX function not supported for CirclePoint class")
        
    def setY(self):
        """
        Sets the y coordinate of a Point. The resulting Point will not 
        necessarily be a CirclePoint, so an error will be raised if
        this method is called.
        
        """
        
        raise RuntimeError("setX function not supported for CirclePoint class")
        
