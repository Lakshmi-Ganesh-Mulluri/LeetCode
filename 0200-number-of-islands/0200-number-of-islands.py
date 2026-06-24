class Solution(object):
    def numIslands(self,g):
        if not g:
            return 0
        r=len(g)
        c=len(g[0])
        ans=0
        def dfs(i,j):
            if i<0 or i>=r or j<0 or j>=c or g[i][j]=='0':
                return
            g[i][j]='0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(r):
            for j in range(c):
                if g[i][j]=='1':
                    ans+=1
                    dfs(i,j)
        return ans