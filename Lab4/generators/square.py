n=int(input())
square=(int(i)**2 for i in range(n))
for i in range(n):
    print(next(square))