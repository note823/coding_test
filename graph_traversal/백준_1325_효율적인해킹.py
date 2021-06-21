N, M = map(int, input().split())
info = [[] for _ in range(N)]
max_cnt = -1
answer = []

for _ in range(M):
    com2, com1 = map(lambda x: int(x)-1, input().split())
    info[com1].append(com2)

for com1 in range(N):
    is_visited = [False] * N
    if len(info[com1]) > 0:
        cnt = 1
        is_visited[com1] = True
        stack = [com1]

        while len(stack) > 0:
            cur = stack.pop()

            for new_com2 in info[cur]:
                if is_visited[new_com2] is False:
                    cnt += 1
                    stack.append(new_com2)
                    is_visited[new_com2] = True

        if max_cnt < cnt:
            max_cnt = cnt
            answer = [com1]
        elif max_cnt == cnt:
            answer.append(com1)

answer.sort()
answer = list(map(lambda x: x+1, answer))

for ele in answer:
    print(ele, end=" ")
