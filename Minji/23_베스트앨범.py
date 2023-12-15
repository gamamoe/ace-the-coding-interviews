def solution(genres, plays):
    answer = []
    genre = {}
    play = {}
    play_sort = {}
    
    for i in range(len(genres)):
        if genres[i] not in genre:
            genre[genres[i]] = {}
            play[genres[i]] = 0

        genre[genres[i]][i] = plays[i]

        play[genres[i]] += plays[i]
    
    genre_sort = sorted(play.items(), key=lambda x: x[1], reverse=True)
    
    for j in range(len(genre_sort)):
        play_sort[genre_sort[j][0]] = sorted(genre[genre_sort[j][0]].items(), key=lambda item: item[1], reverse=True)[:2]

        answer.extend([idx for idx, _ in play_sort[genre_sort[j][0]]])
        
    return answer
