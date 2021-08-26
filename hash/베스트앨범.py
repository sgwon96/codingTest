from collections import defaultdict


def solution(clothes):
    closet = defaultdict(lambda: [])
    for name, item_type in clothes:
        closet[item_type].append(name)

    answer = 1
    for items in closet.values():
        answer *= len(items) + 1
    return answer - 1