from fastapi import FastAPI
from src.api import core, market_management, bidding, market_making

app: FastAPI = FastAPI(
        title="Prediction Market API",
        description="Open Source double auction prediction market service",
        version="0.1.0a",
        docs_url=None,
        redoc_url="/documentation"
)

app.include_router(core.router, tags=["Core"])
app.include_router(market_management.router, tags=["Market Management"])
app.include_router(bidding.router, tags=["Bid Management"])
app.include_router(market_making.router, tags=["Market Making"])

if __name__ == '__main__':
    import uvicorn  # type: ignore # pragma: no cover

    uvicorn.run(app=app, host="localhost", port=8000)  # pragma: no cover
