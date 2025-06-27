from google.genai import types
from config import WORKING_DIR

from functions.get_files_info import schema_get_files_info
from functions.get_files_info import get_files_info
from functions.get_file_content import schema_get_file_content
from functions.get_file_content import get_file_content
from functions.run_python_file import schema_run_python_file
from functions.run_python_file import run_python_file
from functions.write_file import schema_write_file
from functions.write_file import write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

functions_list = {
    'get_files_info': get_files_info,
    'get_file_content': get_file_content,
    'run_python_file': run_python_file,
    'write_file': write_file,
}

def call_function(function_call_part, verbose=False):
    if verbose: 
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    function_name = function_call_part.name
    arguments = function_call_part.args.copy()
    arguments["working_directory"] = WORKING_DIR
    
    if function_name not in functions_list:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    try:
        function_result = functions_list[function_name](**arguments)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )
    except Exception as e:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Error: {e}"}
                )
            ]
        )