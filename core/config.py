from starlette.config import Config

config = Config(".env")

TESTING = config("TESTING", cast=str, default=False)
TEST_DATABASE_NAME = config("TEST_DATABASE_NAME", cast=str, default=False)
DATABASE_URL = config("DATABASE_URL" if not TESTING else "TEST_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("SECRET_KEY", cast=str, default="46e4ac0d9421b44175e593a7d4d1665b6e2c4c7074f4424ad50c8fda789c627a")
