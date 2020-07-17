def max_abs_diff(nums, j):
    """Given an array of integers of length N, returns the maximum absolute difference between 
    the j numbers chosen and those remaining in the array.

    Args:
        nums (array): array of integers
        j (integer): integer representing the number of items to select from the array
    """
    return j


nums = [2, 6, 2, 1, 10]
j = 2
#Output: Here 1,2 are selected, with the difference between the sum of j (3) 
#and the remaining #s (6+10+2 = 5) being 15

nums = [1, 4, 3, 2, 4]
j = 4
#Output: Here we would select 4, 4, 3, and 2 for a sum of 13, whereas the sum of the remaining # is 1.
#Therefore, the difference between j and our remaining # is 12