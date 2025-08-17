def unicode_to_bytes(codepoint_str: str, encoding: str = "utf-8") -> bytes:
	r"""
	Convert a unicode codepoint string to its byte representation.

	Args:
		codepoint_str: String representing a unicode codepoint
		encoding: The encoding to use for bytes conversion

	Raises:
		ValueError: If the codepoint string is invalid or out of range

	Returns:
		bytes: The unicode character encoded as bytes

	Examples:
		>>> unicode_to_bytes("10450")
		b'\xe2\xa3\x92'
		>>> unicode_to_bytes("0x1F600")  # 😀 emoji
		b'\xf0\x9f\x98\x80'
		>>> unicode_to_bytes("U+0041")  # Letter 'A'
		b'A'
	"""
	try:
		# Handle different input formats
		codepoint_str = codepoint_str.strip()

		# Remove common prefixes
		if (
			codepoint_str.upper().startswith("U+")
			or codepoint_str.upper().startswith("0X")
			or codepoint_str.upper().startswith("\\U")
		):
			codepoint_str = codepoint_str[2:]
			base = 16
		else:
			# Try to determine base automatically
			base = 16 if any(c in codepoint_str.upper() for c in "ABCDEF") else 10

		# Convert string to integer codepoint
		codepoint = int(codepoint_str, base)

		# Convert codepoint to character
		char = chr(codepoint)

		# Encode character to bytes
		return char.encode(encoding)

	except ValueError as e:
		raise ValueError(f"Invalid codepoint string: {codepoint_str}. Error: {e}") from e

	except OverflowError as e:
		raise ValueError(f"Codepoint {codepoint_str} is out of valid Unicode range") from e


def unicode_to_string(codepoint_str: str, encoding: str = "utf-8") -> str:
	r"""
	Convert a unicode codepoint string to its string representation.

	Args:
		codepoint_str: String representing a unicode codepoint
		encoding: The encoding to use for bytes conversion

	Returns:
		str: The unicode character represented as a string

	Examples:
		>>> unicode_to_string("U+10450")
		'𐑐'
		>>> unicode_to_string("0x1F600")
		'😀'
	"""
	return unicode_to_bytes(codepoint_str, encoding=encoding).decode(encoding)
