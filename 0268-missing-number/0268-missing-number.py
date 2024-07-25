class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actualsum = (n*(n+1))//2
        butsum = sum(nums)
        return actualsum-butsum
        # n=len(nums)
        # xor1 = 0
        # xor2 = 0
        # for i in range(n):
        #     xor1 = xor1^i
        #     xor2 = xor2^nums[i]
        # xor1 = xor1^n
        # return xor1^xor2
        