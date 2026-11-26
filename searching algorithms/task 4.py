def linear_search(book_ids, target):
    """Return (index, comparisons) using Linear Search."""
    comparisons = 0

    for index, book_id in enumerate(book_ids):
        comparisons += 1
        if book_id == target:
            return index, comparisons

    return -1, comparisons


def binary_search(book_ids, target):
    """Return (index, comparisons) using Binary Search on a sorted list."""
    left = 0
    right = len(book_ids) - 1
    comparisons = 0

    while left <= right:
        middle = (left + right) // 2
        comparisons += 1

        if book_ids[middle] == target:
            return middle, comparisons
        if book_ids[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1, comparisons


book_ids_unsorted = [840, 210, 530, 120, 760, 450, 680]
book_ids_sorted = sorted(book_ids_unsorted)

for target in [530, 999]:
    linear_index, linear_comparisons = linear_search(book_ids_unsorted, target)
    binary_index, binary_comparisons = binary_search(book_ids_sorted, target)

    print(f"\nBook ID: {target}")
    print(f"Linear Search: index={linear_index}, comparisons={linear_comparisons}")
    print(f"Binary Search: index={binary_index}, comparisons={binary_comparisons}")

print("""
For a large collection that is already sorted, Binary Search is usually
more suitable: it takes O(log n) time, compared with Linear Search's O(n).
Binary Search requires sorted IDs; Linear Search works in any order.
""")