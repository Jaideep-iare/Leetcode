class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = nums[0]
        count, i = 0, 0
        while i<len(nums):
            if nums[i]==ele:
                count+=1
            else:
                count-=1
                if count==0:
                    ele = nums[i+1]
                    c=0
            i=i+1
        return ele
        