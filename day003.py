
####(1~3)일차 복습

#출력은 print()를 쓴다.
#변수에 대입해서 print를 쓰면 숫자, 영문, 사칙연산 등 골고루 출력이 가능하다.

#조건문 if
a = 3
if a > 2:
    print("a는 2보다 크다")

#반복문 for
for a in [1, 2, 3,]:
    print(a)

#반복문 while
i = 0 
while i < 3:
    i = i + 1
    print(i)

#함수
def add(a, b):
    return a + b
add(3, 4)
print(add(3, 4))


######################################################################

# 제곱 연산자
a = 3
b = 4
result = a ** b 
print(result)

# 연산자 간단 풀이
a = 10
b = 18
c = 2
d = 11

quiz_1 = a * b ** + 2 + c * 11
print(quiz_1)
# **뒤에 얼마나 곱해지는지 수를 써야함

# 모듈러(나머지연산자)
e = 10
f = 4
g = e % f
print(g)