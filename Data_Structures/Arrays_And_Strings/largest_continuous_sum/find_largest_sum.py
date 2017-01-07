##TODO - This solution needs to be improved to run it O(n) time complexity

#Problem Statement - Find the maximum continuous Sum in a given array of positive and negative integers
#For example - Give items [1,2,-1,3,4,10,10, -10, -1]
#Largest Continuous Sum = 29 (Starting from index 0 element (1)

#Time Complexity O(n^2)

def find_largest_sum(arr_1):
  #Optimization
  if len(arr_1) == 0: #If provided array is empty return 0
    return 0

  #If all elements of given array are positive, simply return sum of all elements
  if min(arr_1) >= 0:
    return sum(arr_1)  
  
  a = {} #Empty dictionary to hold the starting element and maximum sum
  k = 0 #An integer that would represent index of array element as well as key of Dictionary
  for e in arr_1: #Let's traverse through the array
    a[k] = 0 #Sum would be 0 if we start from last element
    for i in range(k+1,len(arr_1)): #Add element next to the starting point
      if k != (len(arr_1)-1): #Avoid Index Out Of bounds exception 
        if a[k] < (a[k] + arr_1[i]): #Update Dictionary value corresponding to the index of starting element, only if sum is higher than the already existing value
          a[k] = a[k] + arr_1[i]

    #Proceed to the next element
    k += 1 #Increment k by 1

  #print(a)
  return max(a.items(), key=lambda item:item[1]) #Return the tuple (index of the starting item and maximum sum)

#Test 01
tup = find_largest_sum([1,2,-1,3,4,10,10, -10, -1])
print('Maximum Sum: ', tup[1])
print('Starting element at index: ', tup[0])

#Test 02 - Empty Array
print(find_largest_sum([]))

#Test 03 - All positive elements
print(find_largest_sum([1,2,3,4,5]))
