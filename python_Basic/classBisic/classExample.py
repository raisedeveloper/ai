###  class1 - 간단한 클래스 예제   ###
class Dof:
    #초기화 메서드 (생성자)
    def __init__(self,name):
        self.name = name # 인스턴스 변수
        
    def bark(self):
        print(f"{self.name}가 짖습니다!")
            
# 객체 형성
my_dog = Dog("멍멍이")
my_dog.bark()   # 출력 : 멍멍이가 짖습니다.





### class2 - 클래스 예제(상속) ###
class Animal:
    #초기화 메서드 (생성자)
    def __init__(self,name):
        self.name = name # 인스턴스 변수 - instance : 객체
        
    def speak(self):
        pass

class Cat(Animal):  #Animal 클래스 상속
    def speak(self):
        return f"{self.name}가 야옹하고 웁니다."

# 객체 생성 및 사용 
cat1 = Cat("나비")  # Cat 클래스의 인스턴스(객체) 생성
print(cat1.name) # 출력 : 미야
print(cat1.speak())   # 출력 : 나비가 야옹하고 웁니다.

cat2 = Cat("나비")  # Cat 클래스의 인스턴스(객체) 생성
print(cat2.name) # 출력 : 미야
print(cat2.speak())   # 출력 : 나비가 야옹하고 웁니다.





# class3 - 클래스 예제(캡슐화) ###

class BankAccount:
    def __init__(self):
        sef.__balance = 0   # 비공개 변수
        
    def deposit(self, amount):
        if amount>>0:
            self.__balance
            
# 실행 예제
account = BankAccount()
account.deposit(1000)
print(account.get_balance())    # 출력 : 1000
# print(account._balance)   # 오류발생 : 직접 접근 불가





### class4 - 클래스 변수와 인스턴스 변수 예제 ###

class Student:
    school_name = "파이썬 고등학교" # 클래스 변수
    student_count = 0   # 클래스 변수
    
    def __init__(self,name):
        self.name = name    #인스턴스 변수
        Student.student_count += 1
        
### 실행예제 ###
student1 = Student("김철수")
student2 = Student("김영희")

print(Student.school.name)  # 출력: 파이썬 고등학교
print(student1.school_name) # 출력: 파이썬 고등학교
print(student2.school_name) # 출력: 파이썬 고등학교
print(Student.student_count)    # 출력: 2




### class5 - 클래스 예시(계산기) ###
#   계산기 클래스 예제
class Calculator:
    # 초기화 메서드: 아무 상태 없이 계산만 수행
    def __init__(self):
        print("계산기를 초기화합니다.")
        
    # 두 숫자를 더하는 메서드
    def add(self,a,b):
        return a + b
    # 두 숫자를 곱하는 메서드
    def multiply(self, a, b):
        return a * b
    
    # 객체 생성 및 메서드 호출
    calc = Calculator()  # 출력 : 계산기를 초기화 합니다.
    print("덧셈 결과:", calc.add(10, 20))    # 출력 : 덧셈결과 : 30
    print("곱셈 결과:", calc.multiply(10, 20))  # 출력 : 곱셈결과 : 200
    
    
    
    
### class6 - 클래스 예시(계산기) ###
# 학생정보 관리 클래스 예제
class Student:
    # 생성자 : 학생 이름과 나이를 초기화    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 학생 정보 출력 메서드
    def display_info(self):
        print(f"이름: {self.name}, 나이: {self.age}")
        
# 객체 생성 및 메서드 호출
student1 = Student("홍길동", "16")
student2 = Student("김철수", "18")

student1.display_info()    # 출력 : 이름: 홍길동, 나이 : 16
student2.display_info()    # 출력 : 이름: 김철수, 나이 : 18




### class7 - 클래스 예시(영화티켓할인) ###
#영화 티켓 할인 관리 클래스 예제
class MovieTicket:
    # 생성자 : 영화 제목과 기본 티켓 가격 초기화
    def __init__(self, title, price):
        self.title = title
        self.price = price
    #할인 적용 메서드
    def apply_discount(self, discount):
        self.pprice -= discount
        print("f{self.title} 영화의 할인된 가격: {self.price}원")
            
# 객체 생성 및 메서드 호출
ticket = MovieTicket("어벤져스",  12000)
ticket.apply_discount(2000) # 출력 : 어벤져스 영화의 할인된 가격 : 10000원




### class8 - 클래스 예시(은행계좌) ###
# 간단한 은행 계좌 클래스

class BankAccount:
    def __init(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    # 입금
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}원이 입금되었습니다. 현재 잔액: {self.balance}원")
    # 출금
    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족합니다.")
        else:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다. 현재잔액: {self.balance}원")
            
# 사용 예시
account = BankAccount("홍길동", 10000)
account.deposit(5000)   # 출력 : 5000원이 입금되었습니다. 현재 잔액: 15000원
account.withdraw(20000) # 출력 : 2000원이 출금되었습니다. 현재 잔액: 13000원