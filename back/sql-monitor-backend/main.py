from fastapi import FastAPI

app = FastAPI()


# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the API. Use /docs for API documentation."}


# Health check route
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running smoothly."}


# About route
@app.get("/about")
def about():
    return {
        "app_name": "FastAPI Example",
        "version": "1.0.0",
        "description": "This is a sample FastAPI project.",
    }
