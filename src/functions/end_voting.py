from src.misc import TgKeys
from src.state import State
from src.functions import send_voting
from aiogram import Bot

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')


def find_duplicates(array):
    count = {}

    # Count the occurrences of each element in the array
    for item in array:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1

    # Find the elements with count greater than 1 (i.e., duplicates)
    duplicates = [(name, count) for name, count in count.items() if count > 1]

    if len(duplicates) == 0:
        return None

    if len(array) == 1:
        return array[0]

    # Sort duplicates based on count in descending order
    duplicates.sort(key=lambda x: x[1], reverse=True)

    # Return the most duplicated element or the second most duplicated if the most duplicated is 0
    if duplicates[0][0] == 0:
        if len(duplicates) >= 2:
            return duplicates[1][0]
        else:
            return None
    else:
        return duplicates[0][0]


async def end_voting(chat_id):
    state = State()
    vote_objects = [vote.vote_object for vote in state.games[chat_id].votes if vote.vote_object != 0]

    print(vote_objects)  # output [1311292414, 1311292414]
    # object_count, most_common_id = count_dublicates(vote_objects)
    if len(vote_objects) != 0:
        result = find_duplicates(vote_objects)
        print(result)
        await send_voting(chat_id, result)
    else:
        await bot.send_message(chat_id=chat_id,
                               text="Так как жители сидели и дрочили мы не смогли выбрать кого линчевать")
