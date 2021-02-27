import re

CHARACTERS = [
    "\n",
    "\r",
    "\t",
]

# print() --> OUTPUT
PRINT_FORMAT = r"print\((.*?)\)"

# IF STATEMENTS
IF_FORMAT = r"if (.*?):"

# WHILE STATEMENTS
WHILE_FORMAT = r"while (.*?):"


class Main():
    def __init__(self):
        self.code = self.get_code()

    def save_code(self) -> None:
        with open("output.txt", "w") as file:
            file.writelines(self.code)

    def get_code(self) -> [str]:
        """
        Returns the code stored in `code.txt`
        :return STRING ARRAY:
        """
        with open("code.txt", "r") as file:
            return file.readlines()

    def _print(self):
        """
        Converts:
            `print()` to `OUTPUT ""`

        :return _if():
        """

        # loop thought the array
        for index, i in enumerate(self.code):
            # loop though the string
            # gets the code inside the print statement
            try:
                code_in_brackets = i[i.index("print(") + len("print("):-2]

                self.code[index] = re.sub(
                    PRINT_FORMAT, f"OUTPUT {code_in_brackets}", i)
            except ValueError:
                continue

        return self._if()

    def _if(self) -> None:
        """
        Converts:
            `if [condition]` to `IF [condition] THEN`

        :return _while():
        """
        for index, i in enumerate(self.code):
            # loop though the string
            # get the logic
            try:
                logic = i[i.index("if") + len("if"):-2]

                self.code[index] = re.sub(
                    IF_FORMAT, f"IF{logic} THEN", i)
            except ValueError:
                continue
        return self._while()

    def _while(self):
        """
        Converts:
            `if [condition]` to `IF [condition] THEN`

        :return save_code():
        """
        for index, i in enumerate(self.code):
            # loop though the string
            # get the logic
            try:
                logic = i[i.index("while") + len("while"):-2]

                self.code[index] = re.sub(
                    WHILE_FORMAT, f"WHILE{logic} DO", i)
            except ValueError:
                continue

        print(self.code)
        self.save_code()


Main()._print()
