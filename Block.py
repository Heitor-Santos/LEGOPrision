import time
import json
import hashlib
from Transaction import Transaction
class Block(object):
    """Cria um novo bloco que acaba de ser mineirado
    @param index-> index do bloco
    @param transactions-> lista de transaçães feitas neste bloco
    @param timestamp-> marca temporal de quando o bloco foi minerado
    @param lastHash-> a hash do bloco anterior à este
    @param proofOfWork-> prova do trabalho da mineiração do bloco atual
    """ 
    def __init__(self, index, transactions, timestamp, lastHash, proofOfWork):
        self.index = index 
        self.transactions = transactions
        self.timestamp = timestamp
        self. lastHash = lastHash
        self.proofOfWork = proofOfWork
        self.selado= False
        self.hash =''
    #Armazena a hash SHA-256 do bloco atual e o marca como selado
    def selar(self):
        if not self.selado:
            self.hash = generateHash()
            self.selado = True
        else:
            raise ValueError('Este bloco já está selado')
    #Calcula a hash SHA-256 do bloco e retorna a hash
    def generateHash(self):
        block = {
                'index' : self.index 
                'transactions' : self.transactions
                'timestamp' : self.timestamp
                'lastHash' : self.lastHash
                'proofOfWork' : self.proofOfWork
        }
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    #Checa a integridade do bloco comparando a hash armazenada e a hash calculada
    def checkHash(self):
        return self.hash==self.generateHash
    def getIndex(self):
        return self.index
    def getTransactions(self):
        return self.transactions
    def getHash(self):
        if not self.selado raise ValueError('Este bloco ainda não foi selado')
        if not self.checkHash raise ValueError('As hashes não batem')
        return self.hash
    def getLastHash(self):
        return self.lastHash
    def getTimestamp(self):
        return self.timestamp
    def getProofOfWork(self):
        return self.proofOfWork
    def getSelado(self):
        return sel.selado
    