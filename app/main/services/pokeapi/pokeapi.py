import requests
import json
import os
import logging

def pokeapi(pokemon):
    logger: logging.Logger
    logger = logging.getLogger('poke-api-request')

    url = f"{os.getenv('POKE_API_URL','')}/pokemon/{pokemon.lower()}"
    timeout = int(os.getenv('POKE_API_TIMEOUT',10))
    req = requests.Request()
    req.status_code = 102
    response = {}
    erro_msg = ""
        
    logger.debug("POKE API - URL: [%s]", url)
    
    try:
        req = requests.get(url=url, timeout=timeout)
        logger.debug("POKE API - Status Code: [%s] ",req.status_code)
        
        if req.status_code == 200:
            response = json.loads(req.text)
            erro_msg = "Sucesso"
        else:
            logger.critical("POKE API - Erro: [%s]", f"Erro {req.status_code}")
            erro_msg = f"Erro {req.status_code}"
    except Exception as erro:
        logger.exception("POKE API - Exception: [%s] ", erro)
        erro_msg = f"Erro de comunicação com POKE API"

    response['status_code'] = req.status_code
    response['erro_msg'] = erro_msg

    return response

def get_base_experience(pokemon):
    logger: logging.Logger
    logger = logging.getLogger('get-base-experience')
    base_experience = 0
    
    base_experience = pokeapi(pokemon).get('base_experience',0) if pokeapi(pokemon) else base_experience
    logger.debug("GET BASE EXPERIENCE - Pokemon: [%s] - Base Experience: [%s]",pokemon, base_experience)
    
    return base_experience