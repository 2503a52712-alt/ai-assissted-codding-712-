"""Task 3: Anagram Checker using TDD."""


# Tests are written first to describe the required behavior.
def test_is_anagram():
	assert is_anagram("listen", "silent") == True
	assert is_anagram("hello", "world") == False
	assert is_anagram("Dormitory", "Dirty Room") == True
	assert is_anagram("", "") == True  # Empty strings are anagrams.
	assert is_anagram("python", "python") == True  # Identical words match.
	assert is_anagram("A gentleman!", "Elegant man") == True  # Punctuation is ignored.


def is_anagram(str1, str2):
	"""Return True when two strings contain the same characters."""
	cleaned_str1 = ""
	cleaned_str2 = ""

	# Keep only letters and numbers, and make all letters lowercase.
	for character in str1:
		if character.isalnum():
			cleaned_str1 += character.lower()

	for character in str2:
		if character.isalnum():
			cleaned_str2 += character.lower()

	# Anagrams have the same characters in a different order or the same order.
	return sorted(cleaned_str1) == sorted(cleaned_str2)


test_is_anagram()
print("All Task 3 tests passed!")
