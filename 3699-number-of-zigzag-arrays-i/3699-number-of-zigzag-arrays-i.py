class Solution(object):
    def zigZagArrays(self,n,l,r):
        mod=1000000007
        k=r-l+1
        a=[1]*k
        b=[1]*k
        p=[0]*(k+1)
        q=[0]*(k+1)
        for i in range(k):
            p[i+1]=(p[i]+a[i])%mod
            q[i+1]=(q[i]+b[i])%mod
        x=[0]*k
        y=[0]*k
        for i in range(k):
            y[i]=(p[k]-p[i+1])%mod
            x[i]=q[i]
        a,b=x,y
        for _ in range(3,n+1):
            p=[0]*(k+1)
            q=[0]*(k+1)
            for i in range(k):
                p[i+1]=(p[i]+a[i])%mod
                q[i+1]=(q[i]+b[i])%mod
            x=[0]*k
            y=[0]*k
            for i in range(k):
                y[i]=(p[k]-p[i+1])%mod
                x[i]=q[i]
            a,b=x,y
        return (sum(a)+sum(b))%mod