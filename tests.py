from functions.get_files_info import get_files_info

print("calculator", ".")
print(get_files_info("calculator", "."))
print("calculator", ".")
print(get_files_info("calculator", "pkg"))
print("calculator", "/bin")
print(get_files_info("calculator", "/bin"))
print("calculator", "../")
print(get_files_info("calculator", "../"))