def solution(people, limit):
    people.sort()
    couples = 0

    l = 0
    r = len(people) - 1

    while l < r:
        if people[l] + people[r] <= limit:
            l += 1
            couples += 1
        r -= 1

    return len(people) - couples