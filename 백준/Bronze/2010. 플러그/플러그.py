def solution():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N= int(data[0]) #멀티탭수
    
    plug= list(map(int, data[1:N+1])) #멀티탭의 플러그 수
   
    totalplug= sum(plug)
    
    maxplug= totalplug - (N-1)
    
    return maxplug

print(solution())