from collections import deque


class MyStack:
    def __init__(self):
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def top(self) -> int:
        pass

    def empty(self) -> bool:
        pass


if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    # each test case is a list of (operation, args, expected_return)
    # expected_return is None for operations that don't return a checkable value (like push, init)
    test_cases = [
        [
            ("push", [1], None),
            ("push", [2], None),
            ("top", [], 2),
            ("pop", [], 2),
            ("empty", [], False),
        ],
        [
            ("push", [1], None),
            ("push", [2], None),
            ("push", [3], None),
            ("pop", [], 3),
            ("pop", [], 2),
            ("top", [], 1),
            ("empty", [], False),
            ("pop", [], 1),
            ("empty", [], True),
        ],
    ]

    for i, ops in enumerate(test_cases, 1):
        stack = MyStack()
        all_passed = True
        results = []

        for op, args, expected in ops:
            method = getattr(stack, op)
            result = method(*args)
            if expected is not None:
                passed = result == expected
                if not passed:
                    all_passed = False
                results.append(f"{op}({', '.join(map(str, args))}) -> {result} (expected {expected})")
            else:
                results.append(f"{op}({', '.join(map(str, args))})")

        status = f"{GREEN}PASS{RESET}" if all_passed else f"{RED}FAIL{RESET}"
        print(f"Test {i}: [{status}]")
        for r in results:
            print(f"  {r}")