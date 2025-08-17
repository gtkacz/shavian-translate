from enum import Enum, StrEnum


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
	"""Combined enum for Shavian characters with unicode and pronunciation properties."""

	def __init__(self, unicode_val: str, pronunciation_val: str) -> None:  # noqa: D107
		self.unicode = unicode_val
		self.pronunciation = pronunciation_val

	# Tall
	PEEP = (ShavianUnicode.PEEP, ShavianPronunciation.PEEP)
	TOT = (ShavianUnicode.TOT, ShavianPronunciation.TOT)
	KICK = (ShavianUnicode.KICK, ShavianPronunciation.KICK)
	FEE = (ShavianUnicode.FEE, ShavianPronunciation.FEE)
	THIGH = (ShavianUnicode.THIGH, ShavianPronunciation.THIGH)
	SO = (ShavianUnicode.SO, ShavianPronunciation.SO)
	SURE = (ShavianUnicode.SURE, ShavianPronunciation.SURE)
	CHURCH = (ShavianUnicode.CHURCH, ShavianPronunciation.CHURCH)
	YEA = (ShavianUnicode.YEA, ShavianPronunciation.YEA)
	HUNG = (ShavianUnicode.HUNG, ShavianPronunciation.HUNG)

	# Deep
	BIB = (ShavianUnicode.BIB, ShavianPronunciation.BIB)
	DEAD = (ShavianUnicode.DEAD, ShavianPronunciation.DEAD)
	GAG = (ShavianUnicode.GAG, ShavianPronunciation.GAG)
	VOW = (ShavianUnicode.VOW, ShavianPronunciation.VOW)
	THEY = (ShavianUnicode.THEY, ShavianPronunciation.THEY)
	ZOO = (ShavianUnicode.ZOO, ShavianPronunciation.ZOO)
	MEASURE = (ShavianUnicode.MEASURE, ShavianPronunciation.MEASURE)
	JUDGE = (ShavianUnicode.JUDGE, ShavianPronunciation.JUDGE)
	WOE = (ShavianUnicode.WOE, ShavianPronunciation.WOE)
	HAHA = (ShavianUnicode.HAHA, ShavianPronunciation.HAHA)

	# Short
	LOLL = (ShavianUnicode.LOLL, ShavianPronunciation.LOLL)
	MIME = (ShavianUnicode.MIME, ShavianPronunciation.MIME)
	IF = (ShavianUnicode.IF, ShavianPronunciation.IF)
	EGG = (ShavianUnicode.EGG, ShavianPronunciation.EGG)
	ASH = (ShavianUnicode.ASH, ShavianPronunciation.ASH)
	ADO = (ShavianUnicode.ADO, ShavianPronunciation.ADO)
	ON = (ShavianUnicode.ON, ShavianPronunciation.ON)
	WOOL = (ShavianUnicode.WOOL, ShavianPronunciation.WOOL)
	OUT = (ShavianUnicode.OUT, ShavianPronunciation.OUT)
	AH = (ShavianUnicode.AH, ShavianPronunciation.AH)
	ROAR = (ShavianUnicode.ROAR, ShavianPronunciation.ROAR)
	NUN = (ShavianUnicode.NUN, ShavianPronunciation.NUN)
	EAT = (ShavianUnicode.EAT, ShavianPronunciation.EAT)
	AGE = (ShavianUnicode.AGE, ShavianPronunciation.AGE)
	ICE = (ShavianUnicode.ICE, ShavianPronunciation.ICE)
	UP = (ShavianUnicode.UP, ShavianPronunciation.UP)
	OAK = (ShavianUnicode.OAK, ShavianPronunciation.OAK)
	OOZE = (ShavianUnicode.OOZE, ShavianPronunciation.OOZE)
	OIL = (ShavianUnicode.OIL, ShavianPronunciation.OIL)
	AWE = (ShavianUnicode.AWE, ShavianPronunciation.AWE)

	# Compound
	ARE = (ShavianUnicode.ARE, ShavianPronunciation.ARE)
	OR = (ShavianUnicode.OR, ShavianPronunciation.OR)
	AIR = (ShavianUnicode.AIR, ShavianPronunciation.AIR)
	ERR = (ShavianUnicode.ERR, ShavianPronunciation.ERR)
	ARRAY = (ShavianUnicode.ARRAY, ShavianPronunciation.ARRAY)
	EAR = (ShavianUnicode.EAR, ShavianPronunciation.EAR)
	IAN = (ShavianUnicode.IAN, ShavianPronunciation.IAN)
	YEW = (ShavianUnicode.YEW, ShavianPronunciation.YEW)

	# Namer
	NAMER = (ShavianUnicode.NAMER, ShavianPronunciation.NAMER)
