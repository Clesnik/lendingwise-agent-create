import sys
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import json
import tempfile

def main(username, password):
    print(f"[DEBUG] Username: {username}", flush=True)
    print(f"[DEBUG] Password: {password}", flush=True)
    url = "https://app.brrrr.com/backoffice/LMRequest.php?eOpt=0&cliType=PC&tabOpt=QAPP&moduleCode=HMLO&supp=help"
    print(f"[INFO] Navigating to {url}", flush=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector('input#userName', timeout=10000)
        page.fill('input#userName', username)
        page.fill('input#pwd', password)
        page.click('button#submitbutton')
        print("[INFO] Login attempted", flush=True)
        browser.close()


# --- FastAPI server entry ---
from fastapi import FastAPI, Request
import uvicorn
from starlette.concurrency import run_in_threadpool

app = FastAPI()

@app.post("/run-playwright")
async def run_playwright(request: Request):
    data = await request.json()
    username = data.get("username", "")
    password = data.get("password", "")
    print(f"[DEBUG] Received: {username}, {password}", flush=True)
    await run_in_threadpool(main, username, password)
    return {"status": "done"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("brrrr_login:app", host="0.0.0.0", port=8000, reload=True)
