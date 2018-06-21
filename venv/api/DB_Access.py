

entries = [
    {'ID': 1,
     'content': "hello world",
     'creator': 34,
     'upvotes': 0,
     'downvotes': 0},
]

def search_entry(id):
    #ToDo: find the entry in the database and retrun it in json format
    entry = [e for e in entries if (e['ID'] == id)]
    return entry[0]

def add_entry(entryRequest):
    #ToDo: Parse the request and add it to te DB
    pass

def delete_entry(id):
    #ToDo: delete the etry at id
    pass
