from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Expected [1, 2, 1, 1, 2, 1]
    test1 = [1, 2, 1]
    res1 = sol.getConcatenation(test1)
    print(f"Test 1 Input:  {test1}")
    print(f"Test 1 Output: {res1}\n")
    
    # Test Case 2: Expected [1, 3, 2, 1, 1, 3, 2, 1]
    test2 = [1, 3, 2, 1]
    res2 = sol.getConcatenation(test2)
    print(f"Test 2 Input:  {test2}")
    print(f"Test 2 Output: {res2}")