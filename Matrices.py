# Matrices #

''' Adding two arrays together  '''
def AddArrays(list1, list2, result):
    for i in list1:
        for j in list2:
            result[i,j]= list1[i,j] + list2[i,j]

''' Multiplying two normal two dimensional arrays   '''
def MultiplyArrays(list1, list2, result):
    for i in list1:
        for j in list2:
            # Calculate the [i,j] result
            result[i,j] = 0
            for k in list2:
                result[i,j] = result[i,j] + list1[i,k] * list2[k,j]


''' High-Level algorithm adds two sparse matrices:  '''
def AddArrays(list1, list2, result):
    # Get pointers into the matrices' row lists.

    list1_row = list1.sentinel.nextRow
    list2_row = list2.sentinel.nextRow
    result_row = result.sentinel

    # Repeat while both input rows have items left
    while list1_row != None and list2_row != None:
        if list1_row.RowNumber < list2_row.RowNumber:
            # list1_row's RowNumber is smaller Copy it
            result_row = list1_row
            list1_row = list1_row.NextRow

        elif list2_row.RowNumber < list2_row.RowNumber:
            # list2_row's RowNumber is smaller Copy it!
            result_row = list2_row
            list2_row = list2_row.NextRow
        else:
            # The input rows have the same RowNumber
            # Add the values int both rows to the result
            result_row = list1_row, list2_row
            list1_row = list1_row.NextRow
            list2_row = list2_row.NextRow

    # Copy and remaining items from either input matrix
    if list1_row != None:
        while list1_row != None:
            result_row = list1_row
            list1_row = list1_row.NewtRow
    if list2_row != None:
        while list2_row != None:
            result_row = list2_row
            list1_row = list2_row.NewtRow
        
        #<Copy list2_row's remaining rows to the result>











































            
