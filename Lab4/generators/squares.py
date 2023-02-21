a,b=map(int,(input().split()))
squares=(int(i)**2 for i in range(a,b))
for i in range(a,b):
    print(next(squares),end=" ")
