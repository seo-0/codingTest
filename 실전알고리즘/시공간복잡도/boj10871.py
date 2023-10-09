# a, b= map(int, input().split())
# c= [a] 
# i=0 
# def func1():
#     for i in range(a):
#         if c[i] < b:
#             print(c[i])
#             i+=1
# result= c[i]
a, b= map(int, input().split())
num = list(map(int, input().split()))

for i in range(a):
    if num[i] <b:
        print(num[i], end= " ")