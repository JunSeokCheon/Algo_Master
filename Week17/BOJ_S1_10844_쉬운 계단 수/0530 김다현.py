'''
< 백트래킹을 이용한 풀이 ==> 메모리 초과로 실패ㅠㅠ >
1. 한자리씩 이동하면서 0은 1로 9는 8로 2~8은 두가지 경우의 수로 이동하게함.
2. 입력받은 길이가 되면 return 해주기
'''
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
visited = set()
def dp(num,path):
    global cnt
    global visited
    if path=='0': #0으로 시작하면 탐색아예 안하게 해서 시간단축
        return
    if len(path)==n:
        cnt+=1
        visited.add(path)
        return
    else:
        if num==9:
            dp(num-1,path + str(num-1))
            path = path[:-1]
        elif num==0:
            dp(num+1,path + str(num+1))
            path = path[:-1]
        else:
            dp(num+1,path + str(num+1))
            dp(num-1,path + str(num-1))
            path = path[:-1]
for i in range(1,10):
    dp(i,'')
print(len(visited))

'''
<DP를 이용한 풀이>
1. 그리디, 구현, 완전 탐색으로 일단 해보기
2. 재귀 함수로 비효율적인 완탐을 작성한 뒤 중간답을 기억할 수 있다면 DP사용!
'''
