from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False
    
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test Case 1: Expected output True (contains duplicate 1)
    test1 = [1, 2, 3, 1]
    result1 = solution.containsDuplicate(test1)
    print(f"Test 1 {test1} -> Result: {result1}")
    
    # Test Case 2: Expected output False (all unique elements)
    test2 = [1, 2, 3, 4]
    result2 = solution.containsDuplicate(test2)
    print(f"Test 2 {test2} -> Result: {result2}")
    
    # Test Case 3: Expected output True (multiple duplicates)
    test3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result3 = solution.containsDuplicate(test3)
    print(f"Test 3 {test3} -> Result: {result3}")