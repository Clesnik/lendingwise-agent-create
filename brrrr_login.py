import sys
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import json
import tempfile
import asyncio

from fastapi import FastAPI, Request, HTTPException
from starlette.concurrency import run_in_threadpool
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

app = FastAPI()

def do_login(username, password):
    if not username or not password:
        raise ValueError("Username and password are required")
    browser = None
    context = None
    page = None
    try:
        print('[PY] Launching browser...', flush=True)
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            print('[PY] Navigating to login page...', flush=True)
            page.goto('https://app.brrrr.com/backoffice/LMRequest.php?eOpt=0&cliType=PC&tabOpt=QAPP&moduleCode=HMLO&supp=help', wait_until='domcontentloaded', timeout=15000)

            print('[PY] Waiting for username field...', flush=True)
            page.wait_for_selector('input#userName', timeout=10000)
            print('[PY] Filling username...', flush=True)
            page.fill('input#userName', username)

            print('[PY] Waiting for password field...', flush=True)
            page.wait_for_selector('input#pwd', timeout=10000)
            print('[PY] Filling password...', flush=True)
            page.fill('input#pwd', password)

            print('[PY] Waiting for login button...', flush=True)
            page.wait_for_selector('button#submitbutton', timeout=10000)
            print('[PY] Clicking login button...', flush=True)
            page.click('button#submitbutton')

            # Optionally, wait for a post-login element or confirmation
            print('[PY] Waiting for post-login page...', flush=True)
            page.wait_for_timeout(2000)

            print('[PY] Login attempted.', flush=True)
            return {"result": "Login attempted"}
    except PlaywrightTimeoutError as e:
        print('[PY] Timeout error:', e, flush=True)
        return {"error": f"Timeout error: {e}"}
    except Exception as e:
        print('[PY] General error:', e, flush=True)
        return {"error": str(e)}
    finally:
        if page:
            try:
                page.close()
            except Exception:
                pass
        if context:
            try:
                context.close()
            except Exception:
                pass
        if browser:
            try:
                browser.close()
                print('[PY] Browser closed.', flush=True)
            except Exception:
                pass

@app.post("/run-playwright")
async def run_playwright(request: Request):
    data = await request.json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        raise HTTPException(status_code=400, detail="username and password required")
    result = await run_in_threadpool(do_login, username, password)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("brrrr_login:app", host="0.0.0.0", port=8000, reload=True)
