class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h={0:1}
        preSum=0
        ans=0
        for i in nums:
            preSum+=i
            ans+=h.get(preSum-k,0)
            if preSum in h:
                h[preSum]+=1
            else:
                h[preSum]=1

        return ans