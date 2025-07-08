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
            
            # Additional borrower information variables
            pg_one_work = "7329259148"
            pg_one_street = "15 Burr Ave"
            pg_one_unit = "1"
            pg_one_city = "Morganville"
            pg_one_state = "New Jersey"
            pg_one_zip = "07751"
            pg_one_county = "Monmouth"
            pg_one_country = "United States"
            mailing_street = "15 Burr Ave"
            mailing_unit = "1"
            mailing_city = "Morganville"
            mailing_state = "New Jersey"
            mailing_zip = "07751"
            mailing_country = "United States"
            pg_one_dob = "01/18/2001"
            pg_one_ssn = "123456789"
            pg_one_marital_status = "maritalStatus_1"
            pg_one_citizenship = "borrowerCitizenship_0"
            pg_one_mid_fico = "720"

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
            print(f"[INFO] Property process '{prop_process}' selected.")

            page.select_option('#primaryStatus', value=primary_status)
            print(f"[INFO] Primary status '{primary_status}' selected.")

            # Fill referral source fields
            page.fill('#leadSource', value=lead_source)
            print(f"[INFO] Lead source '{lead_source}' filled.")

            page.fill('#referringParty', value=referring_party)
            print(f"[INFO] Referring party '{referring_party}' filled.")

            # Fill borrower fields
            page.fill('#borrowerFName', value=pg_one_fname)
            print(f"[INFO] Borrower first name '{pg_one_fname}' filled.")

            page.fill('#borrowerMName', value=pg_one_mname)
            print(f"[INFO] Borrower middle name '{pg_one_mname}' filled.")

            page.fill('#borrowerLName', value=pg_one_lname)
            print(f"[INFO] Borrower last name '{pg_one_lname}' filled.")

            page.fill('#borrowerEmail', value=pg_one_email)
            print(f"[INFO] Borrower email '{pg_one_email}' filled.")

            page.fill('#cellNo', value=pg_one_cell)
            print(f"[INFO] Borrower cell '{pg_one_cell}' filled.")

            # Fill work number
            page.fill('#workNumber', value=pg_one_work)
            print(f"[INFO] Work number '{pg_one_work}' filled.")

            # Fill present address fields
            page.fill('#presentAddress', value=pg_one_street)
            print(f"[INFO] Present address '{pg_one_street}' filled.")

            page.fill('#presentUnit', value=pg_one_unit)
            print(f"[INFO] Present unit '{pg_one_unit}' filled.")

            page.fill('#presentCity', value=pg_one_city)
            print(f"[INFO] Present city '{pg_one_city}' filled.")

            page.select_option('#presentState', value=pg_one_state)
            print(f"[INFO] Present state '{pg_one_state}' selected.")

            page.fill('#presentZip', value=pg_one_zip)
            print(f"[INFO] Present zip '{pg_one_zip}' filled.")

            page.select_option('#presentCounty', value=pg_one_county)
            print(f"[INFO] Present county '{pg_one_county}' selected.")

            page.select_option('#presentCountry', value=pg_one_country)
            print(f"[INFO] Present country '{pg_one_country}' selected.")

            # Fill mailing address fields
            page.fill('#mailingAddress', value=mailing_street)
            print(f"[INFO] Mailing address '{mailing_street}' filled.")

            page.fill('#mailingUnit', value=mailing_unit)
            print(f"[INFO] Mailing unit '{mailing_unit}' filled.")

            page.fill('#mailingCity', value=mailing_city)
            print(f"[INFO] Mailing city '{mailing_city}' filled.")

            page.select_option('#mailingState', value=mailing_state)
            print(f"[INFO] Mailing state '{mailing_state}' selected.")

            page.fill('#mailingZip', value=mailing_zip)
            print(f"[INFO] Mailing zip '{mailing_zip}' filled.")

            page.select_option('#mailingCountry', value=mailing_country)
            print(f"[INFO] Mailing country '{mailing_country}' selected.")

            # Fill personal information
            page.fill('#borrowerDOB', value=pg_one_dob)
            print(f"[INFO] Date of birth '{pg_one_dob}' filled.")
            page.click('body', position={'x': 10, 'y': 10})

            page.fill('#ssn', value=pg_one_ssn)
            print(f"[INFO] SSN '{pg_one_ssn}' filled.")

            # Select marital status
            page.wait_for_selector(f'label[for="{pg_one_marital_status}"]', timeout=10000)
            page.click(f'label[for="{pg_one_marital_status}"]')
            print(f"[INFO] Marital status '{pg_one_marital_status}' selected.")

            # Select citizenship status
            page.wait_for_selector(f'label[for="{pg_one_citizenship}"]', timeout=10000)
            page.click(f'label[for="{pg_one_citizenship}"]')
            print(f"[INFO] Citizenship status '{pg_one_citizenship}' selected.")

            # Fill FICO score
            page.fill('#midFicoScore', value=pg_one_mid_fico)
            print(f"[INFO] Mid FICO score '{pg_one_mid_fico}' filled.")

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
