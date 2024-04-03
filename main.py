from fastapi import FastAPI

from api.routes import berries

app = FastAPI(
    title="PokeBerriesAPI",
    description="A simple API to get information about Pokemon Berries",
    version="1.0.0",
    docs_url="/",
)

app.include_router(berries.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
