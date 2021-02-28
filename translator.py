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

# VARIABLE equals VALUE
VARIABLE = r"(.*?) = (.*?)"
VARIABLE_2 = r"(.*?): \[(.*?)\] = (.*?)"
VARIABLE_3 = r"(.*?)=(.*?)"

# DEF
DEF_FORMAT = r"def (.*?)\((.*?)\):"

# FOR STATEMENT
FOR_FORMAT = r"for (.*?) in range\((.*?), (.*?)\)"
FOR_FORMAT_2 = r"for (.*?) in range\((.*?),(.*?)\)"


class Main():
    def __init__(self):
        self.code = self.get_code()
        self._print()

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

                self.code[index] = re.sub(IF_FORMAT, f"IF{logic} THEN", i)
            except ValueError:
                continue
        return self._while()

    def _while(self):
        """
        Converts:
            `if [condition]` to `IF [condition] THEN`

        :return variable_equals_value():
        """

        for index, i in enumerate(self.code):
            # loop though the string
            # get the logic
            try:
                logic = i[i.index("while") + len("while"):-2]
                self.code[index] = re.sub(WHILE_FORMAT, f"WHILE{logic} DO", i)
            except ValueError:
                continue

        return self.variable_equals_value()

    def variable_equals_value(self):
        """
        Converts:
            `q = 4` to `q <- 4`

        :return _def():
        """

        for index, i in enumerate(self.code):
            # loop though the string
            # get the variable and its value
            try:
                variable, value = i.split("=")
                if new_var := variable.split(":"):
                    variable = new_var[0]

                if re.findall(VARIABLE, i):
                    self.code[index] = re.sub(
                        f"{VARIABLE}", f"{variable}<-{str(value)[0]}", i)
                    continue

                if re.findall(VARIABLE_2, i):
                    self.code[index] = re.sub(
                        f"{VARIABLE_2}", f"{variable}<-{str(value)[0]}", i)
                    continue

                if re.findall(VARIABLE_3, i):
                    self.code[index] = re.sub(
                        f"{VARIABLE_3}", f"{variable}<- {str(value)[0]}", i)
                    continue

            except ValueError:
                continue

        return self._def()

    def _def(self):
        """
        Converts:
            `def Name()` to `FUNCTION Name()`

        :return _for():
        """

        for index, i in enumerate(self.code):
            # loop though the string
            # get the funcion name and parameter(s)
            try:
                function = i[i.index("def ") + len("def"):-1]
                func_name = function.split("(")[0]  # gets the function name
                func_parameters = function.split(
                    "(")[1][:-2]  # gets the parameter
                self.code[index] = re.sub(
                    DEF_FORMAT, f"PROCEDURE{func_name}({func_parameters})", i)
            except (ValueError, IndexError):
                continue

        return self._for()

    def _for(self):
        """
        Converts:
            `def Name()` to `FUNCTION Name()`

        :return small_to_caps():
        """

        for index, i in enumerate(self.code):
            # loop though the string
            # get the logic
            try:
                variable = i[i.index("for") + len("for"):-2].split("in")[0]
                start, end = i[i.index(
                    "for") + len("for"):-2].split("in")[1][len("range(")+1:-1].split(",")
                end = end if end[0] != " " else end[1:]

                if re.findall(FOR_FORMAT, i):
                    self.code[index] = re.sub(
                        FOR_FORMAT, f"FOR{variable}<- {start} TO {end}", i)
                    continue

                if re.findall(FOR_FORMAT_2, i):
                    self.code[index] = re.sub(
                        FOR_FORMAT_2, f"FOR{variable}<- {start} TO {end}", i)
                    continue

            except (ValueError, IndexError):
                continue

        return self.small_to_caps()

    def small_to_caps(self):
        """
        Converts:
            `break` -> `BREAK`
            `return` -> `RETURN`
            `#` -> `//`

        :return save_code():
        """

        for index, i in enumerate(self.code):
            # loop though the string
            # get the function name and parameter(s)
            try:
                if "break" in i:  # capitalize `break`
                    self.code[index] = i.replace("break", "BREAK")
                    continue

                if "return" in i:  # capitalize `return`
                    self.code[index] = i.replace("return", "RETURN")
                    continue

                if "#" in i:  # convert `#` to `//`
                    self.code[index] = i.replace("#", "//")
                    continue

                if "==" in i:  # convert `==` to `=`
                    self.code[index] = i.replace("==", "=")
                    continue

                self.code[index] = i
            except ValueError:
                continue

        return self.save_code()


Main()
