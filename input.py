import sys
import translator

print("Please enter the python code: \n")
code = sys.stdin.read()


print("Processing your code")
with open("code.txt", "w") as file:
    file.write(code)

translator.Main()
print("Your code has been processed successfully \nPlease check the file named: `output.txt`")
