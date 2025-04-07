
from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/items/{item_id}")     # HTTP method decorator with path parameters
async def read_items(item_id: str, q: str):   # Path Operation Function: Required Query Parameter, q
    return_parameters = {"item_id": item_id, "q": q}    # in order to make a Query Parameter required, remove any default values assigned to it, ie. ...q: str | None = None
    return return_parameters
    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Required Query Parameters:
https://fastapi.tiangolo.com/tutorial/query-params/#required-query-parameters

-----

Minimal expected URL includes path parameter, item_id, and Query Parameter, q.
http://127.0.0.1:8000/items/wrench?q=socket

Raw Data stdout:
{"item_id":"wrench", "q" : "socket"}


'''