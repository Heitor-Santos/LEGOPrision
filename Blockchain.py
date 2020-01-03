import time
import json

class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.workingBlock= Block()
        self.newBlock(previousash=1, proofOfwork=100)
    def newBlock(self, previousHash, proofOfwork):
        currBlock = {
            'index': len(self.chain)
            'timestamp': time()
            'previousHash': previousHash
            'proofOfWork'
        }