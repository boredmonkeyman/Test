from solana.account import Account
from solana.rpc.api import Client
from solana.rpc.types import TokenAccountOpts
from solana.wallet import Wallet
from solana.utils import pubkey_to_address
from bip_utils import Bip39MnemonicGenerator, Bip39WordsNum, Bip39MnemonicValidator

def generate_mnemonic():
    # Generate a random mnemonic phrase
    mnemonic = Bip39MnemonicGenerator().Generate(Bip39WordsNum.BIP39_WORDS_NUM_24)
    return mnemonic

def save_mnemonic_with_balance(mnemonic):
    # Initialize Solana client
    solana_client = Client("https://api.devnet.solana.com")

    # Create a wallet from the mnemonic
    wallet = Wallet(mnemonic)

    # Get the public key of the wallet
    public_key = wallet.address()

    # Get the balance of the wallet
    balance = solana_client.get_balance(public_key)

    if balance > 0:
        # Save mnemonic and balance to a file
        with open("mnemonic_with_balance.txt", "a") as file:
            file.write(f"Mnemonic: {mnemonic}\nBalance: {balance}\n\n")

def main():
    # Generate 10 mnemonic phrases
    for _ in range(10):
        mnemonic = generate_mnemonic()
        save_mnemonic_with_balance(mnemonic)

if __name__ == "__main__":
    main()
