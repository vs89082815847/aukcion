from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI(title="NeoAuction Core Engine")

app.mount("/static", StaticFiles(directory="."), name="static")
@app.get("/", response_class=HTMLResponse)
def serve_index():
    return FileResponse("index.html")
