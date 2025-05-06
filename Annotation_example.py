from typing import Annotated
from pathlib import Path


#Declaring a 'type'
FilePath = Annotated[Path, "This is a path to the a file."]

def process_file(file_path: FilePath) -> None:
    print(f"Path to file: {file_path}")


path = Path("./Setup_Access_Fastapi.txt")
process_file(path)