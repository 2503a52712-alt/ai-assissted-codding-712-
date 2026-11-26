from time import perf_counter


def linear_search(items, target):
    """Return (index, comparisons). Time complexity: O(n)."""
    comparisons = 0

    for index, item in enumerate(items):
        comparisons += 1
        if item == target:
            return index, comparisons

    return -1, comparisons


def binary_search(items, target):
    """Return (index, comparisons). Requires sorted input; time: O(log n)."""
    left = 0
    right = len(items) - 1
    comparisons = 0

    while left <= right:
        middle = (left + right) // 2
        comparisons += 1

        if items[middle] == target:
            return middle, comparisons
        if items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1, comparisons


def timed_search(search_function, items, target, repetitions=100):
    """Return the search result and average elapsed time in milliseconds."""
    result = search_function(items, target)

    start = perf_counter()
    for _ in range(repetitions):
        search_function(items, target)
    elapsed = (perf_counter() - start) / repetitions

    return result, elapsed * 1000


print(
    f"{'Size':>8} {'Target case':>12} {'Algorithm':>10} "
    f"{'Index':>8} {'Comparisons':>12} {'Time (ms)':>12}"
)

for size in [1_000, 10_000, 100_000]:
    product_ids = list(range(1, size + 1))
    targets = [
        ("first", product_ids[0]),
        ("middle", product_ids[size // 2]),
        ("last", product_ids[-1]),
        ("missing", size + 1),
    ]

    for case_name, target in targets:
        for search_name, search_function in [
            ("Linear", linear_search),
            ("Binary", binary_search),
        ]:
            (index, comparisons), elapsed_ms = timed_search(
                search_function, product_ids, target
            )
            print(
                f"{size:>8} {case_name:>12} {search_name:>10} "
                f"{index:>8} {comparisons:>12} {elapsed_ms:>12.6f}"
            )

print("""
Conclusion:
For sorted product IDs and frequent lookups, Binary Search is appropriate:
its search time grows as O(log n), while Linear Search grows as O(n).
Linear Search works on unsorted data and may be preferable for small lists.
Binary Search requires sorted data; sorting also takes time if the data is
not already ordered. For frequently changing collections, maintaining that
sorted order has a cost.
""")