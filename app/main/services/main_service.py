from app.main.services.pokeapi import get_base_experience
from app.main.model.player import get_player_data
from app.main.model.trade import get_trade_data
from app.main.model.redis_connection import RedisConnection

#conexao redis
redis = RedisConnection()
redis = redis.connect()

def add_pokemon_tolist(player,id_troca,pokemon):
    # max 6
    lista = f"lista_pokemon_player{player}"
    
    lista_atual = redis.hmget(id_troca,lista)[0] if redis.hexists(id_troca,lista) else ""
    if len(lista_atual) < 5:
        lista_atual.append(pokemon)
        redis.hset(id_troca,lista,lista_atual)

def sum_base_experience(pokemon_list,player,id_troca):
    sum = 0
    for pokemon in pokemon_list:
        sum += get_base_experience(pokemon)

    chave = f"soma_experience_player{player}"
    redis.hset(id_troca,chave,sum)
    return sum

def fair_trade(id_troca,player):
    #recuperar lista de pokemon, somar experiencias e associar ao jogador solicitante
    lista_player_atual = redis.hmget(id_troca,"lista_pokemon_player1")[0] if player == '1' else redis.hmget(id_troca,"lista_pokemon_player2")[0]
    lista_other_player = redis.hmget(id_troca,"lista_pokemon_player1")[0] if player == '1' else redis.hmget(id_troca,"lista_pokemon_player2")[0]
    sum_player_atual = sum_base_experience(lista_player_atual,player,id_troca)
    sum_other_player = sum_base_experience(sum_other_player,player,id_troca)
    
    #taxa de 'proximo' como chave do redis, para facil alteracao/manuntencao
    default = 0.80
    fair_percentage = redis.get(fair_percentage)
    fair_percentage = fair_percentage if fair_percentage else default

    fair = (sum_player_atual * fair_percentage) <= sum_other_player
    redis.hset(id_troca,"troca_justa",fair)
    return fair

def get_trade_history(player):
    #get lista trades, depois get infos da trade
    history = []
    lista_trades = get_player_data(player)
    for trade in lista_trades:
        history.append(get_trade_data(trade))

    return history
