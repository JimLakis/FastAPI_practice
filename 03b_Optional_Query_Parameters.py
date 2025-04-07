
from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---


# Path Operation
@app.get("/items/{item_id}")     # HTTP method decorator with path parameter, item_id
async def read_items(item_id: str, q: str | None = None):   # Path Parameter Function: Optional Query Parameter, q, defined as a string OR if no value is entered for it explicitly in the URL its default value is set to None
        if q:   # if q exist...
            return {"item_id": item_id, "q": q}
        return {"item_id": item_id} # if q does not exist
    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Optional Query Parameters:
https://fastapi.tiangolo.com/tutorial/query-params/#optional-parameters


-----

Mixing user defined Path Parameters with Query Parameters in a URL looks like the following...
http://127.0.0.1:8000/items/Frank?q=Tom
stdout Raw Data:
{"item_id":"items_id=Frank","q":"Tom"}

or

With no optional Query Parameter defined in the URL looks like the following...
http://127.0.0.1:8000/items/Frank
stdout Raw Data:
{"item_id":"items_id=Frank"}

-----





'''