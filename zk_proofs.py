from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import json

# Generate RSA keys for encryption/decryption
key = RSA.generate(2048)
public_key = key.publickey()
cipher_encrypt = PKCS1_OAEP.new(public_key)
cipher_decrypt = PKCS1_OAEP.new(key)

def generate_proof(vote):
    """
    Encrypts the vote using the public key.
    """
    encrypted_vote = cipher_encrypt.encrypt(vote.encode())
    return encrypted_vote

def verify_proof(encrypted_vote):
    """
    Decrypts the vote using the private key to verify it.
    """
    decrypted_vote = cipher_decrypt.decrypt(encrypted_vote)
    return decrypted_vote.decode()
