# py10_function.py - 함수
# 수학의 함수와 동일

print('함수!!') ## 내장(built-in)함수

# 함수 정의(definition)
## 사용자 정의함수
def add(a, b):
    result = a + b
    return result # return -> 결과를 돌려줘(반환하라!)

def minus(a, b):
    result = a - b
    return result

def multiple(a, b):
    result = a * b
    print('곱은 -> ', result)
    # return # 아무것도 반환할 게 없으면 리턴은 생략함 

def divide(a, b):
    zzzzzz = a / b
    return zzzzzz

x = 11
y = 22
z = add(x,y)
print('합의결과는', z, '입니다')

x = 101
y = 203
print('합의결과는', add(x, y), '입니다')

x = 35
y = 15
print('차의 결과는', minus(x, y))

x = 30
y = 10
z = multiple(x, y)
print(z)

x = 100
y = 5
z = divide(x, y)
print(z)


''' 내장 함수 - 파이썬에서 자주 사용할것같은 함수를 미리 만들어 둔것 '''
'''# 대부분 stdlib(standard library)에 들어있음
print(max(1, 3, 7, 15))
print(min(1, 3, 7, 15))
print(abs(-5)) # 절대값 ->5
print(2 ** 10) # 2의 10승
print(pow(2, 10)) # 2의 10승 (power) == 2 ** 10
'''
