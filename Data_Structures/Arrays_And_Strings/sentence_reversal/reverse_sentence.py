#Problem Statement - Reverse the given statement

#Assumptions - 
#Leading and Trailing whitespaces are deleted
#Capitalization is not considered

#Time Complexity - 
#String split() method
#String strip() method
#String join() method
#String reverse() method

def reverse(str):
  #Optimization
  if len(str.split()) < 2:
    return str

  str = str.strip() #Strip leading and trailing spaces

  l = str.split() #Split given string with default white space separator and get a list
  l.reverse() #Reverse the list in place

  return ' '.join(l) #Reverse the list and join by white space to get the string out of reversed list


#Test 01 - one word sentence (Grammatically incorrect though)
print(reverse('Do'))

#Test 02
print(reverse('This is the best'))

#Test 03 - Leading and Trailing white spaces
print(reverse('    This is the best    '))
