"""
You are given an array of n integers. Write a function that rearranges the array so that the middle half of the elements (considering the left and right quarters have been eliminated) move to the beginning of the array. The remaining elements, the left and right quarters, should move to the end of the array. If n is not divisible by 4, include the extra elements in the middle half.

Specifically:

Divide the array into four quarters.
Move the second and third quarters to the front.
Move the first and fourth quarters to the back.
The function should modify the array in place.

For example, if the input array is [1, 2, 3, 4, 5, 6, 7, 8], your function should rearrange the array to [3, 4, 5, 6, 1, 2, 7, 8].

The solution should have a time complexity of 

O(n).
"""

def rearrange_array(nums):
    n = len(nums)
    quarter_size = n // 4
    
    # Calculate the indices for slicing
    first_quarter = nums[:quarter_size]
    second_quarter = nums[quarter_size:2*quarter_size + (n % 4) // 2]
    third_quarter = nums[2*quarter_size + (n % 4) // 2:3*quarter_size + (n % 4)]
    fourth_quarter = nums[3*quarter_size + (n % 4):]
    
    # Rearrange the array
    nums[:] = second_quarter + third_quarter + first_quarter + fourth_quarter