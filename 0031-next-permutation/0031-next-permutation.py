class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=n-2
        index=-1
        while i>=0:
            if nums[i]<nums[i+1]:
                index=i
                break
            i-=1
        if index==-1:
            nums = nums.reverse()
        else:
            i=n-1
            while i>index:
                if nums[i]>nums[index]:
                    nums[i],nums[index]=nums[index],nums[i]
                    break
                i-=1
            nums[index+1:]=reversed(nums[index+1:])