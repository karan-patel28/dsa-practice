class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        first = 0
        second = 0

        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1

        while first < len(word1) and second < len(word2):
            result += word1[first] + word2[second]
            first += 1
            second += 1

        if first < len(word1):
            result += word1[first:]
        else:
            result += word2[second:]

        return result


if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    sol = Solution()

    test_cases = [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
        ("a", "b", "ab"),
        ("", "abc", "abc"),
    ]

    for i, (word1, word2, expected) in enumerate(test_cases, 1):
        result = sol.mergeAlternately(word1, word2)
        passed = result == expected
        status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: mergeAlternately({word1!r}, {word2!r}) -> {result!r} (expected {expected!r}) [{status}]")