class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        
        # This works but I just prefer using a hash set
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False


        # I liked it but it is not efficient enough
        # seen = {}
        # for i in range(len(nums)):
        #     if nums[i] in seen.values():
        #         return True
        #     else:
        #         seen[i] = nums[i]

        # return False
        


        


        
