"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

url = "https://httpbin.io/json"

response = httpx.get(url)   # httpx object, get() method, returns a response object

if response.status_code == 200:  # check if the request was successful
    print(response.status_code)  # response object, status_code attribute
    print(response.json())      # response object, json() method
else:
    print(f"Request failed with status code: {response.status_code}")