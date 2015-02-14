# Sample Challenge
# This is a simple challenge to get things started. Given a sorted array (ar) and a number (V), can you print the index location of V in the array?
#
# {The next section describes the input format. You can often skip it, if you are using included methods. }
#
# Input Format
# There will be three lines of input:
#
#    V - the value that has to be searched.
#    n - the size of the array.
#    ar - n numbers that make up the array.
#
# Output Format
# Output the index of V in the array.
#
# {The next section describes the constraints and ranges of the input. You should check this section to know the range of the input. }

V = eval(input())
n = eval(input())
i = 0
ar = []

while(len(ar) != n):
    temp = eval(input("add value in list"))
    ar.append(temp)
print(ar)

for i in range(len(ar) - 1) :
    if ar[i] == V:
        print(ar.index(V))
    
        
