# https://leetcode.com/problems/roman-to-integer/

class roman_to_integer:

    def solution(s: str):
        roman_dict = {
            'I': 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900, 
        }

        sum = 0

        # Iterate over every character in the string
        flag = False
        for i in range(len(s)):
            if flag is True:
                
                flag = False
                continue

            if s[i:i+2] in roman_dict:
                sum += roman_dict[s[i:i+2]]
                flag = True
            else:
                sum += roman_dict[s[i]]
        
        return sum