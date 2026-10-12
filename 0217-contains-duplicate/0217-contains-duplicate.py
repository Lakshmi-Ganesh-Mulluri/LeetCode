class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s=set()
        for ele in nums:
            if ele not in s:
                s.add(ele)
            else:
                return True
        return False