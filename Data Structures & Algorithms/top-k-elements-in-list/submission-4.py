from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # output = []
        # count = Counter(nums)
        # ranked = count.most_common()

        # for i in range(k):
        #     it = ranked[i][0]
        #     output.append(it)
        
        # return output

        # heap = []
        # counter = Counter(nums)
        # heap = []
        # output = []

        # for key, v in counter.items():
        #     heapq.heappush(heap, (v, key))

        #     if len(heap) > k:
        #         heapq.heappop(heap)
                            
        # for i in range(k):
        #     output.append(heapq.heappop(heap)[1])

        # return output

        counter = Counter(nums)
        heap = []
        output = []
        for key, v in counter.items():
            heapq.heappush(heap, (-v, key))

        for i in range(k):
            v, k = heapq.heappop(heap)
            output.append(k)

        return output

            

            




        

        

        