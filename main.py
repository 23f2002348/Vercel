from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
    expose_headers=["*"]  # Expose all headers
)


# Hard-code the student data since file loading is unreliable in serverless environments
students_data = [{"name":"10X5qblMbP","marks":61},{"name":"x08q","marks":73},{"name":"CSVuKm","marks":16},{"name":"T8etZrrp","marks":62},{"name":"pTuyTK","marks":98},{"name":"x","marks":88},{"name":"7hYy2","marks":65},{"name":"SupK","marks":81},{"name":"FD","marks":58},{"name":"wwM3iq","marks":19},{"name":"cvXM","marks":95},{"name":"y0OZEleB","marks":67},{"name":"ubIMbZ","marks":92},{"name":"3jrqUvrs2F","marks":51},{"name":"1","marks":81},{"name":"ATwe9lI","marks":92},{"name":"MRx1Dw5V","marks":83},{"name":"DayueuC","marks":51},{"name":"TFmcLZMFEK","marks":93},{"name":"0","marks":81},{"name":"0PllkeWgfT","marks":36},{"name":"F6Yijxg","marks":4},{"name":"7v7qRj7W","marks":23},{"name":"ldg4n","marks":45},{"name":"9lxG8mvFa","marks":84},{"name":"6kFZOmxEe","marks":39},{"name":"Ms3fMDr","marks":37},{"name":"Ww","marks":66},{"name":"XdE6uzNaN","marks":99},{"name":"B21YNwTrpV","marks":36},{"name":"wvIGEVlt","marks":51},{"name":"KNwvkl3H","marks":39},{"name":"CFb6cq6","marks":5},{"name":"a1ivJ","marks":26},{"name":"DApg","marks":92},{"name":"q","marks":25},{"name":"XgAW","marks":8},{"name":"9RpT","marks":17},{"name":"2fWe0Fh1h7","marks":48},{"name":"cE","marks":11},{"name":"kiP3F","marks":81},{"name":"k0Os","marks":25},{"name":"Ovw","marks":41},{"name":"IZR8B","marks":15},{"name":"bwWVxK2a","marks":90},{"name":"c","marks":42},{"name":"1TrhZTiB","marks":16},{"name":"B0kiI","marks":42},{"name":"6j","marks":22},{"name":"fE","marks":73},{"name":"Ni7wOm4q","marks":48},{"name":"V49nVtEn","marks":70},{"name":"dUrbw5WXTw","marks":99},{"name":"LR","marks":55},{"name":"L","marks":66},{"name":"Mtl1HJc","marks":80},{"name":"zidiGL7","marks":5},{"name":"b","marks":43},{"name":"JU","marks":17},{"name":"hh6","marks":71},{"name":"UL5pe","marks":38},{"name":"ch8fyr9CG3","marks":64},{"name":"2k","marks":72},{"name":"nVsyFMAdke","marks":71},{"name":"LMB","marks":17},{"name":"Gnd4","marks":24},{"name":"a7fH0NbWU","marks":19},{"name":"sdb3QYNV8","marks":15},{"name":"TJre1HB","marks":1},{"name":"wW5","marks":74},{"name":"O1Il","marks":92},{"name":"pZLytXpqH","marks":72},{"name":"6Z","marks":87},{"name":"eUOT2wlaqN","marks":4},{"name":"kDYn0lV1","marks":40},{"name":"GjKu","marks":28},{"name":"kPU","marks":20},{"name":"p","marks":63},{"name":"nFoH26BAw","marks":86},{"name":"AL","marks":8},{"name":"Gqh1fsL2","marks":62},{"name":"lcY","marks":96},{"name":"F67MhyqQyE","marks":98},{"name":"iT1NiiiUcy","marks":99},{"name":"F4zlCkkn","marks":60},{"name":"xUyRyn","marks":39},{"name":"6QXr1VXHg","marks":87},{"name":"nRNI8nWc","marks":44},{"name":"k7QS5","marks":7},{"name":"dwdfW","marks":97},{"name":"QuDHSR","marks":46},{"name":"fPeuG","marks":11},{"name":"Ln","marks":27},{"name":"A","marks":52},{"name":"UuzA","marks":81},{"name":"r","marks":41},{"name":"xQ8DKtl","marks":35},{"name":"D","marks":91},{"name":"YSuBt7","marks":55},{"name":"H","marks":40}]

# Create a lookup dictionary for faster access
marks_lookup = {student["name"]: student["marks"] for student in students_data}

@app.get("/")
def root():
    return {"message": "Welcome to the Student Marks API. Use /api?name=X&name=Y to get marks."}

@app.get("/api")
async def get_marks(name: Optional[List[str]] = Query(default=None)):
    # If name parameter is not provided, return empty list
    if name is None:
        return {"marks": []}
    
    # Get marks for each name in the order they were provided
    result = []
    for n in name:
        mark = marks_lookup.get(n)
        result.append(mark)  # This will include None for names not in the dataset
    
    return {"marks": result}

# Add a catch-all route for debugging
@app.get("/{path:path}")
def catch_all(path: str):
    return {"message": f"Path '{path}' not found. Use /api?name=X&name=Y to get marks."}


@app.get("/api")
def get_marks(name: List[str] = []):
    result = [marks_lookup.get(n, None) for n in name]
    return {"marks": result}
