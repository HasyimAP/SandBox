#=========================================================#
# leetcode.com problems
# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.
#=========================================================#

def lengthOfLongestSubstring(s: str) -> int:
    charCache = []
    maxCount = 0

    for char in s:
        if char not in charCache:
            charCache.append(char)
            maxCount = max(len(charCache), maxCount)
        else:
            del charCache[:(charCache.index(char)+1)]
            charCache.append(char)

    return maxCount
    
#=========================================================#
# Testing
#=========================================================#
print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring(' '))
print(lengthOfLongestSubstring('aab'))
print(lengthOfLongestSubstring('dvdf'))