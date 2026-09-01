class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mult = 1
        right_mult = 1
        n= len(nums)
        left = [0] * n
        right = [0] * n
        output = [0] * n
        for i in range(n):
            j = -i - 1
            left[i] = left_mult
            right[j] = right_mult
            left_mult *= nums[i]
            right_mult *= nums[j] 

        for i in range(n):       
            output[i] = left[i] * right [i]            
        return output
            


            
        

        

            


            

        