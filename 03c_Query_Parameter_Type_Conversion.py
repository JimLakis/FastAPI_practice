
from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---


# Path Operation
@app.get("/items/{item_id}")     # HTTP method decorator with path parameter, item_id
async def read_items(item_id: str, q: str | None = None, short: bool = False):   # Path Operation Function: Optional Query Parameter, q, of type string OR if no value is entered for it explicitly in the URL its default value is set to None. Also Query Parameter, short, is of type bool and its default is False.
        '''
        item_id is a path path parameter
        q and short are query parameters with default values being set to None and False respectfully
        '''
        item = {"item_id": item_id}
        if q:   # if q exists...
            item.update({"q": q}) # add q to item
        if not short: # if short is false, interpreted as 'not False' which is True in this statement...
            item.update({"description": "Some text pertaining to 'short'"}) # add a dictionary placeholder for 'short'
        return item
    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Query Parameters Type Conversion - example Booleans:
https://fastapi.tiangolo.com/tutorial/query-params/#query-parameter-type-conversion


-----


URL entered with Query Parameter, q, equal False
http://127.0.0.1:8000/items/Frank?q=Tom&short=False
or
URL entered with Query Parameter, q, type conversion, 0 to False...
http://127.0.0.1:8000/items/Frank?q=Tom&short=0

(aside: URL entered with Query Parameter, q, equal to False or not provided...)
or
http://127.0.0.1:8000/items/Frank?q=Tom

stdout Raw Data:
{"item_id":"Frank","q":"Tom","description":"Some text pertaining to 'short'"}


-----


URL entered with Query Parameter, q, equal to True...
http://127.0.0.1:8000/items/Frank?q=Tom&short=True
or
URL entered with Query Parameter, q, type conversion, 1 to True...
http://127.0.0.1:8000/items/Frank?q=Tom&short=1

stdout Raw Data:
{"item_id":"Frank","q":"Tom"}


-----


'''