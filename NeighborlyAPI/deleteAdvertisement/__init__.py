import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://neighborappdb:o4AIXWJqcJ8LAL2Xw7agNzE4OEIaX9s6Pjz65lsdArgUpkRPJRO7rSScsQpkvZVR5jEwyJIKoMQeACDbKL83Lg==@neighborappdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@neighborappdb@"
            client = pymongo.MongoClient(url)
            database = client['neighborlyappdichlb']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
