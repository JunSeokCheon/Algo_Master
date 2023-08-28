from collections import deque
import sys
dice = [0]*6
def roll(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
input = sys.stdin.readline
n,m, x,y,k = list(map(int, input().split()))
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))
move = list(map(int, input().split()))
move_dice= [0,[0,1],[0,-1],[-1,0],[1,0]]

nx,ny= x,y
for i in move:
    dx,dy= move_dice[i] 
    nx+=dx
    ny+=dy

    if 0<=nx<n and 0<=ny<m:
        roll(i)
        if arr[nx][ny]!=0:
            dice[-1] = arr[nx][ny]
        else:
            arr[nx][ny] = dice[-1]
            dice[-1]=0
    else:
        nx-= dx
        ny-= dy
        continue
    print(dice[0])