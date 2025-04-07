from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/items/")     # HTTP method decorator, no path parameters defined
async def read_items(q: Annotated[str, Query()]):   # Path Operation Function: Query Parameter, q, is required since a default value is not assigned
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Required QP Parameters

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#required-parameters


-----


Above App's Path Operation employs only a GET request, so one uses just a browser to view example, ie no use of curl...

Browser Address: http://127.0.0.1:8000/items/?q=cats
stdout:
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":"cats"}


However in curl...

>curl --request GET -v http://127.0.0.1:8000/items/?q=cats
stdout:
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":"cats"}* Connection #0 to host 127.0.0.1 left intact




'''