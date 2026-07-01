class Solution(object):
    def reverse(self, num):
        low=-2**31
        high=2**31 - 1
        if num<0:
            s=-1
        else:
            s=1
        value=abs(num)
        ans=int(str(value)[::-1])*s
        if ans<low or ans>high:
            return 0
        return ans