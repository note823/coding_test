dict_start_idx = {}
info = []
total_cnt = 0


def dfs(path, visit):
    if len(path) == total_cnt:
        return path

    start = path[-1]

    if start in dict_start_idx:
        idx_start = dict_start_idx[start]
        for i, new_end in enumerate(info[idx_start]):
            if visit[idx_start][i] is False:
                visit[idx_start][i] = True
                ret = dfs(path + [new_end], visit)
                visit[idx_start][i] = False

                if ret:
                    return ret


def solution(tickets):
    global dict_start_idx, info, total_cnt

    visit = []
    total_cnt = len(tickets) + 1
    num_start = 0

    for start, end in tickets:
        if start in dict_start_idx:
            info[dict_start_idx[start]].append(end)
            visit[dict_start_idx[start]].append(False)
        else:
            dict_start_idx[start] = num_start
            info.append([end])
            visit.append([False])
            num_start += 1

    for ele in info:
        ele.sort()

    path = ['ICN']

    answer = dfs(path, visit)

    return answer
