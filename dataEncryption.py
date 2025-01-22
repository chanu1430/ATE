import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os


key = os.urandom(32)  # AES-256 uses 32 bytes key
iv = os.urandom(16)  # 16 bytes initialization vector (IV) for CBC mode



def encrypt_data(data: str) -> str:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data.encode(), AES.block_size) 
    encrypted_token = cipher.encrypt(padded_data)
    return base64.urlsafe_b64encode(iv + encrypted_token).decode()


def decrypt_data(encrypted_data: str) ->str:
    decoded_data = base64.urlsafe_b64decode(encrypted_data)
    iv = decoded_data[:16]  # Extract IV
    encrypted_token = decoded_data[16:]  # Extract encrypted token

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_token), AES.block_size)  # Unpad after decryption
    return decrypted_data.decode()


