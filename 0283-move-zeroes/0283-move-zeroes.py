class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = -1
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                j = i
                break
        if j==-1:
            return nums
        i=j+1
        while i<n:
            if nums[i]!=0:
                nums[j],nums[i] = nums[i],nums[j]
                j +=1
            i+=1
        return nums
        # j=-1
        # for i in range(len(nums)):
        #     if j==-1 and nums[i]==0:
        #         j=i
        #     if j!=-1 and nums[i]!=0:
        #         nums[i],nums[j]= nums[j],nums[i]
        #         j+=1
        # return nums
            