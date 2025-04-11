
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


    """
    
    ** See file 04_NOTES_Request_Body.txt for notes on how to test the endpoints of this file. **
    
    """
