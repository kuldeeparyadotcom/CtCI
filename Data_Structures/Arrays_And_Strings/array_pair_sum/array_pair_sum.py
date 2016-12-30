def count_pairs(l,s): #Takes list l and sum s
  counter = 0 #Number of pairs #Time Complexity O(1)
  pairs = [] #store pairs  #Time Complexity O(1)
  for i in l: #Time Complexity O(n) where n is number of items in list
    print('processing...', i)
    l.remove(i) #Remove the item from list  #Time Complexity
    print('now l: ', l)
    expected = s - i #find the expected number to get the desired sum
    print('Expected value: ', expected)
    if expected in l:   #Time Complexity
      print('expected found in list', l)
      counter += 1 #pair found
      print('value of counter after increment: ', counter)
      pairs.append((i, expected))  #Time Complexity
      print('current pairs: ', pairs)
  print(pairs)
  return counter

#Let's test the function
print(count_pairs([1,3,2,2], 4))
print(count_pairs([1,2,3,4,5],6))    #THERE IS A BUG IN THIS CODE, THAT'S WHY IT TRAVERSE ONLY ALTERNATIVE ITEMS IN LIST l`
