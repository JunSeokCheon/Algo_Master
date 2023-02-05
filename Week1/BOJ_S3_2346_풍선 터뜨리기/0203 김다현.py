from collections import deque

n=int(input())
q=deque(enumerate(map(int, input().split()),start=1))
ans=[]
while q:
    idx, num = q.popleft()
    if num>0:
        q.rotate(-(num-1))
    else:
        q.rotate(-num)
    ans.append(idx)
print(*ans)