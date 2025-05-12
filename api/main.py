from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks from local JSON file
with open("api/q-vercel-python.json") as f:
    marks_data = {entry["name"]: entry["marks"] for entry in json.load(f)}

@app.get("/")
def get_marks(name: list[str] = []):
    return {"marks": [marks_data.get(n, None) for n in name]}
