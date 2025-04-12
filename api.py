from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/hello")
def hello(name: str = "Sahan"):
    return {"message": f"Hello {name}"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
