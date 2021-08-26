from collections import Counter


def solution(participant, completion):
    count_p = Counter(participant)
    count_c = Counter(completion)

    for p in count_p:
        if p not in count_c or count_p[p] > count_c[p]:
            return p