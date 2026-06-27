class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n = len(s)

        # If no alpha exists, then return true
        if sum([char.isalnum() for char in s]) == 0:
            return True

        # Sandwich two pointers method
        pointer1 = 0
        pointer2 = n-1
        
        while pointer1 < pointer2:

            # If non alpha character found, continue until first alpha is found
            while not s[pointer1].isalnum():
                pointer1 += 1
            while not s[pointer2].isalnum():
                pointer2 -= 1
            
            # Check for case when middle characters are not alpha, so the pointers overlap
            if pointer1 > pointer2:
                break

            if s[pointer1].lower() != s[pointer2].lower():
                return False

            pointer1 += 1
            pointer2 -= 1
        
        return True
        