import subprocess
import json
import os

from dotenv import load_dotenv

from bit import key, PrivateKey, PrivateKeyTestnet
from bit.network from NetworkAPI
from bit import *
from web3 import Web3
from eth_account import Account


command = './derive -g --mnemonic="INSERT HERE" --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)

from constants import *

mnemonic = os.getenv('MNEMONIC', 'annual police carpet session length teach fee derive shoe sniff outdoor always field win shell')
print(mnemonic)

