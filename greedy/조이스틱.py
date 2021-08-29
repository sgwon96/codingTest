def match_char_moves(target):
    direct = ord(target) - ord('A')
    loop = ord('Z') - ord(target) + 1
    return min([direct, loop])


def solution(name):
    n = len(name)
    vertical_count = 0
    horizontal_move = len(name) - 1
    for i in range(len(name)):
        vertical_count += match_char_moves(name[i])

        if name[i] == 'A':
            j = i
            while name[j] == 'A' and j < n - 1:
                j += 1
            horizontal_move = min(horizontal_move, 2 * (i - 1) + n - j)
    return vertical_count + horizontal_move