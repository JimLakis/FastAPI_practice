from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

@app.get("/second_level_page/me") # Constant path end points must be listed first before a reference to the same page that accepts path parameters
# viewed at: http://127.0.0.1:8000/second_level_page/me
async def return_constant():
    content = "sample content from me page"
    return {"constant_path_parameter": content}

@app.get("/second_level_page/{path_parameter}") # This path operation also references the second_level_page, but it accepts a path parameter
async def return_input(path_parameter: str):
    return {"path_parameter": path_parameter}

# ---

@app.get("/users") # This path operation's function will always ALWAYS be called/ran because it's listed first.
async def return_users_1():
    return ["Rick", "Morty"]

@app.get("/users") # This path operation's function will NEVER called/ran.
async def return_users_2():
    return ["Batman", "Robin"]

# ---
    
def main():
    pass


if __name__ == "__main__":
    main()


'''
Notes:

Path Parameters
https://fastapi.tiangolo.com/tutorial/path-params/#order-matters

-----

Order Matters:
The order of the path operations in a file matters since they are read by Python's interrupter top down.

-----


Again, to view the site's pages tree (all of the pages) in Swagger, again the simple Swagger page is used...
http://127.0.0.1:8000/docs#/


'''