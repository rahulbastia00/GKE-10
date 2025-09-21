from fastapi import FastAPI

#initialize the app
app = FastAPI(
    title='Api &code explanation Agent',
    description="An AI agent to answer questions about the Bank of Anthos API spec and source code.",
    version='0.1.0'
)

@app.get("/", tags=["Health Check"])
async def read_root():
     """
    A simple health check endpoint to confirm the server is running.
    """
     return {"message": "Server is running"}