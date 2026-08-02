import re

# () Grupos -> pode ser acessado com retrovisores, parecido com variavel \1
# Contar aberturas de parentesis para contar os retrovisores

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''

tags = re.findall(r'<([divp]{1,3})>(.+?)<(\/[divp]{1,3})>', texto)
print(tags)

tags2 = re.findall(r'(<[divp]{1,3}>)(.+?)(<\/[divp]{1,3}>)', texto)
print(tags2)

# usando retrovisores para substituir textos
# \s* no início engole qualquer espaço ou quebra de linha entre uma tag e outra
print(re.sub(r'\s*(<.*?>)(.*?)(<\/.*?>)', r'\1[\2]\3\n', texto))
