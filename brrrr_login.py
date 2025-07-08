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
            # Debug: Print all options in the branch dropdown
            branch_options = page.query_selector_all('select#branchId option')
            print("[DEBUG] Available branches:")
            for option in branch_options:
                print(option.inner_text())
            result = page.select_option('select#branchId', value=branch_id)
            if not result or result[0] != branch_id:
                print(f"[ERROR] Branch ID '{branch_id}' not found in dropdown!")
            else:
                print(f"[SUCCESS] Branch ID '{branch_id}' selected!")
                page.wait_for_load_state('networkidle', timeout=10000)
                page.wait_for_selector('select#secondaryAgentId', timeout=20000)
                secondary_options = page.query_selector_all('select#secondaryAgentId option')
                print("[DEBUG] Available secondary agents:")
                for option in secondary_options:
                    print(option.inner_text())

            # --- Additional actions after branch selection ---
            secondary_agent = "Chris Lesnik - Clesnik@brrrr.com"
            loan_program = "DSCR - Rental - Long Term (LTR)"
            internal_program = "BPL - DSCR - 1-8 - Purchase"
            prop_process = "Have Property Under Contract"
            primary_status = "83239"
            lead_source = "Broker"
            referring_party = "Allen Wu"
            pg_one_fname = "Chris"
            pg_one_mname = "George"
            pg_one_lname = "Lesnik"
            pg_one_email = "cglesnik@gmail.com"
            pg_one_cell = "7328040939"

            # Select secondary agent by passed-in label
            result = page.select_option('select#secondaryAgentId', label=secondary_agent)
            print(f"[DEBUG] Selected secondary agent result: {result}")

            # Open and select loan program
            print(f"[INFO] Selecting loan program: {loan_program}")
            page.wait_for_selector('div#LMRClientType_chosen', timeout=10000)
            page.click('div#LMRClientType_chosen')
            page.click(f'ul.chosen-results li.active-result:has-text("{loan_program}")')
            print("[INFO] Loan program selected.")

            # Open the "Select Internal Loan Program" Chosen multi-select
            print(f"[INFO] Selecting internal program: {internal_program}")
            page.wait_for_selector('div#LMRInternalLoanProgram_chosen', timeout=10000)
            page.click('div#LMRInternalLoanProgram_chosen')
            page.click(f'ul.chosen-results li.active-result:has-text("{internal_program}")')
            print("[INFO] Internal program selected.")

            # Select property process and primary status
            page.select_option('#propDetailsProcess', value=prop_process)
            page.select_option('#primaryStatus', value=primary_status)

            # Fill referral source fields
            page.fill('#leadSource', value=lead_source)
            page.fill('#referringParty', value=referring_party)

            # Fill borrower fields
            page.fill('#borrowerFName', value=pg_one_fname)
            page.fill('#borrowerMName', value=pg_one_mname)
            page.fill('#borrowerLName', value=pg_one_lname)
            page.fill('#borrowerEmail', value=pg_one_email)
            page.fill('#cellNo', value=pg_one_cell)

        except PlaywrightTimeoutError as e:
            print(f"[ERROR] Timeout waiting for element: {e}")
        except Exception as e:
            print(f"[ERROR] {e}")
        browser.close()

if __name__ == "__main__":
    # For testing, use hardcoded credentials and branch_id
    username = "clesnik@brrrr.com"
    password = "Lesnik$"
    branch_id = "c533ddbb5dd3a1f2"
    main(branch_id, username, password)
