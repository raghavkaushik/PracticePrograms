#Verify the numbers present in the sudoku are as per the rules.
#Each row, column, square must have a unique number.
import collections

row=collections.OrderedDict(set)
cols=collections.OrderedDict(set)
square=collections.OrderedDict(set)

grid=[[]]
#Here grid is a 2D matrix of shape 9X9 as per sudoku
#Each dictionary will hold values and compare if already exist value is not repeated again.

for r in range(9):
    for c in range(9):
        if grid[r][c] in row[r] or grid[r][c] in cols or grid[r][c] in square[(r//3),(c//3)]:
            print("Fail")
            break
        row[r].add(grid[r][c])
        cols[c].add(grid[r][c])
        square[(r//3),(c//3)].add(grid[r][c])
    print("True")