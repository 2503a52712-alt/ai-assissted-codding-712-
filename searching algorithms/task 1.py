def linear_search(arr, target):
    """Return the index of target, or -1 if absent.

    Time complexity:
    Best case:    O(1) — target is the first element.
    Average case: O(n)
    Worst case:   O(n) — target is last or absent.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


test_cases = [
    ([10, 20, 30, 40], 30),
    ([10, 20, 30, 40], 99),
    ([], 10),
]

for values, target in test_cases:
    print(f"List: {values}, target: {target}, index: {linear_search(values, target)}")