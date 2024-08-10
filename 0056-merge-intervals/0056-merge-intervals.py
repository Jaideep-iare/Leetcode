class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort()
        for i in range(len(intervals)):
            if ans and ans[-1][1]>intervals[i][1]:
                continue
            if ans and ans[-1][1]>=intervals[i][0]:
                ans[-1][1]=max(ans[-1][1], intervals[i][1])
            
            else:
                ans.append([intervals[i][0],intervals[i][1]])
        return ans