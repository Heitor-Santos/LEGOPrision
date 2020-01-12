import time
import json
import hashlib
from Block import Block
from Transaction import Transaction
from uuid import uuid4
from flask import Flask
import requests
class Blockchain(object):
    def __init__(self, peerUUID):
        self.chain=[]
        self.pendingTransactions=[]
        self.peerUUID = peerUUID
        self.peers=[]
        self.peers.append(peerUUID)
        self.addBlock()#gera o bloco gênese

    def addBlock(self, proof=100):
        index = len(self.chain)
        trans = self.pendingTransactions
        timestamp= time.time()
        if len(self.chain)==0 lastHash=1
        else lastHash= self.lastBlock().hash
        newBlock = Block(index,trans,timestamp, lastHash, proof)
        newBlock.selar()
        if not newBlock.checkHash(): 
            raise ValueError('Este bloco ainda não foi selado')
        if not validProof(self.lastBlock().proof, newBlock.proof):
            raise ValueError('Esta POW não é válida')
        self.chain.append(newBlock)
        self.pendingTransactions=[]

    def proofOfWork(self, lastProof):
        proof = 0
        while self.validProof(lastProof, proof) is False:
            proof += 1

    def validProof(self, lastProof, proof):
        attempt = f'{lastProof}{proof}'.encode()
        attemptHash = hashlib.sha256(attempt).hexdigest()
        return attemptHash[:4] == "0000"

    def lastBlock(self):
        return self.chain[-1]

    def mine(self):
        proof = self.proofOfWork(self.lastBlock())
        #já que calculou a POW ganha 100 moedas em retorno 
        #sender 0 pra indicar que a transação é resultado da mineração
        recompensa = Transaction(0, self.peerUUID, 100)
        self.pendingTransactions.append(recompensa)
        #gera o novo blovo recém minerado
        self.addBlock(proof)

    def addPeer(self, peerUUID):
        self.peers.append(peerUUID)

    def addTransaction(self, trans):
        self.pendingTransactions.append(trans)

    def checkChain(self, chain):
        if chain[0].transactions!=0 return False
        if chain[0].index!=0 return False
        if not chain[0].checkHash return False
        for i in range(0,len(chain)):
            if chain[i].index!=i return False
            if not chain[i].checkHash return False
            if chain[i].lastHash!= chain[i-1].hash return False
            if not validProof(chain[i-1].proof, chain[i].proof) return False
        return True
    def consensus(self):
        maxLength = len(self.chain)
        for peer in peers:
            response = requests.get(f'http://{peer}/chain')
            if response.status_code == 200:
                chain = response.json()['chain']
                length = response.json()['length']
                if length > maxLength and self.checkChain(chain):
                    newChain = chain
                    maxLength = length
        if newChain: self.chain = newChain 
    
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new Block"
  
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)