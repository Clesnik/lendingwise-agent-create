from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.post("/run-playwright")
def run_playwright():
    result = subprocess.run(["python3", "brrrr_login.py"], capture_output=True, text=True)
    return {"stdout": result.stdout, "stderr": result.stderr}