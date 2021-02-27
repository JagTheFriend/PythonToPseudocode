import re

CHARACTERS = [
    "\n",
    "\r",
    "\t",
]

# print() --> OUTPUT
PRINT_FORMAT = r"print\((.*?)\)"

# IF STATEMENTS
IF_logic = r"^if (.*?) :"
IF_2_logic = r"^if (.*?):"
IF_STMT = r"(.*?)if (.*?):"

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

    def output(self):
        """
        Converts:
            `print()` to `OUTPUT ""`
        
        :return _if():
        """

        # loop thought the array
        for index, i in enumerate(self.code):
            # loop though the string
            code_in_brackets = i[11:-2] # gets the code inside the print statement
            self.code[index] = re.sub(PRINT_FORMAT, f"OUTPUT \"{code_in_brackets}\"", i)

        return self._if()

    
    def _if(self) -> None:
        """
        Converts:
            `if [condition]` to `IF [condition] THEN`
        """

        # loop thought the array
        for index, i in enumerate(self.code):
            # loop though the string
            code_in_brackets = i[11:-2] # gets the code inside the print statement
            self.code[index] = re.sub(PRINT_FORMAT, f"OUTPUT \"{code_in_brackets}\"", i)

        for index, i in enumerate(self.code):
            logic_in_if = re.findall(f"{IF_logic}", self.code[index])
            logic_in_if_2 = re.findall(f"{IF_2_logic}", self.code[index])

            for logics in [logic_in_if, logic_in_if_2]:
                if logics:
                    for logic in logics:
                        self.code[index] = re.sub(IF_STMT, f"IF {logic} THEN", self.code[index])

        return self.save_code()


code = "print('ggg')"
Main().output()
