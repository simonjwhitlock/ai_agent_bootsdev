import os

def get_files_info(working_directory, directory=None):
    working_abs_path = os.path.abspath(working_directory)
    directory_abs_path = os.path.abspath(os.path.join(working_abs_path, directory))
    if not directory_abs_path.startswith(working_abs_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(directory_abs_path):
        return f'Error: "{directory}" is not a directory'
    list_out = []
    count = len(os.listdir(directory_abs_path))
    for file in os.listdir(directory_abs_path):
        count -= 1
        file_path = os.path.join(directory_abs_path, file)
        list_out.append(f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
    str_out = "\n".join(list_out)
    return str_out