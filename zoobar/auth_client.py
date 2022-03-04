from debug import *
from zoodb import *
import rpclib

sys.path.append(os.getcwd())
import readconf

import profilemod_client

def login(username, password):
    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as c:
        ret = c.call('login', username=username, password=password)
        return ret 

def register(username, password):
    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as c:
        ret = c.call('register', username=username, password=password)
        # make new Person entry for newly registered users
        if ret:
            db = person_setup()
            newperson = Person()
            newperson.username = username
            db.add(newperson)
            db.commit()
            # also make empty Profile entry via RPC call
            profilemod_client.create_empty(username)
        return ret 

def check_token(username, token):
    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as c:
        ret = c.call('check_token', username=username, token=token)
        return ret

def set_token(username, token):
    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as c:
        ret = c.call('set_token', username=username, token=token)
    
