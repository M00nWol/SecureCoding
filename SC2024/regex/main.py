import re

buf = """<SCRIPT>
function doSpellCheck(form, field) {
  // Make sure not empty
  if (field.value == '') {
    return false;
  }
  //Init
  var windowName='spellWindow';
  var
  spellCheckURL='spell.cfm?formname=Comment&fieldname='+field.name;
  //Done
  return false
}
</SCRIPT>
"""

# re.match를 re.search로 변경
ptn = re.compile(r"<SCRIPT>([\d\D]*?)<\/SCRIPT>", re.DOTALL)

result = ptn.search(buf)  # search를 사용하여 전체를 탐색
if result:
    print(result.group())  # 매칭된 전체 결과를 출력
