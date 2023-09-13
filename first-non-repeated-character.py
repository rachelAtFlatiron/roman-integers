'''
You need to write a function, that returns the first non-repeated character in the given string.

If all the characters are unique, return the first character of the string.
If there is no unique character, return null in JS or Java, None in Python, '\0' in C.
'''

''' 
1. what are the constraints if any?
2. some particular edge/special cases
3. brainstorm / pseudocode (standard english, human syntax)
'''

'''
test #standard case
teeter #edge case, our letter is at the end
11223212351122111 #standard case
banana #edge case, letter at the beginning
"" #edge case, empty string
a #edge case, one letter
aaaaa #edge case, all repeated (no unique character) 
aaabc #standard case
abcccc #standard case 

'''

import ipdb 

'''

Big O = Runtime (the amount of time a piece of code takes to run)
O(1) = constant time (if/elses, setting variables)
O(n) = linear time (for loops)
O(n^2) = quadratic time #slower than linear time
'''


banana = "banana"
test = "test"
abccc = "abccc" 
aaabc = "aaabc"
aabbcc = "aabbcc" 
aabcc = "aabcc"
fox = "fox" 
empty = "" 
single = "a"

# def fxn(string): 
#     # count the amount of every letter, results that are < 2 is valid
#     # use find to find next first letter 
#     # save each unique character in a list

#     # count the amount of every letter
#     char_counts = {}
#     unique_chars = tuple(string)
#     print(unique_chars)
#     for i in range(0, len(unique_chars)):
#         char_counts[unique_chars[i]] = string.count(unique_chars[i]) 
#     for key in char_counts:
#         if(char_counts[key] == 1):
#             return key
#         else: 
#             None




# O(n) - one while loop iteration 
# def fxn(string):
#     found = False #if we found the correct character 
#     i = 0 #the current index
#     while(not found and i <= len(string) - 1): #last index is len(string) - 1
#         char = string[i]
#         if(string.count(char) == 1):
#             found = True 
#         else: 
#             i += 1 
#     if(not found):
#         return None 
#     else:
#         return char #python does not have block scope, this is in function scope

#O(n^2)
# 1 for loop: n while loops
# 2 for loop: n while loops 
#.
#.
#.
#n for loops: n while loops
def fxn(string):
    #O(n)
    for el in string: #strings are immutable, however some list methods work on strings
        #in c, strings are a list of characters
        #python itself is written in the c programming language 
        if(string.count(el) == 1): #.count O(n)
            return el 

    return None 


print(f'''
      banana: {fxn(banana)} should be 'b'
      test: {fxn(test)} should be 'e'
      abccc: {fxn(abccc)} should be 'a'
      aaabc: {fxn(aaabc)} should be 'b'
      aabbcc: {fxn(aabbcc)} should be 'None'
      aabcc: {fxn(aabcc)} should be 'b'
      fox: {fxn(fox)} should be 'f'
      a: {fxn(single)} should be 'a' 
      "": {fxn(empty)} should be None
''')