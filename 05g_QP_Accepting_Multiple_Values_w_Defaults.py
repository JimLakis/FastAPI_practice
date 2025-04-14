from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/items/")     # HTTP method decorator, no path parameters defined
async def read_items(q: Annotated[list[str], Query()] = ['foo', 'bar']):   # Path Operation Function: Query Parameter, q, will accept multiple values. Default values are provided if none are furnished in the URL.
    return {"q": q}
    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Query parameter list / multiple values with assigned default value

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#query-parameter-list-multiple-values-with-defaults


-----


Above App's Path Operation employs only a GET request, so one uses just a browser to view example, ie no use of curl required...


In order for a "none" value to be offered in the request body for QP q, its value must include the two quotes: "" ...


Browser:

No value for QP provided...
http://127.0.0.1:8000/items/

stdout:
{"q":["foo","bar"]}


Values provided...
http://127.0.0.1:8000/items/?q=Tom
http://127.0.0.1:8000/items/?q=Tom&q=Jerry

stdout:
{"q":["Tom"]}
{"q":["Tom","Jerry"]}

---

cURL:

curl -X 'GET' 'http://127.0.0.1:8000/items/' -H 'accept: application/json'

stdout:
{"q":["foo","bar"]}


curl -X 'GET' 'http://127.0.0.1:8000/items/?q=Tom&q=Jerry' -H 'accept: application/json'

stdout:
{"q":["Tom","Jerry"]}


---

'''