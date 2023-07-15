import sys

# 초기 입력
n, m = map(int, sys.stdin.readline().split())
n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 8방향(x, y) 입력 , 방향(d)의 입력의 범위가 1~8이기 때문에 인덱스 0은 temp 값으로 처리
dx_8 = ["temp", 0, -1, -1, -1, 0, 1, 1, 1]
dy_8 = ["temp", -1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 4방향(물복사버그 마법을 위한 방향 체크)
dx_4 = [-1, -1, 1, 1]
dy_4 = [-1, 1, -1, 1]

# 첫 구름 좌표(좌표 -> 인덱스니깐 -1 해줘야한다.)
cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for _ in range(m):
    d, s = map(int, sys.stdin.readline().split())
    moved_cloud = []

    # 1. 구름 이동
    for x, y in cloud:
        # d방향으로 s만큼 이동(처음과 끝이 연결되어 있기 때문에 모듈로 연산)
        nx = (x + dx_8[d] * s) % n
        ny = (y + dy_8[d] * s) % n
        # 물의 양 증가
        n_list[nx][ny] += 1
        moved_cloud.append((nx,ny))
    
    # 2. 물복사버그 마법
    for x, y in moved_cloud:
        # 물이 있는 바구니 수 check
        check = 0
        # 대각선 4방향 check
        for i in range(4):
            nx = x + dx_4[i]
            ny = y + dy_4[i]

            # 범위가 벗어나지 않는지 check
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            # 바구니에 물이 1이상 있는지 check
            if n_list[nx][ny] > 0:
                check += 1
            
        # 바구니 수 만큼 값을 더한다.
        n_list[x][y] += check

    # 3. 구름 생성
    clouds = []
    for i in range(n):
        for j in range(n):
            # 구름이 생겼던 칸을 제외하고, 물의 양이 2 이상인 경우만 조건 수행
            if (i, j) in moved_cloud or n_list[i][j] < 2:
                continue
            # 물의 양을 2 감소하고, 새로운 구름 리스트 생성
            n_list[i][j] -= 2
            clouds.append((i,j))
    
    # 새로운 구름 리스트를 다시 루프 수행
    cloud = clouds

# 물의 합 계산
answer = 0
for i in range(n):
    for j in range(n):
        answer += n_list[i][j]
print(answer)