import re
import sys

# 예제 1: Tmoney
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
    """예제 1: T-money 확인"""
    print("--- 예제 1: T-money ---")
    
    my_tmoney = Tmoney()
    friend_tmoney = Tmoney()

    print("--- 1, 2번 인스턴스에 10,000원 충전 ---")
    my_tmoney.charge(10000)
    friend_tmoney.charge(10000)
    print(f"my_tmoney 잔액: {my_tmoney.balance}원")
    print(f"friend_tmoney 잔액: {friend_tmoney.balance}원")

    print("\n--- 1, 2번 인스턴스에서 1,000원 사용 ---")
    my_tmoney.use(1000)
    friend_tmoney.use(1000)
    print(f"my_tmoney 잔액: {my_tmoney.balance}원")
    print(f"friend_tmoney 잔액: {friend_tmoney.balance}원")
    print("-" * 20 + "\n")

# 예제 2: 공유 펀드
class SharedFund:
    """
    공유 잔고(deposit)는 클래스 변수로,
    개인 잔고(deposit)는 인스턴스 변수로 가집니다.
    """
    
    # 클래스 변수 (공유 잔고)
    deposit = 0

    def __init__(self):
        # 인스턴스 변수 (개인 잔고)
        self.deposit = 0

    def send_to_class(self, amount):
        """인스턴스 -> 클래스 송금"""
        if self.deposit >= amount:
            self.deposit -= amount
            SharedFund.deposit += amount
            print(f"인스턴스 -> 클래스 {amount}원 송금. (인스턴스 잔고: {self.deposit}, 클래스 잔고: {SharedFund.deposit})")
        else:
            print(f"인스턴스 잔고가 부족하여 송금할 수 없습니다. (인스턴스 잔고: {self.deposit})")

    def receive_from_class(self, amount):
        """클래스 -> 인스턴스 송금"""
        if SharedFund.deposit >= amount:
            SharedFund.deposit -= amount
            self.deposit += amount
            print(f"클래스 -> 인스턴스 {amount}원 송금. (인스턴스 잔고: {self.deposit}, 클래스 잔고: {SharedFund.deposit})")
        else:
            print(f"클래스 잔고가 부족하여 송금받을 수 없습니다. (클래스 잔고: {SharedFund.deposit})")

def main_ex2():
    """예제 2: 자유 적금 확인"""
    print("--- 예제 2: 자유 적금 ---")
    
    SharedFund.deposit = 10000
    s1 = SharedFund()
    s2 = SharedFund()
    print(f"초기 상태 - 클래스: {SharedFund.deposit}, s1: {s1.deposit}, s2: {s2.deposit}")

    s1.receive_from_class(10000)
    print(f"결과 (s1이 받음) - 클래스: {SharedFund.deposit}, s1: {s1.deposit}, s2: {s2.deposit}")

    # 확인을 위해 s2가 5,000원을 가지고 있다고 가정
    s2.deposit = 5000
    print(f"\n[확인을 위해 s2에 5,000원 임의 충전] - 클래스: {SharedFund.deposit}, s1: {s1.deposit}, s2: {s2.deposit}")
    s2.send_to_class(5000)
    print(f"결과 (s2가 보냄) - 클래스: {SharedFund.deposit}, s1: {s1.deposit}, s2: {s2.deposit}")
    print("-" * 20 + "\n")

# 예제 3: 수강 과목
class Course:
    """
    과목명, 과목코드, 학점 정보를 가지며 평점(GPA) 변환 기능을 제공합니다.
    """
    
    # 학점 -> 평점(GPA) 변환 매핑 (클래스 변수)
    GRADE_TO_GPA = {
        'A+': 4.5, 'A': 4.0,
        'B+': 3.5, 'B': 3.0,
        'C+': 2.5, 'C': 2.0,
        'D+': 1.5, 'D': 1.0,
        'F': 0.0
    }

    def __init__(self, name, code, grade):
        self.name = name
        self.code = code
        self.grade = grade

    def get_gpa(self):
        """학점을 평점(GPA)으로 환산"""
        return self.GRADE_TO_GPA.get(self.grade, 0.0)

    def print_info(self):
        """과목 정보(평점 포함)를 한 줄로 출력"""
        gpa = self.get_gpa()
        print(f"과목명: {self.name}, 과목코드: {self.code}, 학점: {self.grade}, 평점: {gpa}")

