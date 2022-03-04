import rpclib
from debug import *
from zoodb import *

sys.path.append(os.getcwd())
import readconf

def create_empty(username):
    host = readconf.read_conf().lookup_host('profilemod')
    with rpclib.client_connect(host) as c:
        ret = c.call('create_empty', username=username)

def update(username, new_profile, token):
    host = readconf.read_conf().lookup_host('profilemod')
    with rpclib.client_connect(host) as c:
        ret = c.call('update', username=username, 
                new_profile=new_profile, token=token)
    return ret

def read(username):
    host = readconf.read_conf().lookup_host('profilemod')
    with rpclib.client_connect(host) as c:
        ret = c.call('read', username=username)
    return ret




