import re


class Tokenize:
    @staticmethod
    def get_range(range: str) -> list:
        """
        Return a list of length 2, containing two integer values (the first and
        last line to consider by the 'tokenize subcommand')
        """
        if not re.match(r"^\d*:\d*$", range):
            exception_message = "Range argument must have the form "
            exception_message += "'INTEGER:INTEGER', where INTEGER is any "
            exception_message += "integer number in decimal notation."
            raise Exception(exception_message)

        else:
            range = range.split(":")
            range[0] = int(range[0])
            range[1] = int(range[1])
            # TODO: Check that first value is less than second. Rise exception
            #       otherwise
            # TODO: Check that values aren't 0. Rise exception otherwise
            return range

    @staticmethod
    def get_language(language: str) -> str:
        """
        Return a string representing one of the languages supported by the
        program. If the user's argument isn't valid, raise an exception.
        """
        match (language.strip().lower()):
            case "en":
                return "en"
            case "fr":
                return "fr"
            case "es":
                return "es"
            case "de":
                return "de"
            case _:
                exception_message = "Valid arguments for the --language (-l) "
                exception_message += "flag are: 'en', 'es', 'de', 'fr'"
                raise Exception(exception_message)
