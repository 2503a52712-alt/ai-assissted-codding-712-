"""Task 1: Password Strength Validator using TDD."""


# Tests are written first to describe the required behavior.
def test_is_strong_password():
	assert is_strong_password("Abcd@123") == True
	assert is_strong_password("abcd123") == False
	assert is_strong_password("ABCD@1234") == False
	assert is_strong_password("Abcd @123") == False  # Spaces are not allowed.
	assert is_strong_password("Abcd@123!") == True  # More than one special character is valid.


def is_strong_password(password):
	"""Return True when password meets all strength requirements."""
	if len(password) < 8 or " " in password:
		return False

	has_uppercase = False
	has_lowercase = False
	has_digit = False
	has_special = False

	# Check each character for the required character types.
	for character in password:
		if character.isupper():
			has_uppercase = True
		elif character.islower():
			has_lowercase = True
		elif character.isdigit():
			has_digit = True
		else:
			has_special = True

	return has_uppercase and has_lowercase and has_digit and has_special


test_is_strong_password()
print("All Task 1 tests passed!")
