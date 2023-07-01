from aiogram import Dispatcher, types, Bot

from src.functions.show_initial_roles import show_initial
from src.state import State, UserState
from src.state.enums import Roles
from src.settings.main import get_language

async def win_check(chat_id, bot: Bot) -> bool:
    state = State()
    game = state.games[chat_id]
    users = state.games[int(chat_id)].users

    bad = [user for user in users if int(user.role) == Roles.DON.value or int(user.role) == Roles.MAFIA.value]
    good = [user for user in users if int(user.role) != Roles.DON.value and int(user.role) != Roles.MAFIA.value]
    print(bad, good)

    if len(bad) >= len(good):
        msg = f"{get_language(chat_id)['win_bad']}"
        await show_initial(chat_id, bot, True)
    elif len(bad) == 0:
        msg = f"{get_language(chat_id)['win_good']}"
        await show_initial(chat_id, bot, False)
    else:
        print('win check: continue')
        return True
    print('win check: game ended')
    await bot.send_message(chat_id, text=f"{get_language(chat_id)['game_end']}\n{msg}", parse_mode='Markdown')
    return False
