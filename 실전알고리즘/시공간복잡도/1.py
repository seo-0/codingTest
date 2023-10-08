N= int(input("정수 N을 입력하세요: "))

def func1(N):
    total=0
    for i in range(1, N+1):
        if(i%3 ==0 or i%5 ==0):
            total+=i
       
    return total

result = func1(N)
print(f"이 문제의 정답은: {result}")

