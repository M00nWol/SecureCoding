## 추출하고 싶다!

import re

buf = """Python python
Pythonpython
python, Python
"""

ptn = re.compile(r"([Pp]ython(, )?)+")

for result in ptn.finditer(buf):
    print(result)