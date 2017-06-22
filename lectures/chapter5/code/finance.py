def future_value(PV, r, n, t):
    """
    Calculates the future value of an account
    
    Parameters
    ----------
    PV : float
        present value
    r : float
        interest rate (decimal form)
    n : int
        compounds per year
    t : int
        number of years
        
    Returns
    -------
    FV : float
        future value of the account after t years
    
    """
    
    return PV*(1 + r/n)**(n*t)
    
def present_value(FV, r, n, t):
    """
    Calculates the present value of an account
    
    Parameters
    ----------
    FV : float
        future value of the account
    r : float
        interest rate (decimal form)
    n : int
        compounds per year
    t : int
        number of years
        
    Returns
    -------
    FV : float
        future value of the account after t years
    
    """
    
    return FV*(1 + r/n)**(-n*t)
    
def years(PV, FV, r, n):    
    """
    Calculates the number of years needed to reach a target value
    
    Parameters
    ----------
    PV : float
        present value of the account
    FV : float
        future value of the account    
    r : float
        interest rate (decimal form)
    n : int
        compounds per year
        
    Returns
    -------
    t : float
        number of years need to reach FV from PV
    
    """
    
    from math import log
    return (log(FV) - log(PV))/(n*log(1 + r/n))
