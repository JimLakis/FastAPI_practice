from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/items/")     # HTTP method decorator, no path parameters defined
async def read_items(q: Annotated[list[str] | None, Query()] = None):   # Path Operation Function: Query Parameter, q, will accept multiple values. By default if no values are provided the value None is provided.  must have a no chars, ie "" for the None response. Or of course, it accepts a string
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

Query parameter list / multiple values

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#query-parameter-list-multiple-values


-----


Above App's Path Operation employs only a GET request, so one uses just a browser to view example, ie no use of curl...


In order for a "none" value to be offered in the request body for QP q, its value must include the two quotes: "" ...


http://127.0.0.1:8000/items/
http://127.0.0.1:8000/items/?
stdout
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}


Browser Address: http://127.0.0.1:8000/items/?q=
stdout:
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":[""]}


Browser Address: http://127.0.0.1:8000/items/?q=Tom
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":["Tom"]}


Browser Address: http://127.0.0.1:8000/items/?q=foo&q=bar
stdout:
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":["foo","bar"]}


(IMPORTANT ASIDE: When using the Windows command line it is best to enclose the URL in quotes to ensure that curl interprets them correctly.)
Same as above in curl...

> curl --request GET -v "http://127.0.0.1:8000/items/?"
> curl --request GET -v "http://127.0.0.1:8000/items/?q="

> curl --request GET -v "http://127.0.0.1:8000/items/?q=foo&q=bar"


stdout:
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}* Connection #0 to host 127.0.0.1 left intact
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":[""]}* Connection #0 to host 127.0.0.1 left intact

{"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":["foo"]}* Connection #0 to host 127.0.0.1 left intact
'q' is not recognized as an internal or external command,
operable program or batch file.


In PowerShell invoking its Rest library...

PS> Invoke-RestMethod "http://127.0.0.1:8000/items/?q=foo&q=bar"
stdout:
items                            q
-----                            -
{@{item_id=Foo}, @{item_id=Bar}} {foo, bar}







'''