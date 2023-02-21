def generator(n):
    for i in range(0,n):
        if i%3==0 or i%4==0:
            yield i 


n=(int)(input())
divisible=generator(n)
for i in range(0,n):
    print(next(divisible),end=" ")