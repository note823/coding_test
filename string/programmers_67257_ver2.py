import re
from itertools import permutations

def divide_and_conquer(expression, permutation, idx):
    if len(re.findall(r'\D+', expression)) == 0:
        return expression

    list_split = expression.split(permutation[idx])
    list_cal = []
    for split in list_split:
        list_cal.append(divide_and_conquer(split, permutation, idx + 1))
    return str(eval(permutation[idx].join(list_cal)))

#     if permutation[idx] == '+':
#         list_split = expression.split('+')
#         list_cal = []
#         for split in list_split:
#             list_cal.append(divide_and_conquer(split, permutation, idx + 1))
#         return str(eval('+'.join(list_cal)))

#     elif permutation[idx] == '-':
#         list_split = expression.split('-')
#         list_cal = []
#         for split in list_split:
#             list_cal.append(divide_and_conquer(split, permutation, idx + 1))
#         return str(eval('-'.join(list_cal)))

#     elif permutation[idx] == '*':
#         list_split = expression.split('*')
#         list_cal = []
#         for split in list_split:
#             list_cal.append(divide_and_conquer(split, permutation, idx + 1))
#         return str(eval('*'.join(list_cal)))


def solution(expression):
    answer = 0

    list_operator = list(set(re.findall(r'\D+', expression)))
    list_permutation = permutations(list_operator)

    for permutation in list_permutation:
        answer = max(answer, abs(int(divide_and_conquer(expression, permutation, 0))))

    return answer