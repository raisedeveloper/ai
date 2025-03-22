# while 문과 if문을 같이 사용하여 간단한 계산기 프로그램을 만들어 보세요.

# 사용자로부터 두 개의 숫자와 연산자(+, -, *, /)를 입력받아 계산 결과를 출력하는 프로그램을 작성하세요.
# while 문을 사용하여 계산을 반복하도록 구현하세요.
# 사용자가 'q'를 입력하면 프로그램을 종료하도록 하세요.
# 0으로 나누는 경우 "0으로 나눌 수 없습니다."를 출력하고 다시 입력을 받으세요.
# 잘못된 연산자가 입력되면 "잘못된 연산자입니다."를 출력하고 다시 입력을 받으세요.

# break & continue
# brak 만나면 반복만 벗어남
# continue 아래의 코드는 실행되지 않고, 반복문의 조건 검사로 다시 돌아감


#################문제2########################
# number1 = input("첫번 째 숫자를 입력하세요: ")
# number1 = float(number1)
# number2 = input("두번 째 숫자를 입력하세요: ")
# number2 = float(number2)

# while True:
#   m = input("연산을 입력하세요(+,-,*,/): ")
#   if m not in ['+', '-', '*', '/']:
#     m = input("연산을 다시 입력하세요(+,-,*,/): ")
#   elif m == '+':
#     print(number1 + number2)
#   elif m == '-':
#     print(number1 - number2)
#   elif m == '*':
#     print(number1 * number2)
#   elif m == '/':
#     if number2 == 0:
#       print("0으로 나눌 수 없습니다.")
#       break
#     else:
#       print(number1/number2)
#   print("계속하려면 연산자를 누르세요. 종료하려면 'q'를 입력하세요: ")
#   if input() == 'q':
#     break

##################################################


# while True:
#     # 첫 번째 숫자 입력 (잘못된 입력 처리)
#     try:
#         number1 = input("숫자1을 입력하세요: ")
#         if number1 == 'q':
#             print("프로그램을 종료합니다.")
#             break
#         number1 = float(number1)
#     except ValueError:
#         print("잘못된 숫자입니다. 숫자를 다시 입력하세요.")
#         continue

#     # 두 번째 숫자 입력 (잘못된 입력 처리)
#     try:
#         number2 = input("숫자2을 입력하세요: ")
#         if number2 == 'q':
#             print("프로그램을 종료합니다.")
#             break
#         number2 = float(number2)
#     except ValueError:
#         print("잘못된 숫자입니다. 숫자를 다시 입력하세요.")
#         continue

#     # 연산자 입력
#     while True:
#         m = input("연산을 입력하세요(+,-,*,/): ")
#         if m == 'q':
#             print("프로그램을 종료합니다.")
#             break
#         if m not in ['+', '-', '*', '/']:
#             print("잘못된 연산자입니다. 다시 입력하세요.")
#         else:
#             break
    
#     # 연산 수행
#     if m == '+':
#         print(f"{number1} + {number2} = {number1 + number2}")
#     elif m == '-':
#         print(f"{number1} - {number2} = {number1 - number2}")
#     elif m == '*':
#         print(f"{number1} * {number2} = {number1 * number2}")
#     elif m == '/':
#         if number2 == 0:
#             print("0으로 나눌 수 없습니다.")
#         else:
#             print(f"{number1} / {number2} = {number1 / number2}")
    
#     # 프로그램 종료 여부 확인
#     continue_program = input("계속하려면 엔터를 누르세요. 종료하려면 'q'를 입력하세요: ")
#     if continue_program == 'q':
#         print("프로그램을 종료합니다.")
#         break