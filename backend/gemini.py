import google.generativeai as genai
import firebase
import json

# Read in the API Key from the local dot_env file
with open('keys/gemini_api_key.txt', 'r') as file:
    api_key = file.read()

# configure with the Gemeni genai object
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# function to send a request to Gemini
def ask_gemini(prompt, tokens=256):
    response = model.generate_content(prompt,
        generation_config=genai.types.GenerationConfig(
            candidate_count=1,
            max_output_tokens=tokens,
            temperature=0.3,
        ),
    )

    return response.candidates[0].content.parts[0].text

# returns a list of keywords from a resource description
def get_keywords_from_description(description):
    response = ask_gemini(
        f''' 
           Generate a comprehensive list of keywords from the following description of a CUNY resource: 
           {description} 

           These keywords should only describe the services provided by this resource and situations where the resource is applicable.

           Return these keywords as a comma-separated list.
           I should be able to use .split(',') on the response.

           Please give me no more than 15 keywords.
        ''')
    return response.split(",") 


def categorize_text_keywords(campus , query):
    keywords = firebase.get_keywords(campus)
    response = ask_gemini( f'''
    Given this list of keywords:
    {str(keywords)} 

    And a CUNY student's situation: 
    {query}

    Think about possible solutions or resources that could help the student.
    Return a list of keywords that strongly correlate to those solutions and resources.
    Avoid words that don't relate to the situation, and the names of campuses.
    All the words you return must be a direct match with some word/phrase in the list of keywords.
    The list should be unique.

    Return these keywords as a comma-separated list.
    I should be able to use .split(',') on the response.
    If there are no relevant keywords, return an empty string
    ''', tokens=len(query)*10)
    res = response.split(",")
    return res

# student_in_distress = "Help, I need childcare services for my baby"
# student_in_distress2 = "Help, I need some study resources"
#
# print(categorize_text_keywords(student_in_distress2))
#


def generateResourceSchema(scraped_text):
    response = ask_gemini(f'''
                              I have some text that I scraped from a website of a resource at a CUNY college.
                              I want you to summarize the information into a succinct description of services, and also return some structured data.
                              Using this JSON schema:
                                  ResourceData = {{
                                      "campus": string; // This should be the specific CUNY campus this resource is from. Your options are: "BRCH BKLN CSTI HUNT JJAY LMAN MDEV NYCT QNSC CCNY YORK CUNY". CUNY is for resources that are not specific to a campus, and available to all campuses.
                                      "name": string; // The resource's official name. This should be specific. Make sure not to inlcude any characters that would make this field input an invalid path for the Firebase realtime database (e.g. don't use the special character '.')
                                      "location": string; // Where to physically access the resource. What address, building, room, etc.
                                      "hours": string; // When this resource is available, 24/7, days of the week, time start and end, lunch breaks.
                                      "phone": string; // The primary number to contact. Ensure this is a valid 10 digit phone number without the extension code, return the string with dashes in the spots you would traditionally see them.
                                      "email": string; // The main email that the student should contact. Make sure this is a valid email format.
                                      "website": string; // Leave as empty string.
                                      "description": string; // This is the description you are generating.
                                  }}

                              If you did not find a definitive, specific answer for the location, hours, phone, or email, please return an empty string for that field.
                              If the website seems to have returned an error, return an empty string
                              Here is the text:
                              {scraped_text}
                          ''', 500)

    return response
