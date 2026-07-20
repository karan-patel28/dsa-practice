class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if len(stack) == 0:
                stack.append(i)
                continue
            
            if i == ")":
                if stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif i == "}":
                if stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            elif i == "]":
                if stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0


if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    sol = Solution()

    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(((", False),
        (")))", False),
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        result = sol.isValid(s)
        passed = result == expected
        status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: isValid({s!r}) -> {result} (expected {expected}) [{status}]")