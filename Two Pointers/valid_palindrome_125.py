class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(c for c in s if c.isalnum()).lower()
        
        left = 0
        right = len(cleaned_s) - 1

        while left < right:
            if cleaned_s[left] != cleaned_s[right]:
                return False

            left += 1
            right -= 1

        return True

if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " "
    ]
    
    for s in test_cases:
        result = sol.isPalindrome(s)
        print(f"Input: '{s}' -> Result: {result}")
