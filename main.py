from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Static JSON object simulating marks of students
marks_data = {
    "Alice": 10,
    "Bob": 20,
    "Charlie": 30,
    "David": 40
}

@app.get("/api")
def get_marks(name: List[str] = []):
    result = [marks_data.get(n, None) for n in name]
    return {"marks": result}
