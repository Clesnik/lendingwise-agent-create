import sys
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import json
import tempfile
import asyncio

def main(username, password):
    print(f"[DEBUG] Username received: {username}", flush=True)
    print(f"[DEBUG] Password received: {password}", flush=True)

    url = "https://app.brrrr.com/backoffice/LMRequest.php?eOpt=0&cliType=PC&tabOpt=QAPP&moduleCode=HMLO&supp=help"
    print(f"[INFO] Navigating to {url}", flush=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        print("[INFO] Page loaded.", flush=True)

        page.wait_for_selector('input#userName', timeout=10000)
        print("[INFO] Found username input.", flush=True)

        page.fill('input#userName', username)
        print(f"[INFO] Filled username input with: {username}", flush=True)

        page.fill('input#pwd', password)
        print(f"[INFO] Filled password input with: {password}", flush=True)

        page.click('button#submitbutton')
        print("[INFO] Clicked login button.", flush=True)

        page.wait_for_timeout(2000)  # optional wait for any response

        browser.close()
        print("[INFO] Browser closed.", flush=True)


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
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, main, username, password)  # run `main` in background
    return {"status": "started"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("brrrr_login:app", host="0.0.0.0", port=8000, reload=True)
