from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            l = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, l * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
if __name__ == "__main__":
    obj = Solution()

    # Example 1
    height1 = [1,8,6,2,5,4,8,3,7]
    result1 = obj.maxArea(height1)
    print(result1)  # Expected: 49

    # Example 2
    height2 = [1,1]
    result2 = obj.maxArea(height2)
    print(result2)  # Expected: 1