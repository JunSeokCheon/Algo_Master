'''
<접근법>
1. path에 한글자씩 저장한다.
2. <를 만나면 answer에 이전까지 저장한 path를 거꾸로 추가
3. >를 만나면 answer에 이전까지 저장한 path를 그대로 추가
4. list(map(~~))을 안쓰면 문자열 그대로 반대되서 오답 , 공백 기준으로 나눠야함
'''
```python
import sys
input = sys.stdin.readline
s= input().strip()
path=''
answer=''

for i in s:
    if i=='<':
        answer+=' '.join(list(map(lambda x: x[::-1],path.split(' '))))
        path=''
        path+=i
    elif i=='>':
        path+=i
        answer+=path
        path=''
    else:
        path+=i
answer+=' '.join(list(map(lambda x: x[::-1],path.split(' '))))
print(answer)
```