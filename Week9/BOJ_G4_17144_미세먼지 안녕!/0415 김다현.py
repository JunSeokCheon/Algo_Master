import sys
input = sys.stdin.readline

r,c,t = map(int, input().split())

arr= [list(map(int, input().split())) for _ in range(r)]

up , down = 0,0

#공기청정기 위치 찾기
for i in range(r):
    if arr[i][0]==-1: #항상 1열에 있으므로
        up=i
        down = i+1
        break

def spread():
    dx=[-1,0,0,1]
    dy=[0,-1,1,0]
    
    t_arr = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j]!=0 and arr[i][j]!=1:
                tmp=0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k]+j
                    if 0<=nx<r and 0<=ny<c and arr[nx][ny]!= -1:
                        t_arr[nx][ny]+= arr[i][j]//5
                        tmp += arr[i][j]//5
                arr[i][j] -= tmp #퍼뜨린만큼 -
    for i in range(r):
        for j in range(c):
            arr[i][j] += t_arr[i][j] #퍼뜨리기
def u():
    dx=[0,-1,0,1]
    dy= [1,0,-1,0]
    direct =0
    before = 0
    x,y = up,1
    while True:
        nx= x+dx[direct]
        ny = y+dy[direct]
        if x==up and y==0:
            break
        if nx<0 or nx>=r or ny<0 or ny>=c:
            direct+=1
            continue
        #swap
        arr[x][y],before = before, arr[x][y]
        x= nx
        y=ny

def d():
    dx=[0,1,0,-1]
    dy= [1,0,-1,0]
    direct =0
    before = 0
    x,y = down,1
    while True:
        nx= x+dx[direct]
        ny = y+dy[direct]
        if x==down and y==0:
            break
        if nx<0 or nx>=r or ny<0 or ny>=c:
            direct+=1
            continue
        #swap
        arr[x][y],before = before, arr[x][y]
        x= nx
        y=ny

for _ in range(t):
    spread()
    u()
    d()
    
answer=0
for i in range(r):
    for j in range(c):
        if arr[i][j]>0:
            answer+=arr[i][j]
print(answer)