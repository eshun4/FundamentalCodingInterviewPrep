"""
You are provided with an array of n integers and a number k. Your task is to perform an anti-clockwise rotation 
(toward the front) of the array by k positions. The rotation should be done in place, which means you have to 
directly manipulate the input array without creating a new one. Note that k might be bigger than the array length.

For example, if the input array is [1, 2, 3, 4, 5, 6, 7], and k = 3, then after the operation, the input array should look like [4, 5, 6, 7, 1, 2, 3].
"""


from typing import List

def anti_rotate_array(nums: List[int], k: int) -> None:
    # TODO: Implement anti-clockwise rotation of the array nums by k steps.
    k = k % len(nums)
    nums[k:], nums[:k] = nums[:k], nums[k:]