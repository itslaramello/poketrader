import json
import logging
import os
from app.main.model.mongo_connection import MongoConnection
from app.main.model.redis_connection import RedisConnection

class Trade(object):
    logger: logging.Logger
    lista_pokemon_player1: list
    lista_pokemon_player2: list
    soma_experience_player1: int
    soma_experience_player2: int
    troca_justa: bool
    #conexao redis
    redis = RedisConnection()
    redis = redis.connect()

    def __init__(self,id_troca):
        redis_info = self.redis.hgetall(id_troca)
        self.lista_pokemon_player1 = redis_info.get("lista_pokemon_player1","")
        self.lista_pokemon_player2 = redis_info.get("lista_pokemon_player2","")
        self.soma_experience_player1 = redis_info.get("soma_experience_player1","")
        self.soma_experience_player2 = redis_info.get("soma_experience_player2","")
        self.troca_justa = redis_info.get("troca_justa","")

    def get_data(self):
        data = {
            "lista_pokemon_player1":self.lista_pokemon_player1,
            "lista_pokemon_player2":self.lista_pokemon_player2,
            "soma_experience_player1":self.soma_experience_player1,
            "soma_experience_player2":self.soma_experience_player2,
            "troca_justa": self.troca_justa
        }
        return data

    def save_trade(self, id_troca):
        try:
            db = MongoConnection()
            collection = db.connect('trade')
            collection.update_one({'id_troca': id_troca}, {'$set': self.get_data()}, upsert=True)
            self.logger.debug("TROCA [%s] - Gravada Mongo", id_troca)
        except Exception as err:
            self.logger.exception("TROCA [%s] - Mongo Erro: [%s]", id_troca, err)

    def get_trade_data(self, id_troca):
        trade = ""
        try:
            db = MongoConnection()
            collection = db.connect('trade')
            trade = collection.find({"id_troca": id_troca})
            self.logger.debug("TROCA [%s] - Get Mongo", id_troca)
        except Exception as err:
            self.logger.exception("TROCA [%s] - Mongo Erro: [%s]", id_troca)

        return trade