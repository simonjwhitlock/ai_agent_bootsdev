from functions.run_python_file import run_python_file

print("test 1: ", "calculator", "main.py")
print(run_python_file("calculator", "main.py"))

print("test 2: ", "calculator", "tests.py")
print(run_python_file("calculator", "tests.py"))

print("test 3: ", "calculator", "../main.py")
print(run_python_file("calculator", "../main.py"))

print("test 4: ", "calculator", "nonexistent.py")
print(run_python_file("calculator", "nonexistent.py"))