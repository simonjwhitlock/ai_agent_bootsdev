import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    working_abs_path = os.path.abspath(working_directory)
    file_abs_path = os.path.abspath(os.path.join(working_abs_path, file_path))
    if not file_abs_path.startswith(working_abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(file_abs_path, "r") as f:
            content = f.read(MAX_CHARS)
            if os.path.getsize(file_abs_path) > MAX_CHARS:    
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                    )
        return content
    except Exception as e:
        return f'Error: error raised whilst reading file "{file_path}": {e}'