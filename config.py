__version__ = "1.0.0"

from pydantic import BaseSettings, AnyHttpUrl, IPvAnyAddress
from urllib.parse import quote_plus
from os.path import dirname, abspath


class Settings(BaseSettings):
    BASE_DIR: str = dirname(abspath(__file__))
    # LOG FILE MAX
    LOG_FILE_MAX: int = 160
    # REQUESTS CONFIG
    REQUESTS_TIMEOUT: int = 30
    # MYSQL CONNECT CONFIG
    DB_SQL_DEBUG: bool = False
    DB_MAXIUM_OVERFLOW: int = 10
    DB_POOL_SIZE: int = 5
    DB_RECYCLE_SECOND: int = 5
    # RABBITMQ CONFIG
    RABBITMQ_HOST: IPvAnyAddress = "127.0.0.1"
    RABBITMQ_PORT: int = 5672
    RABBITMQ_QUEUE: str = ""
    RABBITMQ_DELAY_QUEUE: str = ""
    RABBITMQ_USER: str = ""
    RABBITMQ_PASSWORD: str = ""
    RABBITMQ_V_HOST: str = "/"
    RABBITMQ_EXCHANGE_NAME: str = ""

    # FLASK
    DEBUG: bool = False
    SECRET_KEY: str = ""

    # MONGODB
    MONGODB_WRITE_FLAG: bool = True
    MONGO_URI: str = "mongodb://{user}:{password}@{host}:{port}/{db_name}".format(
        user=quote_plus("root"),
        password=quote_plus("123456"),
        host="127.0.0.1",
        port=27017,
        db_name="pis_middle_layer"
    )


settings = Settings()
