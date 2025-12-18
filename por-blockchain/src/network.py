import random
from .block import Block


class Network:
    def __init__(self, blockchain, nodes):
        self.blockchain = blockchain
        self.nodes = nodes

    def propose_block(self, data):
        last = self.blockchain.get_last_block()
        return Block(last.index + 1, last.hash, data)

    def get_random_approvers(self, k=5):
        return random.sample(self.nodes, k)
