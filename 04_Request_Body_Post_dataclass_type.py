
from fastapi import FastAPI
from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    price: float
    description: str | None = None  # optional attributes, these must be listed AFTER required attributes
    tax: float | None = None    # " "

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


** See file 04_NOTES_Request_Body.txt for notes on how to test the endpoints of this file on the Command Line or PowerShell. **


Example of a dataclass from a chatbot...

from dataclasses import dataclass, field

@dataclass
class Order:
    net_price: float
    vat_rate: float
    total_price: float = field(init=False) # Exclude from __init__, calculate in __post_init__

    def __post_init__(self):
        self.total_price = self.net_price * (1 + self.vat_rate)

order = Order(net_price=100, vat_rate=0.2)
print(order)
# Expected output: Order(net_price=100, vat_rate=0.2, total_price=120.0)


"""
