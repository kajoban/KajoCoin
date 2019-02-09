import datetime as date
from kajocoinBlock import Block

#first block in chain
def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")
