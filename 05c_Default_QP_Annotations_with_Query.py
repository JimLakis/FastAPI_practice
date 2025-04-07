from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/items/")     # HTTP method decorator, no path parameters defined
async def read_items(q: Annotated[str, Query()] = "cats"):   # Path Operation Function: Query Parameter, q, assigned a default value.
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Additional validation - type.Annotation[] and fastapi.Query()
    If Query() is employed within Annotate to provide a default value it's best to not provide Query() with an argument.

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#query-as-the-default-value-or-in-annotated

and

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#default-values


**************

It was also HIGHLY suggested to use typing.Annotation when declaring default values for QPs.

**************

-----


Above App's Path Operation employs only a GET request, so one uses just a browser to view example, ie no use of curl...

Browser Address: http://127.0.0.1:8000/items/
stdout:
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":"cats"}




'''