#!/usr/bin/env python3

import rpclib
import sys
import auth
from debug import *
from zoodb import *
import bank

class BankRpcServer(rpclib.RpcServer):
    def rpc_transfer(self, sender, recipient, zoobars, token):
        return bank.transfer(sender, recipient, zoobars, 
                token, self.caller) 

    def rpc_balance(self, username):
        return bank.balance(username)

    def rpc_get_log(self, username):
        return bank.get_log(username)

    def rpc_register(self, username):
        return bank.register(username)

s = BankRpcServer()
s.run_fork(sys.argv[1])
