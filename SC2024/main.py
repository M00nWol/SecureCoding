import re

buf = "password123"

ptn = re.compile(r"\w{5,}")

# search를 사용하면 ! 이후만 가져옴
# result = ptn.search(buf)

# match 쓰면 pw 조건 아니면 안 가져옴 : 처음부터 일치하는지 확인하는 목적
result = ptn.match(buf)
print(result)