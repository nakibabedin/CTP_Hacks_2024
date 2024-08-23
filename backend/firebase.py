import firebase_admin
from firebase_admin import credentials, db

with open('keys/database_url.txt') as file:
    database_url = file.read()

cred = credentials.Certificate("keys/coogle-db.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': f'{database_url}'
})

def add_resource(campus, resource_name, resource_data):
    ref = db.reference(f'/{campus}/resource/{resource_name}')
    ref.set( resource_data )

# returns a python dictionary if a JSON obj
def get_data_for_campus(campus):
    ref = db.reference(f'/{campus}/resource')
    return ref.get()

def append_to_keywords(campus, new_keywords):
    ref = db.reference(f"{campus}/keywords")
    snapshot = ref.get()
    curr_keywords = ref.get() if snapshot else []
    all_keywords = list(set( curr_keywords + new_keywords ))
    ref.set(list(all_keywords))
    return

def get_keywords(campus):
    ref = db.reference(f"{campus}/keywords")
    return ref.get()
