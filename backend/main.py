from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

from backend import ui_contract as ui
from backend.execution import setup_steps, reset_execution

app = FastAPI()

# serve generated audio files
app.mount("/audio", StaticFiles(directory="backend/audio"), name="audio")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Routine(BaseModel):
    steps: List[str]

@app.get("/")
def root():
    return {"status": "STEPWISE running"}

@app.post("/setup")
def setup_routine(routine: Routine):
    setup_steps(routine.steps)
    return {"status": "routine loaded"}

@app.post("/reset")
def reset():
    reset_execution()
    return {"status": "execution reset"}

@app.get("/step")
def step():
    return ui.ui_get_step()

@app.post("/done")
def done():
    return ui.ui_done()

@app.get("/stuck")
def stuck():
    return ui.ui_check_stuck()

@app.get("/parent")
def parent():
    return ui.ui_parent_view()
