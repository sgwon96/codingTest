def solution(n, lost, reserve):
    reserve = set(reserve)
    lost = set(lost)
    lost, reserve = lost - reserve, reserve - lost

    borrow_fail_count = 0

    for num in sorted(lost):
        if num - 1 in reserve:
            reserve.remove(num - 1)
        elif num + 1 in reserve:
            reserve.remove(num + 1)
        else:
            borrow_fail_count += 1

    return n - borrow_fail_count