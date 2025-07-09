from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = [
   "http://localhost:3000"   
]

app.add_middleware(
     CORSMiddleware,
     allow_origins = ["*"],
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)

tasks = []

class Task(BaseModel):
     id: Optional[UUID] = None
     title : str 
     desc: Optional[str]= None
     status : bool = False
  

@app.get("/tasks/", response_model= List[Task])
def read_task():
     return tasks

@app.get("/tasks/{task_id}", response_model = Task)
def read_task_byid(task_id : UUID):
     for task in tasks:
          if task.id == task_id:
               return task
     raise HTTPException(status_code=404, detail="Task Id does not found")     

@app.post("/tasks/", response_model = Task)
def create_task(task: Task):
     task.id = uuid4()
     tasks.append(task)     
     return task     

@app.put("/tasks/{task_id}", response_model = Task)
def update_task(task_id : UUID, task_update : Task):
     for idx, task in enumerate(tasks):
          if task.id == task_id:
               updated_task = task.copy(update = task_update.dict(exclude_unset=True))
               tasks[idx] = updated_task
               return updated_task
     raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model= Task)
def delete_task(task_id : UUID):
     for idx, task in enumerate(tasks):
          if task_id == task.id:
               return tasks.pop(idx)
     raise HTTPException(status_code=404, detail="Task Not Found")     
          

if __name__=="__main__": 
     uvicorn.run(app, host="0.0.0.0", port=8000)