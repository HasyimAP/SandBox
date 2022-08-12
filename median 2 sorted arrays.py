#=========================================================#
# leetcode.com problems
# Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).
#=========================================================#

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    nums1 += nums2
    nums1.sort()
    l = len(nums1)
    if l % 2 != 0:
        return nums1[l // 2]
    else:
        return (nums1[l // 2] + nums1[l // 2 - 1]) / 2

#=========================================================#
# Testing
#=========================================================#

print(findMedianSortedArrays([1,3], [2]))
print(findMedianSortedArrays([1,3], [2,4]))