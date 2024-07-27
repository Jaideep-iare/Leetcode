class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l=[0]*len(nums)
        evi=0
        odi=1
        for i in nums:
            if i>0:
                l[evi]=i
                evi+=2
            else:
                l[odi]=i
                odi+=2
        return l