import enum


class Mafia(enum.Enum):
    M1FOR3 = '1to3'
    M1FOR4 = '1to4'


def get_mafia_from_code(quantity):
    for quantity in Mafia:
        if quantity.value == quantity:
            return quantity
    return None
