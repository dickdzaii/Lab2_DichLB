import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://neighborappdb:o4AIXWJqcJ8LAL2Xw7agNzE4OEIaX9s6Pjz65lsdArgUpkRPJRO7rSScsQpkvZVR5jEwyJIKoMQeACDbKL83Lg==@neighborappdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@neighborappdb@"
        client = pymongo.MongoClient(url)
        database = client['neighborlyappdichlb']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)