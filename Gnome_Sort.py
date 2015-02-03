## Author: Enes Kemal Ergin
## Date  : 02/02/15

def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i+= 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
    return seq

# test 1
seq = [1,4,5,7,12,3,4,7,8,10,2,6,87,98]
print(gnomesort(seq))
