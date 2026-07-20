class Solution(object):
    def shiftGrid(self, grid, k):
        a=len(grid)
        b=len(grid[0])
        total=a*b
        flat=[val for row in grid for val in row]
        k%=total
        flat=flat[-k:]+flat[:-k]
        return [flat[i*b:(i+1)*b]for i in range(a)]