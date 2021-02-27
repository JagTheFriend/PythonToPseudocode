import re

CHARACTERS = [
    "\n",
    "\r",
    "\t",
]

# print() --> OUTPUT
PRINT_TO_OUTPUT = r"(.*?)print\((.*?)\)"
PRINT_FORMAT = r"print\((.*?)\)"

class Main():
    def __init__(self):
        self.code = self.get_code()
    
    def get_code(self) -> [str]:
        """
        Returns the code stored in `code.txt`
        :return STRING ARRAY:
        """
        with open("code.txt", "r") as file:
            return file.readlines()

    def output(self) -> _if:
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

        return _if()

code = "print('ggg')"
Main().output()
