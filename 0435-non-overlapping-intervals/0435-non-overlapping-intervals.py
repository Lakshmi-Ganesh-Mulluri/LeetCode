class Solution:
    def eraseOverlapIntervals(s,i:List[List[int]])->int:
        i.sort(key=lambda x:x[1])
        r=0
        prev=float('-inf')
        for a,b in i:
            if a>=prev:
                prev=b
            else:
                r+=1
        return r