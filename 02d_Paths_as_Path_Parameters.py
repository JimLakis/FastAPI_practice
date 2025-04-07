
from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

@app.get("/files/{file_path:path}") # Crucial - in the path parameter there can be no spaces around the colon between "...path:path"
async def return_input(file_path: str):
        return {"file_path": file_path}
    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Paths as Path Parameters:
https://fastapi.tiangolo.com/tutorial/path-params/#predefined-values


-----

Try: http://127.0.0.1:8000/files/to/infinity/and/beyond
Will yield: file_path: "to/infinity/and/beyond" on the JSON page.

Try: http://127.0.0.1:8000/files/to/infinity/and/beyond/file.txt
Will yield: file_path: "to/infinity/and/beyond/file.txt" on the JSON page.


'''