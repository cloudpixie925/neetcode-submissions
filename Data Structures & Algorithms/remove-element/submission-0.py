class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) > 0:
            i = 0
            while i < len(nums):
                if nums[i] == val:
                    nums.pop(i)
                else:
                    i += 1
            k = 0
            for num in nums:
                k+=1
            return k
        else:
            k = 0
            return k