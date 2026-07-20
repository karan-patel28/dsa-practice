from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in seen:
                return [seen.get(rem), i]
            seen[nums[i]] = i

        return None


if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    sol = Solution()

    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ]

    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = sol.twoSum(nums, target)
        # order of indices might differ, so compare as sets
        passed = result is not None and set(result) == set(expected)
        status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: twoSum({nums}, {target}) -> {result} (expected {expected}) [{status}]")