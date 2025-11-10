

import re
import sys

#예제1번
class Tmoney:
    def __init__(self):
        self.balance = 0

    def charge(self, amount):
        self.balance += amount
        print(f"{amount}원이 충전되었습니다. 현재 잔액: {self.balance}원")

    def use(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount}원이 사용되었습니다. 남은 잔액: {self.balance}원")
        else:
            print(f"잔액이 부족합니다. (현재 잔액: {self.balance}원)")

def main_ex1():
    """예제 1: T-money 확인 방법 실행"""
    print("--- 💳 예제 1: T-money ---")
    
    # [확인 1] Tmoney 클래스로부터 두 인스턴스를 만든다
    my_tmoney = Tmoney()
    friend_tmoney = Tmoney()

    # [확인 2] 두 인스턴스에 10,000원씩 충전하고 두 인스턴스의 잔액을 출력한다
    print("--- 1, 2번 인스턴스에 10,000원 충전 ---")
    my_tmoney.charge(10000)
    friend_tmoney.charge(10000)
    print(f"my_tmoney 잔액: {my_tmoney.balance}원")
    print(f"friend_tmoney 잔액: {friend_tmoney.balance}원")

    # [확인 3] 두 인스턴스로부터 1,000원씩 사용하고 두 인스턴스의 잔액을 출력한다
    print("\n--- 1, 2번 인스턴스에서 1,000원 사용 ---")
    my_tmoney.use(1000)
    friend_tmoney.use(1000)
    print(f"my_tmoney 잔액: {my_tmoney.balance}원")
    print(f"friend_tmoney 잔액: {friend_tmoney.balance}원")
    print("-" * 20 + "\n")

# 예제2번
class SharedFund:
    """
    SharedFund 클래스는 공유 잔고(deposit)를 클래스 변수로,
    개인 잔고(deposit)를 인스턴스 변수로 가집니다.
    """
    
    # [조건 1] SharedFund 클래스에는 잔고(deposit) 변수가 존재한다 (클래스 변수)
    deposit = 0

    def __init__(self):
        """
        [조건 2] SharedFund 클래스의 인스턴스는 독자적인 잔고 변수를 가진다.
        인스턴스 생성 시 개인 잔고(self.deposit)를 0으로 초기화합니다.
        """
        self.deposit = 0

    def send_to_class(self, amount):
        """
        [조건 3] 인스턴스는 자신의 잔고에서 클래스에 송금할 수 있다.
        인스턴스 변수(self.deposit)에서 차감하여 클래스 변수(SharedFund.deposit)에 더합니다.
        """
        if self.deposit >= amount:
            self.deposit -= amount
            SharedFund.deposit += amount
            print(f"인스턴스 -> 클래스 {amount}원 송금. (인스턴스 잔고: {self.deposit}, 클래스 잔고: {SharedFund.deposit})")
        else:
            print(f"인스턴스 잔고가 부족하여 송금할 수 없습니다. (인스턴스 잔고: {self.deposit})")

    def receive_from_class(self, amount):
        """
        [조건 4] 인스턴스는 클래스 잔고에서 자신에게로 송금할 수 있다.
        클래스 변수(SharedFund.deposit)에서 차감하여 인스턴스 변수(self.deposit)에 더합니다.
        """
        if SharedFund.deposit >= amount:
            SharedFund.deposit -= amount
            self.deposit += amount
            print(f"클래스 -> 인스턴스 {amount}원 송금. (인스턴스 잔고: {self.deposit}, 클래스 잔고: {SharedFund.deposit})")
        else:
            print(f"클래스 잔고가 부족하여 송금받을 수 없습니다. (클래스 잔고: {SharedFund.deposit})")

def main_ex2():
    """예제 2: 자유 적금 확인 방법 실행"""
    print("--- 💰 예제 2: 자유 적금 ---")
    
    # [확인 1] SharedFund 클래스의 잔고를 10,000원으로 설정한 후 두 인스턴스(#1, #2)를 만든다
    SharedFund.deposit = 10000
    s1 = SharedFund()
    s2 = SharedFund()
    print(f"초기 상태 - 클래스: {SharedFund.deposit}, s1: {s1.deposit}, s2: {s2.deposit}")

    # [확인 2] 인스턴스#1에서 클래스로부터 10,000원을 송금 받은 후 잔고 출력
    s1.receive_from_class(10000)
    print(f"결과 (s1이 받음) - 클래스: {SharedFund.deposit}, s1: {s1.deposit}, s2: {s2.deposit}")

    # [확인 3] 인스턴스#2에서 클래스에 5,000원을 송금한 후 잔고 출력
    # (확인 방법을 위해 s2가 5,000원을 가지고 있다고 가정하고 임의로 충전)
    s2.deposit = 5000
    print(f"\n[확인을 위해 s2에 5,000원 임의 충전] - 클래스: {SharedFund.deposit}, s1: {s1.deposit}, s2: {s2.deposit}")
    s2.send_to_class(5000)
    print(f"결과 (s2가 보냄) - 클래스: {SharedFund.deposit}, s1: {s1.deposit}, s2: {s2.deposit}")
    print("-" * 20 + "\n")

