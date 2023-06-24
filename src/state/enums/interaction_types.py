import enum


class InteractionTypes(enum.IntEnum):
    nothing = 0
    kill = 1
    heal = 2
    check = 3
    check_or_hill = 4
    podsos = 5
    justify = 6
    lie = 7
    vote_kill = 8
    switch = 9
    fuck = 10