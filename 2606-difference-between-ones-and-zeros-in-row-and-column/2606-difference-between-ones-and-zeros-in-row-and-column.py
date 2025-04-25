class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        r = len(grid)
        c = len(grid[0])
        rows = [0] * r
        cols = [0] * c

        for a in range(r):
            for b in range(c):
                if grid[a][b] == 0:
                    rows[a] -= 1
                    cols[b] -= 1
                else:
                    rows[a] += 1
                    cols[b] += 1
        for i in range(r):
            for j in range(c):
                grid[i][j] = rows[i] + cols[j]
        return grid
                

        





        