#예제 3번
class Course:
    """
    Course 클래스는 과목명, 과목코드, 학점 정보를 인스턴스 변수로 가집니다.
    학점을 평점(GPA)으로 변환하고, 과목 정보를 출력하는 기능을 제공합니다.
    """
    
    # [조건 2] 학점을 평점(GPA)으로 환산하는 기능을 위한 매핑 (클래스 변수)
    GRADE_TO_GPA = {
        'A+': 4.5, 'A': 4.0,
        'B+': 3.5, 'B': 3.0,
        'C+': 2.5, 'C': 2.0,
        'D+': 1.5, 'D': 1.0,
        'F': 0.0
    }

    def __init__(self, name, code, grade):
        """
        [조건 1] Course 클래스는 과목명(name), 과목코드(code), 학점 정보(grade)를 가진다.
        """
        self.name = name
        self.code = code
        self.grade = grade

    def get_gpa(self):
        """
        [조건 2] Course 클래스는 학점을 평점(GPA)으로 환산하는 기능을 가진다.
        """
        return self.GRADE_TO_GPA.get(self.grade, 0.0)

    def print_info(self):
        """
        [조건 3] Course 클래스는 과목명, 과목코드, 학점 정보와 평점을 한 줄로 출력하는 기능을 가진다.
        """
        gpa = self.get_gpa()
        print(f"과목명: {self.name}, 과목코드: {self.code}, 학점: {self.grade}, 평점: {gpa}")

def main_ex3():
    """예제 3: 수강과목 확인 방법 실행"""
    print("--- 📚 예제 3: 수강과목 ---")
    
    # [확인 1] Course 클래스를 통해 인스턴스를 세 개 만든 후 리스트에 삽입한다
    c1 = Course("비주얼 프로그래밍", "CSE101", "A+")
    c2 = Course("자료구조", "CSE102", "B")
    c3 = Course("운영체제", "CSE103", "F")
    
    course_list = [c1, c2, c3]

    # [확인 2] 리스트의 각 원소를 순회하며 조건3의 기능을 통해 내용을 출력한다
    for course in course_list:
        course.print_info()
    
    print("-" * 20 + "\n")
    
    # 예제 4에서 사용하기 위해 c1, c2, c3 반환
    return c1, c2, c3

#예제 4번

class CourseManager:
    """
    CourseManager 클래스는 Course 인스턴스 리스트를 관리하며,
    전체 평점 계산(F학점 포함) 및 과목 검색 기능을 제공합니다.
    """
    
    def __init__(self):
        """
        [조건 1] CourseManager 클래스는 Course 클래스의 인스턴스를 관리한다.
        인스턴스 변수 self.courses(리스트)에 Course 객체들을 저장합니다.
        """
        self.courses = []

    def add_course(self, course):
        """Course 인스턴스를 관리 목록에 추가"""
        if isinstance(course, Course):
            self.courses.append(course)
        else:
            print("Course 객체만 추가할 수 있습니다.")

    def calculate_total_gpa(self):
        """
        [조건 2] CourseManager 클래스는 보유한 Course 인스턴스로부터 전체 평점을 계산한다.
        (F학점 포함, 열람용 계산방식)
        """
        if not self.courses:
            return 0.0
        
        # 모든 과목의 GPA 합계 계산
        total_gpa_sum = sum(course.get_gpa() for course in self.courses)
        
        # 과목 수로 나누어 평균 평점 반환
        return total_gpa_sum / len(self.courses)

    def search_course(self, code):
        """
        [조건 3] CourseManager 클래스는 특정 과목코드를 검색하는 기능을 가진다.
        """
        found = False
        for course in self.courses:
            if course.code == code:
                print(f"검색 결과 (과목코드: {code}):")
                course.print_info()
                found = True
                break # 첫 번째 일치하는 과목을 찾으면 중단
        if not found:
            print(f"검색 결과: 과목코드 {code}에 해당하는 과목을 찾을 수 없습니다.")

