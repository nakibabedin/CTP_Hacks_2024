import google.generativeai as genai


# Read in the API Key from the local dot_env file
with open('keys/gemini_api_key.txt', 'r') as file:
    api_key = file.read()

# configure with the Gemeni genai object
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# function to send a request to Gemini
def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text
