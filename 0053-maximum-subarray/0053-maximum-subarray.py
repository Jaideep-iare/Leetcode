class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=float("-inf")
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            maxsum = max(maxsum,s)
            if s<0:
                s=0
        return maxsum
