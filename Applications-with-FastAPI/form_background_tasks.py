from fastapi import BackgroundTasks, FastAPI, Form
from typing import Optional
import time
import uvicorn

app = FastAPI()

def process_form(data: str):
  # Simulate some time-consuming process
  time.sleep(5)  # Simulates a 5-second processing task
  with open("processed_data.txt", "a") as f:
      f.write(f"Processed: {data}\n")

@app.post("/submit/")
async def submit_form(
  background_tasks: BackgroundTasks,
  data: str = Form(...)
):
  background_tasks.add_task(process_form, data)
  return {"message": f"Processing data: {data}"}

# Add a root endpoint for testing
@app.get("/")
async def root():
  return {"message": "Welcome to the API"}

if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=8000)

