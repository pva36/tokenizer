import re


class Tokenize:
    @staticmethod
    def tokenize(
        range: tuple[int, int],
        lang: str,
        skip_chars: list[str],
        output_file: str,
        input_file: str,
    ):
        """
        Main function of the class.
        """
        # TODO: define the return type of the function
        with open(input_file) as fin:
            lines: list[str] = fin.readlines()
        print(len(lines))

        Tokenize._check_range(range, len(lines))

        tokens: list[str] = Tokenize._get_tokens(lines, range, skip_chars)

    @staticmethod
    def _get_tokens(
        lines: list[str], range: tuple[int, int], skip_chars: list[str]
    ) -> list[str]:
        """
        Returns a list containing all the tokens in the list of lines provided,
        deleting from it any character in skip_chars.
        """
        line_counter: int = 0
        tokens: list[str] = []

        return tokens

    @staticmethod
    def _check_range(range: tuple[int, int], fin_lines: int) -> bool:
        """
        Checks whether the range provided by the user is is valid. If not, an
        Exception is raised. Else, return True.
        """
        if (range[1] > fin_lines) or (range[0] > fin_lines):
            raise Exception(
                "The range provided exceeds the range of the input file: "
                + f"it has {fin_lines} lines."
            )
        else:
            return True

    @staticmethod
    def get_range(range: str) -> tuple[int, int]:
        """
        Return a tuple of length 2, containing two integer values (the first
        and last line to consider by the 'tokenize subcommand')
        """
        if not re.match(r"^\d*:\d*$", range):
            exception_message = "Range argument must have the form "
            exception_message += "'INTEGER:INTEGER', where INTEGER is any "
            exception_message += "positive integer number in decimal notation."
            raise Exception(exception_message)

        else:
            range_list: list[str] = range.split(":")
            start: int = int(range_list[0])
            end: int = int(range_list[1])

            if (end == 0) or (start == 0):
                raise Exception(
                    "Neither the end nor the start of the range can have the"
                    + " value of 0."
                )
            if end < start:
                raise Exception(
                    "The end of the range cannot be less than its start."
                )
            return start, end

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
