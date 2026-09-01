class MyHashMap:
    def __init__(self):
        pass

    def put(self, key: int, value: int) -> None:
        pass

    def get(self, key: int) -> int:
        pass

    def remove(self, key: int) -> None:
        pass


if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    # each test case is a list of (operation, args, expected_return)
    # expected_return is None for operations that don't return a checkable value (like put, remove, init)
    test_cases = [
        [
            ("put", [1, 1], None),
            ("put", [2, 2], None),
            ("get", [1], 1),
            ("get", [3], -1),
            ("put", [2, 1], None),
            ("get", [2], 1),
            ("remove", [2], None),
            ("get", [2], -1),
        ],
    ]

    for i, ops in enumerate(test_cases, 1):
        hm = MyHashMap()
        all_passed = True
        results = []

        for op, args, expected in ops:
            method = getattr(hm, op)
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