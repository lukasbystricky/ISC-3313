def gcd(u, v):
    
    while v != 0:
        r = u % v
        u = v
        v = r
        
    return u
