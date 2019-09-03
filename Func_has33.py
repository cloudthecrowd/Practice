# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] and nums[i+1] is 3:
            return True
        else:
            return False