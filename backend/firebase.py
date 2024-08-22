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
    