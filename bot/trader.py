from .solana_client import get_token_balance


def start_trading():
    print("Starting Solana trading bot...")
    wallet = "42PW3RvoW2E1a8RBXf1Drf3tyUnFFr71EHECUa6cdevG"
    balance = get_token_balance(wallet)
    print(f"Wallet Balance: {balance} lamports")
