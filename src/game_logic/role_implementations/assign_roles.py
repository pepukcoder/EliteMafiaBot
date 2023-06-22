from aiogram import Bot

import random
import enum

class Roles(enum.Enum):
    DON = "Дон"
    MAFIA = "Мафия"
    PIZDABOL = "Пиздабол"
    OSVEDOMITEL = "Осведомитель"
    DOCTOR = "Доктор"
    COMMISSAR = "Коммисар"
    SHLYUKHA = "Шлюха"
    OMEZHKA = "Омежка"
    SUICIDNIK = "Суицидник"
    ADVOKAT = "Адвокат"
    ALFACH = "Альфач"

roles_count = {
    4: {Roles.DON: 1, Roles.DOCTOR: 1, Roles.MAFIA: 0, Roles.COMMISSAR: 0, Roles.PIZDABOL: 0,
        Roles.OSVEDOMITEL: 0, Roles.SHLYUKHA: 0, Roles.OMEZHKA: 0, Roles.SUICIDNIK: 0,
        Roles.ADVOKAT: 0, Roles.ALFACH: 0},
    5: {Roles.DON: 1, Roles.DOCTOR: 1, Roles.MAFIA: 1, Roles.COMMISSAR: 0, Roles.PIZDABOL: 0,
        Roles.OSVEDOMITEL: 0, Roles.SHLYUKHA: 0, Roles.OMEZHKA: 0, Roles.SUICIDNIK: 0,
        Roles.ADVOKAT: 0, Roles.ALFACH: 0},
    6: {Roles.DON: 1, Roles.DOCTOR: 1, Roles.MAFIA: 0, Roles.COMMISSAR: 1, Roles.PIZDABOL: 0,
        Roles.OSVEDOMITEL: 0, Roles.SHLYUKHA: 0, Roles.OMEZHKA: 0, Roles.SUICIDNIK: 0,
        Roles.ADVOKAT: 0, Roles.ALFACH: 1},
    7: {Roles.DON: 1, Roles.DOCTOR: 1, Roles.MAFIA: 1, Roles.COMMISSAR: 1, Roles.PIZDABOL: 0,
        Roles.OSVEDOMITEL: 0, Roles.SHLYUKHA: 0, Roles.OMEZHKA: 0, Roles.SUICIDNIK: 0,
        Roles.ADVOKAT: 0, Roles.ALFACH: 1},
    8: {Roles.DON: 1, Roles.DOCTOR: 1, Roles.MAFIA: 1, Roles.COMMISSAR: 1, Roles.PIZDABOL: 0,
        Roles.OSVEDOMITEL: 0, Roles.SHLYUKHA: 0, Roles.OMEZHKA: 0, Roles.SUICIDNIK: 0,
        Roles.ADVOKAT: 0, Roles.ALFACH: 1}
}

def assign_roles_randomly(player_count):
    roles = [role for role, count in roles_count[player_count].items() for _ in range(count)]
    random.shuffle(roles)
    return roles[:player_count]

player_count = 5

assigned_roles = assign_roles_randomly(player_count)
for i, role in enumerate(assigned_roles):
    print(f"Player {i+1}: {role.value}")