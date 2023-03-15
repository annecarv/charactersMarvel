import hashlib
import dotenv
import os
import datetime

dotenv.load_dotenv(dotenv.find_dotenv())

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

private_key = os.getenv('privateKey')
public_key = os.getenv('publicKey')

def hash_config():
    hash_Md5 = hashlib.md5()
    hash_Md5.update(f'{time_stamp}{private_key}{public_key}'.encode('utf-8'))
    hash_config = hash_Md5.hexdigest()

    return hash_config

hash_config()