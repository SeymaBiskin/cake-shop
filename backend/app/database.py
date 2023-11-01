import motor.motor_asyncio

from bson import ObjectId
from decouple import config

from app.models import Cake


db_username = config("MONGO_USER")
db_password = config("MONGO_PASSWORD")
client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb+srv://{db_username}:{db_password}@cakeshop.9kc7omy.mongodb.net/?retryWrites=true&w=majority")

database = client.cakeDB

collection = database.cakes


async def fetch_one_cake(id):
    document = await collection.find_one({"_id": ObjectId(id)})
    return document


async def fetch_all_cakes():
    cakes = []
    cursor = collection.find({})
    async for document in cursor:
        cakes.append(Cake(**document))
    return cakes


async def create_cake(cake):
    await collection.insert_one(cake)
    return cake


async def update_cake(id, name, comment, image_url, yum_factor):
    await collection.update_many({"_id": ObjectId(id)},
                                 {"$set": {
                                            "name": name,
                                            "comment": comment,
                                            "imageUrl": image_url,
                                            "yumFactor": yum_factor
                                        }})
    document = await collection.find_one({"_id": ObjectId(id)})
    if document:
        await collection.update_many({"_id": ObjectId(id)},
                                    {"$set": {
                                        "name": name,
                                        "comment": comment,
                                        "imageUrl": image_url,
                                        "yumFactor": yum_factor
                                    }})
    return document


async def remove_cake(id):
    await collection.delete_one({"_id": ObjectId(id)})
    return True