def main_ex3():
    """예제 3: 수강과목 확인"""
    print("--- 예제 3: 수강과목 ---")
    
    c1 = Course("비주얼 프로그래밍", "CSE101", "A+")
    c2 = Course("자료구조", "CSE102", "B")
    c3 = Course("운영체제", "CSE103", "F")
    
    course_list = [c1, c2, c3]

    for course in course_list:
        course.print_info()
    
    print("-" * 20 + "\n")
    
    # 예제 4에서 사용하기 위해 반환
    return c1, c2, c3

# 예제 4: 과목 관리
class CourseManager:
    """
    Course 인스턴스 리스트를 관리하며, 전체 평점 계산 및 과목 검색 기능을 제공합니다.
    """
    
    def __init__(self):
        # Course 객체들을 저장할 리스트
        self.courses = []

    def add_course(self, course):
        """Course 인스턴스를 관리 목록에 추가"""
        if isinstance(course, Course):
            self.courses.append(course)
        else:
            print("Course 객체만 추가할 수 있습니다.")

    def calculate_total_gpa(self):
        """
        보유한 Course 인스턴스로부터 전체 평점을 계산 (F학점 포함)
        """
        if not self.courses:
            return 0.0
        
        total_gpa_sum = sum(course.get_gpa() for course in self.courses)
        
        return total_gpa_sum / len(self.courses)

    def search_course(self, code):
        """특정 과목코드를 검색"""
        found = False
        for course in self.courses:
            if course.code == code:
                print(f"검색 결과 (과목코드: {code}):")
                course.print_info()
                found = True
                break
        if not found:
            print(f"검색 결과: 과목코드 {code}에 해당하는 과목을 찾을 수 없습니다.")

def main_ex4(c1, c2, c3):
    """예제 4: 과목관리 확인 (예제 3의 인스턴스 사용)"""
    print("--- 예제 4: 과목관리 ---")
    manager = CourseManager()
    
    manager.add_course(c1)
    manager.add_course(c2)
    manager.add_course(c3)

    total_gpa = manager.calculate_total_gpa()
    # (4.5 + 3.0 + 0.0) / 3 = 2.5
    print(f"전체 평점 (F 포함): {total_gpa:.2f}")

    print("\n--- 과목 검색 테스트 ---")
    manager.search_course("CSE102") # 성공
    manager.search_course("CSE999") # 실패
    print("-" * 20 + "\n")

import re

# 이미지에서 제공된 Complex 클래스를 기반으로 수정
class Complex:
    # __init__ 메서드: 이미지와 동일하게 'r'과 'i'를 사용
    def __init__(self, r, i):
        self.r = r
        self.i = i

    # __repr__ 메서드: 이미지의 메서드는 출력이 불완전하여
    # 이전 코드의 __str__과 같이 더 명확한 출력이 되도록 수정
    def __repr__(self):
        """출력 형식 (예: 1-1i, 1+2i)"""
        if self.i == 0:
            return f"{self.r}"
        if self.r == 0:
            return f"{self.i}i"
        
        if self.i > 0:
            return f"{self.r}+{self.i}i"
        else:
            # self.i가 음수일 경우 (예: -1)
            return f"{self.r}{self.i}i" # "1-1i"

    # __add__ 메서드: 이미지와 동일하게 'value'를 인자로 사용
    def __add__(self, value):
        return Complex(r=self.r + value.r,
                       i=self.i + value.i)

    # __sub__ 메서드: 덧셈/뺄셈 요청에 맞춰 뺄셈 기능 추가
    def __sub__(self, value):
        return Complex(r=self.r - value.r,
                       i=self.i - value.i)


def parse_complex_str(s):
    """'1-2' 같은 문자열을 (1, -2)로 파싱하여 Complex 객체 반환"""
    match = re.match(r"(-?\d+)([+-]\d+)", s)
    if match:
        real = int(match.group(1))
        imag = int(match.group(2))
        # Complex 클래스의 __init__에 맞게 r과 i로 전달
        return Complex(r=real, i=imag)
    return None

