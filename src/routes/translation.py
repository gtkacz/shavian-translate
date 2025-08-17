from litestar import get

from src.util.translate import translate_ipa_to_shavian_str, translate_shavian_str_to_ipa


@get("/translate/ipa_to_shavian/{ipa:str}")
async def translate_ipa_to_shavian_endpoint(ipa: str) -> str:  # noqa: RUF029
	"""
	Endpoint to translate IPA to Shavian script.

	Args:
		ipa: The input IPA string to be translated.

	Returns:
		str: The translated text in Shavian script.
	"""
	return translate_ipa_to_shavian_str(ipa)


@get("/translate/shavian_to_ipa/{shavian:str}")
async def translate_shavian_str_to_ipa_endpoint(shavian: str) -> str:  # noqa: RUF029
	"""
	Endpoint to translate Shavian script to IPA.

	Args:
		shavian: The input Shavian text to be translated.

	Returns:
		str: The translated text in IPA pronunciation.
	"""
	return translate_shavian_str_to_ipa(shavian)
