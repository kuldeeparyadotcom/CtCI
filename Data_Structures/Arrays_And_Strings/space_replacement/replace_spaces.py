'''
Purpose: to replace all spaces in a given string by '%20'
This problem is requested to be solved in place. String in python are immutable, therefor it does not seem possible to solve this problem in place.
The closer approach, I think, can be using List to solve this problem.
'''

def rep_space(s): #Input - A string (no specific charset)
    l = list(s) #Create a list corresponding to the given string for making in place operations as Strings in python are immutable

    #If provided string is of length 1
    if len(l) == 1:
        return s

    #Edge case
    if (not (' ' in l)): #If there is no space in provided string
        return s
   
    for character in l: #Iterate through the list O(n) time complexity
        if (character.isspace()): #check if character is a space
            space_index = l.index(character) #Get index of space encountered
            l.remove(character) #Remove the space
            l.insert(space_index, '%20') #Insert '%20' as the ' ' replacement
    
    return ''.join(l) #convert list to string and return

#Test cases
print(rep_space('H'))
print(rep_space(''))
print(rep_space('Mr.Amitabh'))
print(rep_space('Mr. Amitabh Bachchan'))

