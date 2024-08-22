import gemini
import firebase

# returns a new data obj with a keywords field
# also adds the keywords to realtime database
def process_description(data):
    description = data['description']
    keywords = gemini.get_keywords_from_description(description)
    firebase.append_to_keywords(keywords)

    data['keywords'] = keywords
    return data 

def process_situation( user_situation ):
    return gemini.categorize_text_keywords( user_situation )
    

# TESTING

# resource_data = {
#     "name": "CUNY Central Library",
#     "location": {
#         "address": "365 5th Ave, New York, NY 10016",
#         "building": "Central Library Building",
#         "room": "Main Floor"
#     },
#     "hours": {
#         "monday": "9:00 AM - 8:00 PM",
#         "tuesday": "9:00 AM - 8:00 PM",
#         "wednesday": "9:00 AM - 8:00 PM",
#         "thursday": "9:00 AM - 8:00 PM",
#         "friday": "9:00 AM - 6:00 PM",
#         "saturday": "10:00 AM - 5:00 PM",
#         "sunday": "Closed"
#     },
#     "contact": {
#         "phone": "555-1234",
#         "email": "central.library@cuny.edu",
#         "website": "https://library.cuny.edu"
#     },
#     "description": "The CUNY Central Library offers a wide range of books, digital resources, and study areas. It provides access to academic journals, databases, and research materials.",
#     "services": [
#         "Book Lending",
#         "Research Assistance",
#         "Study Rooms",
#         "Public Computers",
#         "Printing and Copying"
#     ]
# }
# process_description_keywords(resource_data)