def main_ex5():
    """예제 5: 복소수 덧셈/뺄셈 계산기 (1회 실행)"""
    print("--- 예제 5: 복소수 덧셈/뺄셈 계산기 ---")
    print("복소수 덧셈 또는 뺄셈을 1회 수행합니다. (예: 1-2+3-4)")

    # 덧셈(+)과 뺄셈(-) 연산자만 허용
    parser_pattern = re.compile(r"(-?\d+[+-]\d+)([+\-])(-?\d+[+-]\d+)")

    # while 루프 없이 1회만 실행
    try:
        exp = input("식을 입력하세요: ").strip().replace(" ", "")
        
        match = parser_pattern.match(exp)
        if not match:
            print("잘못된 형식입니다. '실수부허수부[+,-]실수부허수부' (예: 1-2+3-4) 형식으로 입력하세요.")
            return # 함수 종료

        s1, op, s2 = match.groups()
        
        c1 = parse_complex_str(s1)
        c2 = parse_complex_str(s2)

        if c1 is None or c2 is None:
            print("잘못된 숫자 형식입니다.")
            return # 함수 종료
        
        result = None
        if op == '+':
            result = c1 + c2
        elif op == '-':
            result = c1 - c2
            
        if result:
            print(f"결과: {result}")

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
        
    print("-" * 20 + "\n")
    print("(1회 계산 완료. 프로그램을 종료합니다.)")


if __name__ == "__main__":
    
    # 1. main_ex1() 실행
    main_ex1()
    
    # 2. main_ex2() 실행
    main_ex2()
    
    # 3. main_ex3()을 실행하고, 반환되는 Course 객체들을 c1, c2, c3 변수에 저장
    c1, c2, c3 = main_ex3()
    
    # 4. main_ex4()에 위에서 받은 c1, c2, c3 객체를 전달하여 실행
    main_ex4(c1, c2, c3)
    
    # 5. main_ex5() 실행
    main_ex5()

# # 예제 6: 도서관
# class Library:
    
#     def __init__(self):
#         # self.books: {도서명: 학번} (0은 대출 가능 상태)
#         self.books = {
#             '파이썬 프로그래밍': 0,
#             'C언어 정복': 0,
#             '맨먼스 미신': 0,
#             '뇌를 자극하는 C언어': 0
#         }
#         # self.borrowers: {학번: 도서명} (대출자 정보)
#         self.borrowers = {}

#     def rent_process(self):
#         """도서 대출 처리"""
#         book_name = input("도서명을 입력하세요: ").strip()
#         student_id = input("학번을 입력하세요: ").strip()

#         # 조건 2: 사용자는 한 권의 도서만 대여 가능
#         if student_id in self.borrowers:
#             print(f"오류: 대출한 도서('{self.borrowers[student_id]}')를 먼저 반납하시기 바랍니다.")
#             return

#         if book_name not in self.books:
#             print("오류: 소장하지 않은 도서입니다.")
#             return

#         # 조건 4: 이미 대출된 도서는 대출 불가
#         if self.books[book_name] != 0:
#             print(f"오류: 이미 대여된 도서입니다. (대출자: {self.books[book_name]})")
#             return

#         # 대출 성공
#         self.books[book_name] = student_id
#         self.borrowers[student_id] = book_name
#         print("대출되었습니다.")

#     def return_process(self):
#         """도서 반납 처리"""
#         book_name = input("도서명을 입력하세요: ").strip()
#         student_id = input("학번을 입력하세요: ").strip()

#         if student_id not in self.borrowers:
#             print("오류: 대출 이력이 없습니다.")
#             return

#         if self.borrowers[student_id] != book_name:
#             print(f"오류: 반납 대상 도서가 아닙니다. (대출한 도서: '{self.borrowers[student_id]}')")
#             return
            
#         if book_name not in self.books:
#             print("오류: 소장하지 않은 도서입니다. (데이터 불일치)")
#             return

#         # 반납 성공
#         self.books[book_name] = 0
#         del self.borrowers[student_id]
#         print("반납되었습니다.")

# def main_ex6():
#     """예제 6: 도서 대출관리 프로그램"""
#     print("---  예제 6: 도서 대출관리 ---")
#     lib = Library()
    
#     while True:
#         print("\n--- 도서 대출 관리 ---")
#         print("1. 대출")
#         print("2. 반납")
#         print("3. 종료")
#         task = input("작업을 선택하세요: ").strip()

#         if task == '1':
#             lib.rent_process()
#         elif task == '2':
#             lib.return_process()
#         elif task == '3':
#             print("프로그램을 종료합니다.")
#             break
#         else:
#             print("잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")
            
#     print("-" * 20 + "\n")

# # 예제 7: 사원 관리
# class Employee:
#     """
#     사원 정보 (부서, 직급, 이름, 사번)를 담는 클래스.
#     """
#     def __init__(self, emp_id, name, dept, position):
#         self.emp_id = emp_id
#         self.name = name
#         self.dept = dept
#         self.position = position

