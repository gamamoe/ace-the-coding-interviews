from collections import Counter


def range_check(position, direction):
    if -5 <= position[0]+direction[0] <= 5 and -5 <= position[1]+direction[1] <= 5:
        return position[0]+direction[0], position[1]+direction[1]
    else:
        return position

def solution(dirs):
    position_history = set()
    direction = {
        'U': (0,1),
        'D': (0,-1),
        'R': (1,0),
        'L': (-1,0)
    }
    prev_position = (0, 0)
    for d in dirs:
        position = range_check(prev_position, direction[d])
        if prev_position!=position:
            position_history.add( (prev_position,position) )
            position_history.add( (position,prev_position) )
        prev_position = position
    return round(len(position_history)/2)
