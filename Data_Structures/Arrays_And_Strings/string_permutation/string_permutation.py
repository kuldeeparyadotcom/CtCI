#Program to check if two given strings are permutation of each other

#Assumption
#Input Strings are ASCII
#Entertain lower and upper case (if stick to only one case it can reduce space complexity as it requires less storage)
#Whitespaces are entertained as well

#Optimization
#If length of the both strings is different, then we won't process further.

#Logic
#Letter and their respective frequency must be same in both strings
#Data Structure - Hash Table

#Time Complexity = O(n) + O(n) + O(1) = O(n)
#Space Complexity = O(128)

def is_permutation(str_1, str_2):
  if len(str_1) != len(str_2): #Optimization check
    return False
  #Allocate one initial list with sufficient storage to entertain ASCII string
  a = [0]*128  #Default value for each array element is 0
  for s in str_1: #Traverse first string
    a[ord(s)] += 1 #Increase letter frequency by 1
  
  for s in str_2: #Traverse second string
    a[ord(s)] -= 1 #Decrease character frequency by 1

  #If both strings are permutation of each other, then each element of array must be 0
  if a.count(0) != len(a) : #All elements must be 0  
    return False
  return True

#Test 01
print(is_permutation('ABC', 'BCA'))

#Test 02
print(is_permutation('xABC', 'BCA'))

#Test 03
print(is_permutation('abcdefghijklm', 'labcdefghijkl'))

#Test 04
print(is_permutation('aBc ', ' Bca'))
