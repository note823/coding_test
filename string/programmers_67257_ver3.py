import re
from itertools import permutations
import copy

def solution(expression):
    answer = 0

    list_num = list(map(int, re.findall(r'\d+', expression)))
    list_operator = re.findall(r'\D+', expression)
    set_operator = set(list_operator)
    list_permutation = permutations(list(set_operator))

    for permutation in list_permutation:
        copy_list_num = copy.deepcopy(list_num)
        copy_list_operator = copy.deepcopy(list_operator)

        for operator in permutation:
            idx_operator = 0

            while idx_operator < len(copy_list_operator):
                if copy_list_operator[idx_operator] == operator:
                    ele = eval(str(copy_list_num[idx_operator]) + operator + str(copy_list_num[idx_operator + 1]))
                    copy_list_num[idx_operator] = ele
                    copy_list_num.pop(idx_operator + 1)
                    copy_list_operator.pop(idx_operator)
                else:
                    idx_operator += 1

        answer = max(answer, abs(copy_list_num[0]))

    return answer