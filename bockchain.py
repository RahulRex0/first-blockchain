import hashlib
class block:
    def __init__(self,data,previous_hash):
        self.data=data
        self.previous_hash=previous_hash
        self.hash=self.calculate_hash()
    def calculate_hash(self):
        sha=hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest
class blockchain:
    def __init__(self):
        self.chain=[self.create_genesis_block()]
    def create_genesis_block(self):
        return block("Genesis block","0")
    def add_block(self,data):
        prev_block=self.chain[-1]
        new_block=block(data,prev_block.hash)
        self.chain.append(new_block)
    
blockchain=blockchain()
blockchain.add_block('first block')
blockchain.add_block('second block')
blockchain.add_block('third block')
print('blockchain:')
for block in blockchain.chain:
    print('data:',block.data)
    print('previous hash:',block.previous_hash)
    print('hash:',block.hash)
    print()
