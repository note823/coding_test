def solution(people, limit):
    answer = 0

    people.sort()
    idx_light = 0
    idx_heavy = len(people) - 1

    while idx_light < idx_heavy:
        if people[idx_heavy] + people[idx_light] <= limit:
            answer += 1
            idx_heavy -= 1
            idx_light += 1
        else:
            answer += 1
            idx_heavy -= 1

    if idx_light == idx_heavy:
        answer += 1

    return answer
