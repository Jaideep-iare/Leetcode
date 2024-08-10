class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort()
        for i in range(len(intervals)):
            x1=intervals[i][0]
            y1=intervals[i][1]
            if ans and ans[-1][1]>=x1:
                ans[-1][1]=max(ans[-1][1], y1)
            
            else:
                ans.append([x1,y1])
        return ans