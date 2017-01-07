#Problem Statement - An array is given of non negative integers. Another array is formed by shuffling elements of first array and followed by deletion of one element.
#For example - 
#Aray [1,2,3,4,5,6,7,8,9]
#Array 2 [3,2,5,4,6,7,8,9]
#Missing element in Array 2 is 1

#Assumptions - 
#Duplicate elements in Array are not entertained

#Logic -
#A python Dictionary to capture presence of a non negative integer in arrays

#Time Complexity -
#O(n) for each traversal (both arrays and dictionary)
#O(1) for locating value using key in Dictionary
#O(1) Dictionary allocation
#OVerall O(n)

def find_missing_element(arr_1, arr_2):
  tracker = {} #Dictionary to track element presence
  for e in arr_1: #Traverse first array and capture presence
    tracker[e] = True

  for e in arr_2: #Traverse second array and start marking false
    tracker[e] = False

  for e in arr_1: #Traverse through Dictionary using keys in arr_1 to find out which key has value True (missing element)
    if(tracker[e]):
      return e

#Test 01
print(find_missing_element([1,2,3,4,5,6], [2,3,6,5,4]))
