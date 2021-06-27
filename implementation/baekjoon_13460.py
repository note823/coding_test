import collections

answer = -1
drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]
num_row, num_col = map(int, input().split())
info = []
for row in range(num_row):
    info.append(list(input()))

pos_red = (-1, -1)
pos_blue = (-1, -1)
for row in range(num_row):
    for col in range(num_col):
        if info[row][col] == 'R':
            pos_red = (row, col)
            info[row][col] = '.'
        elif info[row][col] == 'B':
            pos_blue = (row, col)
            info[row][col] = '.'


def move(dr, dc, cur):
    # return: new_pos, distance
    new_row = cur[0]
    new_col = cur[1]
    distance = 0
    while True:
        if info[new_row][new_col] == 'O' or info[new_row + dr][new_col + dc] == '#':
            return (new_row, new_col), distance
        new_row += dr
        new_col += dc
        distance += 1


def solution():
    q = collections.deque()
    visit = [[[[False] * num_col for _ in range(num_row)] for _ in range(num_col)] for _ in range(num_row)]
    visit[pos_red[0]][pos_red[1]][pos_blue[0]][pos_blue[1]] = True
    q.append((pos_red, pos_blue))
    cnt = 0

    while len(q) > 0 and cnt < 10:
        q_size = len(q)
        cnt += 1

        for _ in range(q_size):
            cur_red, cur_blue = q.popleft()
            for i in range(4):
                dr = drs[i]
                dc = dcs[i]

                new_red, distance_red = move(dr, dc, cur_red)
                new_blue, distance_blue = move(dr, dc, cur_blue)

                if info[new_red[0]][new_red[1]] == 'O':
                    if info[new_blue[0]][new_blue[1]] == 'O':
                        continue
                    else:
                        print(cnt)
                        return
                elif new_red == new_blue:
                    if distance_red > distance_blue:
                        new_red = (new_red[0] - dr, new_red[1] - dc)
                    else:
                        new_blue = (new_blue[0] - dr, new_blue[1] - dc)

                if not visit[new_red[0]][new_red[1]][new_blue[0]][new_blue[1]]:
                    visit[new_red[0]][new_red[1]][new_blue[0]][new_blue[1]] = True
                    q.append((new_red, new_blue))

    print(-1)
    return


solution()