def main_ex4(c1, c2, c3):
    """예제 4: 과목관리 확인 방법 실행 (예제 3의 인스턴스 사용)"""
    print("--- 🗂️ 예제 4: 과목관리 ---")
    manager = CourseManager()
    
    # [확인 1] CourseManager 인스턴스에 세 개의 Course 인스턴스를 입력한다
    manager.add_course(c1)
    manager.add_course(c2)
    manager.add_course(c3)

    # [확인 2] 조건2의 기능을 통해 전체 평점을 계산하여 출력한다
    total_gpa = manager.calculate_total_gpa()
    # (4.5 + 3.0 + 0.0) / 3 = 2.5
    print(f"전체 평점 (F 포함): {total_gpa:.2f}")

    # [확인 3] 조건3의 기능이 잘 수행되는지 확인한다
    print("\n--- 과목 검색 테스트 ---")
    manager.search_course("CSE102") # 성공
    manager.search_course("CSE999") # 실패
    print("-" * 20 + "\n")

# 예제 5번

class ComplexNumber:
    """
    복소수 클래스 (a + bi).
    사칙연산을 위한 특별 메서드(연산자 오버로딩)를 구현합니다.
    """
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        """
        출력 형식 (예: 1-2i, 1+2i)을 맞추기 위한 __str__ 메서드.
        (페이지 84, 출력 예시 1443, 1444)
        """
        if self.imag == 0:
            return f"{self.real}"
        if self.real == 0:
            return f"{self.imag}i"
        
        if self.imag > 0:
            return f"{self.real}+{self.imag}i"
        else:
            # 음수일 경우 부호가 자동으로 포함됨 (예: 1 + -2i -> 1-2i)
            return f"{self.real}{self.imag}i"

    def __add__(self, other):
        """덧셈 (페이지 84, 공식 1424)"""
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return ComplexNumber(real_part, imag_part)

    def __sub__(self, other):
        """뺄셈 (페이지 84, 공식 1425)"""
        real_part = self.real - other.real
        imag_part = self.imag - other.imag
        return ComplexNumber(real_part, imag_part)

    def __mul__(self, other):
        """곱셈 (페이지 84, 공식 1426)"""
        x, y = self.real, self.imag
        u, v = other.real, other.imag
        real_part = (x * u) - (y * v)
        imag_part = (x * v) + (y * u)
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        """나눗셈 (페이지 84, 공식 1439)"""
        x, y = self.real, self.imag
        u, v = other.real, other.imag
        
        denominator = (u**2 + v**2)
        if denominator == 0:
            print("오류: 0으로 나눌 수 없습니다.")
            return ComplexNumber(float('inf'), float('inf'))
            
        real_part = (x * u + y * v) / denominator
        imag_part = (y * u - x * v) / denominator
        return ComplexNumber(real_part, imag_part)


def parse_complex_str(s):
    """
    '1-2' 같은 문자열을 (1, -2)로 파싱하여 ComplexNumber 객체 반환
    (페이지 83, 예시 1406: "xy+uv")
    """
    # 정규표현식: (실수부: -? \d+) (허수부: [+-] \d+)
    match = re.match(r"(-?\d+)([+-]\d+)", s)
    if match:
        real = int(match.group(1))
        imag = int(match.group(2))
        return ComplexNumber(real, imag)
    return None

def main_ex5():
    """예제 5: 복소수 사칙연산 계산기 실행"""
    print("--- 🧮 예제 5: 복소수 사칙연산 계산기 ---")
    print("복소수 사칙연산을 수행합니다. (예: 1-2+3-4)")
    print("종료하시려면 '종료' 또는 빈 줄을 입력하세요.")

    # (복소수1)(연산자)(복소수2) 형식을 파싱
    # 예: ('1-2', '+', '3-4')
    parser_pattern = re.compile(r"(-?\d+[+-]\d+)([+\-\*\/])(-?\d+[+-]\d+)")

    while True:
        try:
            exp = input("식을 입력하세요: ").strip().replace(" ", "")
            if not exp or exp == '종료':
                print("(종료)")
                break

            match = parser_pattern.match(exp)
            if not match:
                print("잘못된 형식입니다. '실수부허수부연산자실수부허수부' (예: 1-2+3-4) 형식으로 입력하세요.")
                continue

            s1, op, s2 = match.groups()
            
            c1 = parse_complex_str(s1)
            c2 = parse_complex_str(s2)

            if c1 is None or c2 is None:
                print("잘못된 숫자 형식입니다.")
                continue
            
            result = None
            if op == '+':
                result = c1 + c2
            elif op == '-':
                result = c1 - c2
            elif op == '*':
                result = c1 * c2
            elif op == '/':
                result = c1 / c2
            
            if result:
                # 슬라이드 예제 (1-2+3-4)의 답은 '2-6i' [1409]로 표기되어 있으나,
                # (1-2i) + (3-4i) = (1+3) + (-2-4)i = 4-6i 입니다.
                # 슬라이드 예제 (1-2*3-4)의 답은 '-5-10i' [1412]이며,
                # (1-2i) * (3-4i) = (1*3 - (-2)*(-4)) + (1*(-4) + (-2)*3)i
                # = (3 - 8) + (-4 - 6)i = -5 - 10i (일치)
                # 덧셈 예제의 오타로 판단하고 계산 결과를 그대로 출력합니다.
                print(f"결과: {result}")

        except Exception as e:
            print(f"오류가 발생했습니다: {e}")
            
    print("-" * 20 + "\n")

