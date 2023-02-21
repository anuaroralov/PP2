n=int(input())
a=(int(i) for i in range(n,0,-1))
for i in range(0,n):
    print(next(a),end=" ")
print(a)