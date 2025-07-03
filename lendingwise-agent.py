from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import webbrowser
import subprocess
from typing import Dict, Any
import logging
from playwright.sync_api import sync_playwright

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="LendingWise Agent",
    description="A FastAPI service for opening URLs and managing browser interactions",
    version="1.0.0"
)

URL_TO_OPEN = "https://app.brrrr.com/backoffice/LMRequest.php?eOpt=0&cliType=PC&tabOpt=QAPP&moduleCode=HMLO&supp=help"


class ResponseModel(BaseModel):
    status: str
    message: str


@app.get("/", response_model=ResponseModel)
def read_root() -> ResponseModel:
    """Health check endpoint."""
    return ResponseModel(status="success", message="Server is running")


@app.post("/open", response_model=ResponseModel)
def open_url() -> ResponseModel:
    """Open the configured URL in the system browser."""
    try:
        webbrowser.open(URL_TO_OPEN)
        logger.info(f"Successfully opened URL: {URL_TO_OPEN}")
        return ResponseModel(status="success", message="Opened in browser")
    except Exception as e:
        logger.error(f"Failed to open URL: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to open URL: {str(e)}")


@app.post("/open-playwright", response_model=ResponseModel)
def open_with_playwright(branch_id: str = Body(..., embed=True)) -> ResponseModel:
    """Trigger Playwright script for browser automation."""
    try:
        subprocess.Popen(["python", "brrrr_login.py", branch_id])
        logger.info(f"Triggered Playwright script with branch_id={branch_id}")
        return ResponseModel(status="success", message="Triggered Playwright script")
    except FileNotFoundError:
        logger.error("Playwright script 'brrrr_login.py' not found")
        raise HTTPException(status_code=404, detail="Playwright script not found")
    except Exception as e:
        logger.error(f"Failed to run Playwright script: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to run Playwright script: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)