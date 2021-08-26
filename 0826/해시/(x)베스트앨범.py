def solution(genres, plays):
    answer = []
    # {장르 : 장르 총 횟수}
    genresPlay = {}
    # {곡 고유 번호 : 곡 횟수}
    songsPlay = {}
    
    for i in range(len(genres)):
        genresPlay[genres[i]] = genresPlay.get(genres[i], 0) + plays[i]
        songsPlay[genres[i]] = songsPlay.get(genres[i], []) + [(i, plays[i])]
        
    genre = sorted(genresPlay.items(), key=lambda x:x[1], reverse=True)
    
    for g in genre:
        s = g[0]
        if len(songsPlay[s]) <= 1:
            answer.append(int(songsPlay[s]))
        else:
            sortPlays = sorted(songsPlay[s], key=lambda x: (x[1], -x[0]), reverse=True)
            answer.append(sortPlays[0][0])
            answer.append(sortPlays[1][0])
            
    return answer
