import google.generativeai as genai
import firebase

# Read in the API Key from the local dot_env file
with open('keys/gemini_api_key.txt', 'r') as file:
    api_key = file.read()

# configure with the Gemeni genai object
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# function to send a request to Gemini
def ask_gemini(prompt):
    response = model.generate_content(prompt,
        generation_config=genai.types.GenerationConfig(
            candidate_count=1,
            max_output_tokens=60,
            temperature=0.1,
        ),
    )
    print(response.candidates[0].content.parts[0].text)

    return response.candidates[0].content.parts[0].text

# returns a list of keywords from a resource description
def get_keywords_from_description(description):
    response = ask_gemini(
        ''' 
           Generate a long and comprehensive 
           list of keywords from the following description of a resource: ''' + description + 
           '''

           I want it to be in the exact format that i describe:
           Write each keyword/phrase seperated by a , in a single string.
           I should be able get a list of keywords by calling response.split(",") in python
           By keywords, I don't necessraily mean words that appear in the string but also words/phrases that generally describe the description well
           Please give me no more than 40 keywords. If you have more, please choose the 40 strongest descriptions
           ''')
    return response.split(",") 

def categorize_text_keywords(text):
    keywords = firebase.get_keywords()
    response = ask_gemini( '''
    Here is a list of keywords that I have:
    ''' + str(keywords) + ''' 
    and here is a bit of text: 
    ''' + text + ''' 
    Can you tell me which keywords are relevant to the text in question? Things should be strongly connected not loosely connected
    
    I want it to be in the exact format that i describe:
    DO NOT just return the exact same keywords as that is not what I want, they should be judged based on how correlated they are
    Write each keyword/phrase seperated by a , in a single string.
    I should be able get a list of keywords by calling response.split(",") in python
    If there are no relevant keywords, return an empty string
    ''')
    return response.split(",")

# student_in_distress = "Help, I need childcare services for my baby"
# student_in_distress2 = "Help, I need some study resources"
#
# print(categorize_text_keywords(student_in_distress2))
#



