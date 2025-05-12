# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import Any
app = FastAPI()
# CORS configuration: Allow all origins (or specify if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict this to specific domains)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)



# Endpoint to fetch data from the JSON file
@app.get("/data")
def get_data() -> Any:
    try:
        # Open and read the JSON file
        with open("q-vercel-python.json", "r") as file:
            data = json.load(file)
        return data
    except Exception as e:
        return {"error": f"Failed to read file: {str(e)}"}
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

