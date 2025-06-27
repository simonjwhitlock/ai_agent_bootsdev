from functions.write_file import write_file

print("test 1: ","calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

print("test 2: ","calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

print("test 3: ","calculator", "/tmp/temp.txt", "this should not be allowed")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))