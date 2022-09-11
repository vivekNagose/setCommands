n = int(input())
s = set(map(int, input().split()))
N=int(input())
command=None
item=None
for i in range(N):
    command=input().split()
    item=input().split()
    if command=="remove":
        s.remove(int(item))
    if command=="pop":
        s.pop()
    if command=="discard":
        s.discard(int(item))
p=sum(s)
print(p)
