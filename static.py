from players import Players


def check_winner(state):
    if state == 1:
        return Players.PLAYER1.value
    if state == -1:
        return Players.PLAYER2.value
    return 0

def explain_state(state):
    if state[0] < 0:
        temp_state = list(state)
        temp_state[0] = - temp_state[0]
        return tuple(temp_state), Players.PLAYER1
    return state, Players.PLAYER2


def children_states(state, mark):
    children = set()
    for index, value in enumerate(state):
        for i in range(value):
            new_state = list(state)
            new_state[index] = i
            if 0 in new_state:
                new_state.remove(0)
            new_state.sort()
            if len(new_state) > 0:
                new_state[0] *= mark.value
                children.add(tuple(new_state))
            else:
                children.add(-mark.value)
    return list(children)