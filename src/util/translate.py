from collections.abc import Sequence

from ipapy import is_valid_ipa

from src.enums.shavian import Shavian
from src.util.unicode import unicode_to_string


def translate_ipa_to_shavian(text: str) -> Sequence[Shavian]:
	"""
	Translate a given IPA pronunciation to Shavian script.

	Args:
		text: The input IPA to be translated.

	Raises:
		ValueError: If the input text is not a valid IPA.

	Returns:
		Sequence[Shavian]: The translated text in Shavian script.
	"""
	if not is_valid_ipa(text):
		raise ValueError(f"Invalid IPA input: {text}")

	raw_output = [Shavian.from_pronunciation(char, raise_errors=False) for char in text]

	if not raw_output:
		raise ValueError(f"Could not translate IPA to Shavian: {text}")

	return raw_output


def translate_shavian_to_ipa(text: Sequence[Shavian]) -> str:
	"""
	Translate a given Shavian text to its IPA pronunciation.

	Args:
		text: The input Shavian text to be translated.

	Raises:
		ValueError: If the input text cannot be translated.

	Returns:
		str: The translated text in IPA pronunciation.
	"""
	raw_output = [char.pronunciation for char in text]

	if not raw_output:
		raise ValueError(f"Could not translate Shavian to IPA: {text}")

	return "".join(raw_output)


def translate_ipa_to_shavian_str(text: str) -> str:
	"""
	Translate a given IPA pronunciation to Shavian script.

	Args:
		text: The input IPA to be translated.

	Returns:
		str: The translated text in Shavian script.
	"""
	raw_output = translate_ipa_to_shavian(text)

	output = [unicode_to_string(char.unicode) for char in raw_output if char]

	return "".join(output)


def translate_shavian_str_to_ipa(text: str) -> str:
	"""
	Translate a given Shavian text to its IPA pronunciation.

	Args:
		text: The input Shavian text to be translated.

	Raises:
		ValueError: If the input text cannot be translated.

	Returns:
		str: The translated text in IPA pronunciation.
	"""
	raw_output = [Shavian.from_unicode(char, raise_errors=False).pronunciation for char in text]

	if not raw_output:
		raise ValueError(f"Could not translate Shavian to IPA: {text}")

	output = [unicode_to_string(char) for char in raw_output if char]

	return "".join(output)
