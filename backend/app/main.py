from fastapi import FastAPI

app = FastAPI(
    title="iFixit AI Assistant API",
    description="Backend para el asistente inteligente de resolución de problemas tecnológicos.",
    version="1.0.0",
)


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "message": "Backend funcionando correctamente"
    }