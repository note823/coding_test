from itertools import permutations
import re


def cal_operator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def solution(expression):
    answer = 0

    list_num = list(map(int, re.findall(r'\d+', expression)))
    list_operator = re.findall(r'\D+', expression)

    for prior1, prior2, prior3 in permutations(['-', '+', '*']):
        idx_num = 0
        list_cal = []
        list_cal.append([list_num[idx_num]])
        idx_num += 1
        while idx_num < len(list_num):
            new_num = list_num[idx_num]
            if list_operator[idx_num - 1] == prior1:
                list_cal[-1][-1] = cal_operator(list_cal[-1][-1], new_num, prior1)
            elif list_operator[idx_num - 1] == prior2:
                list_cal[-1].append(new_num)
            elif list_operator[idx_num - 1] == prior3:
                list_cal.append([new_num])

            idx_num += 1

        mid_answer = eval(prior2.join(map(str, list_cal[0])))

        for idx_list in range(1, len(list_cal)):
            ele = eval(prior2.join(map(str, list_cal[idx_list])))
            mid_answer = cal_operator(mid_answer, ele, prior3)

        answer = max(answer, abs(mid_answer))

    return answer
