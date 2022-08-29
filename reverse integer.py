#=========================================================#
# leetcode.com problems
# Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#=========================================================#

def reverse(x: int) -> int:
    if x < 0:
        reverseInt = int('-' + str(x)[1:][::-1])
    else:
        reverseInt = int(str(x)[::-1])
    if reverseInt >= 2**31 - 1 or reverseInt <= -2**31:
        return 0

    return reverseInt

#=========================================================#
# Testing
#=========================================================#
print(reverse(123))
print(reverse(-123))