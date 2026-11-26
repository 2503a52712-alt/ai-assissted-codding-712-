def linear_search(records, roll_number):
    """Search records in any order; return the matching record or None. O(n)."""
    for record in records:
        if record["roll_number"] == roll_number:
            return record
    return None


def binary_search(records, roll_number):
    """Search records sorted by roll_number; return the record or None. O(log n)."""
    left = 0
    right = len(records) - 1

    while left <= right:
        middle = (left + right) // 2
        current_roll = records[middle]["roll_number"]

        if current_roll == roll_number:
            return records[middle]
        if current_roll < roll_number:
            left = middle + 1
        else:
            right = middle - 1

    return None


unsorted_records = [
    {"roll_number": 104, "name": "Mina", "marks": 86},
    {"roll_number": 101, "name": "Arun", "marks": 91},
    {"roll_number": 103, "name": "Leela", "marks": 78},
    {"roll_number": 102, "name": "Dev", "marks": 88},
]

sorted_records = sorted(unsorted_records, key=lambda record: record["roll_number"])
target_roll = 103

print("Linear search in unsorted records:")
print(linear_search(unsorted_records, target_roll))

print("\nBinary search in sorted records:")
print(binary_search(sorted_records, target_roll))

print("\nSearch for missing roll number:")
print("Linear:", linear_search(unsorted_records, 999))
print("Binary:", binary_search(sorted_records, 999))

print("""
Comparison:
Algorithm       Input requirement       Best       Average    Worst
Linear Search   Any order               O(1)       O(n)       O(n)
Binary Search   Must be sorted           O(1)       O(log n)   O(log n)

Use Linear Search when records are unsorted or the collection is small.
Use Binary Search when records are sorted and searches happen frequently.
""")