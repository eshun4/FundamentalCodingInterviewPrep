"""
You are given two strings, string1 and string2. Your goal is to determine a new string, string3, that is formed by characters that occur in both string1 and string2 in the same order as they occur in string1.

Characters in string3 should maintain their original sequence order from string1. If a character is repeated in string1 and string2, include that character in string3 as many times as it occurs in both strings, but not more than that.

For example, given string1 = "apple" and string2 = "peach", the resulting string3 would be "ape".

Your algorithm should not exceed a time complexity of 
O(string1.length+string2.length).
"""

from collections import Counter

def solution(string1, string2):
    # TODO: Implement the function here
    string_3 = ""
    # Handle base case where the string 1 and string 2 are both empty 
    if not string1 and not string2:
        return ""
    
    # Get the character count of string 2
    string_2_count = Counter(string2)
    
    # Iterate through string1
    for char in string1:
        if char in string_2_count:
            if string_2_count.get(char) > 0:
                string_3 += char
                string_2_count[char] -= 1
    
    return string_3
        
