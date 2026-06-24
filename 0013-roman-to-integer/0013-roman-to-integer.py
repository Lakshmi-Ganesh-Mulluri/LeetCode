class Solution(object):
    def romanToInt(self,s):
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans=0
        mx=0
        for ch in reversed(s):
            v=d[ch]
            if v<mx:
                ans-=v
            else:
                ans+=v
                mx=v
        return ans