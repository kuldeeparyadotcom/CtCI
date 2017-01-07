#This program also solves the same problem

#It utilizes Exclusive OR (XOR) operation to solve this problem
#Logic: If you XOR two same numbers then it would become 0
#We will XOR all elements in both arrays that means elements common in both arrays would result 0 (after XOR operation), but the missing element added XORed to 0 would be the missing element itself (XOR property)
#XOR property
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0

def find_missing(arr_1, arr_2):
  result = 0 #Take one variable that would store result of XOR operation every time
  
  for e in arr_1 + arr_2: #Concatenate both arrays and we will traverse one by one
    result = result ^ e #Sum all array elements using XOR
    
  return result


#Test
print(find_missing([1,2,3,3,4], [2,1,3,4]))
