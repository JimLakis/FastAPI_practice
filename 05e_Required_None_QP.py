from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/items/")     # HTTP method decorator, no path parameters defined
async def read_items(q: Annotated[str | None, Query()]):   # Path Operation Function: Query Parameter, q, must have a no chars, ie "" for the None response. Or of course, it accepts a string
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

Required QP can be none, ie ""

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#required-can-be-none


-----


Above App's Path Operation employs only a GET request, so one uses just a browser to view example, ie no use of curl...


In order for a "none" value to be offered in the request body for QP q, its value must include the two quotes: "" ...

Browser Address: http://127.0.0.1:8000/items/?q=""
stdout:
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":"\"\""}


If NO value is assigned to q, the JSON response body will exclude q from it...

Browser Address: http://127.0.0.1:8000/items/?q=
stdout:
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}


If the QP, q, is excluded entirely the QPs type restrictions will throw an error as seen in the response body...

Browser Address: http://127.0.0.1:8000/items/
stdout:
{"detail":[{"type":"missing","loc":["query","q"],"msg":"Field required","input":null}]}




Same as above in curl...

> curl --request GET -v http://127.0.0.1:8000/items/?q=""
> curl --request GET -v http://127.0.0.1:8000/items/?q=
> curl --request GET -v http://127.0.0.1:8000/items/
stdout:
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}* Connection #0 to host 127.0.0.1 left intact
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}* Connection #0 to host 127.0.0.1 left intact
{"detail":[{"type":"missing","loc":["query","q"],"msg":"Field required","input":null}]}* Connection #0 to host 127.0.0.1 left intact




'''