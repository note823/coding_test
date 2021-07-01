from itertools import permutations
import math


def solution(numbers):
    answer = 0

    set_number = set()
    for i in range(1, len(numbers) + 1):
        set_number |= set(map(int, map(''.join, permutations(numbers, i))))
    set_number -= {0, 1}
    max_number = max(set_number)

    list_prime = [True] * (max_number + 1)
    for prime in range(2, int(math.sqrt(max_number)) + 1):
        if list_prime[prime]:
            set_number -= set(range(prime * 2, max_number + 1, prime))
            list_prime[prime * 2:max_number + 1:prime] = [False] * len(list_prime[prime * 2:max_number + 1:prime])

    answer = len(set_number)
    return answer
