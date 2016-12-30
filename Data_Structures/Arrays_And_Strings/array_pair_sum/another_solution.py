#It uses set and runs in O(n)

def count_pairs(l, s): #Requires list l and sum s
  seen = set()  #A set for tracking number as we traverse through the list
  output = set() #A set to store tuples

  for i in l:
    expected = s - i #Number that we are interested in to make it a successful tuple
    if expected in seen:
      output.add((i, expected)) #Found the tuple
    else:
      seen.add(i) #Keep track that we have seen this number
  print('\n'.join(map(str, list(output))))
  return len(output)

#Let's test this function
print(count_pairs([1,3,2,2,], 4))
print(count_pairs([1,2,3,4,5], 6))
