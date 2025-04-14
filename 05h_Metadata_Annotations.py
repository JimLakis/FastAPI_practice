from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/items/")     # HTTP method decorator, no path parameters defined
async def read_items(
    q: Annotated[
        list[str],
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,   # Note minimum entries must be at least three
        ),
        ] = None,
    ):   # Path Operation Function: Query Parameter, q, will accept multiple string values. Additional annotations are provided in Query()
    return {"q": q}
    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Query parameter with additional metadata annotation

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#declare-more-metadata


-----


Above App's Path Operation employs only a GET request, so one uses just a browser to view example, ie no use of curl required...


Browser:

No value for QP provided...
http://127.0.0.1:8000/items/

stdout:
{"q":null}


Values provided...
http://127.0.0.1:8000/items/?q=Tom

stdout:
{"detail":[{"type":"too_short","loc":["query","q"],"msg":"List should have at least 3 items after validation, not 1","input":["Tom"],"ctx":{"field_type":"List","min_length":3,"actual_length":1}}]}

---

cURL:

curl -X 'GET' 'http://127.0.0.1:8000/items/' -H 'accept: application/json'

stdout:
{"q":["foo","bar"]}


curl -X 'GET' 'http://127.0.0.1:8000/items/?q=Tom&q=Jerry' -H 'accept: application/json'

stdout: Note error messages
{"detail":[{"type":"too_short","loc":["query","q"],"msg":"List should have at least 3 items after validation, not 2","input":["Tom","Jerry"],"ctx":{"field_type":"List","min_length":3,"actual_length":2}}]}


curl -X 'GET' 'http://127.0.0.1:8000/items/?q=Tom&q=Jerry&q=Bill' -H 'accept: application/json'

stdout:
{"q":["Tom","Jerry","Bill"]}

---

'''