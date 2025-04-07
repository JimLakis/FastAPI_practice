
from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/items/{item_id}")     # HTTP method decorator with path parameters
async def read_items(item_id: str, q: str, skip: int = 0, limit: int | None = None):   # Path Operation Function with PP and QPs defined
    '''
    Required QP: q
    Default QP set and thus optional: skip
    Optional QP: limit
    '''
    return_parameters = {"item_id": item_id, "q": q, "skip": skip, "limit": limit}    # 
    return return_parameters
    
def main():
    pass


if __name__ == "__main__":
    main()


'''

Notes:

Required and Optional Query Parameters (QP):
https://fastapi.tiangolo.com/tutorial/query-params/#required-query-parameters

-----

Minimal expected URL includes path parameter, item_id, and QP, q. The default and optional QPs get provided...
http://127.0.0.1:8000/items/wrench?q=Tom

Raw Data stdout:
{"item_id":"wrench","q":"Tom","skip":0,"limit":null}


Over-riding the default QP, skip...
http://127.0.0.1:8000/items/wrench?q=Tom&skip=1

Raw Data stdout:
{"item_id":"wrench","q":"Tom","skip":1,"limit":null}


Providing a value for the optional QP, limit...
http://127.0.0.1:8000/items/wrench?q=Tom&skip=1&limit=5

Raw Data stdout:
{"item_id":"wrench","q":"Tom","skip":1,"limit":5}


'''