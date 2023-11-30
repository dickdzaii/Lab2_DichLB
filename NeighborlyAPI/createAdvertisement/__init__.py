import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://neighborappdb:o4AIXWJqcJ8LAL2Xw7agNzE4OEIaX9s6Pjz65lsdArgUpkRPJRO7rSScsQpkvZVR5jEwyJIKoMQeACDbKL83Lg==@neighborappdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@neighborappdb@"
            client = pymongo.MongoClient(url)
            database = client['neighborlyappdichlb']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )