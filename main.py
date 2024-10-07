from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from starlette import status
from starlette.responses import JSONResponse

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return JSONResponse(
        content="Server is running",
        status_code=status.HTTP_200_OK,
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)