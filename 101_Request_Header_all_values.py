
from typing import Optional

from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/") #Home Page
async def root():
    return {"message": "Hello World"}

# ---

# Path Operation
@app.get("/request_head_user_agent/")
async def return_single_header(request: Request) -> dict[str, Optional[str]]:
    user_agent = request.headers.get("user-agent")
    return {"User-Agent": user_agent}

@app.get("/request_head_all_keys/")
async def return_all_header_keys(request: Request) -> dict[str, list[str]]:    # Path Operation Function. Query Parameter, request, is of type Request
    header_keys = [key for key in request.headers]      # List comprehension iterating over Request().headers dictionary-like object
    return {"Header-Keys": header_keys}     # Returns just the keys


@app.get("/request_http_header_fields_and_values/")
async def return_all_header_key_values(request: Request) -> dict[str, str]:    # Path Operation Function. Query Parameter, request, is of type Request
    return {key: value for key, value in request.headers.items()}

    
def main():
    pass


if __name__ == "__main__":
    main()


'''



Above App's Path Operation employs only a GET request, so one uses just a browser to view example, ie no use of curl...

Browser Address: http://127.0.0.1:8000/return_all_header_keys
stdout:
{
  "Header-Keys": [
    "host",
    "user-agent",
    "accept",
    "accept-language",
    "accept-encoding",
    "referer",
    "dnt",
    "sec-gpc",
    "connection",
    "sec-fetch-dest",
    "sec-fetch-mode",
    "sec-fetch-site",
    "priority"
  ]
}


------------

Side note: Not all information related to the request is provided since some of them may be of None type.

Browser Address: http://127.0.0.1:8000/return_all_header_key_values
stdout:
{
  "host": "127.0.0.1:8000",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
  "accept": "application/json",
  "accept-language": "en-US,en;q=0.5",
  "accept-encoding": "gzip, deflate, br, zstd",
  "referer": "http://127.0.0.1:8000/docs",
  "dnt": "1",
  "sec-gpc": "1",
  "connection": "keep-alive",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-origin",
  "priority": "u=0"
}

'''