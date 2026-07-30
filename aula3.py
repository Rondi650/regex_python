from html.entities import html5
from pydoc import html
import re

texto = '''
<body>
    <header class="main-header-container">
    <div class="main-header container">
        <h1>
            <a class="main-logo" href="/">
                <i class="fas fa-utensils main-logo-icon"></i>
                <span class="main-logo-text">Recipes</span>
            </a>
        </h1>
    </div>
'''

p = re.findall(r'<[^>]*>', texto)
p1 = re.search(r'<[^>]*>', texto)
print(p, p1)