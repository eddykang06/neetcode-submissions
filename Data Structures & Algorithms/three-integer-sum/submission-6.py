class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        triplets = []

        # Sort first 
        nums = sorted(nums)

        # Use two pointers on postfix 
        for i in range(n):
            
            # If positive position, break
            if nums[i] > 0:
                break
            
            # Check that we are not repeating values already seen
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Two pointers
            left = i + 1
            right = n - 1
            target = -nums[i]

            # Two pointers
            while left < right:

                curr_sum = nums[left] + nums[right]

                if curr_sum == target:
                    triplet = [nums[i], nums[left], nums[right]]
                    triplets.append(triplet)

                    # Shift pointer until nonunique value found
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    
                elif curr_sum > target:
                    right -= 1

                else:
                    left += 1
        
        return triplets
            
            







        # Hashmap to store sum: indices
        # int : list[list[int]]
        from collections import defaultdict
        sums = defaultdict(list)

        # Iterate through to get sums
        for i in range(n):
            for j in range(i+1, n):
                sums[nums[i] + nums[j]].append([i, j])

        # Find all triplets
        for i in range(n):
            diff = 0 - i
            for jk_idx in sums[diff]:
                if i not in jk_idx:
                    triplets.append([nums[i]] + [nums[x] for x in jk_idx])

        return nums