#시간복잡도 o(루트n)
# n=int(input())
# def func3(n):
#     for i in range(1, n):
#         if i*i == n:
#             return 1
    
#     return 0
# print("입력값을 입력하세요: ", n)
# print(return)


def func3(N):
    i=1
    while i*i <=N:
        if i*i ==N:
            return 1
        i+=1
    return 0

N = int(input("양의 정수: "))
result = func3(N)

if result ==1:
    print(f"{N}은 제곱수 입니다.")
else:
    print(f"{N}은 제곱수가 아닙니다.")