#예제 6번

class Library:
    """
    도서 대출을 관리하는 클래스.
    self.books: {도서명: 학번} (0이면 대출 가능)
    self.borrowers: {학번: 도서명} (중복 대출 방지용)
    (페이지 88, 슬라이드 1500-1506 기반 설계)
    """
    
    def __init__(self):
        """
        도서 목록(self.books)과 대출자 목록(self.borrowers)을 초기화합니다.
        (페이지 88, 슬라이드 1502-1506)
        """
        # self.books: {도서명: 학번} (0은 대출 가능 상태)
        self.books = {
            '파이썬 프로그래밍': 0,
            'C언어 정복': 0,
            '맨먼스 미신': 0,
            '뇌를 자극하는 C언어': 0
        }
        # self.borrowers: {학번: 도서명} (대출자 정보)
        self.borrowers = {}

    def rent_process(self):
        """
        도서 대출 처리를 담당합니다. (페이지 86, 작업 1)
        """
        book_name = input("도서명을 입력하세요: ").strip()
        student_id = input("학번을 입력하세요: ").strip()

        # [조건 2] 사용자는 한 권의 도서만 대여할 수 있다. (페이지 86, 1473)
        if student_id in self.borrowers:
            print(f"오류: 대출한 도서('{self.borrowers[student_id]}')를 먼저 반납하시기 바랍니다.")
            return

        # (페이지 86, 1471)
        if book_name not in self.books:
            print("오류: 소장하지 않은 도서입니다.")
            return

        # [조건 4] 이미 대출된 도서는 대출할 수 없다. (페이지 86, 1472)
        if self.books[book_name] != 0:
            print(f"오류: 이미 대여된 도서입니다. (대출자: {self.books[book_name]})")
            return

        # 대출 성공 (페이지 86, 1470)
        self.books[book_name] = student_id
        self.borrowers[student_id] = book_name
        print("대출되었습니다.")

    def return_process(self):
        """
        도서 반납 처리를 담당합니다. (페이지 86, 작업 2)
        """
        book_name = input("도서명을 입력하세요: ").strip()
        student_id = input("학번을 입력하세요: ").strip()

        # (페이지 86, 1479)
        if student_id not in self.borrowers:
            print("오류: 대출 이력이 없습니다.")
            return

        # (페이지 86, 1478)
        if self.borrowers[student_id] != book_name:
            print(f"오류: 반납 대상 도서가 아닙니다. (대출한 도서: '{self.borrowers[student_id]}')")
            return
            
        # (페이지 86, 1471 - 소장 도서가 맞는지 확인)
        if book_name not in self.books:
            print("오류: 소장하지 않은 도서입니다. (데이터 불일치)")
            return

        # 반납 성공 (페이지 86, 1477)
        self.books[book_name] = 0
        del self.borrowers[student_id]
        print("반납되었습니다.")

def main_ex6():
    """예제 6: 도서 대출관리 프로그램 실행"""
    print("--- 🏛️ 예제 6: 도서 대출관리 ---")
    lib = Library()
    
    while True:
        print("\n--- 도서 대출 관리 ---")
        print("1. 대출")
        print("2. 반납")
        print("3. 종료")
        task = input("작업을 선택하세요: ").strip()

        if task == '1':
            lib.rent_process()
        elif task == '2':
            lib.return_process()
        elif task == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")
            
    print("-" * 20 + "\n")

#예제 7번

class Employee:
    """
    [조건 1] 사원 정보를 담는 클래스.
    (부서, 직급, 이름, 사번)
    """
    def __init__(self, emp_id, name, dept, position):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.position = position

    def __str__(self):
        """목록 및 조회 시 출력 형식 (페이지 91, 1557)"""
        return f"{self.dept} {self.position} {self.name}({self.emp_id})"

class EmployeeManager:
    """
    사원 입/퇴사, 목록, 조회를 관리하는 클래스.
    """
    def __init__(self):
        # self.employees: {사번: Employee 객체} 형태로 사원 관리
        self.employees = {} 
        # 사번은 10000번부터 순차적으로 자동