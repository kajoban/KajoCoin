import datetime as date
from kajocoinBlock import Block

#build next block based on last
def next_block(last_block):

    next_index = last_block.index + 1
    next_timestamp = date.datetime.now()
    next_data = "Created block " + str(next_index)
    next_hash = last_block.hash 

    return Block(next_index, next_timestamp, next_data, next_hash) 