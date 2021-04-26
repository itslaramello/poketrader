import json
import logging
import os
from app.main.model.mongo_connection import MongoConnection
from app.main.model.redis_connection import RedisConnection

class Player(object):
    logger: logging.Logger
    lista_trades: list
    player: int
    #conexao redis
    redis = RedisConnection()
    redis = redis.connect()

    def get_data(self):
        redis_info = self.redis.hgetall(player)
        data = {
            "lista_trades":redis_info.get(lista_trades,""),
            "player": redis_info.get(player,"")
        }
        return data

    def save_player(self, player_id):
        try:
            db = MongoConnection()
            collection = db.connect('player')
            collection.update_one({'player': player_id}, {'$set': self.get_data()}, upsert=True)
            self.logger.debug("PLAYER [%s] - Gravada Mongo", player_id)
        except Exception as err:
            self.logger.exception("PLAYER [%s] - Mongo Erro: [%s]", player_id, err)

    def get_player_data(self, player_id):
        history = ""
        try:
            db = MongoConnection()
            collection = db.connect('player')
            player = collection.find({"player": player_id})
            history = player.get("lista_trades","")
            self.logger.debug("PLAYER [%s] - Get Mongo", player_id)
        except Exception as err:
            self.logger.exception("PLAYER [%s] - Mongo Erro: [%s]", player_id)

        return history