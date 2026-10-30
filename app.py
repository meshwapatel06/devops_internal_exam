from fastapi import FastAPI
from routes.student_routes import StudentRouter

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(StudentRouter)