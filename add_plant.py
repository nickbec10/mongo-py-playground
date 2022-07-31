from pymongo import MongoClient

# connect to the MongoDB 
client = MongoClient(host='127.0.0.1', port=27017, username='root', password='toor')

# Access database
db = client.plants

# Access collection of the database
live = db.live

# find and delete if entry already created
query = { 'name':'guinea chestnut' }
live.delete_one(query)

# create record
record = {'name':'guinea chestnut', 'origin':'brazil', 'price':'4', 'toxicity': ['non-toxic']}

#insert the record
rec = db.live.insert_one(record)

# find all documents
results = db.live.find()

# display documents from collection
for record in results:
    out_name = str(record['name'])
    out_origin = str(record['origin'])
    print(out_name + ',' + out_origin)

# close the connection to MongoDB
client.close()