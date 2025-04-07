from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/items/")     # HTTP method decorator, no path parameters defined
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=5)] = None,):
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

Adding Additional validation to fastapi.Query()

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#add-more-validations

and

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#add-regular-expressions


*****

(See bottom of page for additional fastapi.Query() arguments)

*****


-----


Above App's Path Operation employs only a GET request, so one uses just a browser to view example, ie no use of curl...

Browser Address: http://127.0.0.1:8000/items/
stdout:
{"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}

Browser Address: http://127.0.0.1:8000/items/?q
stdout: error message generated - 0 characters is shorter than min or 3
{"detail":[{"type":"string_too_short","loc":["query","q"],"msg":"String should have at least 3 characters","input":"","ctx":{"min_length":3}}]}

Browser Address: http://127.0.0.1:8000/items/?q=xx
stdout: error message generated - 2 characters is shorter than min or 3
{"detail":[{"type":"string_too_short","loc":["query","q"],"msg":"String should have at least 3 characters","input":"xx","ctx":{"min_length":3}}]}

If the length of q is longer than limited by its Query() annotation of 5, the raw JSON response body includes an error message...
Browser Address: http://127.0.0.1:8000/items/?q=longstring
stdout:
{"detail":[{"type":"string_too_long","loc":["query","q"],"msg":"String should have at most 5 characters","input":"longstring","ctx":{"max_length":5}}]}


Additional arguments the fastapi.Query() will accept, from Claude.ai...

FastAPI's Query() function accepts several arguments to customize how query parameters are handled. Here are some of the most commonly used arguments:

- `default`: Sets the default value if the parameter is not provided
- `alias`: Provides an alternative name for the parameter
- `title`: Provides a title for the parameter in OpenAPI documentation
- `description`: Adds a description for the parameter in OpenAPI documentation
- `gt`: Greater than validation (for numbers)
- `ge`: Greater than or equal validation
- `lt`: Less than validation
- `le`: Less than or equal validation
- `min_length`: Minimum length validation (for strings)
- `max_length`: Maximum length validation (for strings)
- `pattern` or `regex`: specify a regular expression that the input must match
- `deprecated`: Marks the parameter as deprecated in OpenAPI
- `include_in_schema`: Controls if the parameter should be in the OpenAPI schema
- `example`: Provides an example value for documentation

For example, in a FastAPI route function:


from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: str = Query(
        default=None,
        min_length=3,
        max_length=50,
        description="Search query string",
        deprecated=False,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


'''