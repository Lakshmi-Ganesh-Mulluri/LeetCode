class Solution(object):
    def smallestPalindrome(self,s):
        n=len(s)
        a=sorted(s[:n//2])
        b="".join(a)
        c=s[n//2] if n%2==1 else ""
        return b+c+b[::-1]