#perfect no
n=int(input())
nn=0
for i in range(1,n):
    if n%i==0:
        nn+=i
if nn==n:
    print("perfect")
else:
    print("not perfect")
