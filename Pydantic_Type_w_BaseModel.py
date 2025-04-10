

from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str | None = None  # an optional attribute
    price: float
    tax: float | None = None    # an optional attribute

    
def main():
    product_data = {"name" : "truck", "price" : 2.00}
    product = Product(**product_data)   ## CRUCIAL - Note the double asterisks (**) before the variable name with the Product constuctor. They needed to "unpack" the variables values.
    #product = Product(**{"name" : "truck", "price" : 2.00})    # Also supported.
    print(product)



if __name__ == "__main__":
    main()


'''



'''