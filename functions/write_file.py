import os

def write_file(working_directory, file_path, content):
    working_abs_path = os.path.abspath(working_directory)
    file_abs_path = os.path.abspath(os.path.join(working_abs_path, file_path))
    if not file_abs_path.startswith(working_abs_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_abs_path):
        file_dir = (file_abs_path.rsplit("/", 1))[0]
        if not os.path.exists(file_dir):
            try:
                os.makedirs(file_dir)
            except Exception as e:
                return f'Error: rased whilst creating directory "{file_dir}": {e}'
    try:
        with open(file_abs_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: issue encountered wiriting to file "{file_path}": {e}'
