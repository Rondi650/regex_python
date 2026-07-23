import re

string = """
Olá! Meu nome é Carlos Silva e meu e-mail principal é carlos.silva@email.com, 
mas você também pode entrar em contato pelo suporte@empresa.com.br.

Atualmente, moro na Avenida Paulista, nº 1000, no formato de CEP 01311-200. 
Caso precise me ligar, meus números de telefone são 
(11) 98765-4321 (celular) e (11) 3211-1234 (fixo).

Amanhã é dia 24/07/2026 e tenho uma reunião importante agendada para as 14:30. 
O código de faturamento do projeto atual é REF-98765-X. 
O valor total do contrato ficou em R$ 1.500,50, gerando um lucro 
líquido de +25% em relação ao ano passado.
"""

r = re.search(r'[\d]{2}/?\d{2}/?\d{4}', string)
r2 = re.findall(r'R\$[^,]+,\d{2}', string)
r3 = re.findall(r'^\s*$', string)
print(r, r2)
print(r2)
print(r3)
