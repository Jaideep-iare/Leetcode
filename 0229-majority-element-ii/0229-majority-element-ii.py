class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums)//3
        ans=[]
        c1=c2=0
        e1=e2=0
        for num in nums:
            if c1==0 and num!=e2:
                c1=1
                e1=num
            elif c2==0 and num!=e1:
                c2=1
                e2=num
            elif num==e1:
                c1+=1
            elif num==e2:
                c2+=1
            else:
                c1-=1
                c2-=1
        c1=c2=0
        for num in nums:
            if num==e1:
                c1+=1
            elif num==e2:
                c2+=1
        if c1>freq:
            ans.append(e1)
        if c2>freq:
            ans.append(e2)
        return ans