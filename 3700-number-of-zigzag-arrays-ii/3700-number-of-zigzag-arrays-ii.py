class Solution(object):
    def zigZagArrays(self,n,l,r):
        mod=1000000007
        m=r-l+1
        s=2*m
        def mul(a,b):
            c=[[0]*s for _ in range(s)]
            for i in range(s):
                for k in range(s):
                    if not a[i][k]:
                        continue
                    t=a[i][k]
                    for j in range(s):
                        c[i][j]=(c[i][j]+t*b[k][j])%mod
            return c
        def fast(a,p):
            res=[[0]*s for _ in range(s)]
            for i in range(s):
                res[i][i]=1
            while p:
                if p&1:
                    res=mul(res,a)
                a=mul(a,a)
                p//=2
            return res
        mat=[[0]*s for _ in range(s)]
        for i in range(m):
            for j in range(i):
                mat[i][m+j]=1
            for j in range(i+1,m):
                mat[m+i][j]=1
        mat=fast(mat,n-1)
        ans=0
        for i in range(s):
            ans=(ans+sum(mat[i]))%mod
        return ans