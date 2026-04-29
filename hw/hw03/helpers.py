def gcd(x, y): 
    """
    Arguments:
        x (int): an integer
        y (int): an integer
    Returns:
        (int): the greatest commond divisor of x and y
    """
    while(y): 
        x, y = y, x % y 
  
    return x

def egcd(a, b):
    """
    Performs the Extended Euclidean Algorithm on inputs a and b
    
    Arguments:
        a (int): an integer
        b (int): an integer
    Returns:
        (list): a list of 3 integers (g, y, x) where g is the gcd(a,b) and y and x are the coefficients such that gcd(a,b) = ax + by
    """    
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(e, n):
    """
    Arugments:
      e (int): represents a value in modulo n
      n (int): represents the modulus in which you are working
    Returns:
      (int): if e has a multiplicative inverse in mod n, then this value will be return, if not this value will return False
    """
    g, x, y = egcd(e, n)
    if g != 1:
        return False
    else:
        return x % n

def phi(n):
    """
    Arugments:
      n (int): an integer to work with
    Returns:
      (int): the number of integers between 0 and n (non-inclusive) that are relatively prime to n
    """
    count = 0
    for i in range(1, n): 
        if (gcd(i, n) == 1): 
            count += 1
    return count 
