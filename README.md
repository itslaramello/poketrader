# poketrader


Aplicação back para ser integrada e usada como calculadora de 'fair trade'.

Foram utilizados:
MongoDB
Redis
Python

A ideia é ter o Redis como acesso rápido a informações de cada troca durante o processamento da mesma, facilitando o processamento de diversas trocas diferentes em simultâneo, controladas pelo seu id.

Funções disponíveis:
- adicionar pokemon a lista (escolha dos pokemons elegiveis a troca)
- realizar soma dos 'base_experience' dos pokemons, realizando a consulta a api PokeTrade
- analisar as condições da troca e decidir entre justa ou não
- recuperar todos os dados de cada troca realizada pelo jogador solicitante
- persistência dos dados no Mongo
