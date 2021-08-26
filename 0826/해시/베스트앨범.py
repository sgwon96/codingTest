def solution(genres, plays):
    answer = []
    # {장르 : 장르 총 횟수}
    genresPlay = {}
    # {장르 : (곡 고유 번호, 곡 횟수)}
    songsPlay = {}
    
    for i in range(len(genres)):
        genresPlay[genres[i]] = genresPlay.get(genres[i], 0) + plays[i]
        songsPlay[genres[i]] = songsPlay.get(genres[i], []) + [(i, plays[i])]

    # 총 재생 횟수 많은 순으로 장르 정리    
    genre = sorted(genresPlay.items(), key=lambda x:x[1], reverse=True)
    
    for (g, n) in genre:
        song = songsPlay[g]
        # 재생 횟수 많은 순, 고유 번호 작은 순으로 정리
        song = sorted(song, key=lambda x: (-x[1], x[0]))

        # 하나 밖에 없으면 하나만
        if len(song) == 1:
            answer.append(song[0][0])
        # 첫번째와 두번째 곡 고유 번호
        else:
            answer.append(song[0][0])
            answer.append(song[1][0])
            
    return answer
