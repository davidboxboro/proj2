from debug import *
from zoodb import *
import rpclib

sys.path.append(os.getcwd())
import readconf

def transfer(sender, recipient, zoobars, token):
    host = readconf.read_conf().lookup_host('bank')
    with rpclib.client_connect(host) as c:
        ret = c.call('transfer', sender=sender, 
                recipient=recipient, zoobars=zoobars,
                token=token)
        # handle error
        if not ret:
            raise ValueError()                 

def balance(username):
    host = readconf.read_conf().lookup_host('bank')
    with rpclib.client_connect(host) as c:
        ret = c.call('balance', username=username)
        return ret

def get_log(username):
    host = readconf.read_conf().lookup_host('bank')
    with rpclib.client_connect(host) as c:
        ret = c.call('get_log', username=username)
        return ret

def register(username):
    host = readconf.read_conf().lookup_host('bank')
    with rpclib.client_connect(host) as c:
        ret = c.call('register', username=username)


