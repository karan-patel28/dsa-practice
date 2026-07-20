class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}

        if len(s) != len(t): return False

        for i in s:
            first[i] = first.get(i, 0) + 1
        for i in t:
            second[i] = second.get(i, 0) + 1

        for i in s:
            if first.get(i) != second.get(i):
                return False
        
        return True


if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    sol = Solution()

    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "ab", False),
        ("aacc", "ccac", False),
    ]

    for i, (s, t, expected) in enumerate(test_cases, 1):
        result = sol.isAnagram(s, t)
        passed = result == expected
        status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: isAnagram({s!r}, {t!r}) -> {result} (expected {expected}) [{status}]")