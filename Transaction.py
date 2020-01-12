import time
import json
import hashlib
import uuid

class Transaction:
    """Cria uma nova transação
    @param sender-> Remetente da transação
    @param receiver-> Destinatário da transação
    @param amount-> Quantidade de moedas transferidas
    """
    def __init__(self, sender, receiver, amount):
        #checa se a transação não é resultado de uma mineração e se o remetente é válido
        if sender!=0 and not isValidUuid(sender):
            raise TypeError('Sender deveria ser uuid')
        #checa se a quantidade de moedas realmente um inteiro
        if type(amount)!=int:
            raise TypeError('Amount deveria ser int')
        #checa se o destinatário é válido
        if not isValidUuid(receiver):
            raise TypeError('Receiver deveria ser uuid')
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    #determina se uma dada entrada é um uuid válido
    def isValidUuid(self,val):
        try:
            uuid.UUID(str(val))
            return True
        except ValueError:
            return False
    def getSender(self):
        return self.sender
    def getReceiver(self):
        return self.receiver
    def getAmount(self):
        return self.amount