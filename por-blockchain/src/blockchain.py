from .block import Block


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis()]

    def create_genesis(self):
        return Block(0, "0", "GENESIS")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, block):
        if self.validate_block(block):
            self.chain.append(block)
            return True
        return False

    def validate_block(self, block):
        last = self.get_last_block()
        return block.prev_hash == last.hash
