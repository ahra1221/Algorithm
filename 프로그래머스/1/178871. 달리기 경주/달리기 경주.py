def solution(players, callings):
    dic = {player: i for i, player in enumerate(players)}
    for call in callings:
        tmp = dic[call]
        dic[call] -= 1
        dic[players[tmp-1]] += 1
        players[tmp-1], players[tmp]=players[tmp],players[tmp-1]
    return players