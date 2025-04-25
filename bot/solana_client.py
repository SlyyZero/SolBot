from solana.rpc.api import Client
from solders.pubkey import Pubkey

client = Client("https://api.mainnet-beta.solana.com")

def get_token_balance(public_key_str):
    public_key = Pubkey.from_string(public_key_str)
    response = client.get_balance(public_key)
    return response.value
