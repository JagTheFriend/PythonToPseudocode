import python_to_sudocode

code = str(input("Please enter the python code: \n"))
with open("code.txt", "w") as file:
    file.write(code)

print()
python_to_sudocode.Main(code=code).output()
