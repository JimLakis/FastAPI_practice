import random
from typing import Annotated
from pydantic import AfterValidator
from fastapi import FastAPI, Path, Query


app = FastAPI()


@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/items/{item_id}/")     # HTTP method decorator, with Path Parameter
async def read_items(
    item_id: Annotated[int, Path(title = "The ID of the item to get")],
    q: Annotated[str | None, Query(alias = "item-query")] = None,   # ** Use of Query(alias="new-name") changes the QP's name that is to be entered in the browser. **
):
    ''' Order matters. In this path operation the first parameter is not assigned a default value where as the second one is. This order is allowed.'''
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# @app.get("/items_2/{item_id}/")
# async def read_items(
#     q: Annotated[str | None, Query(alias = "item-query")] = None,
#     item_id: Annotated[int, Path(title = "The ID of the item to get")],
# ):
    ''' This example is not allowed. In the above parameters, Path Parameters and Query Parameters, the first parameter, q, is assigned a default value while the subsequent parameter, item_id, is not.
    This order is not allowed.'''
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Path Parameter (PP) validation. Also, both PP and QP can have additional "metadata" defined.

https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#declare-metadata

fastapi.Path being used for adding metadata to a PP
    pp: Annotated[int, Path(title = "something describing what pp is")]
    
fastapi.Query being used for adding metadata to a PP
    qp: Annotated[str | None, Query(alias = "another-name-for-qp")] = None
    
    ** NOTE alias name must be in format as acceptable URL address by browsers.


-----


Browser:

Value provided...
http://127.0.0.1:8000/items/5/?q=cat

stdout:
{"item_id":5}

** NOTE ABOVE that "q" as the QP name is no longer recognized. The alias must now be used in the browser.


Value provided...
http://127.0.0.1:8000/items/5/?item-query=cat

stdout:
{"item_id":5,"q":"cat"}


---


cURL:

No value provided...
curl --request 'GET' 'http://127.0.0.1:8000/items/5/' -H 'accept: application/json'

stdout:
{"item_id":5}


Value provided...
curl --request 'GET' 'http://127.0.0.1:8000/items/5/?item-query=cat' -H 'accept: application/json'

stdout:
{"item_id":5,"q":"cat"}



---

'''