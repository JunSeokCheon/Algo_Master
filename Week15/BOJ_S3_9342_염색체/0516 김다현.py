import sys
input = sys.stdin.readline
from collections import deque, OrderedDict

n = int(input())
for _ in range(n):
    st= list(input().strip())
    q = deque(st)
    if q[0] in ['A','B','C','D','E','F']:
        q.popleft()
    q = deque(list(OrderedDict.fromkeys(list(q)))) #순서 보장한채 중복제거

    for i in ['A','F','C']:
        if i==q[0]:
            q.popleft()
        
    st = ''.join(q)
    if st.endswith('A') or st.endswith('B') or st.endswith('C') or st.endswith('D') or st.endswith('E') or st.endswith('F'):
        q.popleft()
    answer = 'Infected!' if not q else 'Good'
    print(answer) 
            

        