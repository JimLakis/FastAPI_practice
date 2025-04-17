import random
from typing import Annotated
from pydantic import AfterValidator
from fastapi import FastAPI


app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_valid_id(id: str) -> str:
    prefixes = ("isbn", "imbd") # a tuple of prefix values
    if not id.startswith(prefixes):
        raise ValueError("Invalid ID format, it must start with \"isbn\" or \"imdb\".")
    return id


@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/items/")     # HTTP method decorator, no path parameters defined
async def read_items(
    id: Annotated[str | None,   # "type" checking. str or None
        AfterValidator(check_valid_id)]     # then id starting with portions from keys in data dictionary
        = None      # if non values provided, None is the default
    ):   # Path Operation Function: QP, q, will accept a string, None or have a default value of None assigned. AfterValidator calls our custom func after the first type, string, is checked.
    if id:
        item = data.get(id)     # if the id/key in data dict exists, assign the dict value to item
    else:   # if no entry exists in the data dict, make a suggestion (follows)...
        #my_list = [1,2,3]
        #r = random.choice(my_list)
        id , item = random.choice(list(data.items()))   # randomly choose/"choice" an entry from data.items and convert the key/value pair to a list where each value is assigned to the vars id and item 
    return {"id": id, "item": item}
    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Query parameter custom validation

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#custom-validation


-----


Browser:

Value provided...
http://127.0.0.1:8000/items/?q=isbn-9781529046137

stdout:
{"id":"isbn-9781529046137","item":"The Hitchhiker's Guide to the Galaxy"}


Incorrect start of QP...
http://127.0.0.1:8000/items/?q=isqq-9781529046137

stdout: leads to suggestion, random selection from data
{"id":"imdb-tt0371724","item":"The Hitchhiker's Guide to the Galaxy"}


No value provided...
http://127.0.0.1:8000/items/

stdout: leads to suggestion, random selection from data
{"id":"isbn-9781439512982","item":"Isaac Asimov: The Complete Stories, Vol. 2"}


---


cURL:

No value provided...
curl --request 'GET' 'http://127.0.0.1:8000/items/' -H 'accept: application/json'

stdout:
{"id":"imdb-tt0371724","item":"The Hitchhiker's Guide to the Galaxy"}



Value provided...
curl -X 'GET' 'http://127.0.0.1:8000/items/?=isbn-9781439512982' -H 'accept: application/json'

stdout:
{"id":"isbn-9781439512982","item":"Isaac Asimov: The Complete Stories, Vol. 2"}



Incorrect start of QP...
curl -X 'GET' 'http://127.0.0.1:8000/items/?q=Tom&q=Jerry' -H 'accept: application/json'

stdout:
{"id":"isbn-9781529046137","item":"The Hitchhiker's Guide to the Galaxy"}


---

'''