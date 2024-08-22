import firebase_admin
from firebase_admin import credentials, db

with open('keys/database_url.txt') as file:
    database_url = file.read()

cred = credentials.Certificate("keys/coogle-db.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': f'{database_url}'
})

def add_resource(campus, resource_name, resource_data):
    ref = db.reference(f'/{campus}')
    ref.update({ resource_name:resource_data })

# returns a python dictionary if a JSON obj
def get_data_for_campus(campus):
    ref = db.reference(f'/{campus}')
    return ref.get()

def append_to_keywords(new_keywords):
    ref = db.reference("all_keywords")
    curr_keywords = ref.get()
    curr_keywords += new_keywords
    ref.set(curr_keywords)
    return

def get_keywords():
    ref = db.reference("all_keywords")
    return ref.get()

