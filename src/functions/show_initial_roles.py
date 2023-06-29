from src.state import State

async def show_initial(chat_id, bot):
    state = State()

    try:
        initial_users = state.games[chat_id].initial_roles

        message = "Первоначальные роли:\n"

        for idx, x in enumerate(initial_users):
            message = message + str(idx + 1) + '. ' + str(x.link) + " — " + str(x.role) + "\n"

        print(message)

        await bot.send_message(chat_id, message, parse_mode='Markdown')
    except KeyError:
        print('Error')