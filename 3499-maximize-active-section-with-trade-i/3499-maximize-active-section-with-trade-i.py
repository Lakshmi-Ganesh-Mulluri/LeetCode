class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        ones = 0
        prev_zeros = -10**9
        max_merge = 0
        i = 0
        n = len(s)

        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1

            length = j - i

            if s[i] == '1':
                ones += length
            else:
                max_merge = max(max_merge, prev_zeros + length)
                prev_zeros = length

            i = j

        return ones + max_merge