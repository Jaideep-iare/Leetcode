class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[[intervals[0][0],intervals[0][1]]]
        for i in range(1,len(intervals)):
            if ans[-1][1]>intervals[i][1]:
                continue
            if ans[-1][1]>=intervals[i][0]:
                ans[-1][1]=max(ans[-1][1], intervals[i][1])
            
            else:
                ans.append([intervals[i][0],intervals[i][1]])
        return ans