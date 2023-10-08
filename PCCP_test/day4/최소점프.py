from collections import deque
def solution(home):
    answer=0
    ch=[0]*10001
    Q=deque()
    Q.append(0)
    ch[0]=1
    L=0
    while Q:
        n= len(Q)
        for i in range(n):
            x= Q.popleft()
                for nx in [x-1, x+1, x+5]:
                if nx >=0 and nx<=10000 and ch[nx] ==0:
                    ch[nx]=1
                    Q.append(nx)

        L +=1

         return answer
        
        print(solution(10))