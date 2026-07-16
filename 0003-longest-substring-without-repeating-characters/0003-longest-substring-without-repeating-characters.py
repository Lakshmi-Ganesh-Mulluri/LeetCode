class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w=0
        for i in range(len(s)):
            unique=set(s[i])
            j=i+1
            while j<len(s):
                if s[j] not in unique:
                    unique.add(s[j])
                    j+=1
                else:
                    break
            w=max(w,j-i)
        return w