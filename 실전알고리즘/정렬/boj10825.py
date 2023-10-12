import sys
input = lambda : sys.stdin.readline().rstrip()

n= int(input())
a= []

for _ in range(n):
    name, kor, math, eng= input().split()
    a.append([name, int(kor), int(math), int(eng)])

a.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))

for x in a: #반복가능한객체-리스트의 첫번째 요소부터 마지막까지 반복, 각 반복단계에서 현재 요소는 x에 할당
    print(x[0])