class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)

        # Hashmap of frequency : list[int]
        from collections import defaultdict
        default = defaultdict(list)
        
        # Counter
        counter = {}
        n = len(nums)
        for i in range(n):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
        
        # Add from counter into the frequency hashmap
        for key in counter:
            count = counter[key]
            default[count].append(key)
        
        # Get top k elements
        top_k = []
        for i in range(n, -1, -1):
            for char in default[i]:
                top_k.append(char)
                if len(top_k) == k:
                    return top_k

        