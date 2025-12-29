"""Run helper for development: starts the FastAPI app with Uvicorn using default host/port.

Prints the local URLs for the app and Swagger docs when starting (useful on Windows).
"""

if __name__ == "__main__":
    import os
    import uvicorn

    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))

    display_host = HOST if HOST != "0.0.0.0" else "localhost"
    app_url = f"http://{display_host}:{PORT}"
    docs_url = f"{app_url}/docs"

    print("Starting Gerenciador de Estoque (development mode)")
    print(f"App: {app_url}")
    print(f"Docs: {docs_url}")

    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)
