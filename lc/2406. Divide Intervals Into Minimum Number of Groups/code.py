class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # start,end = [] ,[]
        # for l,r in intervals:
        #     start.append(l)
        #     end.append(r)
        
        # start.sort()
        # end.sort()
        # i,j,ans = 0,0,0
        # while i < len(intervals):
        #     if start[i] <= end[j]:
        #         i += 1
        #     else :
        #         j += 1
        #     ans = max(ans,i - j)
        # return ans

        min_heap = []
        intervals.sort()

        for start, end in intervals:
            if min_heap and min_heap[0] < start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
        
        return len(min_heap)

