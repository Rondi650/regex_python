import re

string = '''
Durante o evento de tecnologia realizado no dia 15 de maio, os palestrantes abordaram o impacto do trabalho remoto na produtividade. A primeira apresentação começou pontualmente às 08:30, embora o credenciamento estivesse aberto desde as 07:00 AM. O palestrante de abertura falou até as 09h15min, fazendo uma pausa rápida para o café das 09h15 até às 09:45.

Na segunda metade da manhã, das 10h00 às 11:30:00, foram apresentados dados estatísticos sobre o horário de pico de tráfego na web, que geralmente ocorre entre 14:00 e 16:30 no horário local, ou seja, 17:00 UTC (equivalente a 5:00 PM). Algumas equipes internacionais relataram reuniões marcadas para as 03h00m, enquanto outras preferem interagir às 22:15:45 para alinhar com o fuso horário asiático.

No relatório final entregue às 18h, constavam registros precisos de servidores com log-times como 23:59:59.999 e 00:00:01. Outro ponto destacado foi a rotina dos funcionários:

    Turno matutino: das 06:00am às 12:00pm

    Turno vespertino: das 01:30 PM às 07:15 pm

    Turno noturno: das 20h30m00s até as 04:45:10 da madrugada.

Um dos casos de estudo mostrou um servidor que entrou em manutenção às 13:05h, permaneceu offline até 13:08:32, e retornou às 13h08m35s. Para conferência, os tempos registrados no sistema do cliente foram 08h30, 9h, 09:05, 12h00min, 15:45:00.123, 8am e 11pm.
'''

# r = re.findall(r'Notur|lembra', string, flags=re.IGNORECASE)
r = re.findall(r'\d\d[:h]\d\d[:m]?(?:\d\d)?', string)
print(r)
