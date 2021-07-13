def solution(gems):
    num_type = len(set(gems))

    answer = []
    max_len = len(gems) + 1

    idx_right = 0
    idx_left = 0
    gem_to_cnt = {gems[0]: 1}

    while idx_right < len(gems) and idx_left < len(gems):
        if len(gem_to_cnt) < num_type and idx_right - idx_left + 1 < max_len:
            # 1) 오른쪽 포인터 + 1
            # 2) 새로운 원소 dict에 반영(추가 or cnt += 1)
            idx_right += 1
            if idx_right == len(gems):
                break
            new_gem = gems[idx_right]
            if new_gem in gem_to_cnt:
                gem_to_cnt[new_gem] += 1
            else:
                gem_to_cnt[new_gem] = 1
        else:
            if len(gem_to_cnt) == num_type and idx_right - idx_left + 1 < max_len:
                answer = [idx_left + 1, idx_right + 1]
                max_len = idx_right - idx_left + 1

            # 1) 왼쪽 포인터 + 1
            # 2) 없어질 원소 dict에 반영
            del_gem = gems[idx_left]
            idx_left += 1
            if gem_to_cnt[del_gem] == 1:
                gem_to_cnt.pop(del_gem)
            else:
                gem_to_cnt[del_gem] -= 1

    return answer
