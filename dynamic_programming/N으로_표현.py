def solution(N, number):
    cases_by_use_count = [[]]
    for i in range(1, 9):
        cases = []
        for j in range(1, i):
            for k in cases_by_use_count[j]:
                for l in cases_by_use_count[i - j]:
                    cases.append(k + l)
                    cases.append(k * l)
                    if k - l >= 0:
                        cases.append(k - l)
                    if k >= l and l != 0 and k % l == 0:
                        cases.append(k // l)
        cases.append(int(str(N) * i))

        if number in cases:
            return i

        cases_by_use_count.append(cases)

    return -1