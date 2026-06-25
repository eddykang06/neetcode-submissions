class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        out = [1] * n

        # Initialize products
        prod1 = 1
        prod2 = 1

        # Prefix update
        for i in range(n):
            
            # Update cumprod
            out[i] = prod1
            prod1 *= nums[i]

        # Suffix update
        for j in range(n-1, -1, -1):

            # update cumprod
            out[j] *= prod2
            prod2 *= nums[j]

        return out
        

        