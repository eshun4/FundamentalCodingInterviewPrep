"""
You are given a string s. Your task is to create a function that checks whether the string s consists of one repeated substring.

If it does, the function should return the substring. If there are multiple possible answers, return the longest one. If it does not consist of a repeated substring, return an empty string.

To clarify, a "repeated substring" refers to a pattern of characters that reoccurs throughout the full string, with no characters left over. For example, the string "abababab" consists of repeated substrings "ab" and "abab". On the other hand, the string "abcabcab" does not consist of a repeated substring, as the final characters "ab" do not complete the repeating pattern of "abc".
"""

def repeat_substring(s):
    # TODO: implement the function according to the task requirements.
    # get the length of the string 
    n = len(s)
    
    # Iterate through the length of the string starting from the middle down to 1
    for i in range(n//2, 0, -1):
        # Since we are looking for repeating patterns we need to check if 
        if n % i == 0:
            substring = s[:i]
            count = n//i
            
            if substring * count == s:
                return substring
                
    return ""
    
    