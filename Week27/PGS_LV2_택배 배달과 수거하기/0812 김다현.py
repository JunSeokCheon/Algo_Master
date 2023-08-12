```
<Greedy>
참고: https://oh2279.tistory.com/147
```
```python
def solution(cap, n, deliveries, pickups):
    #시간 제한 때문에 거꾸로 뒤집기  
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer= 0
    
    dv=0
    pu=0
    #포인트✨: 멀리서 부터 탐색해야함!! 
    for i in range(n):
        #음수라면 cap이하이므로 겸사겸사 한꺼번에 해결가능 
        dv += deliveries[i]
        pu += pickups[i]
        #반대로 양수가 됬다는건 cap이상이므로 물류창고로 다시 가야함 
        while dv > 0 or pu > 0:
            dv -= cap 
            pu -= cap
            answer += (n-i) *2 #한번 가면 무조건 다시 물류창고로 와야함
    return answer
```