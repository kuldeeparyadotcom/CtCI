#This program solves the same sentence reversal problem with same assumptions

#Time Complexity

def reverse(str):
  #strip the leading and trailing spaces
  str = str.strip()    #Time Complexity - 

  #Traverse the string and fetch words
  words = []
  word = '' #to hold collection of characters until it hits space (Assumption - word definition)
  for c in str:  #Time Complexity - O(n)
    if (c.isspace()): #If white space is encountered or end of string is encountered then collections of letters till that point is considered as a word
      words.append(word) #Add word to list words   #Time Complexity of append() function - 
      word = '' #Reset string word to capture next word
    else: 
      word += c
  words.append(word) #Specifically for the last word as whitespace would not be at the end of the given string

  #Form the reversed string and return
  result = ''
  for i in range(len(words)):  #Time Complexity - O(n)
    result += words.pop() + ' ' #One space after every word   #Time Complexity of pop() function -
  return result.strip() #Strip trailing space  #Time Compexity of strip() function - 

#Test 01 - one word sentence (Grammatically incorrect though)
print(reverse('Do'))

#Test 02
print(reverse('This is the best'))

#Test 03 - Leading and Trailing white spaces
print(reverse('    This is the best    '))
