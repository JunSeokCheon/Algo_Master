import copy
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
empty = []
result = []


def bfs(X, Y):
    q = deque()
    q.append((X, Y))

    while q:
        X, Y = q.popleft()

        for d in range(4):
            nx = X + dir[d][0]
            ny = Y + dir[d][1]

            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                q.append((nx, ny))
                temp[nx][ny] = 2


for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty.append((i, j))

comb = list(combinations(empty, 3))

for com in comb:
    cnt = 0
    temp = copy.deepcopy(board)  # 하나의 예를 돌 때 마다 임시로 복사
    for x, y in com:
        temp[x][y] = 1

    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:  # 벽을 설치한 후 바이러스를 퍼트려 0의 개수를 확인함
                bfs(i, j)

    for i in temp:
        cnt += i.count(0)
    result.append(cnt)
print(max(result))
