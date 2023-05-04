import glob
import discord


def find_py_files(filepath: str) -> list[str]:
    files_list = glob.glob(f"{filepath}/*.py")
    for file_index in range(len(files_list)):
        files_list[file_index] = (
            files_list[file_index].replace("/", ".").replace(".py", "")[4:]
        )
    return files_list
