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
# def get_keywords_from_link(url):
#     url_html_contents = get_html_contents(url)

#     response = ask_gemini(''' 
#            Generate a long and comprehensive 
#            list of keywords from the following HTML contents of a webpage: ''' + url_html_contents + 
#            '''  

#            For the keywords, you shouldn't just give me words that directly appear on the webpage.
#            Use your capabilities as a LLM in order to classify the describe the contents of the webpage and what topics it is generally about.
#            Also avoid using the topics that come up in the navbar and footer as topics (e.g. admissions, blackboard, cunyfirst, etc.)
           
#            I want it to be in the exact format that i describe:
#            Write each keyword/phrase seperated by a , in a single string.
#            These keywords/phrases should describe what the website would be useful for and it should not be something like a HTML tag or attribute
#            I should be able get a list of keywords by calling response.split(",") in python
#            ''')
#     return response.split(",")


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
    ''')
    return response.split(",")



student_in_distress_text_1 = '''I’m freaking out. I don't know how to manage coursework and take care of all 3 of my kids. What do i do?'''
student_in_distress_text_2 = '''I sat in the corner of my cramped dorm room, my textbooks scattered around me in a chaotic mess. The pressure from looming exams and mounting responsibilities felt like an insurmountable weight on my shoulders. Each day seemed to blend together, and my once-clear goals now felt lost in a fog of confusion. I found myself pulling away from friends, unsure of how to reach out for the help I needed. In my quieter moments, I longed for a way to find peace and regain some sense of clarity amidst the chaos. I dont want to talk to my parents'''

resource_keywords = ['stressed from coursework', 'need academic help','CUNY child care centers', ' parents', ' early childhood education', ' affordable child care', ' campus child care', ' CUNY parent resources', ' child care services', ' childcare programs', ' New York City child care', ' interest form', ' enroll your child', ' campus resources', '  parent support', ' child care availability', ' waitlist', ' job opportunities', ' events', ' symposium', ' directory', ' enrollment', ' resources', ' contact information', '  parent transition service']
# print(resource_keywords)
print("----------------------------------------------")
print(categorize_text_keywords(student_in_distress_text_2, resource_keywords))


