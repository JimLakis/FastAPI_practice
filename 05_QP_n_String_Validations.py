
from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/items/")     # HTTP method decorator, no path parameters defined
async def read_items(q: str | None = None):   # Path Operation Function: default Query Parameters defined
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    # results: dict[str, object] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]} ## Alternative where PyLance's"overloading" warning is not displayed.
    if q:
        results.update({"q": q})
    return results
    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Query Parameters and String Validations:
https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#query-parameters-and-string-validations

Defining QP type as a string and assigning it a default value of None, thus providing a value to the QP, q, is not required that a user provide a value for it.


-----


Above App's Path Operation employs only a GET request, so one uses just a browser to view example, ie no use of curl...

Browser Address: http://127.0.0.1:8000/items/?q=cat
stdout:
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":"cat"}

(Sides:
Both http://127.0.0.1:8000/items/?q and http://127.0.0.1:8000/items/ return 
stdout:
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}

If the QP WAS NOT optionally defined as a None value, ie...
    async def read_items(q: str):
then...
http://127.0.0.1:8000/items/
stdout:
{"detail":[{"type":"missing","loc":["query","q"],"msg":"Field required","input":null}]}
... as the QP is now required.
)





'''