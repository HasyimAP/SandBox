#=========================================================#
# leetcode.com problems
# String to Integer (atoi)
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# - Read in and ignore any leading whitespace.
# - Check if the next character (if not already at the end of the string) is '-' or '+'. 
#   Read this character in if it is either. 
#   This determines if the final result is negative or positive respectively. 
#   Assume the result is positive if neither is present.
# - Read in next the characters until the next non-digit character or the end of the input is reached. 
#   The rest of the string is ignored.
# - Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
#   If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# - If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. 
#   Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# - Return the integer as the final result.

# Note:

# - Only the space character ' ' is considered a whitespace character.
# - Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
#=========================================================#

from audioop import mul
from unittest import result


def myAtoi(s: str) -> int:
    s = s.lstrip()

    if len(s) == 0:
        return 0

    multiplier = 1
    i = 0

    if s[0] == '-':
        multiplier = -1
        i = 1
    elif s[0] == '+':
        multiplier = 1
        i = 1
        
    result = 0
    
    while i < len(s):
        if not('0' <= s[i] <= '9'):
            return result * multiplier
        
        result = result * 10 + int(s[i])

        lim_int_32 = 2 ** 31
        if result * multiplier >= lim_int_32 - 1:
            return lim_int_32 - 1
        elif result * multiplier <= -lim_int_32:
            return (-lim_int_32)
        
        i += 1

    return result * multiplier

#=========================================================#
# Testing
#=========================================================#
print(myAtoi('42'))
print(myAtoi('    -42'))
print(myAtoi('4193 with words'))
print(myAtoi('words and 987'))
print(myAtoi('-+12'))
print(myAtoi('+-12'))
print(myAtoi('3.14159'))
print(myAtoi("-91283472332"))