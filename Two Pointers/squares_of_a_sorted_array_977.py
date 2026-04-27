from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
        
        return res

if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test1 = [-4, -1, 0, 3, 10]
    test2 = [-7, -3, 2, 3, 11]
    
    print(f"Input: {test1} -> Output: {sol.sortedSquares(test1)}")
    # Expected: [0, 1, 9, 16, 100]
    
    print(f"Input: {test2} -> Output: {sol.sortedSquares(test2)}")
    # Expected: [4, 9, 9, 49, 121]