def solution(number, k):
    answer = ''
    idx_cur = 0
    num_del = 0
    list_sel = []

    while num_del < k and idx_cur < len(number):
        # 리스트의 길이가 0이거나, 리스트의 제일 끝 값이 현재 값보다 크거나 같은 경우 일때 까지 pop
        while list_sel and list_sel[-1] < number[idx_cur] and num_del < k:
            list_sel.pop()
            num_del += 1
        list_sel.append(number[idx_cur])
        idx_cur += 1

    if num_del < k:
        answer = ''.join(list_sel[:len(number) - k])
    else:
        answer = ''.join(list_sel + list(number)[idx_cur:])

    return answer
