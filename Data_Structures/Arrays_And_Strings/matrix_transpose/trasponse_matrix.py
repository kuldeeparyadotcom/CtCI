'''
Purpose:
a N X N matrix is given and you need to transpose it (rows becomes columns and columns become rows)

Question: Can we solve it in place?

The approach below is actually a python utility zip.
For algorithm perspective though, we need to write our own algorithm to achieve it. Check out the another solution in the same directory.
'''

def tra_mat(m): #m would be a list, each item is a tuple that represents a row i.e. [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    result = [] #Empty list to hold the transposed 
    result = zip(*m)
    
    return result

#Test cases
print(list(tra_mat([(1, 4, 7), (2, 5, 8), (3, 6, 9)])))
