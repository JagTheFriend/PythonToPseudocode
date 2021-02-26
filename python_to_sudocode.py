import re

# print() --> OUTPUT
PRINT_TO_OUTPUT = r"print\((.*?)\)"


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
            return file.readlines()

    def store_data(self, code: str = ''):
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

        :return store_data():
        """

        code_between_in_print = self.code[self.code.find(
            "(")+1:self.code.find(")")]
        code = re.sub(PRINT_TO_OUTPUT,
                      f"OUTPUT {code_between_in_print}", self.code)
        print(code)
        # return self.store_data(code


# Main(code="print('gg')").output()
