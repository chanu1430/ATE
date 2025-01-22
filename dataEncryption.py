import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os


# key = os.urandom(32)  # AES-256 uses 32 bytes key
# iv = os.urandom(16)  # 16 bytes initialization vector (IV) for CBC mode

key = b'\x9a\x1d\xa9\xe8\xbeTx\x86[\x97\xe5\xd0l\xb5\xa0O\x8f\x06\xae\x89\xd6\xf5\x94\xa9\xe4\xe3\x03\xa2\xd4[1\xc7'
iv = b'z"\x89_,$\xa4\x9c\x82`\xb0\xb2\xffD{2'


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


