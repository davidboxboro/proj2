#!/usr/bin/env python3

import rpclib
import sys
from debug import *
import profilemod

class ProfilemodRpcServer(rpclib.RpcServer):
    def rpc_create_empty(self, username):
        return profilemod.create_empty(username)

    def rpc_update(self, username, new_profile, token):
        return profilemod.update(username, new_profile, token)

    def rpc_read(self, username):
        return profilemod.read(username)

s = ProfilemodRpcServer()
s.run_fork(sys.argv[1])
