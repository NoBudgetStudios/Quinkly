from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import os
import sys
sys.path.append(os.path.dirname(__file__))
import services
import models

app = FastAPI()

# ========= API ROUTE =========
@app.post("/generate_content", tags=["Content Generator"])
def generate(prompt_data: models.PromptInput):
    output = services.generate_content(prompt_data)
    return {"output": output}

# ========= STATIC FILES SETUP =========
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
INDEX_FILE = os.path.join(STATIC_DIR, "index.html")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# ========= ROOT ROUTE =========
@app.get("/", tags=["UI"])
def read_index():
    if os.path.exists(INDEX_FILE):
        return FileResponse(INDEX_FILE)
    return {"error": "index.html not found"}

@app.on_event("startup")
async def startup_event():
    print("[✅] FastAPI server has started successfully.")
