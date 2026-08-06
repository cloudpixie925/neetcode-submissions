class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        return len(nums) != len(set(nums))


        # seen = {}
        # for i in range(len(nums)):
        #     if nums[i] in seen.values():
        #         return True
        #     else:
        #         seen[i] = nums[i]

        # return False
        


        


        