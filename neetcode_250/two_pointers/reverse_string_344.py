from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    sol = Solution()

    test_cases = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        (["a"], ["a"]),
        (["a", "b"], ["b", "a"]),
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        s_copy = s.copy()
        sol.reverseString(s_copy)
        passed = s_copy == expected
        status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: reverseString({s}) -> {s_copy} (expected {expected}) [{status}]")