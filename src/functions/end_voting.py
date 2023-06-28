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
    
    return duplicates

async def end_voting(chat_id):
    state = State()
    vote_objects = [vote.vote_object for vote in state.games[chat_id].votes if vote.vote_object != 0]
    
    print(vote_objects) # output [1311292414, 1311292414]
    #object_count, most_common_id = count_dublicates(vote_objects)
    result = find_duplicates(vote_objects)
    if result:
        for name, count in result:
            #await send_voting(chat_id,name, get_user_firstname_by_id(chat_id=chat_id, user_id=name))
            await send_voting(chat_id, name, str(name))
    else:
        await bot.send_message(chat_id=chat_id, text="Так как жители - долбоёбы, которые не могут линчевать, мы вынуждены СУКА никого не ЕБАШИТЬ")