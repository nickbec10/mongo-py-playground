from pymongo import MongoClient

# connect to the MongoDB 
client = MongoClient(host='127.0.0.1', port=27017, username='root', password='toor')

# connect to school collection
#db = connection.school
# Access database
db = client.plants

# Access collection of the database
live = db.live

# querey for the record to update
query = { 'name':'aloe' }
# update record with new values
newvalues = { '$set': { 'name':'aloe', 'origin':'usa', 'price':'5', 'toxicity': ['non-toxic']} }
live.update_one(query, newvalues)

# find all documents
results = db.live.find()

# display documents from collection
for record in results:
    out_name = str(record['name'])
    out_origin = str(record['origin'])
    print(out_name + ', ' + out_origin)

# close the connection to MongoDB
client.close()