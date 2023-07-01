from src.settings import get_language
from src.state import State
from src.state.enums import Roles


async def show_initial(chat_id, bot, winner: bool):
    state = State()

    try:
        initial_users = state.games[chat_id].initial_roles
        users = state.games[int(chat_id)].users
        bad = [user for user in users if int(user.role) == Roles.DON.value or int(user.role) == Roles.MAFIA.value]
        good = [user for user in users if int(user.role) != Roles.DON.value and int(user.role) != Roles.MAFIA.value]

        winners = f"{get_language(chat_id)['players_win']}\n"
        if winner:
            for idx, x in enumerate(bad):
                winners = winners + str(idx + 1) + '. ' + str(x.link) + " — " + str(x.role) + "\n"
        else:
            for idx, x in enumerate(good):
                winners = winners + str(idx + 1) + '. ' + str(x.link) + " — " + str(x.role) + "\n"

        message = f"{get_language(chat_id)['initial_roles']}\n"

        for idx, x in enumerate(initial_users):
            message = message + str(idx + 1) + '. ' + str(x.link) + " — " + str(x.role) + "\n"

        result = winners + "\n" + message

        await bot.send_message(chat_id, result, parse_mode='Markdown')
    except KeyError:
        print('Error')