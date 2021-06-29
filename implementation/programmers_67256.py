def number_to_pos(number):
    if number == 0:
        return (3, 1)
    elif number == 1:
        return (0, 0)
    elif number == 2:
        return (0, 1)
    elif number == 3:
        return (0, 2)
    elif number == 4:
        return (1, 0)
    elif number == 5:
        return (1, 1)
    elif number == 6:
        return (1, 2)
    elif number == 7:
        return (2, 0)
    elif number == 8:
        return (2, 1)
    elif number == 9:
        return (2, 2)


def solution(numbers, hand):
    answer = ''

    button_left = [(0, 0), (1, 0), (2, 0)]
    button_right = [(0, 2), (1, 2), (2, 2)]
    pos_left = (3, 0)
    pos_right = (3, 2)

    for number in numbers:
        pos_number = number_to_pos(number)

        if pos_number in button_left:
            answer += 'L'
            pos_left = pos_number
        elif pos_number in button_right:
            answer += 'R'
            pos_right = pos_number
        else:
            dist_left = abs(pos_number[0] - pos_left[0]) + \
                        abs(pos_number[1] - pos_left[1])

            dist_right = abs(pos_number[0] - pos_right[0]) + \
                         abs(pos_number[1] - pos_right[1])

            if dist_left < dist_right:
                answer += 'L'
                pos_left = pos_number
            elif dist_right < dist_left:
                answer += 'R'
                pos_right = pos_number
            else:
                if hand == 'left':
                    answer += 'L'
                    pos_left = pos_number
                else:
                    answer += 'R'
                    pos_right = pos_number

    return answer
