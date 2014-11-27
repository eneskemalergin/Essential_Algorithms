# -*- coding: cp1252 -*-
# Chapter 7 #
#------------------------------------------------------------------------------#
# Question 1
''' Write a program that implements linear search. '''
def linearSearch(list, target):
    for i in range(len(list) -1):
        # if the target is int the ith element, return True
        if list[i] == target:
            return True
    return False # If not found, return false

#------------------------------------------------------------------------------#
# Question 4
''' Write a program that implements binary search. '''
def binarySearch(list, target):
    # Start with the entire sequence of elements
    low = 0
    high = len(list) - 1
    # We need to sort the list first
    list = list.sort()
    # Repeatedly subdivide the sequence in half until the target is found
    while low <= high:
        # find the midpoint of the sequence
        mid = (high+low) // 2
        # Does the midpoint contain the target?
        if list[mid] == target:
            return True
        # or does the target precede the midpoint?
        elif target < list[mid]:
            high  = mid - 1
        else:
            low = mid - 1
    return False

#------------------------------------------------------------------------------#
# Question 6
''' Write a program that implements interpolation search. '''

def interpolationSearch(list, target):
    min = 0
    max = len(list) - 1
    while min <= max:
        # find the dividing item
        mid = min + (max - min) * (target - list[min])/(list[max]- list[min])

        if list[mid] == target:
            return mid

