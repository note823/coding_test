from itertools import permutations
import math


def is_prime(number):
    if number == 1 or math.sqrt(number) == int(math.sqrt(number)):
        return False

    flag = True
    for d in range(2, int(math.sqrt(number)) + 1):
        if number % d == 0:
            flag = False
            break

    if flag:
        return True
    else:
        return False


def solution(numbers):
    answer = 0

    for len_digit in range(1, len(numbers) + 1):
        list_permutation = list(set(permutations(numbers, len_digit)))
        for permutation in list_permutation:
            if permutation[0] == '0':
                continue
            else:
                # 소수인지 판단
                if is_prime(int(''.join(permutation))):
                    answer += 1

    return answer
