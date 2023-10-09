import math
l,a,b,c,d= [ int(input()) for _ in range(5) ]

if (a/c) > (b/d):
    num= l- (a/c)
    print(math.trunc(num))
else:
    num= l- (b/d)
    print(math.trunc(num))