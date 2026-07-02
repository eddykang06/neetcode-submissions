class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Keep a hashmap of {counter: list[str]}
        hashmap = defaultdict(list)

        for s in strs:

            # Character counter for each 
            counter = [0] * 26

            # Update counter
            for c in s:
                counter[ord(c) - ord("a")] += 1
            
            # Convert to tuple
            counter = tuple(counter)

            hashmap[counter].append(s)
        
        return list(hashmap.values())


        