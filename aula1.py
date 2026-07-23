import re

string = """
Olá! Meu nome é Carlos Silva e meu e-mail principal é carlos.silva@email.com, 
mas você também pode entrar em contato pelo suporte@empresa.com.br.
Meu salario e de R$2200

Atualmente, moro na Avenida Paulista, nº 1000, no formato de CEP 01311-200. 
Caso precise me ligar, meus números de telefone são 
(11) 98765-4321 (celular) e (11) 3211-1234 (fixo).

Amanhã é dia 24/07/2026 e tenho uma reunião importante agendada para as 14:30. 
O código de faturamento do projeto atual é REF-98765-X. 
O valor total do contrato ficou em R$ 1.500,50, gerando um lucro 
líquido de +25% em relação ao ano passado.
"""

# procura a data
r = re.search(r'[\d]{2}/?\d{2}/?\d{4}', string)
# procura o valor monetario
r2 = re.findall(r'(R\$ ?[^,]+,?\d{2}?)', string)
# procura linhas vazias
r3 = re.findall(r'^\s*$', string)
# substitui o valor por outro com retrovisor
r4 = re.sub(r'(R\$ ?[^,]+,?\d{2}?)', r'[\1]', string)
# com count substitui apenas a primeira, no ex. abaixo
r4 = re.sub(r'(R\$ ?[^,]+,?\d{2}?)', r'[\1]', string, count=1)

if r:
    print(r.group())
    print(r.start())
    print(r.end())
    print(r.span())

print(r, r2)
print(r2)
print(r3)
print(r4)

# testando grupos, como retrovisores
print('*'*50)
m = re.search(r'(..)/(..)/(....)', string)

if m:
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
    print(m.span())
    print(m)


# compile economiza processamento, rodando uma vez apenas o regex
regexp = re.compile(r'([-+ ]?[\d]+%)')
print('*'*50)
print(regexp.search(string))
print(regexp.sub(r'(\1)', string))
