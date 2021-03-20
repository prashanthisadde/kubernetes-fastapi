import motor.motor_asyncio
import os
mongo_server = os.environ['DB_HOST']
mongo_port = os.environ['DB_PORT']
mongo_db = os.environ['DB_NAME']
mongo_user = os.environ['DB_USER']
mongo_passwd = os.environ['DB_PASSWD']
MONGO_DETAILS = "mongodb://" + mongo_user + ":" + mongo_passwd + "@" + mongo_server + ":" + mongo_port + "/?authSource=admin"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client[mongo_db]
electronic_collection = database.get_collection("electronics")