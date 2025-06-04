"""Backend Server Fast API."""

"""
Calls the core agents:
Embedding Agent → turns image into vector using CLIP.
Vector Match Agent → searches FAISS for similar images.
Metadata Agent → fetches mood/style data from JSON.
Returns → matching partners and reasons as JSON response.
"""
from fastapi import FastAPI, HTTPException, Header, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse
import uvicorn

# Rate limiter imports
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from helpers import JsonHelper
from configs import MainConfigs

# Create FastAPI app in main scope


METADATA = JsonHelper.get_json_data("project_metadata.json")
app = FastAPI(**METADATA["project_metadata"])

# Rate limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


_partner_metadata = JsonHelper.get_json_data("partner_metadata.json")
_id_to_partner = JsonHelper.get_json_data("id_to_partner.json")


@app.get("/", tags=["System"])
@limiter.limit("60/minute")
def read_root(request: Request):
    """Redirect to docs on root."""
    return {"message": "Agentic AI Image Matcher is running with FastAPI!"}


if __name__ == "__main__":
    run_config = MainConfigs.get_run_config()
    uvicorn.run("app:app", **run_config)
