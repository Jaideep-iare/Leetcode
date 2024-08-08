from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h=defaultdict(int)
        h[0]=1
        i=0
        preSum=0
        ans=0
        while i<len(nums):
            preSum+=nums[i]
            comp = preSum-k
            ans+=h[comp]
            h[preSum]+=1
            i+=1

        return ans