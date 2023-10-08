def func4(n):
    i= 1

    while i*2 <= n:
        i *=2   # i**2 거듭제곱꼴이 아니라 i*2로 표현해야 2,4,16의제곱으로 안나옴
    return i

n= int(input("정수를 입력하세요: "))

result = func4(n)
print(result)

