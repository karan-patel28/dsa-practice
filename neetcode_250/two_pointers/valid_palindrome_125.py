class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        lower_s = s.lower()
        while left < right:
            if not lower_s[left].isalnum():
                left += 1
                continue
            elif not lower_s[right].isalnum():
                right -= 1
                continue

            if lower_s[left] != lower_s[right]:
                return False

            left += 1
            right -= 1

        return True

if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    sol = Solution()

    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("a.", True),
        ("", True),
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        result = sol.isPalindrome(s)
        passed = result == expected
        status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: isPalindrome({s!r}) -> {result} (expected {expected}) [{status}]")