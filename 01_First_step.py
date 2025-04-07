
from fastapi import FastAPI

app = FastAPI() #Creates an instance of FastAPI


@app.get("/") #path operation decorator
async def root(): #path operation function
    return {"message": "Hello World"}

'''
Notes:

First Steps
https://fastapi.tiangolo.com/tutorial/first-steps/#step-5-return-the-content

Run the file in the FastAPI Dev server via > fastapi dev file_name.py

Output can be seen in a browser at http://127.0.0.1:8000

Interactive documentation via Swagger can be viewed at http://127.0.0.1:8000/docs

Another interactive documenattion via ReDoc can be viewed at  http://127.0.0.1:8000/redoc

Generated OpenAPI JSON schema can be viewed at http://127.0.0.1:8000/openapi.json

'''