from kajocoinGenesis import *
from kajocoinNewBlock import * 

#controller for building blockchain
def build_blockchain(num):

    blockchain = []
    blockchain.append(create_genesis_block())
    previous_block = blockchain[0]

    num_blocks = num 

    for i in range(0, num_blocks):

        new_block = next_block(previous_block)
        blockchain.append(new_block)
        previous_block = new_block

        print("Block #{} has been added to the kajocoin blockchain!".format(new_block.index))
        print("Block hash is #{}".format(new_block.hash))
        print("Block added at {}\n".format(new_block.timestamp))

build_blockchain(20)