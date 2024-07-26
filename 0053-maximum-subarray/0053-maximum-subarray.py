import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum= -sys.maxsize
        i=0
        s=0
        while i<len(nums):
            s+=nums[i]
            if s<0:
                s=0
            maxsum = max(maxsum,s)
            i+=1
        if maxsum!=0:
            return maxsum
        return max(nums)