# LendingWise Agent

A FastAPI service for opening URLs and managing browser interactions.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Install Playwright browsers (optional, for browser automation):
   ```bash
   playwright install
   ```

## Running the Application

Start the server:
```bash
python lendingwise-agent.py
```

The server will run on `http://localhost:8001`

## API Endpoints

- `GET /` - Health check endpoint
- `POST /open` - Opens the configured URL in the system browser
- `POST /open-playwright` - Triggers Playwright script for browser automation

## Testing the API

```bash
# Health check
curl http://localhost:8001/

# Open URL in browser
curl -X POST http://localhost:8001/open

# Trigger Playwright script
curl -X POST http://localhost:8001/open-playwright
```

## VS Code Configuration

The `.vscode/settings.json` file is configured to use Pylance as the Python language server. If you're still seeing Pylance errors:

1. Make sure the Pylance extension is installed in VS Code
2. Reload VS Code window (Cmd+Shift+P → "Developer: Reload Window")
3. Select the correct Python interpreter (Cmd+Shift+P → "Python: Select Interpreter")

## Dependencies

- FastAPI - Web framework
- Uvicorn - ASGI server
- Pydantic - Data validation
- Playwright - Browser automation (optional) 