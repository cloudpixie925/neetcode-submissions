class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        output = []

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            while j < k:
                triplet = []
                if nums[j] + nums[k] == target:
                    triplet.append(nums[i])
                    triplet.append(nums[j])
                    triplet.append(nums[k])
                    if triplet not in output:
                        output.append(triplet)
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1

        return output