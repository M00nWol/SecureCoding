import re

buf = """The phrase "reqular expression" is often
abbreviated as RegEx or regex."""

result = re.findall("[Rr]eg[Ee]x", buf)
print(result)
