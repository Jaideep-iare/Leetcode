class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = 0
        c=0
        for i in nums:
            if i==1:
                c+=1
            elif i==0:
                maxcount=max(maxcount,c)
                c=0
        if c>maxcount:
            return c
        return maxcount