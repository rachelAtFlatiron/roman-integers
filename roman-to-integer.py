'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

one = "III"
two = "LVIII"
three = "MCMXCIV"
i = "I" 
im = "IM" 
cmxcix = "CMXCIX"
MCDXLIV = "MCDXLIV"

roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

#O(n^2)
# def fxn(num):
#     total = 0
#     fours = num.count("IV") * 2 #4
#     nines = num.count("IX") * 2 #9
#     xls = num.count("XL") * 20 #40
#     xc = num.count("XC") * 20 #90
#     cd = num.count("CD") * 200 #400
#     cm = num.count("CM") * 200 #900
#     nums = fours + nines + xls + xc + cd + cm 
#     for i in roman_object: #O(n)
#         for char in num: #O(n)
#             if(i == char):
#                 total += roman_object[char]
            
#     return total - nums 

#runtime: O(n)
def fxn(roman_input):
    result = 0
    #for loop is going backwards from I to M (from 1 to 1000)
    print(roman_input)
    for list_position in range(len(roman_input) -1, -1, -1): #O(n)
        #current value from dictionary
        current_value = roman_values[roman_input[list_position]] #O(1)
        #list_position < len(roman_input) - 1
        #if we are not at the end of the list 

        #current_value < roman_values[roman_input[list_position + 1]]
        #list_position + 1 => next index to the right
        #roman_input[list_position + 1] => integer value of numeral to the right
        #current_value < integer value to numeral to the right 
        #IV -> True 
        #XX -> False
        #XV -> False

        #are there roman numerals to the right and if so are they less than the current numeral
        

        if(list_position < len(roman_input) - 1 and current_value < roman_values[roman_input[list_position + 1]]): #O(1)
            result -= current_value #O(1)
        else: 
            result += current_value #O(1)
        print(f'current value is {current_value}, result is {result}') #O(1)
    print(f'\n\n\n')
    return result 


    
    # 
    # mcmxciv: {fxn(three)} should be 1994
    # i: {fxn(i)} should be 1 
    # cmxcix: {fxn(cmxcix)} should be 999
    # MCDXLIV: {fxn(MCDXLIV)} should be 1444
print(f'''
    iii: {fxn(one)} should be 3
    lviii: {fxn(two)} should be 58
    iv: {fxn("IV")} should be 4
    ''')

dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


# def fxn(roman):
#     sum = 0
#     for i in range(len(roman)):
#         #subtract 
#         #if not at end of string 
#         #if current char is less than next char
#         if(i < len(roman) - 1 and dict[roman[i]] < dict[roman[i+1]]):
#             sum -= dict[roman[i]]
#         #sum
#         else:
#             sum += dict[roman[i]]
#     return sum

