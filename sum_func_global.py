def print_sum():
    global a, b # a, b는 함수외부에서 선언된 a, b를 사용한다.
a = 100
b = 200
result = a + b
print('print_sum() 내부 :', a, '과', b, '의 합은', result, '입니다.')
a = 10
b = 20
print_sum()
result = a + b
print('print_sum() 외부 :', a, '과', b, '의 합은', result, '입니다.')