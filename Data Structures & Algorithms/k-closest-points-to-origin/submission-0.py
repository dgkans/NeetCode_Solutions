class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            dist_sq = x*x + y*y
            if len(heap) < k:
                heapq.heappush_max(heap, (dist_sq, point))
            else:
                if dist_sq < heap[0][0]:
                    heapq.heappop_max(heap)
                    heapq.heappush_max(heap, (dist_sq, point))
        result = []
        for vals in heap:
            a , b = vals
            result.append(b)
        return result