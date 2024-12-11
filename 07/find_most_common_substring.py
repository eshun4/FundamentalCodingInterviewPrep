"""
You are given a string of characters. Your task is to write a function that will find and return the most common substring of a given length in the input string. If two or more substrings have the same maximum frequency, you should return the lexicographically smallest one.

For example, given the input string "bananabananaba" and a substring length of 5, your function should return "anaba", since it appears twice and is lexicographically smaller than other substrings that also appear twice (e.g., "banan").

The expected time complexity for this task is 

O(str.length⋅length).

"""

from collections import Counter

def find_most_common_substring(s: str, length: int) -> str:
    # Generate all substrings of the given length
    substrings = find_substrings(s, length)
    
    # Count the frequency of each substring
    counter = Counter(substrings)
    
    # Initialize variables to track the most common substring
    most_common_substring = None
    max_frequency = 0
    
    # Iterate over the counted substrings
    for substring, frequency in counter.items():
        # Check if this substring is more frequent or lexicographically smaller
        if frequency > max_frequency or (frequency == max_frequency and (most_common_substring is None or substring < most_common_substring)):
            most_common_substring = substring
            max_frequency = frequency
    
    return most_common_substring

def find_substrings(s, length):
    substrings = []
    for i in range(len(s) - length + 1):
        substring = s[i:i+length]
        substrings.append(substring)
    return substrings