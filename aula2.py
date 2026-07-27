import re

string = '''
O reflexo do sol na água parada cria um brilho que quase cega os olhos. Na margem do lago, o som dos galhos balançando com a brisa é o único ruído em quilômetros. É nesses momentos de calmaria que a mente viaja para longe, resgatando memórias antigas que pareciam esquecidas no fundo da gaveta do tempo. A vida corre rápido demais lá fora, cheia de prazos e barulho, mas aqui o tempo parece ter decidido desacelerar de vez. Cada folha que cai lembra que mudar faz parte do caminho. Às vezes, o melhor destino é apenas sentar e observar o mundo girar devagar.
'''

r = re.findall(r'folha|lembra', string)
print(r)
