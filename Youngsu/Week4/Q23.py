def solution(genres, plays):
    answer = []
    # 1. genre_dic = {장르 : 누적 플레이수}
    # 2. song_dic = {장르 : [[고유번호 : 플레이 수], [고유번호 : 플레이 수]]}
    genre_play_dic = {}
    song_play_dic = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genre_play_dic:
            genre_play_dic[genre] = 0
            song_play_dic[genre] = []
        genre_play_dic[genre] += play
        song_play_dic[genre].append([i, play])

    sorted_genre_play = sorted(genre_play_dic.items(), key=lambda x: x[1], reverse=True)
    print(song_play_dic)
    for genre, play in sorted_genre_play:
        sorted_song_play = sorted(song_play_dic[genre], key=lambda x: (-x[1], x[0]))
        for i in range(2):
            answer.append(sorted_song_play[i][0])
    return answer

# print(solution(["classic", "pop", "classic", "classic", "pop"],
#                [500, 600, 150, 800, 2500]))
print(solution(["pop", "pop", "pop"], [1,1,1]))