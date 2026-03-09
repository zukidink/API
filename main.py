from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/employee")
def get_employee(name):
    return {f"{name}대표님, 환영합니다."}


@app.get("/student")
def get_student(name):
    return {f"{name}학생, 환영합니다."}