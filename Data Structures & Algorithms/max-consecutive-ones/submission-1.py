class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        con_range = []
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
                con_range.append(count)
            else:
                count = 0
        max = 0
        for num in con_range:
            if num > max:
                max = num
        return max

        