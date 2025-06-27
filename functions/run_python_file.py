import os
import subprocess

def run_python_file(working_directory, file_path):
    working_abs_path = os.path.abspath(working_directory)
    file_abs_path = os.path.abspath(os.path.join(working_abs_path,file_path))
    if not file_abs_path.startswith(working_abs_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_abs_path):
        return f'Error: File "{file_path}" not found.'
    if not file_abs_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        file_output = subprocess.run(['/home/simon/Documents/git/ai_agent_bootsdev/.venv/bin/python', file_abs_path], capture_output=True)
        result = f'STDOUT: {file_output.stdout}\nSTDERR: {file_output.stderr}'
        #if file_output.returncode != 0:
        #    print(f'Process exited with code {file_output.returncode}')
        #if file_output == None:
        #    print('no file output produced');
        return result
    except Exception as e:
        return f'Error: executing python file: {e}'