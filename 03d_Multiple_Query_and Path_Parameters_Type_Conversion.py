
from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/users/{user_id}/items/{item_id}")     # HTTP method decorator with path parameters: user_id, item_id
async def read_items(user_id: int, item_id: str, q: str | None = None, short: bool = False):   # Path Operation Function: Optional Query Parameter, q, of type string OR if no value is entered for it explicitly in the URL its default value is set to None. Also Query Parameter, short, is of type bool and its default is False.
    return_parameters = {"user_id": user_id, "item_id": item_id}
    if q:
        return_parameters.update({"q": q})
    if not short:
        return_parameters.update({"short description": "Some text pertaining to 'short'"})
    return return_parameters
    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Multiple Path and Query Parameters:
https://fastapi.tiangolo.com/tutorial/query-params/#multiple-path-and-query-parameters


-----

Minimal expected URL must include both path parameters, user_id and item_id...
http://127.0.0.1:8000/user/55/items/wrench

Raw Data stdout:
{"user_id":55,"item_id":"wrench","short description":"Some text pertaining to 'short'"}
note: the inclusion of Query Parameter, short, since its default value is set to 'False' and the logic test for 'not False' which is 'True'.


Addition of Query Parameters in URL...
http://127.0.0.1:8000/users/55/items/wrench?q=socket&short=True

Raw Data stdout:
{"user_id":55,"item_id":"wrench","q":"socket"}

-----

Aside:
It appears through experimentation that if Path Parameters are listed in the HTTP Function Decorator they must be provided values in the associated Path Operation Function.
The following appear to not be allowed...

async def read_items(user_id: int | None = None, item_id: str | None = None):


'''