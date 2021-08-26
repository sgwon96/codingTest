def solution(clothes):
    cl_map = {}
    for cl in clothes:
        if cl[1] not in cl_map:
            cl_map[cl[1]] = [cl[0]]
        else:
            cl_map[cl[1]].append(cl[0])
            
    mult = 1
    for key in cl_map:
        mult *= len(cl_map[key]) + 1
    mult -= 1
    
    return mult