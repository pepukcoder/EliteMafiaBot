import enum


class Roles(enum.IntEnum):
    #bad roles
    DON = 0
    MAFIA = 1
    LIAR = 2
    INFORMANT = 3
    #good roles
    DOCTOR = 4
    DETECTIVE = 5
    #neutral
    WHORE = 6
    OMEGA = 7
    LAWYER = 8
    ALFA = 9
    TOWNIE = 10