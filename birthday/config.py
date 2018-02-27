import decouple


DEBUG = decouple.config("DEBUG", default="0", cast=int)

MONGO_URL = decouple.config("MONGO_URL", default="mongodb://mongo:27017")