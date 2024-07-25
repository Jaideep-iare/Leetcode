class Solution:
    def check(self, nums: List[int]) -> bool:
        c=0
        i=1
        while i<len(nums):
            if nums[i-1]>nums[i]:
                c+=1
        
            i=i+1
        if nums[-1]>nums[0]:
            c+=1
        if c>1:
            return False
        return True
                