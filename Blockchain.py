import time
import json
import hashlib
class Block(object):
    def __init__(self):
        self.transactions=[]
    def newTransaction(self, sender, receiver, amount):
        currTransaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'timestamp': time.time()
        }
        self.transactions.append(currTransaction)
class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.workingBlock= Block()
        self.newBlock(previousHash=1, proofOfWork=100)
    def newBlock(self, previousHash, proofOfWork):
        currBlock = {
            'index': len(self.chain),
            'timestamp': time.time(),
            'previousHash': previousHash or self.hashBlock(self.lastBlock),
            'proofOfWork': proofOfWork,
            'transactions': self.workingBlock.transactions
        }
        self.chain.append(currBlock)
        workingBlock= Block()
    def hashBlock(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    def proofOfWork(lastProof):
        proof = 0
        while self.validProof(lastProof, proof) is False:
            proof += 1
    def validProof(lastProof, proof):
        attempt = f'{lastProof}{proof}'.encode()
        attemptHash = hashlib.sha256(attempt).hexdigest()
        return attemptHash[:4] == "0000"
    def lastBlock():
        return self.chain[-1]
bola = Blockchain()
print(bola.chain)