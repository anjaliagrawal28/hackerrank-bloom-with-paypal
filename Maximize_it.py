from itertools import product
k,m = map(int,input().split())
num=[]
for _ in range(k):
    r = map(int,input().split()[1:])
    num.append(map(lambda x:x**2%m, r))
print(max(map(lambda x: sum(x)%m, product(*num))))
