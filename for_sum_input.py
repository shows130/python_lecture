n =int(input('수를 입력하세요'))

a=0
for i in range (1, n+1):
    a += i
    print(a)
    print('1부터',n, '까지의 합은' ,a)
    print('1부터 {}까지의 합은 {}'.format(n, a))
    print(f'1부터 {n} 까지의 합은 {a}' )