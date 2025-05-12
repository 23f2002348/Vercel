from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load JSON data from file
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "q-vercel-python.json")

# Read the JSON data
with open(json_path) as f:
    students_data = json.load(f)

# Create a lookup dictionary for faster access
marks_lookup = {student["name"]: student["marks"] for student in students_data}

@app.get("/api")
def get_marks(name: List[str] = []):
    result = [marks_lookup.get(n, None) for n in name]
    return {"marks": result}
