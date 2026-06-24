class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Store hashset 
        hashset = set(nums)

        # Store lengths
        lengths = []

        # Edge case (empty or 1 element)
        if len(nums) < 2:
            return len(nums)

        for n in nums:

            # n starts a sequence only if n-1 not in hashset
            if n-1 not in hashset:

                length = 0

                for i in range(len(nums)):
                    if n + i in hashset:
                        length += 1
                    else:
                        break
                lengths.append(length)
        
        return max(lengths)



        