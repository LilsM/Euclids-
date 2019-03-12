print("Euclid's algorithm of finding the Greates Common Divisor of two non-negative numbers")
def Euclid(m,n):
    while n != 0:
        r = m%n
        m = n
        n = r
    return m

        
        
