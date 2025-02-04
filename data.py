class Data:
    @staticmethod
    def create_language_data(language: str) -> None:
        """
        Creates a data list for the language indicated. If a data list already
        exists for the language, raise an Exception. Assumes that language
        is a string containing any of the strings stored in
        constants.SUPPORTED_LANGS.
        """
