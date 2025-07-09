import sys
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import json
import tempfile

def main(branch_id, username, password, *args):
    print(f"[DEBUG] Username repr: {repr(username)}", flush=True)
    print(f"[DEBUG] Password repr: {repr(password)}", flush=True)
    url = "https://app.brrrr.com/backoffice/LMRequest.php?eOpt=0&cliType=PC&tabOpt=QAPP&moduleCode=HMLO&supp=help"
    print(f"[INFO] Launching browser and navigating to {url}", flush=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        try:
            print("[DEBUG] Waiting for username field...", flush=True)
            page.wait_for_selector('input#userName', timeout=10000)
            print("[DEBUG] Username field found, filling...", flush=True)
            email_field = page.locator('input#userName')
            email_field.click()
            email_field.fill(username)
            print("[DEBUG] Username filled!", flush=True)
            pwd_input = page.locator('input#pwd')
            pwd_input.wait_for(timeout=10000)
            pwd_input.click()
            pwd_input.fill(password)
            print("[DEBUG] Password filled!", flush=True)
            print("[DEBUG] Clicking login button...", flush=True)
            page.click("button#submitbutton")
            print("[DEBUG] Login button clicked!", flush=True)
            # Optionally, wait for redirect or some confirmation
            page.wait_for_timeout(2000)
        except PlaywrightTimeoutError as e:
            print(f"[ERROR] Timeout waiting for element: {e}", flush=True)
        except Exception as e:
            print(f"[ERROR] {e}", flush=True)
        browser.close()


# --- FastAPI server entry ---
from fastapi import FastAPI, Request
import uvicorn
from starlette.concurrency import run_in_threadpool

app = FastAPI()

@app.post("/run-playwright")
async def run_playwright(request: Request):
    data = await request.json()
    args = [
        data.get("branch_id", ""),
        data.get("username", ""),
        data.get("password", "")
    ]
    print(f"[DEBUG] Args list: {args}", flush=True)
    with open("/tmp/fastapi_debug.log", "a") as f:
        f.write("ENDPOINT HIT\n")
        f.write(f"ARGS: {args}\n")
        f.flush()
    try:
        print("ARGS:", args, flush=True)
        await run_in_threadpool(main, *args)
    except Exception as e:
        print("ERROR IN MAIN:", e, flush=True)
        raise
    return {"status": "done", "args": args}

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main(*sys.argv[1:])
    else:
        print("Run with FastAPI. Use: uvicorn brrrr_login:app --host 0.0.0.0 --port 8000")
