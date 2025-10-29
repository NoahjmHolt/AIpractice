
import os

def get_files_info(working_directory, directory="."):
    try:
        abs_work = os.path.abspath(working_directory)
        abs_cand = os.path.abspath(os.path.join(working_directory, directory))

        if not abs_cand.startswith(abs_work):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_cand):
            return f'Error: "{directory}" is not a directory'

        return "OK"  # temporary, until you build the listing
    except Exception as e:
        return f"Error: {e}"
