# a, b= map(int, input().split())
# a= [list(map(int, input()))for _ in range(a)]
import sys
# input = lambda:sys.stdin.readline().rstrip()

t= int(sys.stdin.readline())
for _ in range(t):
    # a, b= list(map(int, input().split()))
    a, b= map(int, sys.stdin.readline().split())
    print(a+b)

# a= int(input())
# b= [list(map(int, input().split()))]

