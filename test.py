import pymongo
# MONGODB_URL = 'mongodb+srv://hamidulla:qwer1234@cluster.4e7csio.mongodb.net/?retryWrites=true&w=majority'
# MONGODB_URL = 'mongodb+srv://<username>:<password>@clusterfileurls.vkkzokc.mongodb.net/?retryWrites=true&w=majority'


MONGODB_URL = 'mongodb+srv://orifovhamidulla:qwer1234@cluster0.3uki4bg.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URL)
# print(client)
db = client["movies"]

collection = db["movies"]

collection.insert_one({
    'test':'testdata'
})
