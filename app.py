"""Backend Server Fast API."""

"""
Calls the core agents:
Embedding Agent → turns image into vector using CLIP.
Vector Match Agent → searches FAISS for similar images.
Metadata Agent → fetches mood/style data from JSON.
Returns → matching partners and reasons as JSON response.
"""
import os
from fastapi import FastAPI, HTTPException, Header, Request, Depends, File, UploadFile
from fastapi.responses import JSONResponse, RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

# Rate limiter imports
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from agents import MatcherAgent
from helpers import JsonHelper, ImageHelper

from configs import MainConfigs

# Create FastAPI app in main scope

if MainConfigs.is_dev_env():
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

METADATA = JsonHelper.get_json_data("project_metadata.json")
app = FastAPI(**METADATA["project_metadata"])
matcher_agent = MatcherAgent()

templates = Jinja2Templates(directory="templates")

# Rate limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# _partner_metadata = JsonHelper.get_json_data("partner_metadata.json")
# _id_to_partner = JsonHelper.get_json_data("id_to_partner.json")


@app.get("/", tags=["System"])
async def home():
    """Redirect to upload page."""
    return RedirectResponse(url="/upload")


@app.get("/upload", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})


@app.post("/upload")
@limiter.limit("60/minute")
async def upload_image(request: Request, image: UploadFile = File(...)):
    image_pil = await ImageHelper.read_image(image)
    matches = matcher_agent.match(image_pil)
    return templates.TemplateResponse("results.html", {
        "request": request,
        "matches": matches
    })


if __name__ == "__main__":
    run_config = MainConfigs.get_run_config()
    uvicorn.run("app:app", **run_config)
