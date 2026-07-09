

BANGLA_TO_ENGLISH = str.maketrans(
    "০১২৩৪৫৬৭৮৯",
    "0123456789"
)

ENGLISH_TO_BANGLA = str.maketrans(
    "0123456789",
    "০১২৩৪৫৬৭৮৯"
)


def bangla_to_english(value):
    if value is None:
        return value

    return str(value).translate(BANGLA_TO_ENGLISH)


def english_to_bangla(value):
    if value is None:
        return ""

    return str(value).translate(ENGLISH_TO_BANGLA)