import hashlib
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

timestamp = os.getenv('timeStamp')
privateKey = os.getenv('privateKey')
publicKey = os.getenv('publicKey')

def hashConfig():
    hashMd5 = hashlib.md5()
    hashMd5.update(f'{timestamp}{privateKey}{publicKey}'.encode('utf-8'))
    hashConfig = hashMd5.hexdigest()

    return hashConfig
