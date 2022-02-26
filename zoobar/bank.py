from zoodb import *
from debug import *

import time
import auth_client

def transfer(sender, recipient, zoobars, token, caller):
    # check that token is valid
    # or calling service is profile 
    valid_token = auth_client.check_token(sender, token)
    if not valid_token and caller != "profile":
        return False

    bankdb = bank_setup()
    senderb = bankdb.query(Bank).get(sender)
    recipientb = bankdb.query(Bank).get(recipient)

    sender_balance = senderb.zoobars - zoobars
    recipient_balance = recipientb.zoobars + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        return False

    senderb.zoobars = sender_balance
    recipientb.zoobars = recipient_balance
    bankdb.commit()

    transfer = Transfer()
    transfer.sender = sender
    transfer.recipient = recipient
    transfer.amount = zoobars
    transfer.time = time.asctime()

    transferdb = transfer_setup()
    transferdb.add(transfer)
    transferdb.commit()
    return True

def balance(username):
    db = bank_setup()
    bank = db.query(Bank).get(username)
    return bank.zoobars

def get_log(username):
    db = transfer_setup()
    l = db.query(Transfer).filter(or_(Transfer.sender==username,
                                      Transfer.recipient==username))
    r = []
    for t in l:
       r.append({'time': t.time,
                 'sender': t.sender ,
                 'recipient': t.recipient,
                 'amount': t.amount })
    return r 

def register(username):
    db = bank_setup()
    newbank = Bank()
    newbank.username = username
    # note: newbank.balance = 10 by default
    db.add(newbank)
    db.commit()
