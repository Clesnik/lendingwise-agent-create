import sys
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

def main(branch_id, username, password):
    url = "https://app.brrrr.com/backoffice/LMRequest.php?eOpt=0&cliType=PC&tabOpt=QAPP&moduleCode=HMLO&supp=help"
    print(f"[INFO] Launching browser and navigating to {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        try:
            # Wait for login form
            page.wait_for_selector('input#userName', timeout=10000)
            print(f"[INFO] Filling in username: {username}")
            email_field = page.locator('input#userName')
            email_field.click()
            email_field.fill(username)
            # Wait for and fill the password
            pwd_input = page.locator('input#pwd')
            pwd_input.wait_for(timeout=10000)
            pwd_input.click()
            pwd_input.fill(password)
            # Click the Login button
            print("[INFO] Submitting login form")
            page.click("button#submitbutton")
            # Wait for redirect to backoffice
            page.wait_for_url("https://app.brrrr.com/backoffice/LMRequest*", timeout=15000)
            print("[INFO] Login successful, now selecting branch")
            page.wait_for_selector('select#branchId', timeout=10000)
            result = page.select_option('select#branchId', value=branch_id)
            if not result or result[0] != branch_id:
                print(f"[ERROR] Branch ID '{branch_id}' not found in dropdown!")
            else:
                print(f"[SUCCESS] Branch ID '{branch_id}' selected!")
        except PlaywrightTimeoutError as e:
            print(f"[ERROR] Timeout waiting for element: {e}")
        except Exception as e:
            print(f"[ERROR] {e}")
        browser.close()

if __name__ == "__main__":
    # For testing, use hardcoded credentials and branch_id
    username = "clesnik@brrrr.com"
    password = "Lesnik$"
    branch_id = "BrrrrLoans"
    main(branch_id, username, password) 