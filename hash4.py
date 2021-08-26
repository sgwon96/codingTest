def solution(genres, plays):
    genrePlayMap = dict()
    genreIdMap = dict()

    for i in range(len(genres)):
        if genres[i] not in genrePlayMap:
            genrePlayMap[genres[i]] = plays[i]
            genreIdMap[genres[i]] = [[i,plays[i]]]
        else:
            genrePlayMap[genres[i]] += plays[i]
            genreIdMap[genres[i]].append([i,plays[i]])

    sortedGenres = [item[0] for item in sorted(genrePlayMap.items(), key = (lambda x: x[1]), reverse = True)]

    answer = []
    for genre in sortedGenres:
        sortedIds = sorted(genreIdMap[genre], key = (lambda x: x[0]))
        sortedIds = sorted(sortedIds, key = (lambda x: x[1]), reverse = True)
        answer += [i[0] for i in sortedIds[:2]]

    return answer