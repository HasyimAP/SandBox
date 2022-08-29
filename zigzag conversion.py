#=========================================================#
# leetcode.com problems
# Zigzag Conversion

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

#    P   A   H   N
#    A P L S I I G
#    Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
#=========================================================#

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    rowList = [''] * numRows
    currRow, down = 0, 1

    for c in s:
        rowList[currRow] += c
        if down == 1:
            if currRow == numRows-1 and down == 1:
                down = 0
            else:
                currRow += 1
        if down == 0:
            if currRow == 0 and down == 0:
                down = 1
                currRow += 1
            else:
                currRow -= 1

    return ''.join(row for row in rowList)
        
#=========================================================#
# Testing
#=========================================================#
print(convert('PAYPALISHIRING', 3))
print(convert('PAYPALISHIRING', 4))