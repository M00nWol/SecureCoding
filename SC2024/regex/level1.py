import re

# 파일에서 텍스트 읽기
def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    
# Level 1 : 기본 과제 수행
def level_1(data):
    print("=========== Level 1: Basic Exercises ===========")

    print("\n====== 1-1. 특정 단어 찾기 : Nurilab ======")
    ptn = r'Nurilab'
    matches = re.findall(ptn, data)
    print(f"Match {matches}")

    print("\n====== 1-2. 모든 문자 찾기 (줄바꿈 제외) : a.b ======")
    ptn = r'a.b'
    matches = re.findall(ptn, data)
    print(f"Match {matches}")
 
    print("\n====== 1-3. 여러 문자 중 하나와 일치시키기 : sales(수) ======")
    ptn = r'sales[1-3]'
    matches = re.findall(ptn, data)
    print(f"Match {matches}")

    print("\n====== 1-4. 숫자 찾기 : 4자리 숫자 ======")
    ptn = r'\b\d{4}\b'
    matches = re.findall(ptn, data)
    print(f"Match {matches}")

    print("\n====== 1-5. 공백 문자 찾기 ======")
    ptn = r'\s'
    matches = re.findall(ptn, data)
    print(f"공백 문자 개수: {len(matches)}")

    print("\n====== 1-6. 이메일 주소 찾기 ======")
    ptn = r'[a-zA-Z0-9_]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    matches = re.findall(ptn, data)
    print(f"Match {matches}")
    
    print("\n====== 1-7. URL 찾기 ======")
    ptn = r'https?://[^\s<>"]+'
    matches = re.findall(ptn, data)
    print(f"Match {matches}")
    
    print("\n====== 1-8. 전화번호 찾기 ======")
    ptn = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    matches = re.findall(ptn, data)
    print(f"Match {matches}")

    print("\n====== 1-9. 날짜 형식 찾기 ======")
    ptn = r'\b\d{4}-\d{2}-\d{2}\b'
    matches = re.findall(ptn, data)
    print(f"Match {matches}")
    

# 메인 함수
if __name__ == '__main__':
    filepath = '정규표현식 실습 예문.txt'
    data = read_file(filepath)

    level_1(data)