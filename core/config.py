from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("SECRET_KEY", cast=str, default="46e4ac0d9421b44175e593a7d4d1665b6e2c4c7074f4424ad50c8fda789c627a")
