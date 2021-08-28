import functools

def solution(numbers):
    numbers.sort(key = functools.cmp_to_key(lambda x, y:compare(x, y)), reverse=True)
    return str(int("".join(list(map(str, numbers)))))

def compare(x, y):
    result = int((str(x)+str(y))) - int(str(y)+str(x))
    return result