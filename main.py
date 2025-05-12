from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the marks from the JSON file once at startup
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)
    marks_dict = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
async def get_marks(name: list[str] = []):
    result = [marks_dict.get(n, None) for n in name]
    return {"marks": result}
