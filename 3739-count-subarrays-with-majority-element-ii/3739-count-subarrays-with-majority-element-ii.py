class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        offset = n + 1
        bit = [0] * (2 * n + 2)
        def update(index, value):
            while index < len(bit):
                bit[index] += value
                index += index & -index
        def query(index):
            total = 0
            while index > 0:
                total += bit[index]
                index -= index & -index
            return total
        update(offset, 1)
        prefix = 0
        answer = 0
        for num in nums:
            if num == target:
                prefix += 1
            else:
                prefix -= 1
            answer += query(prefix + offset - 1)
            update(prefix + offset, 1)
        return answer