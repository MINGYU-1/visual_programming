import requests
from collections import Counter
import re
import os

print("--- [예제 1] 텍스트 파일 기본 입출력 ---")

# 1. 'test.txt'에 쓰기 ('w' 모드: 덮어쓰기)
with open('test.txt', 'w', encoding='utf-8') as file:
    file.write('Hello world\n')
print(">> test.txt에 'Hello world' 작성 완료.")

# 2. 첫 번째 줄 읽기
with open('test.txt', 'r', encoding='utf-8') as file:
    print(f">> 첫 번째 줄 읽기: {file.readline()}", end='')

# 3. 'test.txt'에 이어쓰기 ('a' 모드)
with open('test.txt', 'a', encoding='utf-8') as file:
    file.write('return\n')
print(">> test.txt에 'return' 이어쓰기 완료.")

# 4. 파일 전체 읽기
print(">> 파일 전체 내용:")
with open('test.txt', 'r', encoding='utf-8') as file:
    read_data = file.readline()
    while read_data != '':
        # end=''를 사용하여 각 줄의 내용만 출력
        print(read_data, end='')
        read_data = file.readline()
print("\n--- 예제 1 완료 ---\n")


print("--- [예제 2] CSV 파일 생성 및 출력 ---")

# 3x3 행렬 데이터
matrix_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
csv_filepath = 'test.csv'

# 1. 'test.csv' 파일 쓰기
with open(csv_filepath, 'w', encoding='utf-8') as file:
    for row in matrix_data:
        # f-string을 사용하여 '1,2,3\n' 형식으로 저장
        file.write(f'{row[0]},{row[1]},{row[2]}\n')
print(f">> {csv_filepath} 파일 생성 완료.")

# 2. 'test.csv' 파일 읽기 및 출력
print(f">> {csv_filepath} 내용:")
with open(csv_filepath, 'r', encoding='utf-8') as file:
    read_data = file.readline()
    while read_data != '':
        print(read_data, end='')
        read_data = file.readline()
print("--- 예제 2 완료 ---\n")


print("--- [예제 3] CSV 파일 읽어와 행렬로 변환 ---")

# CSV 파일에서 읽어온 데이터를 저장할 리스트를 초기화합니다.
parsed_matrix = []

# 'test.csv' 파일을 읽고 행렬로 변환
with open(csv_filepath, 'r', encoding='utf-8') as file:
    read_data = file.readline()

    while read_data != '':
        # 1. 줄바꿈 문자 제거 및 쉼표(,)를 기준으로 분리
        row = read_data.strip().split(',')

        # 2. 각 요소를 정수(int)로 변환
        # list comprehension을 사용해 코드를 간결하게 만들었습니다.
        try:
            row_ints = [int(item.strip()) for item in row]
            parsed_matrix.append(row_ints)
        except ValueError as e:
            print(f"[경고] 데이터를 정수로 변환하는 데 실패했습니다. 스킵: {read_data.strip()}")

        # 다음 줄을 읽습니다.
        read_data = file.readline()

# 최종적으로 변환된 행렬 리스트를 출력합니다.
print(">> 변환된 행렬 리스트:")
print(parsed_matrix)
print("--- 예제 3 완료 ---\n")


print("--- [예제 4] 단어 빈도수 분석 및 CSV 저장 (Advanced) ---")

file_url = 'http://ruby.bastardsbook.com/files/fundamentals/hamlet.txt'
csv_result_filepath = 'result.csv'
text_data = ""

# 1. 파일 다운로드 또는 로컬 데이터 사용
try:
    print(f">> {file_url}에서 텍스트 다운로드 시도...")
    response = requests.get(file_url)
    response.raise_for_status()
    text_data = response.text
    print(">> 다운로드 성공.")
except requests.exceptions.RequestException as e:
    # 다운로드 실패 시 대체 텍스트 사용
    text_data = "This is a test. The test counts words. This test is a success."
    print(f">> 파일 다운로드 실패 ({e}). 임시 테스트 데이터로 분석 진행: '{text_data}'")


# 2. 단어 추출 및 빈도수 계산
# 텍스트를 소문자로 변환하고 알파벳 단어만 추출
words = re.findall(r'\b[a-zA-Z]+\b', text_data.lower())
word_counts = Counter(words)

# 빈도수 기준 내림차순 정렬
sorted_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)


# 3. 결과 CSV 파일로 저장 및 출력
print(f"\n>> 분석 결과를 '{csv_result_filepath}'에 저장합니다.")

try:
    with open(csv_result_filepath, 'w', encoding='utf-8') as file:
        file.write('Word,Frequency\n') # 헤더 작성

        # 정렬된 단어 빈도수를 CSV 형식으로 파일에 씁니다.
        for word, count in sorted_counts:
            file.write(f'{word},{count}\n')

    # 저장된 CSV 파일 내용 출력 (상위 10개)
    print("\n--- 저장된 result.csv 내용 (상위 10개) ---")
    with open(csv_result_filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            print(line.strip())
            if i >= 10:
                break
except IOError as e:
    print(f"[오류] 파일 저장 중 오류 발생: {e}")

print("--- 예제 4 완료 ---")