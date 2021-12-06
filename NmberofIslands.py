#In a 2D array check number of islands based on the number of neibhors all considered as one islands.
#Grid - 2D array
import collections


def islands(grid):
    if not grid:
        return False
    rows,cols=len(grid),len(grid[0])
    visited=set()
    island=0
    def dfs(r,c):
        q=collections.deque()
        visited.add((r,c))
        q.append((r,c))
        while q:
            row,col=q.popleft()
            directions=[[1,0],[0,1],[-1,0],[0,-1]]
            for dr,dc in directions:
                r=row+dr
                c=col+dc
                if r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in visited:
                    q.append((r,c))
                    visited.add((r,c))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==1 and (r,c) not in visited:
                dfs(r,c)
                island+=1
    return island

if __name__=="__main__":
    grid = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]
    result=islands(grid)
    print(result)
