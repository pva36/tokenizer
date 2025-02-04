import pathlib
import os
import platform


class Data:
    @staticmethod
    def create_language_data(language: str, username: str) -> None:
        """
        Creates a data list for the language indicated. If a data list already
        exists for the language, raise an Exception. Assumes that language
        is a string containing any of the strings stored in
        constants.SUPPORTED_LANGS.
        """
        HOME_DIR: pathlib.Path = pathlib.Path.home()
        USER_DIR: pathlib.Path = Data.get_user_directory(username)
        os.chdir(USER_DIR)

        filename = f"{language}.txt"
        if not os.path.isfile(pathlib.Path(USER_DIR, filename)):
            with open(filename, "w") as f:
                f.write("")
            print(f"A datalist for '{language}' has been succesfully created!")

        else:
            print(f"A datalist for '{language}' already exists!")

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
