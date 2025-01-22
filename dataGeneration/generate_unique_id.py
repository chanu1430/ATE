import hashlib
import time
import random

async def generate_different_unique_id(user_id: str) -> str:

    salt = str(time.time()) + str(random.randint(1000, 9999))
    input_data = user_id + salt
    hash_object = hashlib.sha256(input_data.encode())
    hex_dig = hash_object.hexdigest()
    unique_id = str(int(hex_dig[:8], 16)).zfill(8)
    return unique_id[:8]
