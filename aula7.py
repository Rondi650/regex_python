import re
from pprint import pprint


texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

# Texto padrao - tudo dentro de grupos
pprint(re.findall(r'(\w+)\s+(\d{3}.\d{3}.\d{1}.\d{1})\s+\w+\s+(\w+)', texto))

# Positive lookahead
pprint(re.findall(r'(\w+)\s+(\d{3}.\d{3}.\d{1}.\d{1})\s+\w+\s+(?=active)', texto))

# Negative lookahead
pprint(re.findall(r'(\w+)\s+(\d{3}.\d{3}.\d{1}.\d{1})\s+\w+\s+(?!active)', texto))
