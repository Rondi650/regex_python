# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A
# \W -> [^a-zA-Z0-9À-ú_]
# \W -> [^a-zA-Z0-9_] -> re.A
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t]
# \S -> [^ \r\n\f\n\t]
# \b -> borda
# \B -> não borda
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve_ALGO 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print('BUSCA [a-z]+:\n', re.findall(r'[a-z]+', texto), '\n')
print('BUSCA [a-zA-Z]+:\n', re.findall(r'[a-zA-Z]+', texto), '\n')
print('BUSCA [a-zA-Z0-9]+:\n', re.findall(r'[a-zA-Z0-9]+', texto), '\n')
print('BUSCA [a-zA-Z0-9À-ú]+:\n', re.findall(r'[a-zA-Z0-9À-ú]+', texto), '\n')
print('BUSCA \\w+:\n', re.findall(r'\w+', texto), '\n')
print('BUSCA \\s+:\n', re.findall(r'\s+', texto), '\n')
print('BUSCA \\W+:\n', re.findall(r'\W+', texto, re.ASCII), '\n')
