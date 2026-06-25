class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n=len(nums)
        total_subarrays=0
        for i in range(n):
            target_count=0
            for j in range(i,n):
                if nums[j]==target:
                    target_count+=1
                subarray_len=j-i+1
                if target_count>subarray_len//2:
                    total_subarrays+=1
        return total_subarrays