def solution(phone_book):
    book_set = set(phone_book)

    for number in phone_book:
        for i in range(len(number)):
            if number[:i] in book_set:
                return False

    return True