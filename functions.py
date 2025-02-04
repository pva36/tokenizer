from constants import SUPPORTED_LANGS


def get_language(language: str) -> str:
    """
    Return a string representing one of the languages supported by the
    program (defined in constants.SUPPORTED_LANGS). If the user's argument
    isn't valid, raise an exception.
    """
    # TODO: add custom exception
    if language.strip().lower() not in SUPPORTED_LANGS:
        exception_message = (
            "Valid arguments for the --language (-l) flag are: "
        )
        for string in SUPPORTED_LANGS:
            exception_message += f"'{string}' "
        raise Exception(exception_message)
    else:
        return language.strip().lower()
