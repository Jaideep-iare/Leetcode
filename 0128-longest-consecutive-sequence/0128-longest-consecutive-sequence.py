class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)   
        longest = 0
        for i in s:
            if i-1 not in s:
                j=i+1
                count = 1
                while j in s:
                    count +=1
                    j+=1
                longest = max(longest, count)
        return longest