# Import Libraries
import subprocess
import json
import os
from dotenv import load_dotenv
from bit import Key, PrivateKey, PrivateKeyTestnet
from bit.network import NetworkAPI
from bit import *
from web3 import Web3
from eth_account import Account
from constants import *


w3 = Web3(Web3.HTTPProvider("http://127.0.0.1.8545"))

load_dotenv

command = './derive -g --mnemonic="INSERT HERE" --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

# Deriving Wallet keys
def derive_wallets(mnemonic, coin, numderive):
    """Use the subprocess library to call the php file script from Python"""
    command = f'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --numderive="{numderive}" --coin="{coin}" --format=json' 
    
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
   
    keys = json.loads(output)
    return  keys

coins = {"eth", "btc-test", "btc"}
numderive = 3

keys = {}
for coin in coins:
    keys[coin]= derive_wallets(os.getenv('mnemonic'), coin, numderive=3)
