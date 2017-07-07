import numpy as np

class Rectangle:
    """ 
    A class that represents a rectangle
    """
    
    def __init__(self, width=1, height=1):
        """ 
        Constructor
        
        Parameters
        ----------
        width [float]
        height [float]
        """
        
        self._width = width
        self._height = height
        
        
    def getHeight(self):
        """
        Get height
        """
        return self._height
        
    def getWidth(self):
        """
        Get width
        """
        return self._width
    
    def setHeight(self,value):
        """
        Set height
        
        Parameters
        ----------
        height [float]
        """
        self._height = value
        
    def setWidth(self, value):
        """
        Set width
        
        Parameters
        ----------
        y [float]
        """
        self._width = value
    
    def scaleHeight(self, factor):
        """ 
        Scales the height of the rectangle
        
        Parameters
        ----------
        factor [float]
        """
        self._height *= factor
        
    def scaleWidth(self, factor):
        """ 
        Scales the width of the rectangle
        
        Parameters
        ----------
        factor [float]
        """
        self._width *= factor
    
    def area(self):
        """
        Computes the area of the rectangle
        """
        
        return self._width * self._height
