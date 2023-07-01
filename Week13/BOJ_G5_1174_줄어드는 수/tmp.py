import sys
input = sys.stdin.readline

n = int(input())
visited = {}
number = []
def back():
    if number:
        visited.add(int(''.join(map(str,number))))
    for i in range(1,10):
        if not number or number[-1]:
            number.append(i)
            back()
            number.pop()
    
    