
from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Path Operation
@app.get("/items/")     # HTTP method decorator, no path parameters defined
async def read_items(skip: int = 0, limit: int = 10):   # Path Operation Function: default Query Parameters defined
        return fake_items_db[skip:skip+limit]
    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Query Parameters:
https://fastapi.tiangolo.com/tutorial/query-params/


-----


Declaring parameter values in Path Operation's Function inherently defines them as Query Parameters.

Viewing the returned Raw Data via: http://127.0.0.1:8000/items/
stdout:
[{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}]

or

Viewing the returned Raw Data via: http://127.0.0.1:8000/items/?skip=0&limit=1
[{"item_name":"Foo"}]


-----


(Lists: side example) Accessing List values via a range of its indexes:

    fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}] ## List only has 3 elements
    
    skip: int = 0   # range set to start with the first element
    limit: int = 10     # range length is greater than the length of the list so ALL elements are returned
    
    print(fake_items_db[skip:skip+limit])
    
    stdout:
    [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


'''