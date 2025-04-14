from typing import Annotated
from fastapi import FastAPI
from pydantic import AfterValidator

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_valid_id(id: str) -> str:
    prefixes = ("isbn", "imbd") # a tuple of prefix values
    if not id.startswith(prefixes):
        raise ValueError()
    return id


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

Query parameter custom validation

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#custom-validation


-----


Above App's Path Operation employs only a GET request, so one uses just a browser to view example, ie no use of curl required...





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