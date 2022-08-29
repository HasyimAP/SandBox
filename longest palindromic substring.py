#=========================================================#
# leetcode.com problems
# Given a string s, return the longest palindromic substring in s.
#=========================================================#

def longestPalindrome(s: str) -> str:
    maxCount = 0
    maxPalindrom = ''

    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if s[i:j] == s[i:j][::-1] and j-i > maxCount:
                maxCount = len(s[i:j])
                maxPalindrom = s[i:j]

    return maxPalindrom

#=========================================================#
# testing
#=========================================================#
print(longestPalindrome('babad'))
print(longestPalindrome('cbbd'))
print(longestPalindrome('a'))
print(longestPalindrome('bb'))
print(longestPalindrome('ac'))