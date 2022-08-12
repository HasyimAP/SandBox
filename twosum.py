#=========================================================#
# leetcode.com problems
# Two Sum
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.
#=========================================================#

def twoSum(nums: list[int], target: int):
    numDict = {} # values: index
    for i, n in enumerate(nums):
        find  = target - n
        if find in numDict:
            return [numDict[find], i]
        numDict[n] = i

#=========================================================#
# Testing
#=========================================================#
print(twoSum([2,7,11,15], 9))
print(twoSum([3,3], 6))
print(twoSum([3,2,4], 6))