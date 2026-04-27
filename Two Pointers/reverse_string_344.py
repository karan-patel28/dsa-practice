from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1

        print(s)
        

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard string
    word1 = ["h", "e", "l", "l", "o"]
    sol.reverseString(word1)
    print(f"Result 1: {word1}")  # Expected: ["o", "l", "l", "e", "h"]
    
    # Test Case 2: Palindrome-like string
    word2 = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(word2)
    print(f"Result 2: {word2}")  # Expected: ["h", "a", "n", "n", "a", "H"]