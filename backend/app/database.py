import motor.motor_asyncio
from bson import ObjectId
from decouple import config

# from models import Role

db_username = config("MONGO_USER")
db_password = config("MONGO_PASSWORD")
client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb+srv://{db_username}:{db_password}@cakeshop.9kc7omy.mongodb.net/?retryWrites=true&w=majority")

# Giving name to db
database = client.cakeDB

# Giving name to table in db
collection  = database.cakes