class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l=[]
        evi=0
        odi=1
        for i in nums:
            if i>0:
                l.insert(evi,i)
                evi+=2
            else:
                l.insert(odi,i)
                odi+=2
        return l