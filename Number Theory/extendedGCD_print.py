def extendedGCD_print(a,b):
    origa = a
    origb = b

    x = 0
    lastx = 1
    y = 1
    lasty = 0

    while b != 0:
        q = a // b
        a, b = b, a % b

        full = "%d = (%d * %d + %d * %d) - %d * (%d * %d + %d * %d) " % ( b, origa, lastx, origb, lasty, q, origa, x, origb, y )
        short = "%d = %d * %d + %d * %d" % ( b, origa, lastx - x * q, origb, lasty - y * q)
        print("%s\t%s\t%s\t%s" % (a, b, full, short))

        x, lastx = (lastx - q * x, x)
        y, lasty = (lasty - q * y, y)

    return (lastx, lasty)

print(extendedGCD_print(78, 42))