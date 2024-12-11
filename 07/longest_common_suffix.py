"""

You are given an array of n strings. Your task is to find the longest common suffix shared among all strings in the array. A suffix is a sequence of letters at the end of a word. For instance, in the word "flying," "ing" is a suffix.

If the given array is empty or there is no common suffix among the strings, your function should return an empty string.

For example, given an array of strings: ["barking", "parking", "starking"], the longest common suffix is "arking".
"""

def solution(strs):
    # TODO: Implement the function
    # If array is empty return empty string
    if not strs:
        return ""
        
    # Since we are looking for suffix and not prefix we have to fist reverse the strings in strs
    strs = [st[::-1] for st in strs]
    
    # next find the shortest string among the reversed string
    shortest = min(strs, key=len)
    
    # loop through each character in the newly reversed strs array and if there is a mismatch in the 
    # characters return the shortest path from index 0 to the index where there is a mismatch(non-inclusive)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                # Return it reversed
                return shortest[:i][::-1]
                
    return shortest[::-1]
            
            
# Second solution
def largest_common_prefix(words):
    # TODO: Implement this function to find the largest common prefix among the words in the array.
    # check base case if the words array is empty
    if not words:
        return ""
        
    # get the shortest prefix to start with
    shortest = min(words, key=len)
    
    # Iterate through each character in shortest and each character in the other strings with doublw for loop
    for i in range(len(shortest)):
        for word in words:
            if word[i] != shortest[i]:
                return shortest[:i]
    # Else return shortest    
    return shortest
            