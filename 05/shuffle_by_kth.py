"""
You are given a list of n integers and a number k.
Your task is to shuffle the array in such a way that, 
starting from the first element, every k-th element moves to the end of the array.

For instance, if nums = [1, 2, 3, 4, 5, 6, 7, 8] and k = 3, 
the output should be [1, 2, 4, 5, 7, 8, 3, 6]. 
Here, the 3rd element 3 and the 6th element 6 
(every 3rd element starting from the first) are moved to the end of the array.
"""

def shuffle_array(nums, k):
    # TODO: implement the function here
    kth_elements, remaining = [], []
    
    for i in range(len(nums)):
        if (i + 1) % k == 0:
            kth_elements.append(nums[i])
        else:
            remaining.append(nums[i])
    return remaining + kth_elements 



"""
You can do it in place too like below
"""

def shuffle_array(nums, k):
    n = len(nums)
    write_index = 0
    
    for i in range(n):
        if (i + 1) % k != 0:
            nums[write_index], nums[i] = nums[i], nums[write_index]
            write_index += 1
    
    # The `k`-th elements are now at the end of the list
    # If order matters, you might need to adjust them here

# # Example usage
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# k = 3
# shuffle_array(nums, k)
# print(nums)  # Output should be [1, 2, 4, 5, 7, 8, 3, 6]