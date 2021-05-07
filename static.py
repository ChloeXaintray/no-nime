from players import Players


def check_winner(state):
    if state == 1:
        return Players.COMPUTER.value
    if state == -1:
        return Players.PLAYER.value
    return 0

def explain_state(state):
    if state[0] < 0:
        temp_state = list(state)
        temp_state[0] = - temp_state[0]
        return tuple(temp_state), Players.COMPUTER
    return state, Players.PLAYER


def children_states(state, mark):

    # if mark.value == 1:
    #     #1 seule ligne avec plus d'un baton
    #     if len(state) == 1 and state[0] > 1:
    #         return [(-1,)]
    #     # Suppression de l'avant dernière ligne avec dernière ligne qui contient 1 baton
    #     if len(state) == 2 and state[0] == 1:
    #         return [(-1,)]
    #     # Egalisation
    #     if len(state) == 2 and state[0] < state[1]:
    #         return [(-state[0], state[0])]
    #     # 3 lignes dont 2 lignes egales
    #     if len(state) == 3:
    #         if state[0] == state[1] or state[0] == state[2]:
    #             return [(-state[0], state[0])]
    #         if state[1] == state[2]:
    #             return [(-state[1], state[1])]
    #     #3 lignes de différents niveaux de batons
    #     #if len(state) == 3:

        # obtenir (1,2,3)

    # 1,1,n => 1,1,1 gagnant

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