#     def __str__(self):
#         """목록 및 조회 시 출력 형식"""
#         return f"{self.dept} {self.position} {self.name}({self.emp_id})"

# class EmployeeManager:
#     """
#     사원 입/퇴사, 목록, 조회를 관리하는 클래스.
#     """
#     def __init__(self):
#         # self.employees: {사번: Employee 객체}
#         self.employees = {} 
#         # 사번은 10000번부터 순차적으로 자동 부여
#         self.next_emp_id = 10000

#     def add_employee(self):
#         """사원 입사 처리"""
#         name = input("이름: ").strip()
#         dept = input("부서: ").strip()
#         position = input("직급: ").strip()
        
#         emp_id = str(self.next_emp_id)
#         self.next_emp_id += 1
        
#         new_employee = Employee(emp_id, name, dept, position)
#         self.employees[emp_id] = new_employee
        
#         print(f"{name}님이 입사처리 되었습니다. (사번: {emp_id})")

#     def remove_employee(self):
#         """사원 퇴사 처리"""
#         emp_id = input("퇴사처리 할 사원의 사번: ").strip()
        
#         if emp_id in self.employees:
#             removed_emp = self.employees.pop(emp_id)
#             print(f"{removed_emp} (사번: {emp_id})님이 퇴사처리 되었습니다.")
#         else:
#             print("오류: 해당 사번을 찾을 수 없습니다.")

#     def list_employees(self):
#         """전체 사원 목록 조회"""
#         print("--- 전체 사원 목록 ---")
#         if not self.employees:
#             print("(사원이 없습니다)")
#         else:
#             for emp in self.employees.values():
#                 print(emp)
#         print("---------------------")

#     def search_employee(self):
#         """사원 상세 조회 (사번 기준)"""
#         emp_id = input("조회할 사원의 사번: ").strip()
        
#         if emp_id in self.employees:
#             print("--- 사원 정보 ---")
#             print(self.employees[emp_id])
#             print("-----------------")
#         else:
#             print("오류: 해당 사번을 찾을 수 없습니다.")

# def main_ex7():
#     """예제 7: 사원 관리 프로그램"""
#     print("---  예제 7: 사원 관리 ---")
#     manager = EmployeeManager()
    
#     while True:
#         print("\n--- 사원 관리 프로그램 ---")
#         print("1. 입사")
#         print("2. 퇴사")
#         print("3. 전체 목록")
#         print("4. 사원 조회")
#         print("5. 종료")
#         task = input("작업을 선택하세요: ").strip()

#         if task == '1':
#             manager.add_employee()
#         elif task == '2':
#             manager.remove_employee()
#         elif task == '3':
#             manager.list_employees()
#         elif task == '4':
#             manager.search_employee()
#         elif task == '5':
#             print("프로그램을 종료합니다.")
#             break
#         else:
#             print("잘못된 입력입니다. 1, 2, 3, 4, 5 중에서 선택하세요.")
            
#     print("-" * 20 + "\n")


# # --- 메인 실행 ---
# def main():
#     if len(sys.argv) == 1:
#         # 인수가 없으면 모든 예제 실행
#         main_ex1()
#         main_ex2()
#         c1, c2, c3 = main_ex3() # 3번 실행 및 4번을 위한 인스턴스 받기
#         main_ex4(c1, c2, c3) # 4번 실행
#         main_ex5()
#         main_ex6()
#         main_ex7()
#     else:
#         # 특정 예제 번호를 인수로 받아 실행
#         example_num = sys.argv[1]
#         print(f"--- 예제 {example_num}번만 실행 ---")
#         if example_num == '1':
#             main_ex1()
#         elif example_num == '2':
#             main_ex2()
#         elif example_num == '3':
#             main_ex3()
#         elif example_num == '4':
#             print("[알림] 예제 4는 예제 3의 인스턴스가 필요합니다. 3번과 4번을 함께 실행합니다.")
#             c1, c2, c3 = main_ex3()
#             main_ex4(c1, c2, c3)
#         elif example_num == '5':
#             main_ex5()
#         elif example_num == '6':
#             main_ex6()
#         elif example_num == '7':
#             main_ex7()
#         else:
#             print(f"잘못된 예제 번호입니다: {example_num}. (1-7)")

# if __name__ == "__main__":
#     main()