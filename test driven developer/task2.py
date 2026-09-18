"""Task 2: Number Classification using TDD."""


# Tests are written first to describe the required behavior.
def test_classify_number():
	assert classify_number(10) == "Positive"
	assert classify_number(-5) == "Negative"
	assert classify_number(0) == "Zero"
	assert classify_number(1) == "Positive"  # Positive boundary value.
	assert classify_number(-1) == "Negative"  # Negative boundary value.
	assert classify_number("10") == "Invalid"
	assert classify_number(None) == "Invalid"


def classify_number(n):
	"""Return whether n is positive, negative, zero, or invalid."""
	if isinstance(n, bool):
		return "Invalid"

	# Use a loop to check whether the input is one of the accepted number types.
	is_number = False
	for number_type in (int, float):
		if isinstance(n, number_type):
			is_number = True

	if not is_number:
		return "Invalid"

	if n > 0:
		return "Positive"
	if n < 0:
		return "Negative"
	return "Zero"


test_classify_number()
print("All Task 2 tests passed!")
