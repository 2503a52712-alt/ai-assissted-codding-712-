def binary_search(arr, target):
    """Return the index of target in a sorted list, or -1 if absent.

    The list must be sorted because each comparison determines which half
    may contain the target; that decision is not valid for an unsorted list.

    Time complexity:
    Best case:    O(1)
    Average case: O(log n)
    Worst case:   O(log n)
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle
        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


numbers = [5, 12, 18, 23, 31, 42, 57]
for target in [5, 57, 23, 100]:
    print(f"Target: {target}, index: {binary_search(numbers, target)}")