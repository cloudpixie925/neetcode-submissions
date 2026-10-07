class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maximum = 0
        while i < j:
            amount = (j-i) * min(heights[i], heights[j])
            if min(heights[i], heights[j]) == heights[i]:
                i += 1
            else:
                j -= 1
            if amount > maximum:
                maximum = amount
        return maximum
