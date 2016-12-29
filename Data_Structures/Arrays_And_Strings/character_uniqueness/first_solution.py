str = input('Enter the string to check unique characterness: ')

#Use Dictionary (Python Hash table implemention) to check character uniqueness
print('Checking Character Uniqueness for string: ', str)

#Build a set of given string
s_str = set(str)
print('Calculated set corresponding to the given string', s_str)

if len(s_str) < len(str):
  print('String has duplicate characters')
elif len(s_str) == len(str):
  print('String has unique characters')
else:
  print('Unknown')
