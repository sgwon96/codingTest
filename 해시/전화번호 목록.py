def solution(phone_book):
    answer = True
    dict = {} # 접두어 후보들
    for phone in phone_book:
        # 우선 value를 1로 다 넣어줌
        dict[phone] = 1
    for phone in phone_book:
        checking = ''
        # 번호를 앞에서부터 하나씩 추가해가며 check
        for n in phone:
            checking += n
            # 본인과도 반드시 한번씩 비교하게 되어있으므로 1일 때 그냥 -1해줌
            if dict.get(checking,-1) == 1:
                dict[checking] -= 1
            # 두번째로 같은 key를 만나면, 접두어가 있다는 
            elif dict.get(checking,-1) == 0:
                answer = False
        
    return answer
