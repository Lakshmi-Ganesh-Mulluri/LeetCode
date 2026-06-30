class Solution(object):
    def rob(self, nums):
        a=0
        b=0
        for i in nums:
            c=max(b,a+i)
            a=b
            b=c
        return b