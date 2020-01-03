import time
import json
class Block(object):
    def __init__(self):
        self.transactions=[]
    def newTransaction(self, sender, receiver, amount):
        currTransaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'timestamp': time()
        }
        self.transactions.append(currTransaction)