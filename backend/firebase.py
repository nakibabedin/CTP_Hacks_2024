import firebase_admin
from firebase_admin import credentials, db

with open('keys/database_url.txt') as file:
    database_url = file.read()

cred = credentials.Certificate("keys/coogle-db.json")
# firebase_admin.initialize_app(cred)
firebase_admin.initialize_app(cred, {
    'databaseURL': f'{database_url}'
})

# write data to the root
ref = db.reference()
ref.set({
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
})