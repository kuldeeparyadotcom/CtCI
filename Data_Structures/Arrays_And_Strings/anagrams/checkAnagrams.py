str_1 = input('Enter first string: ')
str_2 = input('Enter second string: ')


def checkAnagram(str_1, str_2):
  #Assumption - entered string is ASCII - 128 characters
  #Allocate an array
  #Logic - Default value of array elements would be 0.
    #character frequency would be found in ord(character) index
    #White spaces would be ignored as per problem statement
    #Both String would be lowered as per problem requirement
    #Each occurrence of Character in first string would increment element value by 1
    #Each occurrence of Character in second string would decrease element value by 1
  
  #Optimization check - After removing spaces if count of both strings is not same, then we can return "Not Anagrams"
  s1 = str_1.replace(' ', '')
  s2 = str_2.replace(' ', '')
  if len(s1) != len(s2):
    return "Not Anagrams" 
 
  a = [0]*128  #O(1)

  #Process first string - O(n)
  for s in str_1.lower(): #Capitalization is not considered
    if(s.isspace()): #White spaces are ignored
      continue
    else:
      a[ord(s)] += 1 #Increment by 1 for each occurrence in first string
  #print(a)

  #Process second string - O(n)
  for s in str_2.lower(): #Capitalization is not considered
    if(s.isspace()): #spaces are ignored
      continue
    else:
      a[ord(s)] -= 1 #Decrease by one
  #print(a)

  #If array's each element value is 0 then both strings are anagrams of each other - O(n)
  for i in range(len(a)):
    if a[i] != 0:
      return "Not Anagrams"
  
  return "Anagrams"


#Call the above function
print(checkAnagram(str_1, str_2)) 
  
