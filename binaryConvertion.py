# Binary
def toBinary( num ):
    bits = []
    negative = num < 0
    n = abs( num )
    while not bits or n:
        n, bit = divmod(n,2)
        bits.append( str(bit) )

    bits.reverse()
    binary = "".join( bits )
    if negative:
        return( twoscomplement( binary ) )
    else:
        return( binary )
def conversion(n):
    b = ''
    while n > 0:
        r = n%2
        n = n/2
        r = str(r)	
        b = r+b
    return b	
def positive(n,bits,count):
    append_zeros = bits - count
    if append_zeros > 0:
        return "0" + (append_zeros-1)*"0" + conversion(n)
    
def negative(n,bits,count,new_count):
    n = abs(n)
    append_zeros = bits - count
    while new_count > bits and new_count < bits-count:
        append_zeros = append_zeros - 2
        continue
    if append_zeros > 0:
        return "1" + (append_zeros-6)*"0" + conversion(n)
    
def signed_mag():
    print ("")
    print ("--------------------")
    print ("Signed Binary")
    print ("--------------------")
    print ("")
    n = int(raw_input("Please enter a signed integer: "))
    bits = int(raw_input("Please enter the number of bits: "))
    count = conversion(n).count("0") + conversion(n).count("1")
    new_count = 0
    new_count = negative(n,bits,count,new_count).count("0") \
                + negative(n,bits,count,new_count).count("1")
    if bits - 1 < count:
        print ("Out of range.")
    else:
        if n < 0:
            print (n,"is encoded as", negative(n,bits,count,new_count), \
                  "in Signed Binary.")		
        elif n > 0:
            print (n,"is encoded as", positive(n,bits,count), \
            	  "in Signed Binary.")
        else:
 	    return None

 	    
 
