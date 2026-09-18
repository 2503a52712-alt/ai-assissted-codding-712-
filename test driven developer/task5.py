"""Task 5: Date Validation and Formatting using TDD."""

from datetime import datetime


# Tests are written first to describe the required behavior.
def test_validate_and_format_date():
	assert validate_and_format_date("10/15/2023") == "2023-10-15"
	assert validate_and_format_date("02/30/2023") == "Invalid Date"
	assert validate_and_format_date("01/01/2024") == "2024-01-01"
	assert validate_and_format_date("02/29/2024") == "2024-02-29"  # Leap year.
	assert validate_and_format_date("13/15/2023") == "Invalid Date"  # Invalid month.
	assert validate_and_format_date("04/31/2023") == "Invalid Date"  # Invalid day.
	assert validate_and_format_date("2023-10-15") == "Invalid Date"  # Wrong format.


def validate_and_format_date(date_str):
	"""Return a valid date in YYYY-MM-DD format, or an error message."""
	# Check that the input has the exact MM/DD/YYYY shape.
	if (
		len(date_str) != 10
		or date_str[2] != "/"
		or date_str[5] != "/"
		or not date_str[:2].isdigit()
		or not date_str[3:5].isdigit()
		or not date_str[6:].isdigit()
	):
		return "Invalid Date"

	try:
		# datetime checks that the month, day, and year are real calendar values.
		date = datetime.strptime(date_str, "%m/%d/%Y")
		return date.strftime("%Y-%m-%d")
	except ValueError:
		return "Invalid Date"


test_validate_and_format_date()
print("All Task 5 tests passed!")
