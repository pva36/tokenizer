import pathlib
import os
import platform
import re


class Data:
    @staticmethod
    def create_language_data(language: str, username: str) -> None:
        """
        Creates a data list for the language indicated. If a data list already
        exists for the language, raise an Exception. Assumes that language
        is a string containing any of the strings stored in
        constants.SUPPORTED_LANGS.
        """
        # HOME_DIR: pathlib.Path = pathlib.Path.home()
        USER_DIR: pathlib.Path = Data.get_user_directory(username)
        # os.chdir(USER_DIR)

        filename = f"{language}.txt"
        if not os.path.isfile(pathlib.Path(USER_DIR, filename)):
            with open(pathlib.Path(USER_DIR, filename), "w") as f:
                f.write("")
            print(f"A datalist for '{language}' has been succesfully created!")

        else:
            print(f"A datalist for '{language}' already exists!")

    @staticmethod
    def get_language_datalist(language: str, username: str) -> pathlib.Path:
        """
        Returns the path of the datalist according to username and language
        specified. If doesn't exists, raise an exception. Assumes that language
        and username are valid.
        """
        USER_DIR: pathlib.Path = Data.get_user_directory(username)
        filename = f"{language}.txt"
        if not os.path.isfile(pathlib.Path(USER_DIR, filename)):
            raise Exception(
                f"User '{username}' does not have a datalist for '{language}'"
            )
        else:
            return pathlib.Path(USER_DIR, filename)

    @staticmethod
    def create_user_directory(username: str) -> pathlib.Path:
        """
        Creates the user's directory and return an object of type pathlib.Path
        containing the user's directory. If already exists, the object is still
        returned.
        """
        HOME_DIR: pathlib.Path = pathlib.Path.home()
        os.chdir(HOME_DIR)

        USER_DIR: pathlib.Path
        # TODO: add code for macos and windows
        if platform.system().lower() == "linux":
            USER_DIR = pathlib.Path(
                HOME_DIR,
                ".local",
                "share",
                "tokenizator",
                "user",
                f"{username.strip().lower()}",
            )

        if not USER_DIR.exists():
            os.makedirs(USER_DIR)
            print(f"Directory '{USER_DIR}' succesfully created!")
            print("Your user data will be there!")
        else:
            print(f"User directory '{USER_DIR}' already exists!")

        return USER_DIR

    @staticmethod
    def get_user_directory(username: str) -> pathlib.Path:
        """
        returns an object of type Path that contains the user's data directory.
        If user's directory doesn't exist, raise exception.
        """
        HOME_DIR: pathlib.Path = pathlib.Path.home()
        os.chdir(HOME_DIR)

        USER_DIR: pathlib.Path

        # TODO: add code for macos and windows
        if platform.system().lower() == "linux":
            USER_DIR = pathlib.Path(
                HOME_DIR,
                ".local",
                "share",
                "tokenizator",
                "user",
                f"{username.strip().lower()}",
            )

        # If USER_DIR doesn't exist, create it
        if not USER_DIR.exists():
            exception_msg = (
                f"There is no directory for user '{username.lower().strip()}'"
            )
            raise Exception(exception_msg)

        else:
            return USER_DIR

    @staticmethod
    def get_tokens_from_data_list(datalist_path: pathlib.Path) -> list[str]:
        """
        Returns a list containing all the tokens in the datalist specified.
        """
        with open(datalist_path, "r") as dl:
            dl_lines = dl.readlines()

        if len(dl_lines) == 0:
            return []
        else:
            lines: list[str] = []
            for line in dl_lines:
                lines.append(line.replace("\n", ""))
            return lines

    @staticmethod
    def get_tokens_to_add(file_in: str) -> list[str]:
        """
        Returns a list of tokens that the user doesn't need to know.
        """
        with open(file_in, "r") as f:
            lines = f.readlines()

        tokens_to_add: list[str] = []
        for line in lines:
            if "*" not in line:
                tokens = re.sub(r" {2,}", " ", line.strip()).split(" ")
                token = tokens[2].replace("'", "").strip()
                tokens_to_add.append(token)

        return tokens_to_add

    @staticmethod
    def update_datalist(language: str, username: str, file_input: str) -> None:
        """
        Updates the data list for the user and language indicated using the
        input_file. Assumes that language if one of the options defined in
        constants.SUPPORTED_LANGS, user_input exists and username is a valid
        user.
        """
        # check the format of the input file

        # get the tokens to add from the input file
        tokens_to_add: list[str] = Data.get_tokens_to_add(file_input)

        # read the current datalist
        datalist_path: pathlib.Path = Data.get_language_datalist(
            language, username
        )

        datalist_tokens = Data.get_tokens_from_data_list(datalist_path)
        # create a dictionary where every key is the same as the value:
        datalist_dict: dict[str, str] = {}
        for token in datalist_tokens:
            datalist_dict[token] = token

        # compare the current datalist with the list of tokens to add
        # and add the pertinent tokens
        for token in tokens_to_add:
            try:
                if datalist_dict[token] == token:
                    pass
            except KeyError:
                datalist_dict[token] = token

        # update the current datalist
        datalist = Data.get_language_datalist(language, username)
        print(datalist)

        with open(datalist, "w") as f:
            for key in datalist_dict.keys():
                f.write(f"{key}\n")
