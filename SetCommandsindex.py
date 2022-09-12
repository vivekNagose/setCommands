n = int(input())
s = set(map(int, input().split()))
N=int(input())
command=None
item=None
for i in range(N):
    command, *item=input().split()
    if command=="remove":
        s.remove(int(item[0]))
    if command=="pop":
        s.pop()
    if command=="discard":
        s.discard(int(item[0]))
p=sum(s)
print(p)


# #input
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5
#
# #Output
# 4
