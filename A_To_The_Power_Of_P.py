# Calculate A to the power of P

def RaiseToPower():
    a = eval(input("Number  you want to take power"))
    p = eval(input("Power:"))
    i = 1
    result = 1
    while (p >= 1):
        if (p % 2) == 1:
            result  = result * a

        p = p/2
        a = a * a

    return result
# Implement This
'''
// Calculate A to the power P.
Float: RaiseToPower(Float: A, Integer: P)
    <Use the first fact to quickly calculate A, A2, A4, A8, and so on
        until you get to a value AN where N + 1 > P>
    <Use those powers of A and the second fact to calculate AP>
    Return AP
End RaiseToPower
'''
