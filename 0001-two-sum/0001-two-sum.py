class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            c=target-nums[i]
            if c in d:
                return [nums.index(c),i]
            d[nums[i]]=c
            