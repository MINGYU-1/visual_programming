import requests
from collections import Counter
import re
import os

print("--- [예제 1] 텍스트 파일 기본 입출력 ---")

## 예제1
with open('test.txt','w') as file:
    file.write('Hello world\n')
with open('test.txt','r') as file:
    print(file.readline())
with open('test.txt','a') as file:
    file.write('return\n')
with open('test.txt','r') as file:
    read_data = file.readline()
    while read_data != '':
        print(read_data,end = ' ')
        read_data = file.readline()
print("\n--- 예제 1 완료 ---\n")


print("--- [예제 2] CSV 파일 생성 및 출력 ---")
# 예제 2
matrix = [[1,2,3],[4,5,6],[7,8,9]]
with open('test.csv','w') as file:
    for row in matrix:
        file.write(f'{row[0]},{row[1]},{row[2]}\n')

with open('test.csv','r') as file:
    read_data = file.readline()
    while read_data != '':
        print(read_data, end = '')
        read_data = file.readline()

print("--- 예제 2 완료 ---\n")


print("--- [예제 3] CSV 파일 읽어와 행렬로 변환 ---")
matrix = []
with open('test.csv','r') as file:
    read_data = file.readline()
    while read_data != '':
        row = read_data.split(',')
        for index in range(len(row)):
            row[index] = int(row[index])
        matrix.append(row)
        read_data = file.readline()
print(matrix)


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

words = re.findall(r'\b[a-zA-Z]+\b', text_data.lower())
word_counts = Counter(words)
sorted_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
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
