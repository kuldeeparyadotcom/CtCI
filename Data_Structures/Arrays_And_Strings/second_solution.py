str = input('Enter some ASCII String: ')

def findDuplicate(str):
  if(len(str) > 128):
    return 'Duplicate'
  a = [False]*128
  for s in str:
    if(a[ord(s)] == True):
      return 'Duplicate'
    a[ord(s)] = True
  return 'Unique'

print(findDuplicate(str))
