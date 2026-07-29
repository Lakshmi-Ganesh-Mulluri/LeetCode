from collections import Counter
import math
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        counts = Counter(s)
        mid_char = ""
        half_counts = {}
        for char, count in counts.items():
            if count % 2 != 0:
                mid_char = char
            half_counts[char] = count // 2
        m = n // 2 
        def count_permutations(rem_counts, rem_len):
            res = 1
            for count in rem_counts.values():
                if count > 0:
                    res *= math.comb(rem_len, count)
                    rem_len -= count
                    if res > k:
                        return k + 1
            return res
        total_perms = count_permutations(half_counts, m)
        if total_perms < k:
            return ""
        first_half = []
        rem_counts = half_counts.copy()
        for pos in range(m):
            rem_len = m - 1 - pos
            for c_code in range(26):
                char = chr(ord('a') + c_code)
                if rem_counts.get(char, 0) > 0:
                    rem_counts[char] -= 1
                    ways = count_permutations(rem_counts, rem_len)
                    if ways >= k:
                        first_half.append(char)
                        break
                    else:
                        k -= ways
                        rem_counts[char] += 1  
        first_half_str = "".join(first_half)
        return first_half_str + mid_char + first_half_str[::-1]