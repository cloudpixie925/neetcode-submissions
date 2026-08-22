class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        deduplicated = list(set(nums))
        sim_nums = sorted(deduplicated)
        

        if len(sim_nums) == 0:
            return 0
        elif len(sim_nums) == 1:
            return 1
        else:
            count = 1
            maximum = []

            for i in range(len(sim_nums)-1):
                if sim_nums[i+1] == sim_nums[i]+1:
                    count+=1
                    maximum.append(count)            
                else:
                    count = 1
                    maximum.append(count)
            return max(maximum)



            


        