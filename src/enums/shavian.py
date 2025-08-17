from enum import Enum, StrEnum, auto


# https://www.unicode.org/charts/PDF/U10450.pdf
class ShavianUnicode(StrEnum):
	"""Enum for Shavian characters represented by their Unicode codepoints."""

	# Tall
	PEEP = "U+10450"
	TOT = "U+10451"
	KICK = "U+10452"
	FEE = "U+10453"
	THIGH = "U+10454"
	SO = "U+10455"
	SURE = "U+10456"
	CHURCH = "U+10457"
	YEA = "U+10458"
	HUNG = "U+10459"

	# Deep
	BIB = "U+1054A"
	DEAD = "U+1045B"
	GAG = "U+1045C"
	VOW = "U+1045D"
	THEY = "U+1045E"
	ZOO = "U+1045F"
	MEASURE = "U+10460"
	JUDGE = "U+10461"
	WOE = "U+10462"
	HAHA = "U+10463"

	# Short
	LOLL = "U+10464"
	MIME = "U+10465"
	IF = "U+10466"
	EGG = "U+10467"
	ASH = "U+10468"
	ADO = "U+10469"
	ON = "U+1046A"
	WOOL = "U+1046B"
	OUT = "U+1046C"
	AH = "U+1046D"
	ROAR = "U+1046E"
	NUN = "U+1046F"
	EAT = "U+10470"
	AGE = "U+10471"
	ICE = "U+10472"
	UP = "U+10473"
	OAK = "U+10474"
	OOZE = "U+10475"
	OIL = "U+10476"
	AWE = "U+10477"

	# Compound
	ARE = "U+10478"
	OR = "U+10479"
	AIR = "U+1047A"
	ERR = "U+1047B"
	ARRAY = "U+1047C"
	EAR = "U+1047D"
	IAN = "U+1047E"
	YEW = "U+1047F"

	# Namer
	NAMER = "U+00B7"


# https://shavian.info/alphabet/
class ShavianPronunciation(StrEnum):
	"""Enum for Shavian characters represented by their IPA pronunciations."""

	# Tall
	PEEP = "/p/"
	TOT = "/t/"
	KICK = "/k/"
	FEE = "/f/"
	THIGH = "/θ/"
	SO = "/s/"
	SURE = "/ʃ/"
	CHURCH = "/ʧ/"
	YEA = "/j/"
	HUNG = "/ŋ/"

	# Deep
	BIB = "/b/"
	DEAD = "/d/"
	GAG = "/ɡ/"  # noqa: RUF001
	VOW = "/v/"
	THEY = "/ð/"
	ZOO = "	/z/"
	MEASURE = "/ʒ/"
	JUDGE = "/ʤ/"
	WOE = "/w/"
	HAHA = "/h/"

	# Short
	LOLL = "/l/"
	MIME = "/m/"
	IF = "/ɪ/~/i/"  # noqa: RUF001
	EGG = "/ɛ/"
	ASH = "/æ/"
	ADO = "/ə/"
	ON = "/ɒ/"
	WOOL = "/ʊ/"
	OUT = "/aʊ/"
	AH = "/ɑː/"  # noqa: RUF001
	ROAR = "/r/"
	NUN = "/n/"
	EAT = "/iː/"  # noqa: RUF001
	AGE = "/eɪ/"  # noqa: RUF001
	ICE = "/aɪ/"  # noqa: RUF001
	UP = "/ʌ/"
	OAK = "/əʊ/"
	OOZE = "/u(ː)/"  # noqa: RUF001
	OIL = "/ɔɪ/"
	AWE = "/ɔː/"

	# Compound
	ARE = "/ɑː(r)/"  # noqa: RUF001
	OR = "/ɔː(r)/"
	AIR = "/ɛə(r)/"
	ERR = "/ɜː(r)/"
	ARRAY = "/ə(r)/"
	EAR = "/ɪə(r)/"
	IAN = "/ɪə/"
	YEW = "/ju(ː)/"  # noqa: RUF001

	# Namer
	NAMER = ""


class Shavian(Enum):
	"""Enum for Shavian characters with unicode and pronunciation properties."""

	# Tall
	PEEP = auto()
	TOT = auto()
	KICK = auto()
	FEE = auto()
	THIGH = auto()
	SO = auto()
	SURE = auto()
	CHURCH = auto()
	YEA = auto()
	HUNG = auto()

	# Deep
	BIB = auto()
	DEAD = auto()
	GAG = auto()
	VOW = auto()
	THEY = auto()
	ZOO = auto()
	MEASURE = auto()
	JUDGE = auto()
	WOE = auto()
	HAHA = auto()

	# Short
	LOLL = auto()
	MIME = auto()
	IF = auto()
	EGG = auto()
	ASH = auto()
	ADO = auto()
	ON = auto()
	WOOL = auto()
	OUT = auto()
	AH = auto()
	ROAR = auto()
	NUN = auto()
	EAT = auto()
	AGE = auto()
	ICE = auto()
	UP = auto()
	OAK = auto()
	OOZE = auto()
	OIL = auto()
	AWE = auto()

	# Compound
	ARE = auto()
	OR = auto()
	AIR = auto()
	ERR = auto()
	ARRAY = auto()
	EAR = auto()
	IAN = auto()
	YEW = auto()

	# Namer
	NAMER = auto()

	# Empty
	EMPTY = auto()

	@property
	def unicode(self) -> str:
		"""Get the Unicode codepoint for the Shavian character."""
		return ShavianUnicode[self.name].value if self.name != "EMPTY" else ""

	@property
	def pronunciation(self) -> str:
		"""Get the IPA pronunciation for the Shavian character."""
		return ShavianPronunciation[self.name].value if self.name != "EMPTY" else ""

	@classmethod
	def from_pronunciation(cls, pronunciation: str, *, raise_errors: bool = True) -> "Shavian":
		"""
		Get a Shavian character by its pronunciation.

		Args:
			pronunciation: The IPA pronunciation of the Shavian character.
			raise_errors: Whether to raise an error if no match is found.

		Raises:
			ValueError: If no Shavian character matches the given pronunciation.

		Returns:
			Shavian: The Shavian character that matches the pronunciation.
		"""
		for char in cls:
			if char.pronunciation == pronunciation or char.pronunciation.replace("/", "") == pronunciation:
				return char

		if raise_errors:
			raise ValueError(f"No Shavian character found for pronunciation: {pronunciation}")

		return Shavian.EMPTY

	@classmethod
	def from_unicode(cls, unicode_str: str, *, raise_errors: bool = True) -> "Shavian":
		"""
		Get a Shavian character by its Unicode codepoint.

		Args:
			unicode_str: The Unicode codepoint of the Shavian character.
			raise_errors: Whether to raise an error if no match is found.

		Raises:
			ValueError: If no Shavian character matches the given Unicode codepoint.

		Returns:
			Shavian: The Shavian character that matches the Unicode codepoint.
		"""
		for char in cls:
			if char.unicode == unicode_str:
				return char

		if raise_errors:
			raise ValueError(f"No Shavian character found for unicode: {unicode_str}")

		return Shavian.EMPTY
