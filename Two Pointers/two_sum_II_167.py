from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            num1 = numbers[left]
            num2 = numbers[right]

            if num1 + num2 == target:
                return [left + 1, right + 1]
            elif num1 + num2 > target:
                right -= 1
            else:
                left += 1

if __name__ == "__main__":
    obj = Solution()

    # Example 1
    numbers1 = [2,7,11,15]
    target1 = 9
    result1 = obj.twoSum(numbers1, target1)
    print(result1)  # Expected: [1,2]

    # Example 2
    numbers2 = [2,3,4]
    target2 = 6
    result2 = obj.twoSum(numbers2, target2)
    print(result2)  # Expected: [1,3]

    # Example 3
    numbers3 = [-1,0]
    target3 = -1
    result3 = obj.twoSum(numbers3, target3)
    print(result3)  # Expected: [1,2]