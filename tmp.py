n,l,w = map(int, input().split())
lst = list(map(int, input().split()))

bridge = [0]*l
weight , time = 0,0

while bridge:
    time+=1
    bridge.pop(0)
    if lst:
        if sum(bridge)+lst[0]>w:
            bridge.append(0)
        else:
            bridge.append(lst.pop(0))
print(time)