from aiogram import Bot

from src.functions import get_user_id_by_role
from src.game_logic.sending_strategies import Strategy, SendVotingMessages
from src.state import State
from src.state.enums import Roles

def get_name_by_user_id(chat_id: int, user_id: int):
    state = State()
    game = state.games[chat_id]

    for user in game.users:
        if user.user_id == user_id:
            return user.first_name

class SendingContext:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    async def send(self, game_chat_id, bot: Bot):
        state = State()
        try:
            game = state.games[game_chat_id]
            state.games[game_chat_id].interaction_keyboards = []

            for user in game.users:
                if self._strategy.get_text(user.role):
                    msg = await bot.send_message(user.user_id,
                                           text=self._strategy.get_text(user.role),
                                           parse_mode='HTML',
                                           disable_web_page_preview=True,
                                           reply_markup=self._strategy.get_markup(user.role, game_chat_id))
                    state.games[game_chat_id].interaction_keyboards.append([user.user_id, msg.message_id])
                else:
                    # await bot.send_message(user.user_id,
                    #                        text="Ваша роль не активна, вы пропускаете ход.",
                    #                        reply_markup=self._strategy.get_markup(user.role, game_chat_id), parse_mode="Markdown")
                    pass
        except KeyError:
            print(f"Game {game_chat_id} not found")

    async def send_mafia(self, chat_id: int, bot: Bot):
        don = get_user_id_by_role(chat_id, Roles.DON)
        mafia = get_user_id_by_role(chat_id, Roles.MAFIA)
        if mafia:
            await bot.send_message(chat_id=don, parse_mode="Markdown",
                                       text=f"Известная вам мафия:\n1. {get_name_by_user_id(chat_id, don)}\n2. {get_name_by_user_id(chat_id, mafia)}")
            await bot.send_message(chat_id=mafia, parse_mode="Markdown",
                                       text=f"Известная вам мафия:\n1. {get_name_by_user_id(chat_id, don)}\n2. {get_name_by_user_id(chat_id, mafia)}")
        else:
            await bot.send_message(chat_id=don,
                                       text=f"Вы единственная мафия в этой игре.")

    async def send_voting(self, game_chat_id, bot: Bot):
        state = State()
        try:
            game = state.games[game_chat_id]
            state.games[game_chat_id].voting_keyboards = []
            for user in game.users:
                msg = await bot.send_message(user.user_id,
                                       text="За кого ты хочешь проголосовать?",
                                       reply_markup=SendVotingMessages.get_voting(user.role, game_chat_id))
                state.games[game_chat_id].voting_keyboards.append([user.user_id, msg.message_id])
        except KeyError:
            print(f"Game {game_chat_id} not found")
