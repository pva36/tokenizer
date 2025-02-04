import argparse
import constants
from tokenize import Tokenize
import functions as f
from data import Data
import os


def main() -> None:
    # implement argparse ------------------------------------------------------
    parent_parser = argparse.ArgumentParser(prog="tokenizator")

    subparsers = parent_parser.add_subparsers(
        title="subcommands", dest="subcommand"
    )

    # TOKENIZE parser
    parser_tokenize = subparsers.add_parser("tokenize")

    parser_tokenize.add_argument("input_file", type=str)

    tokenize_language_help = "Text's language: fr, en, es, de."
    parser_tokenize.add_argument(
        "-l",
        "--language",
        help=tokenize_language_help,
        type=str,
        required=True,
    )

    tokenize_output_help = "Output file. By default 'out.txt'."
    parser_tokenize.add_argument(
        "-o", "--output", help=tokenize_output_help, type=str
    )

    tokenize_range_help = "Define the range of lines 'integer:integer' "
    tokenize_range_help += "between which the extraction of tokens must be "
    tokenize_range_help += "performed. If not provided, the complete content "
    tokenize_range_help += "of the 'txt' file is considered."
    parser_tokenize.add_argument(
        "-r", "--range", help=tokenize_range_help, type=str
    )

    # DATA parser
    parser_data = subparsers.add_parser("data")
    data_subparsers = parser_data.add_subparsers(
        title="data subcommands", dest="data_subcommand"
    )

    # data create
    parser_create_data = data_subparsers.add_parser("create")

    parser_create_data.add_argument("-l", "--language", type=str)
    parser_create_data.add_argument(
        "-u", "--username", required=True, type=str
    )

    # data update
    # needed: username, language, input_file
    parser_update_data = data_subparsers.add_parser("update")
    parser_update_data.add_argument(
        "-l", "--language", type=str, required=True
    )
    parser_update_data.add_argument(
        "-u", "--username", type=str, required=True
    )
    parser_update_data.add_argument("-i", "--input", type=str, required=True)

    # parse arguments
    args = parent_parser.parse_args()
    # print(args)

    # TOKENIZE functionality --------------------------------------------------
    if args.subcommand == "tokenize":
        # define range
        RANGE: tuple[int, int] = (0, 0)  # default value
        if args.range:
            RANGE = Tokenize.get_range(args.range)

        # define language
        LANG: str = f.get_language(args.language)
        SKIP: list[str] = constants.get_chars_to_skip(LANG)

        # define output
        FILE_OUT: str = "out.txt"
        if args.output:
            FILE_OUT = args.output

        # define input
        INPUT_FILE: str = args.input_file

        frequency_dictionary: dict[str, int] = Tokenize.tokenize(
            RANGE, LANG, SKIP, INPUT_FILE
        )

        sorted_frequency_dictionary: list[tuple[str, int]] = sorted(
            frequency_dictionary.items(), key=lambda x: x[1], reverse=True
        )

        Tokenize.write_frequency_list(sorted_frequency_dictionary, FILE_OUT)

    # DATA functionality ------------------------------------------------------
    if args.subcommand == "data":
        if args.data_subcommand == "create":
            USER_NAME: str = args.username.strip().lower()
            Data.create_user_directory(USER_NAME)

            if args.language:
                LANG = f.get_language(args.language)
                Data.create_language_data(LANG, USER_NAME)

        if args.data_subcommand == "update":
            USER_NAME = args.username.strip().lower()
            LANG = f.get_language(args.language)

            # TODO: maybe this should be part of a function
            if not os.path.isfile(args.input):
                raise Exception(
                    "The file specified with -i / --input does not exists"
                )
            else:
                UPDATE_FILE_IN = args.input
            # TODO
            Data.update_datalist(LANG, USER_NAME, UPDATE_FILE_IN)


if __name__ == "__main__":
    main()
