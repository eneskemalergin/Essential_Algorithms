# -*- coding: utf-8 -*-
# Chapter 4 #
#-----------#
import math
# Question 1#
#------------------------------------------------------------------------------#
'''
Write an algorithm to calculate the sample variance of a one-dimensional
array of numbers where the sample variance for an array containing
N items is defined by this equation:

S = 1/N (SumAll-from i=0 to N-1 with (xi - -x)^2)

Here −x is the mean (average) of the values in the array, and the summation
symbol Σ means to add up all the xi values as i varies from 0 to N – 1.
'''

def findSampleVariance(list):
    # Finding the average
    total = 0
    for i in list:
        total += list[i]

    average = total / len(list)

    # Find the sample variance
    sum_of_squares = 0
    for j in list:
        sum_of_squares = sum_of_squares + (list[i] - average) * (list[i] - average)

    return sum_of_squares / len(list)


#------------------------------------------------------------------------------#
# Question 2

'''
Write an algorithm to calculate the sample standard deviation of a onedimensional
array of numbers where the sample standard deviation is
defi ned to be the square root of the sample variance.
'''

def FindSampleStandartDeviation(list):
    # Finding the sample variance
    variance = findSampleVariance(list)

    # return the standart deviation
    return sqrt(variance)

#------------------------------------------------------------------------------#

# Question 3

'''
Write an algorithm to fi nd the median of a sorted one-dimensional array.
(Be sure to handle arrays holding an even or odd number of items.)
'''

def FindMedian(list):

    if (len(list) % 2 == 0):
        # The array has even length
        # Return the average of the two middle items
        middle = len(list) / 2
        return (list[middle -1] + list[middle]) / 2

    else:
        # The array has odd length
        #  Return the middle item
        middle = len(list) - 1 / 2
        return list[middle]

    


#------------------------------------------------------------------------------#

# Question 4

'''
The section “Removing Items” explained how to remove an item from a
linear array. Write the algorithm in pseudocode.
'''
def RemoveItem(list, index):
    # Slide items left 1 position to fill in where the item is

    for i in range(index, len(list) - 1):
        list[i - 1] = list[i]



#------------------------------------------------------------------------------#

# Question 5

'''
The triangular arrays discussed in this chapter are sometimes called “lower
triangular arrays” because the values are stored in the lower-left half of
the array. How would you modify that kind of array to produce an upper
triangular array with the values stored in the upper-right corner?
'''
def FindIndex(r,c):
    return ((r - 1) * (r - 1) + (r - 1)) / 2 + c

def FindIndex(r,c):
    return ((c - 1) * (c - 1) + (c - 1)) / 2 + r
#------------------------------------------------------------------------------#

# Question 6

'''
How would you modify the lower triangular arrays described in this
chapter to make an “upper-left” array where the entries are stored in the
upper-left half of the array? What is the relationship between row and
column for the entries in the array?
'''

def FindIndex(r, c):
    r = N - 1 - r
    return ((r - 1) * (r - 1) + (r - 1)) / 2 + c



#------------------------------------------------------------------------------#
# Question 7

'''
Suppose you defi ne the main diagonal of a rectangular (and nonsquare)
array to start in the upper-left corner and extend down and to the right
until it reaches the bottom or right edge of the array. Write an algorithm
that fi lls entries on or below the main diagonal with 1s and entries above
the main diagonal with 0s.
'''

def FillListLLtoUR(values[,], ll_value, ur_value):
    for row in values:
        for col in values:
            if row >= col :
                values[row, col] = ur_value
            else:
                values[row, col] = ll_value
                
#------------------------------------------------------------------------------#

# Question 9

'''
Write an algorithm that fi lls each item in a rectangular array with the
distance from that entry to the nearest edge of the array.
'''

def FillListWithDistances(values[,]):
    max_row = values.GetUpperBound(0)
    max_col = values.GetUpperBound(1)

    for row in range(max_row):
        for col in range(max_col):
            values[row, col] = Minimum(row, col, max_row - row, max_col - col)
            


#------------------------------------------------------------------------------#

#Question 10

'''
*Generalize the method for building triangular arrays to build threedimensional
tetrahedral arrays that contain entries value[i, j, k] where
j ≤ i and k ≤ j. How would you continue to extend this method for even
higher dimensions?
'''

def NumCellsForTriangleRows(rows):
    return (rows * rows + rows ) / 2

def NumCellsForTetrahedralRows(rows):
    return (rows * rows * rows + 3 * rows * rows + 2 * rows) / 6

def RowColumnHeightToIndex(row, col, hgt):
    return NumCellsForTriangleRows + NumCellsForTetrahedralRows +hgt


#------------------------------------------------------------------------------#


# Question 12

'''
 Write an algorithm that adds two triangular arrays.

'''

def AddTriangularLists(list1, list2 , result):
    for row in list1:
        for col in list2:
            result[row, col] = list1[row,col] + list2[row, col]


#------------------------------------------------------------------------------#

# Question 13

'''
 Write an algorithm that multiplies two triangular arrays.

'''

def MultiplyLists(list1, list2, result):
    for i in list1:
        for j in list2:
            # Calculate the [i, j] result
            result[i, j] = 0
            for k in list2:
                resutl[i, j] = result[i, j] + list1[i,k] * list2[k,j]
        

#------------------------------------------------------------------------------#

























