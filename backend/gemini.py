import google.generativeai as genai
from webscraper import get_html_contents

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

# returns a list of keywords from a given url
def get_keywords_from_link(url):
    response = ask_gemini(''' 
           Generate a long and comprehensive 
           list of keywords from the following HTML contents of a webpage: ''' + get_html_contents(url) + 
           '''

           I want it to be in the exact format that i describe:
           Write each keyword/phrase seperated by a , in a single string.
           I should be able get a list of keywords by calling response.split(",") in python
           ''')
    return response.split(",")


# returns a list of keywords from a text
def get_keywords_from_text(text):
    response = ask_gemini(
        ''' 
           Generate a long and comprehensive 
           list of keywords from the following text: ''' + text + 
           '''

           I want it to be in the exact format that i describe:
           Write each keyword/phrase seperated by a , in a single string.
           I should be able get a list of keywords by calling response.split(",") in python
           ''')
    
    return response.split(",") 

def categorize_text_keywords(text, keywords):
    response = '''
    Here is a list of keywords that I have:
    ''' + str(keywords) + ''' 
    and here is a bit of text: 
    ''' + text + ''' 
    Can you tell me which keywords are relevant to the text in question? Things should be more than loosely connected
    
    I want it to be in the exact format that i describe:
    Write each keyword/phrase seperated by a , in a single string.
    I should be able get a list of keywords by calling response.split(",") in python
    '''
    return response.split(",")



student_in_distress_text = '''I’m not sure how much longer I can keep this up. It feels like I’m drowning, but no one can see it. Every day, the pressure to succeed, to meet everyone’s expectations, is suffocating. I’m supposed to have it all together, right? But I don’t. I’m just barely holding on.

I wake up with this tightness in my chest, knowing that I have to face another day of pretending. Pretending that I understand the material, that I’m on top of my assignments, that I’m fine. But the truth is, I’m not fine. I’m overwhelmed, exhausted, and scared. Scared of failing, scared of disappointing my parents, my teachers, myself.

Everyone around me seems to have it figured out. They’re confident, they’re doing well, and I feel like I’m falling behind, even when I’m trying my hardest. I’ve tried to talk about it, but it’s like no one really listens. They just say things like “You’ll be fine,” or “Just push through it.” But what if I can’t push through it? What if I’m already at my breaking point?

The nights are the hardest. When everything is quiet, that’s when the thoughts come rushing in. I lie awake thinking about all the things I didn’t do, all the ways I could mess up, and it’s paralyzing. Sleep doesn’t come easily anymore, and when it does, it’s not restful. I wake up more tired than when I went to bed.

I just want to be able to breathe again, to feel like I’m in control of my own life. But right now, I feel like I’m spiraling, and I don’t know how to stop it. I wish I could tell someone, really tell them, what’s going on inside my head, but I’m afraid they won’t understand. I’m afraid they’ll think I’m weak, or that I’m just making excuses.

But I’m not. I’m trying, I really am. I just don’t know how much longer I can keep pretending that everything’s okay when it’s not.'''


resource_keywords = get_keywords_from_link("https://www.cuny.edu/current-students/student-affairs/student-services/counseling/")

print(resource_keywords)
# print("----------------------------------------------")
# print(categorize_text_keywords(student_in_distress_text, resource_keywords))


