class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Two pointers
        n = len(numbers)
        left = 0
        right = n-1

        while left < right:

            # Compute temporary sum
            temp_sum = numbers[left] + numbers[right]
            if temp_sum == target:
                return [left + 1, right + 1]

            if temp_sum > target:
                right -= 1
            else:
                left += 1

