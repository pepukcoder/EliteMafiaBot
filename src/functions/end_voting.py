from aiogram import Bot

from src.game_logic.sending_strategies import Strategy
from src.state import State, VoteState
from src.functions import send_voting
from src.functions import count_dublicates, get_user_firstname_by_id

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
    vote_objects = [vote.vote_object for vote in state.games[chat_id].votes]
    
    print(vote_objects) # output [1311292414, 1311292414]
    #object_count, most_common_id = count_dublicates(vote_objects)
    result = find_duplicates(vote_objects)
    for name, count in result:
        #await send_voting(chat_id,name, get_user_firstname_by_id(chat_id=chat_id, user_id=name))
        await send_voting(chat_id, name, str(name))