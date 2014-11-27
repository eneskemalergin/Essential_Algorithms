# -*- coding: cp1252 -*-
# Exercises 6 #
#------------------------------------------------------------------------------#
# Question 1
''' Write a program that implements insertionsort.'''
def insertionSort(seq):
    n = len(seq)
    # Starts with the first item as the only sorted entry
    for i in range(1, n):
        # save the value to be positioned
        value = seq[i]
        # Find the position where value fits in the ordered part of the list
        pos = i
        while pos > 0 and value < seq[pos - 1]:
            # shift the items to the right during the search
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value
        print seq
    return seq

#------------------------------------------------------------------------------#
# Question 2
''' The For i loop used by the insertionsort algorithm runs from 0 to the
array’s last index. What happens if it starts at 1 instead of 0? Does that
change the algorithm’s run time?
'''

# it will change the result it cannot take the first index...



#------------------------------------------------------------------------------#
# Question 3
''' Write a program that implements selectionsort. '''

def selectionSort(seq):
    n = len(seq)
    for i in range(n-1):
        # Assume the ith element is the smallest
        smallNdx = i
        # Determine if any other element contains smaller value
        for j in range(i + 1, n):
            if seq[j] < seq[smallNdx]:
                smallNdx = j

        # Swap the ith value and smallNdx value if the smallest value is
        # not already i ints proper position.
        if smallNdx != i:
            temp = seq[i]
            seq[i] = seq[smallNdx]
            seq[smallNdx] = temp
        print seq    
    return  seq        

#------------------------------------------------------------------------------#
# Question 5
''' Write a program that implements bubblesort. '''
def bubbleSort(seq):
    not_sorted = True
    n = len(seq)
    while not_sorted:
        # If following statements fail next statement will stop the loop
        not_sorted = False

        for i in range(n - 1):
            if seq[i] < seq[i-1]:
                temp = seq[i]
                seq[i] = seq[i-1]
                seq[i-1] = temp

                not_sorted = True
        print seq
    return seq

#------------------------------------------------------------------------------#
# Question 7
''' Write a program that uses an array-based heap to build a priority queue.
So that you don’t need to resize the array, allocate it at some fixed size,
perhaps 100 items, and then keep track of the number of items that are
used by the heap. (To make the queue useful, you can’t just store priorities.
Use two arrays—one to store string values, and another to store the
corresponding priorities. Order the items by their priorities.) '''
def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break
def heapsort(lst):
  ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
 
  # in pseudo-code, heapify only called once, so inline it here
  for start in range((len(lst)-2)/2, -1, -1):
    siftdown(lst, start, len(lst)-1)
 
  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst

#------------------------------------------------------------------------------#
# Question 8
''' What is the run time for adding items to and removing items from a heapbased
priority queue? '''

# O(logN)

#------------------------------------------------------------------------------#
# Question 9
''' Write a program that implements heapsort.'''
def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break
def heapsort(lst):
  ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
 
  # in pseudo-code, heapify only called once, so inline it here
  for start in range((len(lst)-2)/2, -1, -1):
    siftdown(lst, start, len(lst)-1)
 
  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst

#------------------------------------------------------------------------------#
# Question 10
''' Can you generalize the technique used by heapsort for holding a complete
binary tree so that you can store a complete tree of degree d? Given a
node’s index p, what are its children’s indices? What is its parent’s index?'''

#(?)


#------------------------------------------------------------------------------#
# Question 11
''' Write a program that implements quicksort with stacks. (You can use the
stacks provided by your programming environment or build your own.) '''
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more




#------------------------------------------------------------------------------#
# Question 13
''' Write a program that implements quicksort with in-place partitioning.'''
#!/bin/python
''' Quick Sort 1 - Partition '''
def partition(ar):    
    p = 0
    for j in range(1, len(ar)):
        if ar[j] < ar[p]:
            ar = ar[0:p] + [ar[j]] + ar[p:j] + ar[j+1:]
            p += 1
    print ' '.join([`num` for num in ar])

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)

#------------------------------------------------------------------------------#
# Question 15
''' Write a program that implements countingsort. '''

def CountingSort(list, max_value):
    # Make and array to hold the counts
    counts = []

    # Initialize the array to hold the counts.
    for i in range(max_value):
        counts.append(0)

    # Count the items with each value
    for j in list:
        # Add 1 to the count for this value
        counts[j] += 1

    sortedList = []
    for i in range(max_value):
        if counts[i] > 0:
            for j in range(counts[i]):
                sortedList.append(i)
 
    return sortedList
print(CountingSort([2,16,77,65, 99, 4, 2, 16, 16], 100))

#------------------------------------------------------------------------------#
# Question 19
''' For the following data sets, which sorting algorithms would work well,
and which would not?
a. 10 fl oating-point values
b. 1,000 integers
c. 1,000 names
d. 100,000 integers with values between 0 and 1,000
e. 100,000 integers with values between 0 and 1 billion
f. 100,000 names
g. 1 million fl oating-point values
h. 1 million names
i. 1 million integers with uniform distribution
j. 1 million integers with nonuniform distribution '''

# a) Insertion, selection or Bubble sort would work well.
# b) Heapsort, quicksort, and mergesort would work well.
# c) Heapsort, quicksort, and mergesort would work well. Quicksort
#       would be fastest if the values don’t contain too many duplicates and are not
#       initially sorted or you use a randomized method for selecting dividing items.
#       Countingsort won’t work. Making bucketsort work might be diffi cult. (The
#       trie described in Chapter 10 is similar to a bucketsort, and it would work.)
# d) Countingsort would work
#       very well. Bucketsort would also work well, but not as well as countingsort.
# e) Countingsort would
#       not work very well, because it would need to allocate an array with 1 billion
#       entries to hold value counts. Bucketsort would work well
# f) Countingsort doesn’t work with strings. Making bucketsort
#       work might be diffi cult. (Again, the trie described in Chapter 10 would work.)
#       Heapsort, quicksort, and mergesort would work well, with quicksort being
#       the fastest in the expected case
# g) Countingsort doesn’t work with strings.
#       Bucketsort would work well. Heapsort, quicksort, and mergesort would work
#       but would be much slower.
# h) Heapsort, quicksort, and mergesort would work but would be slow.
# i) Countingsort might work if the
#      range of values is limited. Otherwise, bucketsort would probably be the best
#      choice.
# j) Countingsort might work
#       if the range of values is limited. Bucketsort might have trouble because the
#       distribution is nonuniform. Heapsort, quicksort, and mergesort would work
#       but would be slow.




















