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

            # Placeholders for new variables used in additional actions
            pg_one_fico_range = "700-749"
            borrower_type = "Individual"
            entity_name = "Test Entity LLC"
            trade_name = "Test Trade Name"
            entity_type = "LLC"
            date_of_formation = "01/01/2020"
            state_of_formation = "New Jersey"
            ein_number = "12-3456789"
            business_phone = "7325551234"
            entity_address = "123 Main St"
            entity_city = "Morganville"
            entity_state = "New Jersey"
            entity_zip = "07751"
            member_name_zero = "Member Zero"
            member_title_zero = "Manager"
            member_ownership_zero = "100"
            member_address_zero = "123 Main St"
            member_cell_zero = "7325550000"
            member_ssn_zero = "111223333"
            member_dob_zero = "01/01/1980"
            member_email_zero = "member0@example.com"
            member_fico_score_zero = "720"
            member_guarantor_zero = "guarantor_0"
            member_citizenship_zero = "citizenship_0"
            member_name_one = "Member One"
            member_title_one = "Member"
            member_ownership_one = "50"
            member_address_one = "124 Main St"
            member_cell_one = "7325550001"
            member_ssn_one = "111223334"
            member_dob_one = "02/02/1981"
            member_email_one = "member1@example.com"
            member_fico_score_one = "710"
            member_guarantor_one = "guarantor_1"
            member_citizenship_one = "citizenship_1"
            member_name_two = "Member Two"
            member_title_two = "Member"
            member_ownership_two = "25"
            member_address_two = "125 Main St"
            member_cell_two = "7325550002"
            member_ssn_two = "111223335"
            member_dob_two = "03/03/1982"
            member_email_two = "member2@example.com"
            member_fico_score_two = "705"
            member_guarantor_two = "guarantor_2"
            member_citizenship_two = "citizenship_2"
            member_name_three = "Member Three"
            member_title_three = "Member"
            member_ownership_three = "25"
            member_address_three = "126 Main St"
            member_cell_three = "7325550003"
            member_ssn_three = "111223336"
            member_dob_three = "04/04/1983"
            member_email_three = "member3@example.com"
            member_fico_score_three = "700"
            member_guarantor_three = "guarantor_3"
            member_citizenship_three = "citizenship_3"
            member_name_four = "Member Four"
            member_title_four = "Member"
            member_ownership_four = "10"
            member_address_four = "127 Main St"
            member_cell_four = "7325550004"
            member_ssn_four = "111223337"
            member_dob_four = "05/05/1984"
            member_email_four = "member4@example.com"
            member_fico_score_four = "695"
            member_guarantor_four = "guarantor_4"
            member_citizenship_four = "citizenship_4"
            member_name_five = "Member Five"
            member_title_five = "Member"
            member_ownership_five = "5"
            member_address_five = "128 Main St"
            member_cell_five = "7325550005"
            member_ssn_five = "111223338"
            member_dob_five = "06/06/1985"
            member_email_five = "member5@example.com"
            member_fico_score_five = "690"
            member_guarantor_five = "guarantor_5"
            member_citizenship_five = "citizenship_5"

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

            # Select FICO range
            page.select_option('#borCreditScoreRange', value=pg_one_fico_range)
            print(f"[INFO] FICO range '{pg_one_fico_range}' selected.")

            # Select borrower type
            page.select_option('#borrowerType', value=borrower_type)
            print(f"[INFO] Borrower type '{borrower_type}' selected.")

            # Fill entity name
            page.fill('#entityName', value=entity_name)
            print(f"[INFO] Entity name '{entity_name}' filled.")

            # Fill trade name
            page.fill('#tradeName', value=trade_name)
            print(f"[INFO] Trade name '{trade_name}' filled.")

            # Select entity type
            page.select_option('#entityType', value=entity_type)
            print(f"[INFO] Entity type '{entity_type}' selected.")

            # Fill date of formation
            page.fill('#dateOfFormation', value=date_of_formation)
            print(f"[INFO] Date of formation '{date_of_formation}' filled.")
            page.click('body', position={'x': 10, 'y': 10})

            # Select state of formation
            page.select_option('#entityStateOfFormation', value=state_of_formation)
            print(f"[INFO] State of formation '{state_of_formation}' selected.")

            # Fill EIN number
            page.fill('#ENINo', value=ein_number)
            print(f"[INFO] EIN number '{ein_number}' filled.")

            # Fill business phone
            page.fill('#businessPhone', value=business_phone)
            print(f"[INFO] Business phone '{business_phone}' filled.")

            # Fill entity address
            page.fill('#entityAddress', value=entity_address)
            print(f"[INFO] Entity address '{entity_address}' filled.")

            # Fill entity city
            page.fill('#entityCity', value=entity_city)
            print(f"[INFO] Entity city '{entity_city}' filled.")

            # Select entity state
            page.select_option('#entityState', value=entity_state)
            print(f"[INFO] Entity state '{entity_state}' selected.")

            # Fill entity zip
            page.fill('#entityZip', value=entity_zip)
            print(f"[INFO] Entity zip '{entity_zip}' filled.")

            # Fill member 0 fields
            page.fill('#memberName0', value=member_name_zero)
            print(f"[INFO] Member 0 name '{member_name_zero}' filled.")
            page.fill('#memberTitle0', value=member_title_zero)
            print(f"[INFO] Member 0 title '{member_title_zero}' filled.")
            page.fill('#memberOwnership0', value=member_ownership_zero)
            print(f"[INFO] Member 0 ownership '{member_ownership_zero}' filled.")
            page.fill('#memberAddress0', value=member_address_zero)
            print(f"[INFO] Member 0 address '{member_address_zero}' filled.")
            page.fill('#memberCell0', value=member_cell_zero)
            print(f"[INFO] Member 0 cell '{member_cell_zero}' filled.")
            page.fill('#memberSSN0', value=member_ssn_zero)
            print(f"[INFO] Member 0 SSN '{member_ssn_zero}' filled.")
            page.fill('#memberDOB0', value=member_dob_zero)
            print(f"[INFO] Member 0 DOB '{member_dob_zero}' filled.")
            page.click('body', position={'x': 10, 'y': 10})
            page.fill('#memberEmail0', value=member_email_zero)
            print(f"[INFO] Member 0 email '{member_email_zero}' filled.")
            page.fill('#memberCreditScore0', value=member_fico_score_zero)
            print(f"[INFO] Member 0 FICO score '{member_fico_score_zero}' filled.")
            page.wait_for_selector(f'label[for="{member_guarantor_zero}"]', timeout=10000)
            page.click(f'label[for="{member_guarantor_zero}"]')
            print(f"[INFO] Member 0 guarantor '{member_guarantor_zero}' selected.")
            page.wait_for_selector(f'label[for="{member_citizenship_zero}"]', timeout=10000)
            page.click(f'label[for="{member_citizenship_zero}"]')
            print(f"[INFO] Member 0 citizenship '{member_citizenship_zero}' selected.")
            page.click('span[onclick*="showAndHidePropertyValuationInfo"]')
            print(f"[INFO] Add member 1 button clicked.")
            page.wait_for_timeout(1000)

            # Repeat for member 1
            page.fill('#memberName1', value=member_name_one)
            print(f"[INFO] Member 1 name '{member_name_one}' filled.")
            page.fill('#memberTitle1', value=member_title_one)
            print(f"[INFO] Member 1 title '{member_title_one}' filled.")
            page.fill('#memberOwnership1', value=member_ownership_one)
            print(f"[INFO] Member 1 ownership '{member_ownership_one}' filled.")
            page.fill('#memberAddress1', value=member_address_one)
            print(f"[INFO] Member 1 address '{member_address_one}' filled.")
            page.fill('#memberCell1', value=member_cell_one)
            print(f"[INFO] Member 1 cell '{member_cell_one}' filled.")
            page.fill('#memberSSN1', value=member_ssn_one)
            print(f"[INFO] Member 1 SSN '{member_ssn_one}' filled.")
            page.fill('#memberDOB1', value=member_dob_one)
            print(f"[INFO] Member 1 DOB '{member_dob_one}' filled.")
            page.click('body', position={'x': 10, 'y': 10})
            page.fill('#memberEmail1', value=member_email_one)
            print(f"[INFO] Member 1 email '{member_email_one}' filled.")
            page.fill('#memberCreditScore1', value=member_fico_score_one)
            print(f"[INFO] Member 1 FICO score '{member_fico_score_one}' filled.")
            if member_guarantor_one:
                page.wait_for_selector(f'label[for="{member_guarantor_one}"]', timeout=10000)
                page.click(f'label[for="{member_guarantor_one}"]')
                print(f"[INFO] Member 1 guarantor '{member_guarantor_one}' selected.")
            if member_citizenship_one:
                page.wait_for_selector(f'label[for="{member_citizenship_one}"]', timeout=10000)
                page.click(f'label[for="{member_citizenship_one}"]')
                print(f"[INFO] Member 1 citizenship '{member_citizenship_one}' selected.")
            page.click('span[onclick*="showAndHidePropertyValuationInfo"]')
            print(f"[INFO] Add member 2 button clicked.")
            page.wait_for_timeout(1000)

            # Repeat for member 2
            page.fill('#memberName2', value=member_name_two)
            print(f"[INFO] Member 2 name '{member_name_two}' filled.")
            page.fill('#memberTitle2', value=member_title_two)
            print(f"[INFO] Member 2 title '{member_title_two}' filled.")
            page.fill('#memberOwnership2', value=member_ownership_two)
            print(f"[INFO] Member 2 ownership '{member_ownership_two}' filled.")
            page.fill('#memberAddress2', value=member_address_two)
            print(f"[INFO] Member 2 address '{member_address_two}' filled.")
            page.fill('#memberCell2', value=member_cell_two)
            print(f"[INFO] Member 2 cell '{member_cell_two}' filled.")
            page.fill('#memberSSN2', value=member_ssn_two)
            print(f"[INFO] Member 2 SSN '{member_ssn_two}' filled.")
            page.fill('#memberDOB2', value=member_dob_two)
            print(f"[INFO] Member 2 DOB '{member_dob_two}' filled.")
            page.click('body', position={'x': 10, 'y': 10})
            page.fill('#memberEmail2', value=member_email_two)
            print(f"[INFO] Member 2 email '{member_email_two}' filled.")
            page.fill('#memberCreditScore2', value=member_fico_score_two)
            print(f"[INFO] Member 2 FICO score '{member_fico_score_two}' filled.")
            if member_guarantor_two:
                page.wait_for_selector(f'label[for="{member_guarantor_two}"]', timeout=10000)
                page.click(f'label[for="{member_guarantor_two}"]')
                print(f"[INFO] Member 2 guarantor '{member_guarantor_two}' selected.")
            if member_citizenship_two:
                page.wait_for_selector(f'label[for="{member_citizenship_two}"]', timeout=10000)
                page.click(f'label[for="{member_citizenship_two}"]')
                print(f"[INFO] Member 2 citizenship '{member_citizenship_two}' selected.")
            page.click('span[onclick*="showAndHidePropertyValuationInfo"]')
            print(f"[INFO] Add member 3 button clicked.")
            page.wait_for_timeout(1000)

            # Repeat for member 3
            page.fill('#memberName3', value=member_name_three)
            print(f"[INFO] Member 3 name '{member_name_three}' filled.")
            page.fill('#memberTitle3', value=member_title_three)
            print(f"[INFO] Member 3 title '{member_title_three}' filled.")
            page.fill('#memberOwnership3', value=member_ownership_three)
            print(f"[INFO] Member 3 ownership '{member_ownership_three}' filled.")
            page.fill('#memberAddress3', value=member_address_three)
            print(f"[INFO] Member 3 address '{member_address_three}' filled.")
            page.fill('#memberCell3', value=member_cell_three)
            print(f"[INFO] Member 3 cell '{member_cell_three}' filled.")
            page.fill('#memberSSN3', value=member_ssn_three)
            print(f"[INFO] Member 3 SSN '{member_ssn_three}' filled.")
            page.fill('#memberDOB3', value=member_dob_three)
            print(f"[INFO] Member 3 DOB '{member_dob_three}' filled.")
            page.click('body', position={'x': 10, 'y': 10})
            page.fill('#memberEmail3', value=member_email_three)
            print(f"[INFO] Member 3 email '{member_email_three}' filled.")
            page.fill('#memberCreditScore3', value=member_fico_score_three)
            print(f"[INFO] Member 3 FICO score '{member_fico_score_three}' filled.")
            if member_guarantor_three:
                page.wait_for_selector(f'label[for="{member_guarantor_three}"]', timeout=10000)
                page.click(f'label[for="{member_citizenship_three}"]')
                print(f"[INFO] Member 3 guarantor '{member_guarantor_three}' selected.")
            if member_citizenship_three:
                page.wait_for_selector(f'label[for="{member_citizenship_three}"]', timeout=10000)
                page.click(f'label[for="{member_citizenship_three}"]')
                print(f"[INFO] Member 3 citizenship '{member_citizenship_three}' selected.")
            page.click('span[onclick*="showAndHidePropertyValuationInfo"]')
            print(f"[INFO] Add member 4 button clicked.")
            page.wait_for_timeout(1000)

            # Repeat for member 4
            page.fill('#memberName4', value=member_name_four)
            print(f"[INFO] Member 4 name '{member_name_four}' filled.")
            page.fill('#memberTitle4', value=member_title_four)
            print(f"[INFO] Member 4 title '{member_title_four}' filled.")
            page.fill('#memberOwnership4', value=member_ownership_four)
            print(f"[INFO] Member 4 ownership '{member_ownership_four}' filled.")
            page.fill('#memberAddress4', value=member_address_four)
            print(f"[INFO] Member 4 address '{member_address_four}' filled.")
            page.fill('#memberCell4', value=member_cell_four)
            print(f"[INFO] Member 4 cell '{member_cell_four}' filled.")
            page.fill('#memberSSN4', value=member_ssn_four)
            print(f"[INFO] Member 4 SSN '{member_ssn_four}' filled.")
            page.fill('#memberDOB4', value=member_dob_four)
            print(f"[INFO] Member 4 DOB '{member_dob_four}' filled.")
            page.click('body', position={'x': 10, 'y': 10})
            page.fill('#memberEmail4', value=member_email_four)
            print(f"[INFO] Member 4 email '{member_email_four}' filled.")
            page.fill('#memberCreditScore4', value=member_fico_score_four)
            print(f"[INFO] Member 4 FICO score '{member_fico_score_four}' filled.")
            if member_guarantor_four:
                page.wait_for_selector(f'label[for="{member_guarantor_four}"]', timeout=10000)
                page.click(f'label[for="{member_guarantor_four}"]')
                print(f"[INFO] Member 4 guarantor '{member_guarantor_four}' selected.")
            if member_citizenship_four:
                page.wait_for_selector(f'label[for="{member_citizenship_four}"]', timeout=10000)
                page.click(f'label[for="{member_citizenship_four}"]')
                print(f"[INFO] Member 4 citizenship '{member_citizenship_four}' selected.")
            page.click('span[onclick*="showAndHidePropertyValuationInfo"]')
            print(f"[INFO] Add member 5 button clicked.")
            page.wait_for_timeout(1000)

            # Repeat for member 5
            page.fill('#memberName5', value=member_name_five)
            print(f"[INFO] Member 5 name '{member_name_five}' filled.")
            page.fill('#memberTitle5', value=member_title_five)
            print(f"[INFO] Member 5 title '{member_title_five}' filled.")
            page.fill('#memberOwnership5', value=member_ownership_five)
            print(f"[INFO] Member 5 ownership '{member_ownership_five}' filled.")
            page.fill('#memberAddress5', value=member_address_five)
            print(f"[INFO] Member 5 address '{member_address_five}' filled.")
            page.fill('#memberCell5', value=member_cell_five)
            print(f"[INFO] Member 5 cell '{member_cell_five}' filled.")
            page.fill('#memberSSN5', value=member_ssn_five)
            print(f"[INFO] Member 5 SSN '{member_ssn_five}' filled.")
            page.fill('#memberDOB5', value=member_dob_five)
            print(f"[INFO] Member 5 DOB '{member_dob_five}' filled.")
            page.click('body', position={'x': 10, 'y': 10})
            page.fill('#memberEmail5', value=member_email_five)
            print(f"[INFO] Member 5 email '{member_email_five}' filled.")
            page.fill('#memberCreditScore5', value=member_fico_score_five)
            print(f"[INFO] Member 5 FICO score '{member_fico_score_five}' filled.")
            if member_guarantor_five:
                page.wait_for_selector(f'label[for="{member_guarantor_five}"]', timeout=10000)
                page.click(f'label[for="{member_guarantor_five}"]')
                print(f"[INFO] Member 5 guarantor '{member_guarantor_five}' selected.")
            if member_citizenship_five:
                page.wait_for_selector(f'label[for="{member_citizenship_five}"]', timeout=10000)
                page.click(f'label[for="{member_citizenship_five}"]')
                print(f"[INFO] Member 5 citizenship '{member_citizenship_five}' selected.")

            # Additional actions for guarantors and other fields would follow the same pattern...

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
