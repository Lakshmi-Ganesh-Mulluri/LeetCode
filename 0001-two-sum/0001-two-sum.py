class Solution:
    def twoSum(self,a,b):
        d={}
        for i,x in enumerate(a):
            y=b-x
            if y in d:
                return [d[y],i]
            d[x]=i