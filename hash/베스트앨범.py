from collections import defaultdict


def solution(genres, plays):
    genre_songs = defaultdict(list)
    genre_play_count = defaultdict(int)

    for i in range(len(genres)):
        genre_songs[genres[i]].append([i, plays[i]])
        genre_play_count[genres[i]] += plays[i]

    genre_play_count = [(genre, plays) for genre, plays in genre_play_count.items()]
    genre_play_count.sort(key=lambda x: x[1], reverse=True)

    answer = []
    for genre, play_count in genre_play_count:
        genre_songs[genre].sort(key=lambda x: (x[1], -x[0]), reverse=True)
        for song_num, play_count in genre_songs[genre][:2]:
            answer.append(song_num)

    return answer