#=========================================================#
# leetcode.com problems
# Palindrom Number
# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.
#=========================================================#

def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

#=========================================================#
# Testing
#=========================================================#
print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
print(isPalindrome(123456789))