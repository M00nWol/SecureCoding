import re

buf = """Send personal email to ben@nurilab.com. For questions about a book use support@nurilab.com. Feel free to send unsolicited email to spam@nurilab.com (wouldn't it be nice if it were that sample, huh?).kim.su@gsad.co.kr"""

ptn = re.compile(r"(\w[\w.-]*)@\w+(\.\w+)+")

result = ptn.search(buf)

for p in ptn.finditer(buf):
    print(p.group())
    # print(p.groups()[0])   # 최초 탐지 결과
    print(p.span())    # 최초 탐지 위치    
