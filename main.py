import argparse
import constants
from tokenize import Tokenize


def main():
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

    # parse arguments
    args = parent_parser.parse_args()
    # print(args)

    # TOKENIZE functionality --------------------------------------------------
    if args.subcommand == "tokenize":
        # define range
        RANGE: tuple[int, int] = (0, 0)  # default value
        if args.range:
            RANGE = Tokenize.get_range(args.range)
            # TODO: handle the case were the user provides a range outside the
            #       limits of the file

        # print("range: " + f"{RANGE[0]}:{RANGE[1]}")

        # define language
        LANG: str = Tokenize.get_language(args.language)
        SKIP: list[str] = constants.get_chars_to_skip(LANG)
        # print("language: " + LANG)

        # define output
        FILE_OUT: str = "out.txt"
        if args.output:
            FILE_OUT = args.output

        # print("output file: " + FILE_OUT)

        # define input
        INPUT_FILE: str = args.input_file
        # print("input file: " + INPUT_FILE)

        frequency_dictionary: dict[str, int] = Tokenize.tokenize(
            RANGE, LANG, SKIP, FILE_OUT, INPUT_FILE
        )

        # print(frequency_dictionary)

    # sorted_frequency_dictionary = sorted(
    #     frequency_dictionary.items(), key=lambda x: x[1]
    # )
    # # print the results:
    # counter = 0
    # with open("out.txt", "w") as f:
    #     for item in sorted_frequency_dictionary:
    #         counter += 1
    #         # print(f"{counter}) {item[1]}:\t{item[0]}")
    #         f.write(f"{counter}] {item[1]}: {item[0]}\n")


if __name__ == "__main__":
    main()
