import redis
import os

class RedisConnection(object):
    redis_host: str
    redis_port: int
    redis_user: str
    redis_password: str

    def __init__(self):
        self.redis_host = os.getenv('REDIS_HOST','localhost')
        self.redis_port = int(os.getenv('REDIS_PORT',6379))
        self.redis_user = os.getenv('REDIS_USER',"")
        self.redis_password = os.getenv('REDIS_PASSWORD',"")

    def connect(self,collection):
        return redis.StrictRedis(host=self.redis_host, port=self.redis_port,password=self.redis_password, decode_responses=True)