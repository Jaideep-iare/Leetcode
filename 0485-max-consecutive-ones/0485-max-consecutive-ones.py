class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = 0
        c=0
        for i in nums:
            if i==1:
                c+=1
                maxcount=max(maxcount,c)
            else:
                c=0
        return maxcount