from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/items/")     # HTTP method decorator, no path parameters defined
async def read_items(q: Annotated[str | None, Query(max_length=5)] = None):   # Path Operation Function: Query Parameter, q, defined as optional, of str type, of max length of 50 and None if not provided.
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

Additional validation - type.Annotation[] and fastapi.Query()

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#additional-validation

Employing type.Annotation to add additional non-generic type arguments and metadata reguarding those types.

fastapi.Query() directs FastAPI server to explictedly interpret information in the query string, information after the '?' in a URL as QPs to be used for validation purposes, AND it provides additional metadata of the annotated types.


-----


Above App's Path Operation employs only a GET request, so one uses just a browser to view example, ie no use of curl...

Browser Address: http://127.0.0.1:8000/items/?q=cat
stdout:
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":"cat"}

or

If the length of q is longer than limited by its Query() annotation of 5, the raw JSON response body includes an error message...
Browser Address: http://127.0.0.1:8000/items/?q=longstring
stdout:
{"detail":[{"type":"string_too_long","loc":["query","q"],"msg":"String should have at most 5 characters","input":"longstring","ctx":{"max_length":5}}]}


(Sides:
Both http://127.0.0.1:8000/items/?q and http://127.0.0.1:8000/items/ return 
stdout:
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}

Optionally, one can see the QP's ,q , metadata, Query(max_length=50), posted on the Swagger page.
)





'''