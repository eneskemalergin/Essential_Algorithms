def rprime(x, y):
    for d in range(2, min(x, y) + 1):
        if x % d == 0 and y % d == 0:
            return False
    return True

def PPT_UnitCircle(upper):
    for u in range(1, upper+1):
        for v in range(1, u):
            a = u**2 - v**2
            b = 2*u*v
            c = u**2 + v**2
            if (u + v) % 2 != 0 and rprime(u, v): 
                print(a, b, c), 

PPT_UnitCircle(5)