from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

@app.get("/second_level_page/{path_parameter}") #parameter taken from user's addition to address and passed as the argument to the async function return_func
# Example: http://127.0.0.1:8000/second_level_page/100 - will produce the JSON data - {path_parameter: 100}
async def return_input(path_parameter: int):
    return {"path_parameter": path_parameter}
    
def main():
    pass


if __name__ == "__main__":
    main()



'''
Notes:

Path Parameters
https://fastapi.tiangolo.com/tutorial/path-params/

-----

Path Parameters take input from web address typically entered in a browser's address field.
Typically the parameter is attached to the end of the address.
Example: http://127.0.0.1:8000/second_level_page/100 will yield a JSON value of path_parameter 100 in the return web page.

Or again, the root page and the /second_level_page's type expectations can be seen via Swagger at: 127.0.0.1:8000/docs#/

-----

Original author's version:

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


Again, to view the site's pages tree (all of the pages) in Swagger, again the simple Swagger page is used...
http://127.0.0.1:8000/docs#/


To pass input to the page's Raw ouput viewed at...
http://127.0.0.1:8000/second_level_page/foo




'''