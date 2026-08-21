from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        count = Counter(nums)
        ranked = count.most_common()

        for i in range(k):
            it = ranked[i][0]
            output.append(it)
        
        return output

            




        

        

        