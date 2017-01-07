#Problem Statement - Compress a given string
#Example - AAAaaaBB is compressed to A3a3B2

#Assumptions - 
#Charset - ASCII (Doesn't matter in this logi actually)
#Case Sensitivity - Yes
#Spaces - Not entertained
#False Compression - i.e. A is compressed to A1 (in case of only one occurrence of a character)

'''
Logic:
variable previous will hold the last processed character
variable current will hold the current character being processed
variable count will hold the current frequeny of character
varaible result will hold the compressed string
'''

def compress(raw_str):
  raw_str = raw_str.strip() #Removing leading and trailing spaces in case if any
  
  if (raw_str == ''): #Edge case
    return None

  previous = None #Starting Value
  current = None #Before starting string traversal
  count = 0 #Before starting string traversal
  result = '' #No result before process starts

  for c in raw_str: #Traverse through string O(n)
    previous = current
    current = c
    if (previous != current):
      if (previous is not None): #To exempt start of string
        result = result + previous + str(count) #Store compressed string
      count = 1 #Reset counter
    else:
      count += 1 #Increment counter
  #For the last character frequency
  result = result + current + str(count) #Store compressed string 
  return result

#Test
print(compress('AAAaaaBB'))
print(compress('AAAAABBBBCCC'))
print(compress('AAAAABBBBC'))
print(compress('AAAAABC'))
print(compress('')) #Length 0 edge case
print(compress('A')) #Length 1 edge case
