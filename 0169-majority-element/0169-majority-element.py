class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = 0
        count, i = 0, 0
        while i<len(nums):
            if count==0:
                ele = nums[i]
                count = 1
            elif ele==nums[i]:
                count+=1
            else:
                count-=1
            i+=1
        return ele
        