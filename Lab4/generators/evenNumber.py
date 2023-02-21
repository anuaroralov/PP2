def generator(n):
    for i in range(0,n):
        if i%2==0:
            yield i 


n=(int)(input())
evenNumbers=generator(n)
for i in range(0,n):
    print(next(evenNumbers),end=" ")