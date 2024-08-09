class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #optimal
        n=len(nums)
        nums.sort()
        ans=[]
        for i in range(n):
            if nums[i]>0:
                break
            elif i!=0 and nums[i]==nums[i-1]:
                    continue
            j=i+1
            k=n-1
            while j<k:              
                s=nums[i]+nums[j]+nums[k]
                if s>0:                   
                    k-=1
                elif s<0:
                    j+=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    k-=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                    
        return ans
#         #better but time limit exceed
#         h=set()
#         for i in range(len(nums)):
#             s=set()
#             for j in range(i+1,len(nums)):
#                 comp=-(nums[i]+nums[j])
#                 if comp in s:
#                     temp = [nums[i],nums[j],comp]
#                     temp.sort()
#                     h.add(tuple(temp))
#                 s.add(nums[j])
        
#         return list(h)
                