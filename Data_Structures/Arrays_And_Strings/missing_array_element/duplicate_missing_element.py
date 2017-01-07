#This program solves the same problem but this time it entertains duplicate elements as well

def find_missing(arr_1, arr_2):
  a = {} #Empty Dictionary to tracker the array element frequency
  
  #Time Complexity - O(n)
  for e in arr_1:  #Traverse through the first array
    if e in a.keys():
      a[e] += 1 #If element is already in dictionary then increment it by 1
    else:
      a[e] = 1 #If element is not already in dictionary then just initialize it by 1


  #Time Complexity - O(n)
  for e in arr_2: #Similarly traverse second array
    #There would not be any case where a new element is encountered as per problem statement
    a[e] -= 1 #Decrease the frequency by 1
  
  
  #Time Complexity - O(n)
  #Now find the Dictionary key where element is non 0, that's the missing element
  for e in arr_1: #Traverse Dictionary using keys in first array
    if a[e] != 0:
      return e  #Return the missing array element


#Test
print(find_missing([1,2,3,3,3,4,5,6], [6,4,3,5,3,2,1]))
