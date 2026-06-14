class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for num in nums:
            if num not in count_dict.keys():
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        out = sum([count > 1 for count in count_dict.values()]) > 0
        return out
        