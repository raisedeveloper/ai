num1 = 10
num2 = -20
print(num1, num2)

a = 10
b = 20
print (a + b)
print (a - b)
print (a / b)
print (a * b)

미지수 값 구하기
a = 12354123
a + b = 7845545

text = "Python"
print(text[2])
print(text[-3])
print(text[5])

text = "Python"
print(text[::3])
print([0:3:5]) // 왜 안되지?

text = "Python"
print(text.upper())

text = "banana"
print(text.find('a'))
print(text.count('a'))

text = " Hello World " # 양쪽 공백 제거 / 좌, 우 각각
print(text.strip())
print(text.lstrip())
print(text.rstrip())

text = " I love my sons "
print(text.strip())
print(text.rstrip())

text = "Python is fun"
words = text.split()
print(words)
joined_text = ' '.join(words)
print(joined_text)

name = "Eunice"
age = 30
print(f"My name is {name} and I am {age} years old.")

name = "bbolong"
age = 14
print(f"{name} is a well known as a cutie dog, he is {age} years old as a human age.")

#특수문자
print("Hello\nPython") #줄바꿈
print("탭을\t사용한\t예시") #탭
print("백슬래시는 이렇게 \\ 출력") #백슬래시

bool 지정하는 순간 T, F를 정해버림
a = True
b = False
print(a and b)
print(a or b)
print(not a)

불린 활용 예제
is_authentication = True
has_permission = False
if is_authentication and has_permission:
    print("접근 허용")
else:
    print("접근 거부")

리스트 생성과 초기화
[빈 리스트 생성]
enpty_list = []

#[초기값 설정]
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

인덱스 접근 및 슬라이싱
[인덱스로 접근]
fruits = ["apple", "bannaa", "cherry"]
print(fruits[0])

#슬라이싱
fruits = ["apple", "banana", "cherry"]
print(fruits[0:2])

#인덱스 값 변경 (리스트가 수정가능함)
list_numbers = [1, 2, 3, 4, 5]
list_numbers[0] = 10
print(list_numbers)

리스트 활용예제
초기값
numbers = [3, 1, 4, 1, 5]

# 요소 추가
numbers.append(9)
print(numbers)

# 요소 정렬
numbers.sort()
print(numbers)

# 요소 제거
numbers.remove(1)
print(numbers) #첫 번째 발견되는 1을 제거

# 특정 위치의 요소 추출 및 삭제
removed_item = numbers.pop(2) #팝콘 튀겨질 떄 튕겨낸다
print(numbers)
print(removed_item)

# 리스트 뒤집기
numbers.reverse()
print(numbers)

print(numbers)

# 리스트 요소 개수 세기
count = numbers.count(5)
print(count)

#리스트 복사
new_numbers = numbers.copy()
print(new_numbers) #원본 훼손 안되고 새로운 메모리 차지

#리스트 확장 - 뒤에 가져다 붙임
numbers.extend([6, 7, 8])
print(numbers)

#리스트 합치기
another_list = [10, 11, 12]
combined_list = numbers + another_list
print(combined_list)

튜플의 불변성(튜플은 수정이 불가)
my_tuple = (1, 2, 3, 4, 5)
my_tuple[0] = 10
print(my_tuple) # error 발생 => 튜플은 수정이 불가한 부분을 확인 // 리스트와 다른 부분

# 인덱스로 접근
colors = ("red", "green", "blue")
print(colors[1])

# 슬라이싱 = 마지막 숫자에서 -1
colors = ("red", "green", "blue")
print(colors[:-1]) # 앞을 비움은 모두 다 가져올게라는 의미 / 마이너스 -1은 맨 끝에 것 / 콜론 뒤 것은 제외해

# 특정 값의 개수 세기
numbers = (1, 2, 3, 2, 4)
print(numbers.count(2))

# 특정 값의 인덱스 찾기(index)
print(numbers.index(3))

#예제
point = (3, 4)
print("x 좌표:", point[0])
print("y 좌표:", point[1])

#딕셔너리
# 초기값 설정
empty_tuple = {}
person = {"name":"Bob", "age":30, "city": "New York"}

# 키를 통한 접근
person = {"name": "Bob", "age":30, "city": "New York"}
print(person["name"])

# 값 수정
person["age"] = 31
print(person["age"])

# 활용 예제
# 키에 대응하는 값 반환 (get)
info = {"name": "Charlie", "age": 22}
print(info.get("name"))

# 데이터가 아주 많을 때 값을 추출하는 데 유용
# 모든 키를 반환 (keys)
print(info.keys())

# 모든 값을 반환 (values)
print(info.values())

# 키 - 값 쌍을 튜플 형태로 반환 (items)
print(info.items())


if 조건문
score = 85
if score > 80:
    print("테스트에 합격하셨습니다.")
    
    number = 5
if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
    
score = 85
if score > 90:
    print("A학점")
elif score >= 80:
    print("B학점")
else:
    print("C학점")    
    
x, y = 10, 20
if x > 5 and y > 30:
    print("조건을 만족합니다.")
else:
    print("조건을 만족하지 않습니다.")

score = 100
if 90 <= score <= 100: # 90점 이상
    print("A학점")
elif 80 <= score < 90: #~89점
    print("B학점")
elif 70 <= score < 80: #~79점
    print("C학점")
elif 60 <= score < 70: #~69점
    print("D학점")
elif 50 <= score < 60: #~59점
    print("F학점")
elif score < 0: # 0보다 작으면
    print("잘못된 점수입니다.")
else: # 100보다 크면
    print("잘못된 점수입니다.")


기본 for문
numbers= [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)
    
# range()
for i in range(1, 6): # -1
    print(f"현재 값: {i}")
    
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i: {i}, j: {j}")
        
# enumerate() 
# 시퀀스를 순회하면서 인덱스와 값을 튜플형태로 함꺠 반환하는 내장 함수 
# 어떤 인덱스의 값 처리 중인지 알고 싶을 때 사용
items = ["A", "B", "C"]
for idx, item in enumerate(items):
    print(f"인덱스 {idx}: {item}")
    
# while문
# 조건이 참일 동안 특정 코드를 반복, 반복 횟수를 알 수 없을 때 사용
# 조건식의 값이 변하지 않으면 무한 루프 주의
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1 # count = count+1

while True:
    user_input = input("종료하려면 'exit' 입력: ")
    if user_input == "exit":
        break

조건과 else 사용 - 조건이 f로 바뀌면 else 블록 실행
x = 5
while x > 0:
    print(x)
    x -= 1
else:
    print("반복 종료")
    
# break & continue
# brak 만나면 반복만 벗어남
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue # 짝수는 출력 건너뜀
    print(n)
    if n == 7:
        break # 7에서 반복 종료
    
# input 함수 사용 예제
# input 함수 : 사용자로부터 입력을 받는 데 사용하는 내장함수, 문자열 형태로 변환
name = input("이름을 입력하세요: ")
print("안녕하세요. " + name + "님!")    

age = input("나이를 입력하세요. :")
age = int(age)
print("당신의 나이는", age, "살입니다.")

password = "password123"
attempt = 0
while attempt < 3:
    user_password = input("비밀번호를 입력하세요.")
    attemt += 1
    if user_password == password:
        print("비밀번호가 일치합니다.")
        break
    else:
        print("비밀번호가 틀렸습니다.")
if attempt == 3:
    print("비밀번호 입력 횟수를 초과했습니다.")
        