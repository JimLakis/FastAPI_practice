from enum import Enum

from fastapi import FastAPI

# Defining our own type.
# Predefining acceptable path parameter values.
# Enum - https://docs.python.org/3/library/enum.html
class ModelName(str, Enum):
    a = "alexnet"   # "Deep Learning FTW!"
    b = "resenet"   # "LeCNN all images"
    c = "lenet"     # "Recognizing handwriting"

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

@app.get("/models/{model_name}") # 
async def return_input(model_name: ModelName):
    if model_name is ModelName.a:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "resenet":
        return {"model_name": model_name, "message": "LeCNN all images"}
    if model_name is ModelName.c:
        return {"model_name": model_name, "message": "Recognizing handwriting"}
    else:
        return {"model_name": "not pre-defined"}
    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Predefined Path Parameters
https://fastapi.tiangolo.com/tutorial/path-params/#predefined-values

-----

Evaluating Path Parameters against predefined values:

Path parameters are evaluated with the help of class enum.

The process is seen in action by entering the path's endpoint of interest along with an input path parameter...
example: http://127.0.0.1:8000/models/alexnet

of and end point's path parameter that is not included in the Enum object, ModelName, will yield the error page results.

Then again, to view the site's pages tree in Swagger along with the default types excepted as valid path parameters...


'''