inp=input().split()
m=int(inp[0])
n=int(inp[1])
s=list()
count = 0
s=list(map(int,input().strip().split()))
a=set(map(int,input().strip().split()))
b=set(map(int,input().strip().split()))
for i in s:
    if i in a:
        count+=1
    if i in b:
        count-=1
print(count)
