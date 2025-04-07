
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):  # defining the Data Model's attributes
    name: str
    description: str | None = None  # an optional QP
    price: float
    tax: float | None = None    # an optional QP

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.post("/items/") # HTTP method decorator, post, with path parameter
async def create_item(item: Item): # Path Operation Function with QP of type defined in our Data Model above
    return item

    
def main():
    pass


if __name__ == "__main__":
    main()


'''

Notes:

Request Body:
https://fastapi.tiangolo.com/tutorial/body/#request-body

-----

Notes:

Typically client PCs on the internet send Request Bodies to APIs running on servers.
Though they don't have to send the "body" part of request, sometimes they just request a path and some query parameters (QPs).
The "body" tends to be information (JSON) sent in a request.

Then the server sends Response Bodies in return.

In the example above a Pydantic BaseModel object is used to define the names of and types of the QPs in the Request.


************************************************************
************************************************************
************************************************************
************************************************************

IMPORTANT DEPARTURE FROM PREVIOUS SCRIPTS/SECTIONS IN THE TUTORIALS...

The above request includes the use of a POST HTTP method. That type of request in NOT supported when being made via a browser's address bar.
ie. one can not provide QPs on the address bar as...
http://127.0.0.1:8000/items/?name=tom&price=1.0 

That address will invoke the raw data JOSN respone...
{"detail":"Method Not Allowed"}

************************************************************

However, one can still confirm that the QPs exist and are defined as Item types in Swagger as usual...

http://127.0.0.1:8000/docs#


-----


(* Note: below examples truncate the number of attributes for the JSON request body to just one: name. *)


--- curl on the Command Line ---

Using curl to test the endpoints via the Command Line once the FastAPI dev environment server is running and offering the expected page...

C:...> curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"tom\"}" http://127.0.0.1:8000/item

note:

    Command Line can utilize curl alias


--- curl in PowerShell ---

Using curl to test the endpoints via the PowerShell once the FastAPI dev environment server is running and offering the expected page...

PS C:...> curl.exe -X POST http://127.0.0.1:8000/items/ -H "Content-Type: application/json" --data-binary '"{\"name\":\"tom\"}"'

notes:
    PowerShell needs to call the curl.exe explictedly
    ** Single quotes need to enclose the entire JSON Request Body/JSON payload in order to escape the first set of double quotes **

or

PS C:...> curl.exe -X POST http://127.0.0.1:8000/items/ -H "Content-Type: application/json" --data-binary "{\""name\"":\""tom\""}"

notes:
    PowerShell needs to call the curl.exe explictedly
    ** Double quotes also need to be utilized around JSON key/value pair elements in order to double-escape for PowerShell and the curl **


--- PowerShell's innate Representational State Transfer (REST) web services

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/items/" -ContentType "application/json" -Body '{"name":"tom"}'


************************************************************
************************************************************
************************************************************
************************************************************

'''