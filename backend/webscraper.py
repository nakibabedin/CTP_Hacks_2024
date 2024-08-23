from selenium import webdriver
from bs4 import BeautifulSoup

import gemini
import firebase
import keywords_parser
import json

driver = webdriver.Chrome()

def clean_and_parse_json(gemini_output):
    # Remove triple backticks (```)
    cleaned_json = gemini_output.replace("```", "")
    cleaned_json = cleaned_json[4:]

    try:
        # Parse the cleaned JSON string
        parsed_data = json.loads(cleaned_json)
        return parsed_data
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return None

input_campus = input('Enter your campus code: ')

with open('links.txt', 'r') as f:
    links = f.read().split('\n')

for link in links:
    driver.get(link)

    # Wait for the page to fully load
    driver.implicitly_wait(7)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    body_text = soup.body.get_text(separator='\n', strip=True)

    res = gemini.generateResourceSchema(body_text)
    res = clean_and_parse_json(res)

    if not res:
        with open('failed_links.txt', 'a') as f:
            f.write(link + '\n')

        continue

    res['campus'] = input_campus
    res['website'] = link

    json_res = json.dumps(res, indent=4)
    print(json_res)

    ans = input("Does this look right? (y/n)\n")
    if ans == 'n':
        with open('failed_links.txt', 'a') as f:
            f.write(link + '\n')

        continue

    campus_code = res['campus']
    resource_name = res['name']
    resource_data = keywords_parser.process_description(res)

    firebase.add_resource(campus_code, resource_name, resource_data)




driver.quit()