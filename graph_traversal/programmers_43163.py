import collections


def is_one_diff(str1, str2):
    diff = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff += 1
            if diff > 1:
                return False

    return True


def solution(begin, target, words):
    answer = 0

    visit = [False] * len(words)
    q = collections.deque([begin])
    if begin in words:
        visit[words.index(begin)] = True
    cnt = 0

    while len(q) > 0:
        q_size = len(q)

        for _ in range(q_size):
            cur = q.popleft()
            if cur == target:
                answer = cnt
                return answer

            for idx_next_ele, next_ele in enumerate(words):
                if visit[idx_next_ele] is False and is_one_diff(cur, next_ele) is True:
                    visit[idx_next_ele] = True
                    q.append(next_ele)
        cnt += 1

    return answer
