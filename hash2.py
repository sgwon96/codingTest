def solution(phone_book):
    phone_dic = {}
    
    for phone_num in phone_book:
        dic = phone_dic
        flag = False
        
        for i in phone_num:
            if len(phone_dic) != 0 and len(dic) == 0 and not flag:
                return False
            
            if i not in dic:
                dic[i] = {}
                flag = True
                
            dic = dic[i]
        
        if not flag:
            return False
        
    return True