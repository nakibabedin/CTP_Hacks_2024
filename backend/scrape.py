import gemini
import firebase
import keywords_parser
import json
# from json_checker import Checker

data = open('sample.txt', 'r').read()

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

res = gemini.generateResourceSchema(data)
res = clean_and_parse_json(res)

print(res)

# TODO: Add URL back to the resource

# TODO: Manually validate the resource

campus_code = res['campus']
resource_name = res['name']
resource_data = keywords_parser.process_description(res)

firebase.add_resource(campus_code, resource_name, resource_data)
