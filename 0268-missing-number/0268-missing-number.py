class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actualsum = (n*(n+1))//2
        butsum = sum(nums)
        return actualsum-butsum