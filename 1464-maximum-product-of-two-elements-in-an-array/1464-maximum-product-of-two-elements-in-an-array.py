class Solution(object):
    def maxProduct(self,nums):
        a=0
        b=0
        for c in nums:
            if c>a:
                b=a
                a=c
            elif c>b:
                b=c
        return(a-1)*(b-1)