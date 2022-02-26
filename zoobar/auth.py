from zoodb import *
from debug import *

import hashlib
import random
import pbkdf2
import os

import bank_client

def newtoken(db, cred):
    hashinput = "%s%.10f" % (cred.password, random.random())
    cred.token = hashlib.md5(hashinput.encode('utf-8')).hexdigest()
    db.commit()
    return cred.token

def newsalt():
    return "%s" % os.urandom(64)

def slowhash(password, salt):
    return pbkdf2.PBKDF2(password, salt).hexread(32)

def login(username, password):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if not cred:
        return None
    salt = cred.salt
    if cred.password == slowhash(password, salt):
        return newtoken(db, cred)
    else:
        return None

def register(username, password):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred:
        return None
    newcred = Cred()
    newcred.username = username
    newcred.salt = newsalt()
    newcred.password = slowhash(password, newcred.salt)
    db.add(newcred)
    db.commit()
    # initialize bank account with balance of 10
    bank_client.register(username)
    return newtoken(db, newcred)

def check_token(username, token):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred and cred.token == token:
        return True
    else:
        return False

def set_token(username, token):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    cred.token = token

