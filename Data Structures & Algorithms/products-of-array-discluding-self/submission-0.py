class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = []
        for i in range(n):
            product = 1
            for j in list(range(0, i)) + list(range(i+1, n)):
                product = product * nums[j]
            out.append(product)
        return out
        

        