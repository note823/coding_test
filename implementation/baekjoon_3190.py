import collections


def change_flag(dir, flag):
    if dir == 'L':  # 왼쪽으로 90도
        if flag == 0:
            return 2
        elif flag == 1:
            return 3
        elif flag == 2:
            return 1
        elif flag == 3:
            return 0
    elif dir == 'D':  # 오른쪽으로 90도
        if flag == 0:
            return 3
        elif flag == 1:
            return 2
        elif flag == 2:
            return 0
        elif flag == 3:
            return 1


def solution():
    N = int(input())
    num_apple = int(input())
    info = [[' '] * (N + 2) for _ in range(N + 2)]

    for row in range(N+2):
        info[row][0] = '#'
        info[row][N + 1] = '#'

    for col in range(N+2):
        info[0][col] = '#'
        info[N + 1][col] = '#'

    info[1][1] = 's'  # snake

    for _ in range(num_apple):
        row, col = map(int, input().split())
        info[row][col] = 'a'  # apple

    num_dir = int(input())
    info_dir = []

    for i in range(num_dir):
        time, dir = input().split()
        time = int(time)
        info_dir.append((time, dir))

    drs = [-1, 1, 0, 0]
    dcs = [0, 0, -1, 1]
    flag = 3  # 0:상, 1:하, 2:좌, 3:우

    # 꼬리정보, 머리정보
    tail = (1, 1)
    head = (1, 1)

    time = 0 # 현재시간
    idx_dir = 0
    queue_snake = collections.deque([(1, 1)])

    while True:
        if idx_dir < num_dir and info_dir[idx_dir][0] == time:
            flag = change_flag(info_dir[idx_dir][1], flag)
            idx_dir += 1

        time += 1
        # 움직임
        new_row_head = head[0] + drs[flag]
        new_col_head = head[1] + dcs[flag]
        head = (new_row_head, new_col_head)
        queue_snake.append(head)
        # 머리쪽이 사과일 경우 -> tail 변화 x
        if info[new_row_head][new_col_head] == 'a':
            info[new_row_head][new_col_head] = 's'
            continue
        # 머리쪽이 벽면이나 몸일경우 -> time return
        elif info[new_row_head][new_col_head] == 's' or \
                info[new_row_head][new_col_head] == '#':
            print(time)
            return
        # 그냥 빈 공간일 경우 -> tail 변화
        else:
            info[new_row_head][new_col_head] = 's'
            info[tail[0]][tail[1]] = ' '
            new_row_tail = tail[0] + drs[flag]
            new_col_tail = tail[1] + dcs[flag]
            queue_snake.popleft()
            tail = queue_snake[0]


solution()
