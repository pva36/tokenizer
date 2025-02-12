SUPPORTED_LANGS = ["fr", "en"]
FRENCH_SKIP = [
    ":",
    ".",
    '"',
    ",",
    "_",
    "\n",
    "\t",
    ";",
    "«",
    "»",
    "“",
    "”",
    "?",
    "!",
    "--",
    "(",
    ")",
]


def get_chars_to_skip(language: str) -> list[str]:
    """
    Returns an array of strings, each one containing the characters to skip
    while tokenizing the file. Accepted inputs are: 'fr'. Anything else will
    raise an Exception.
    """
    # TODO: define ACCEPTED_INPUT programmatically
    ACCEPTED_INPUT: str = "fr"
    match (language):
        case "fr":
            return FRENCH_SKIP
        case _:
            raise Exception(
                "function get_chars_to_skip() only accepts"
                + f"{ACCEPTED_INPUT} as input"
            )
