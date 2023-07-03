from src.state import State



def get_role_by_user_id(chat_id: int, user_id: int):
    state = State()
    game = state.games[chat_id]

    for user in game.users:
        if user.user_id == user_id:
            return user.role

def get_user_id_by_role(chat_id: int, role: int):
    state = State()
    game = state.games[chat_id]

    for user in game.users:
        if int(user.role) == role:
            return user.user_id


def set_role(chat_id: int, user_id: int, role):
    state = State()
    game = state.games[chat_id]

    for user in game.users:
        if user.user_id == user_id:
            user.role = role
            break

def change_user_role(chat_id: int, user_id: int, new_role):
    # Find the user based on the user ID
    # Assuming you have a list of user objects called "users"
    state = State()
    game = state.games[chat_id]
    for user in game.users:
        if user.user_id == user_id:
            user.role = new_role
            break
    else:
        # User not found
        print("User not found.")