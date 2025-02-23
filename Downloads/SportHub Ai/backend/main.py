from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from match_data import get_live_match_data
from commentary import generate_commentary

app = FastAPI()

# CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend is running!"}

@app.get("/get_live_match_data")
def fetch_match_data():
    return get_live_match_data()

@app.get("/generate_commentary")
def get_commentary():
    match = get_live_match_data()
    commentary = generate_commentary(match)
    return {"match": match, "commentary": commentary}
