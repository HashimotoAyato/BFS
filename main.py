from collections import deque

n, m = map(int, input().split())
stage = [input() for i in range(n)]

queue = deque()
distance = [[-1 for j in range(m)] for i in range(n)]
flag = [[False for j in range(m)] for i in range(n)]

# first element
for i in range(n):
    for j in range(m):
        if stage[i][j] == 'S':
            queue.append([i, j])
            distance[i][j] = 0
            flag[i][j] = True

# bfs
while len(queue) > 0:
    x = queue.popleft()
    if stage[x[0]][x[1]] == 'G':
        print(distance[x[0]][x[1]])
        break
    else:
        next_distance = distance[x[0]][x[1]] + 1
        if 0 < x[0] and stage[x[0]-1][x[1]] != '#' and flag[x[0]-1][x[1]] == False:
            queue.append([x[0]-1, x[1]])
            distance[x[0]-1][x[1]] = next_distance
            flag[x[0]-1][x[1]] = True
        
        if x[0] < n-1 and stage[x[0]+1][x[1]] != '#' and flag[x[0]+1][x[1]] == False:
            queue.append([x[0]+1, x[1]])
            distance[x[0]+1][x[1]] = next_distance
            flag[x[0]+1][x[1]] = True

        if 0 < x[1] and stage[x[0]][x[1]-1] != '#' and flag[x[0]][x[1]-1] == False:
            queue.append([x[0], x[1]-1])
            distance[x[0]][x[1]-1] = next_distance
            flag[x[0]][x[1]-1] = True

        if x[1] < n-1 and stage[x[0]][x[1]+1] != '#' and flag[x[0]][x[1]+1] == False:
            queue.append([x[0], x[1]+1])
            distance[x[0]][x[1]+1] = next_distance
            flag[x[0]][x[1]+1] = True
