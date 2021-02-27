import re

# print() --> OUTPUT
PRINT_TO_OUTPUT = r"(.*?)print\((.*?)\)"
# \t\nprint() --> \t\nOUTPUT
PRINT_TO_OUTPUT_INDENTED = r":\n\t(.*?)print\((.*?)\)"

# IF STATEMENTS
IF_logic = r"^if (.*?) :"
IF_2_logic = r"^if (.*?):"

IF_STMT = r"(.*?)if (.*?):"

# WHILE LOOP
WHILE_logic = r"^while (.*?) :"
WHILE_2_logic = r"^while (.*?):"

WHILE_STMT = r"(.*?)while (.*?):"


class Main():
    def __init__(self, *, code):
        """
        Storing the code in a variable,
        Which might be used in the future
        """
        self.code = code

    def get_data(self) -> [str]:
        """
        Returns the data
        :return String Array:
        """

        with open("code.txt", "r") as file:
            return file.read()

    def store_data(self, code):
        """
        Stores the code in a file called: `output.txt`
        :return None:
        """

        with open("output.txt", "w") as file:
            file.write(code)

    def output(self):
        """
        Converts 
            `print` to `OUTPUT`
            `\n\tprint` to `\n\tOUTPUT`
        :return _if():
        """

        code_in_print = self.code[self.code.find("(")+1:self.code.find(")")]

        self.code = re.sub(
            PRINT_TO_OUTPUT, f"\tOUTPUT {code_in_print}", self.code
        ) or re.sub(
            PRINT_TO_OUTPUT_INDENTED, f"\tOUTPUT {code_in_print}", self.code
        )

        return self._if()

    def _if(self):
        """
        Converts:
            `if [condition]:` to `IF [condition] THEN`

        :return _while():
        """

        logic_in_if = re.findall(f"{IF_logic}", self.code)
        logic_in_if_2 = re.findall(f"{IF_2_logic}", self.code)

        for i in [logic_in_if, logic_in_if_2]:
            for logic in i:
                self.code = re.sub(IF_STMT, f"IF {logic} THEN", self.code)

        return self._while()

    def _while(self):
        """
        Converts:
            `while [condition]:` to `WHILE [condition] DO`

        :return store_data():
        """

        logic_in_while = re.findall(f"{WHILE_logic}", self.code)
        logic_in_while_2 = re.findall(f"{WHILE_2_logic}", self.code)

        code = ""
        for i in [logic_in_while, logic_in_while_2]:
            for logic in i:
                self.code = re.sub(WHILE_STMT, f"WHILE {logic} DO", self.code)

        print(self.code)
        return self.store_data(self.code)


code = "while True:\n\tif g == 8:\n\tprint('gg')\nif hyman == 5 :\n\tprint('ded')"
Main(code=code).output()
